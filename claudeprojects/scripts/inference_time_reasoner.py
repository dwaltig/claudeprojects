#!/usr/bin/env python3
"""
Inference-Time Reasoner (RLM Scaffold)
======================================

This script implements a "Recursive Language Model" (RLM) scaffold.
It allows an autonomous agent to:
1. Load large context into memory without feeding it all to the context window.
2. Interact with a Python REPL to slice, inspect, and manipulate that data.
3. Recursively call an LLM on specific chunks to perform sub-tasks.

Usage:
    python3 scripts/inference_time_reasoner.py --context_file "path/to/large/file.txt"

Dependencies:
    pip install litellm openai
"""

import sys
import os
import argparse
import code
import io
from pathlib import Path
from typing import Optional, Any

try:
    from litellm import completion
    from dotenv import load_dotenv
    load_dotenv() # Load .env file immediately
except ImportError:
    print("❌ Error: 'litellm' or 'python-dotenv' not found.")
    print("   Please run: pip install litellm python-dotenv")
    sys.exit(1)


class RLMEnvironment:
    """
    The environment exposed to the agent inside the REPL.
    """
    def __init__(self, context_path: Optional[str] = None):
        self.CONTEXT = ""
        self.CONTEXT_PATH = context_path
        self._load_context()
        self.history = []

    def _load_context(self):
        """Loads context into memory if a path is provided."""
        if self.CONTEXT_PATH:
            try:
                with open(self.CONTEXT_PATH, 'r', encoding='utf-8') as f:
                    self.CONTEXT = f.read()
                print(f"✅ Loaded context from {self.CONTEXT_PATH}")
                print(f"   Length: {len(self.CONTEXT)} characters")
                print("   Variable name: CONTEXT")
            except Exception as e:
                print(f"❌ Failed to load context file: {e}")
                self.CONTEXT = "Error loading context."

    def llm_query(self, task: str, content: str, model: str = "gpt-5.2", depth: int = 0, max_depth: int = 3, json_mode: bool = False) -> str:
        """
        Recursive LLM Call.
        
        Args:
            task (str): The specific instruction for this sub-step.
            content (str): The data to process.
            model (str): Model to use (default: gpt-5.2).
            depth (int): Current recursion depth.
            max_depth (int): Maximum allowed recursion depth.
            json_mode (bool): If True, enforces JSON output format.
        
        Returns:
            str: The LLM's response.
        """
        if depth > max_depth:
            return f"[STOP] Recursion depth limit ({max_depth}) reached. Returning content summary: {content[:100]}..."

        print(f"\\n🧠 [Recursion Depth {depth}] sending {len(content)} chars to {model} (JSON={json_mode})...")
        
        system_prompt = (
            "You are a sub-agent processing a specific chunk of data.\\n"
            "1. Output ONLY the requested result.\\n"
            "2. Do NOT add preamble, 'Here is the code', or fluff.\\n"
            "3. CRITICAL: Your output is used AS-IS. Do not include placeholders like '[Insert Data]'.\\n"
            "4. If the task is impossible, state specific reasons why."
        )
        
        if json_mode:
            system_prompt += "\\n5. You must output valid JSON."

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Task: {task}\\n\\nData:\\n{content}"}
        ]

        # Check for OpenAI API Key
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
             print("\\n⚠️  [WARNING] OPENAI_API_KEY not found. Attempting call anyway (might fail or use other env vars)...")

        try:
            kwargs = {
                "model": model,
                "messages": messages,
                "api_key": api_key
            }
            
            if json_mode:
                kwargs["response_format"] = { "type": "json_object" }

            response = completion(**kwargs)
            
            result = response.choices[0].message.content
            print("✅ [Recursion] Response received.")
            self.history.append({"task": task, "result": result})
            return result
        except Exception as e:
            error_string = str(e)
            if "AuthenticationError" in error_string or "Incorrect API key" in error_string:
                print("\\n⚠️  [MOCK MODE] Authentication failed. Returning mock response to keep REPL alive.")
                print(f"   Error: {error_string[:100]}...")
                mock_result = f"[MOCK RESULT for '{task}']: This is a simulated response because the API key was invalid."
                self.history.append({"task": task, "result": mock_result})
                return mock_result
            else:
                error_msg = f"❌ LLM Call Failed: {e}"
                print(error_msg)
                return error_msg

    def inspect(self, variable: Any, length: int = 500):
        """Safe inspection helper."""
        s = str(variable)
        print(f"Type: {type(variable)}")
        print(f"Length: {len(s)}")
        print(f"Preview:\\n{s[:length]}...")


def start_repl(context_file: Optional[str]):
    """Starts the interactive REPL loop."""
    
    # Initialize the environment
    env = RLMEnvironment(context_file)
    
    # Create the namespace for the REPL
    namespace = {
        'CONTEXT': env.CONTEXT,
        'llm_query': env.llm_query,
        'inspect': env.inspect,
        'env': env,
        'os': os,
        'sys': sys
    }
    
    banner = """
================================================================
🤖 RLM INFERENCE-TIME REASONER
================================================================
Variables available:
  - CONTEXT (str): The loaded file content.
  - llm_query(task, content): Function to call LLM recursively.
  - inspect(var): Helper to view data safely.

Type python code to interact. Use exit() or Ctrl-D to quit.
================================================================
    """
    
    # Check for API Key
    if not os.environ.get("OPENAI_API_KEY"):
        print("⚠️  WARNING: OPENAI_API_KEY not found in environment variables.")
        print("   Recursion (llm_query) will likely fail unless configured via other means.")

    # Start Interactive Console
    try:
        code.interact(banner=banner, local=namespace)
    except SystemExit:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recursive Language Model Scaffold")
    parser.add_argument("--context", "-c", help="Path to text file to load into context")
    args = parser.parse_args()

    start_repl(args.context)
