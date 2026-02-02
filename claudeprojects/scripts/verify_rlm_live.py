
import sys
import os

# Add scripts directory to path to import the module
sys.path.append(os.path.join(os.getcwd(), "scripts"))

try:
    from inference_time_reasoner import RLMEnvironment
except ImportError:
    print("Failed to import RLMEnvironment. formatting issue?")
    sys.exit(1)

def test_rlm():
    print("Initializing RLM Environment...")
    # Initialize without context file for a simple test
    env = RLMEnvironment()
    
    test_content = "The quick brown fox jumps over the lazy dog."
    test_task = "Extract the animal names into a JSON list."
    
    print(f"Testing llm_query with json_mode=True...")
    try:
        # Use a very small model if possible, or standard default
        # Note: Using json_mode=True
        result = env.llm_query(
            task=test_task, 
            content=test_content, 
            json_mode=True,
            model="gpt-4o"
        )
        
        print("\n--- RESULT ---")
        print(result)
        print("--------------")
        
        if "fox" in result and "dog" in result and ("[" in result or "{" in result):
            print("✅ VERIFICATION SUCCESS: RLM returned structured data.")
        else:
            print("⚠️ VERIFICATION WARNING: Output might not be valid JSON or missing data.")
            
    except Exception as e:
        print(f"❌ VERIFICATION FAILED: {e}")

if __name__ == "__main__":
    test_rlm()
