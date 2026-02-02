#!/usr/bin/env python3
"""
Ralph Loop: Iterative Convergence for Buddhist Translation MAS

A "Ralph Wiggum" style loop that cycles translations between agents
until convergence criteria are met.

Usage:
    python ralph_loop.py --source SOURCE.txt --type translation --max-iter 5
    python ralph_loop.py --source ARTICLE.md --type review --max-iter 3
"""

import argparse
import json
import os
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Optional
from pathlib import Path


@dataclass
class IterationResult:
    """Single iteration outcome."""
    iteration: int
    timestamp: str
    agent_a_changes: int
    agent_b_changes: int
    delta_percent: float
    agent_a_signoff: bool
    agent_b_signoff: bool
    flags: list[str]
    status: str  # 'continuing', 'converged', 'interrupted'
    
    
@dataclass 
class LoopConfig:
    """Configuration for a Ralph Loop execution."""
    max_iterations: int = 5
    min_iterations: int = 2
    convergence_threshold: float = 5.0  # percent
    stagnation_limit: int = 3
    force_human_triggers: list[str] = None
    
    def __post_init__(self):
        if self.force_human_triggers is None:
            self.force_human_triggers = [
                "doctrinal concern",
                "ghost character",
                "requires human judgment",
                "regression detected"
            ]


