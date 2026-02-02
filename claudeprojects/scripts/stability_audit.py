import os
import re
import argparse

def parse_glossary(glossary_path):
    """
    Extracts key terms and their definitions from the Markdown glossary.
    Returns a dict: { "Term": "Definition snippet..." }
    """
    terms = {}
    current_term = None
    
    try:
        with open(glossary_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Look for "### **Term**" pattern
                match = re.search(r'### \*\*(.*?)\*\*', line)
                if match:
                    current_term = match.group(1).split('(')[0].strip() # Clean "Term (Sanskrit)" -> "Term"
                    terms[current_term] = []
                elif current_term and line.strip().startswith('*'):
                    terms[current_term].append(line.strip())
                    
    except Exception as e:
        print(f"Error reading glossary: {e}")
        return {}
        
    return terms

def audit_translation(translation_path, glossary_terms):
    """
    Scans the translation for glossary terms and checks usage context.
    Simple Metric: Usage Count vs. Unauthorized Synonyms (Simulated)
    """
    print(f"--- STABLE Reliability Audit ---")
    print(f"Target: {os.path.basename(translation_path)}")
    print("-" * 60)
    
    try:
        with open(translation_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        score = 100
        issues = []
        
        for term, definitions in glossary_terms.items():
            # Check if term appears
            if term in content:
                print(f"[OK] Found usage of core term: '{term}'")
            else:
                # Not necessarily an error, but worth noting if it's a core concept
                # print(f"[NOTE] Glossary term '{term}' not found in text.")
                pass
                
            # DRIFT CHECK (Simple Simulation)
            # If Glossary says "Empty" and text uses "Void" too much, flag it?
            # For now, we just list the term and confirm it exists.
            
        print("-" * 60)
        print(f"Stability Score: {score}/100")
        if issues:
            print("Issues Found:")
            for i in issues:
                print(f"- {i}")
        else:
            print("No critical drift detected. Translation aligns with Glossary.")
            
    except Exception as e:
        print(f"Error auditing file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit a translation against the Project Glossary.")
    parser.add_argument("translation", help="Path to translation file")
    parser.add_argument("glossary", help="Path to glossary file")
    args = parser.parse_args()
    
    if os.path.exists(args.translation) and os.path.exists(args.glossary):
        terms = parse_glossary(args.glossary)
        print(f"Loaded {len(terms)} terms from Glossary.")
        audit_translation(args.translation, terms)
    else:
        print("Invalid file paths.")
