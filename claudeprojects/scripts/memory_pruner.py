import os
import time
import math
import argparse
from datetime import datetime

# --- CONFIGURATION ---
# Halflife (days): How long until a file loses 50% of its Recency score
HALFLIFE_DAYS = 30 
# Keywords that boost Relevance score (The "Heartwood")
CORE_KEYWORDS = ["Lotus", "Sutra", "Blues", "Dharma", "Glosssary", "Architecture", "Agent", "Vow"]

def calculate_rif_score(file_path):
    """
    Calculates the Retention Score (RIF) for a file.
    Formula: Score = (Recency * Relevance * Frequency)
    """
    
    # 1. Recency (Decay Function)
    # Get file modification time
    stats = os.stat(file_path)
    last_mod_ts = stats.st_mtime
    age_seconds = time.time() - last_mod_ts
    age_days = age_seconds / (24 * 3600)
    
    # Exponential Decay: N(t) = N0 * (1/2)^(t/t_half)
    # We normalize N0 to 1.0
    recency_score = math.pow(0.5, age_days / HALFLIFE_DAYS)
    
    # 2. Relevance (Keyword Density)
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read().lower()
            
        keyword_hits = 0
        for kw in CORE_KEYWORDS:
            if kw.lower() in content:
                keyword_hits += 1
        
        # Simple normalization: Cap at 1.0 (all keywords found) or scale
        # Let's say 5 keywords = max relevance 1.0
        relevance_score = min(keyword_hits / 5.0, 1.0)
        # Ensure non-zero
        relevance_score = max(relevance_score, 0.1)
        
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        relevance_score = 0.1

    # 3. Frequency (Access/Link Count)
    # Since we don't have access logs, we simulate Frequency via "Backlinks" or "Size" as proxy?
    # Better proxy: Is it referenced in other files? (Too slow for this script)
    # Let's use specific TAGS as a frequency booster.
    # If file contains "#CRITICAL_DECISION", Frequency = 2.0. Else 1.0.
    frequency_score = 1.0
    if "#CRITICAL_DECISION" in content:
        frequency_score = 2.0
    if "GLOSSARY" in file_path.upper(): # Glossaries are high freq
        frequency_score = 1.5

    # --- FINAL SCORE ---
    rif_score = recency_score * relevance_score * frequency_score
    
    return {
        "file": os.path.basename(file_path),
        "age_days": round(age_days, 1),
        "R_recency": round(recency_score, 3),
        "R_relevance": round(relevance_score, 3),
        "F_frequency": round(frequency_score, 1),
        "TOTAL_RIF": round(rif_score, 4)
    }

def scan_directory(dir_path):
    print(f"--- RIF Memory Pruner Scan: {dir_path} ---")
    print(f"{'Filename':<40} | {'Age(d)':<6} | {'Rec':<5} | {'Rel':<5} | {'Frq':<3} | {'SCORE':<6} | {'Action'}")
    print("-" * 100)
    
    files = [f for f in os.listdir(dir_path) if f.endswith('.md')]
    
    for filename in files:
        file_path = os.path.join(dir_path, filename)
        metrics = calculate_rif_score(file_path)
        
        # ACTION LOGIC (The "Pruning" Gate)
        score = metrics["TOTAL_RIF"]
        action = "KEEP"
        if score < 0.1:
            action = "PRUNE (Archive)"
        elif score < 0.3:
            action = "REVIEW (Consolidate)"
            
        print(f"{metrics['file'][:40]:<40} | {metrics['age_days']:<6} | {metrics['R_recency']:<5} | {metrics['R_relevance']:<5} | {metrics['F_frequency']:<3} | {metrics['TOTAL_RIF']:<6} | {action}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan a directory and calculate RIF Retention Scores.")
    parser.add_argument("path", help="Path to directory to scan")
    args = parser.parse_args()
    
    if os.path.isdir(args.path):
        scan_directory(args.path)
    else:
        print(f"Invalid directory: {args.path}")