class RalphLoop:
    """
    Manages iterative convergence between translation agents.
    
    Named for the "Ralph Loop" technique - like Ralph Wiggum,
    it just keeps going until the job is truly done.
    """
    
    LOOP_TYPES = {
        'translation': {
            'agent_a': 'The Professor',
            'agent_b': 'The Bluesman',
            'convergence_check': 'translation_convergence'
        },
        'review': {
            'agent_a': 'JAR_Editorial_Reviewer',
            'agent_b': 'Cultural_Sensitivity_Reviewer', 
            'convergence_check': 'review_convergence'
        },
        'audit': {
            'agent_a': 'DeepSeek_Auditor',
            'agent_b': 'The Professor',
            'convergence_check': 'audit_convergence'
        }
    }
    
    def __init__(
        self, 
        source_file: str, 
        loop_type: str = 'translation',
        config: Optional[LoopConfig] = None,
        output_dir: Optional[str] = None
    ):
        if loop_type not in self.LOOP_TYPES:
            raise ValueError(f"Unknown loop type: {loop_type}. Choose from {list(self.LOOP_TYPES.keys())}")
            
        self.source_file = Path(source_file)
        self.loop_type = loop_type
        self.config = config or LoopConfig()
        self.output_dir = Path(output_dir) if output_dir else self.source_file.parent
        
        self.iteration = 0
        self.history: list[IterationResult] = []
        self.converged = False
        self.human_interrupt = False
        self.interrupt_reason = None
        
        # Load source content
        self.original_content = self._load_source()
        self.current_content = self.original_content
        self.previous_content = None
        
    def _load_source(self) -> str:
        """Load the source file content."""
        with open(self.source_file, 'r', encoding='utf-8') as f:
            return f.read()
            
    def _calculate_delta(self, previous: str, current: str) -> float:
        """Calculate character-level change percentage."""
        if not previous:
            return 100.0
        prev_len = len(previous)
        diff = abs(len(current) - prev_len)
        # Also count character-level differences
        changes = sum(1 for a, b in zip(previous, current) if a != b)
        changes += abs(len(current) - len(previous))
        return (changes / max(prev_len, 1)) * 100
        
    def _check_for_interrupt_triggers(self, agent_output: str) -> Optional[str]:
        """Check if agent output contains phrases that require human review."""
        output_lower = agent_output.lower()
        for trigger in self.config.force_human_triggers:
            if trigger in output_lower:
                return trigger
        return None
        
    def _check_convergence(self, iteration_result: IterationResult) -> bool:
        """Determine if the loop has converged."""
        # Must complete minimum iterations
        if self.iteration < self.config.min_iterations:
            return False
            
        # Both agents must sign off
        if not (iteration_result.agent_a_signoff and iteration_result.agent_b_signoff):
            return False
            
        # Delta must be below threshold
        if iteration_result.delta_percent > self.config.convergence_threshold:
            return False
            
        # No flags
        if iteration_result.flags:
            return False
            
        return True
        
    def _check_stagnation(self) -> bool:
        """Check if we've stagnated (no progress for N iterations)."""
        if len(self.history) < self.config.stagnation_limit:
            return False
            
        recent = self.history[-self.config.stagnation_limit:]
        deltas = [r.delta_percent for r in recent]
        
        # If all recent deltas are < 1% but we haven't converged, we're stagnating
        return all(d < 1.0 for d in deltas)
        
    def run_iteration(self) -> IterationResult:
        """
        Execute a single iteration of the loop.
        
        In actual use, this would call the AI agents. For now, this is
        a framework that can be extended with actual agent invocations.
        """
        self.iteration += 1
        self.previous_content = self.current_content
        
        # Placeholder for actual agent calls
        # In production, these would invoke the Professor and Bluesman agents
        agent_a_output = self._invoke_agent_a(self.current_content)
        agent_b_output = self._invoke_agent_b(agent_a_output)
        
        self.current_content = agent_b_output
        
        # Calculate metrics
        delta = self._calculate_delta(self.previous_content, self.current_content)
        
        # Check for interrupt triggers
        interrupt_a = self._check_for_interrupt_triggers(agent_a_output)
        interrupt_b = self._check_for_interrupt_triggers(agent_b_output)
        
        flags = []
        if interrupt_a:
            flags.append(f"Agent A: {interrupt_a}")
        if interrupt_b:
            flags.append(f"Agent B: {interrupt_b}")
            
        # Detect sign-offs (simplified - in production, parse agent output)
        signoff_phrases = ["no further changes", "sign-off", "approved as-is", "satisfied"]
        agent_a_signoff = any(p in agent_a_output.lower() for p in signoff_phrases)
        agent_b_signoff = any(p in agent_b_output.lower() for p in signoff_phrases)
        
        # Build result
        result = IterationResult(
            iteration=self.iteration,
            timestamp=datetime.now().isoformat(),
            agent_a_changes=self._count_changes(self.previous_content, agent_a_output),
            agent_b_changes=self._count_changes(agent_a_output, agent_b_output),
            delta_percent=round(delta, 2),
            agent_a_signoff=agent_a_signoff,
            agent_b_signoff=agent_b_signoff,
            flags=flags,
            status='continuing'
        )
        
        # Check various termination conditions
        if flags:
            self.human_interrupt = True
            self.interrupt_reason = "; ".join(flags)
            result.status = 'interrupted'
        elif self._check_convergence(result):
            self.converged = True
            result.status = 'converged'
        elif self._check_stagnation():
            self.human_interrupt = True
            self.interrupt_reason = "Stagnation detected"
            result.status = 'interrupted'
            
        self.history.append(result)
        return result
        
    def _invoke_agent_a(self, content: str) -> str:
        """
        Placeholder for Agent A invocation.
        Override this method or extend the class for actual agent integration.
        """
        # In production: call The Professor / JAR Reviewer / DeepSeek
        return content + "\n\n[Agent A processed - no further changes needed. Sign-off.]"
        
    def _invoke_agent_b(self, content: str) -> str:
        """
        Placeholder for Agent B invocation.
        Override this method or extend the class for actual agent integration.
        """
        # In production: call The Bluesman / Cultural Sensitivity Reviewer
        return content + "\n\n[Agent B processed - satisfied with translation. Sign-off.]"
        
    def _count_changes(self, before: str, after: str) -> int:
        """Count approximate number of changes between versions."""
        return sum(1 for a, b in zip(before, after) if a != b) + abs(len(after) - len(before))
        
    def execute(self) -> dict:
        """
        Run the full Ralph Loop until convergence or termination.
        
        Returns a summary dict with final status and output paths.
        """
        print(f"🔄 Starting Ralph Loop: {self.loop_type}")
        print(f"   Source: {self.source_file}")
        print(f"   Max iterations: {self.config.max_iterations}")
        print()
        
        while not self.converged and not self.human_interrupt:
            if self.iteration >= self.config.max_iterations:
                self.human_interrupt = True
                self.interrupt_reason = f"Max iterations ({self.config.max_iterations}) reached"
                break
                
            result = self.run_iteration()
            print(f"   Iteration {result.iteration}: Δ={result.delta_percent}% | "
                  f"A:{'+' if result.agent_a_signoff else '○'} "
                  f"B:{'+' if result.agent_b_signoff else '○'} | "
                  f"{result.status}")
                  
        # Compile final output
        return self._compile_output()
        
    def _compile_output(self) -> dict:
        """Generate final output files and summary."""
        # Write converged content
        output_file = self.output_dir / f"{self.source_file.stem}_converged.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(self.current_content)
            
        # Write iteration log
        log_file = self.output_dir / f"{self.source_file.stem}_ralph_log.json"
        log_data = {
            'source_file': str(self.source_file),
            'loop_type': self.loop_type,
            'config': asdict(self.config),
            'total_iterations': self.iteration,
            'converged': self.converged,
            'human_interrupt': self.human_interrupt,
            'interrupt_reason': self.interrupt_reason,
            'history': [asdict(h) for h in self.history]
        }
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2)
            
        # Final summary
        summary = {
            'converged': self.converged,
            'total_iterations': self.iteration,
            'final_delta': self.history[-1].delta_percent if self.history else None,
            'convergence_reason': self._get_convergence_reason(),
            'human_review_needed': self.human_interrupt,
            'interrupt_reason': self.interrupt_reason,
            'output_file': str(output_file),
            'log_file': str(log_file)
        }
        
        print()
        if self.converged:
            print(f"✅ CONVERGED after {self.iteration} iterations")
        else:
            print(f"⚠️  STOPPED: {self.interrupt_reason}")
        print(f"   Output: {output_file}")
        print(f"   Log: {log_file}")
        
        return summary
        
    def _get_convergence_reason(self) -> str:
        """Describe why the loop terminated."""
        if self.converged:
            return "both_agents_signoff"
        elif self.human_interrupt:
            return f"human_interrupt: {self.interrupt_reason}"
        else:
            return "unknown"


def main():
    parser = argparse.ArgumentParser(
        description="Ralph Loop: Iterative convergence for Buddhist translation MAS"
    )
    parser.add_argument('--source', required=True, help='Source file path')
    parser.add_argument('--type', choices=['translation', 'review', 'audit'],
                       default='translation', help='Loop type')
    parser.add_argument('--max-iter', type=int, default=5, help='Maximum iterations')
    parser.add_argument('--min-iter', type=int, default=2, help='Minimum iterations')
    parser.add_argument('--threshold', type=float, default=5.0,
                       help='Convergence threshold (percent)')
    parser.add_argument('--output-dir', help='Output directory (default: source dir)')
    
    args = parser.parse_args()
    
    config = LoopConfig(
        max_iterations=args.max_iter,
        min_iterations=args.min_iter,
        convergence_threshold=args.threshold
    )
    
    loop = RalphLoop(
        source_file=args.source,
        loop_type=args.type,
        config=config,
        output_dir=args.output_dir
    )
    
    result = loop.execute()
    print()
    print("Summary:", json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
