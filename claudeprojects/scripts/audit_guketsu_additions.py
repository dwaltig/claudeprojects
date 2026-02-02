import os
import re

# Configuration
BASE_DIR = "/Users/williamaltig/claudeprojects/Miao-lo/Guketsu_Project/01_TRANSLATIONS"
OUTPUT_REPORT = "Guketsu_Translation_Audit_Report.md"

def get_scholarly_files():
    """Finds all Scholarly markdown files."""
    files = []
    for f in os.listdir(BASE_DIR):
        if "Scholarly" in f and f.endswith(".md"):
             files.append(f)
    files.sort()
    return files

def analyze_file(filename):
    """Analyzes a single file for translation artifacts."""
    path = os.path.join(BASE_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    stats = {
        "bracketed_segments": 0,
        "inline_pinyin_chinese": 0,
        "added_headers": 0,
        "blockquotes": 0, # Assuming blockquotes are pure source
        "total_lines": len(lines),
        "examples": []
    }
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Headers
        if line.startswith('#'):
            stats["added_headers"] += 1
            
        # Blockquotes
        if line.startswith('>'):
            stats["blockquotes"] += 1
            
        # Bracketed Interpolations [text]
        # Regex: \[.*?\] matches anything inside brackets
        # But exclude simple references like [1] unless they are interpolations. 
        # Typically interpolations are words: [set forth], [students]
        brackets = re.findall(r'\[(.*?)\]', line)
        for b in brackets:
            # Filter out likely citation numbers [1], [2]
            if not b.isdigit() and len(b) > 1:
                stats["bracketed_segments"] += 1
                if len(stats["examples"]) < 3 and "Bracketed" not in str(stats["examples"]):
                     stats["examples"].append(f"Bracketed: [{b}]")

        # Pinyin/Chinese pairs: (*pinyin* char) or just char
        # Often formatted as `*pinyin* char` or `char [meaning]`
        # Let's count runs of Chinese characters as "Source Text" presence, 
        # but if they are embedded in English, it's a "Gloss".
        # Regex for Chinese characters: [\u4e00-\u9fff]
        chinese_chars = re.findall(r'[\u4e00-\u9fff]+', line)
        if chinese_chars:
            stats["inline_pinyin_chinese"] += len(chinese_chars)
            if len(stats["examples"]) < 5 and "Chinese" not in str(stats["examples"]):
                stats["examples"].append(f"Inline Chinese: {chinese_chars[0]}")

    return stats

def generate_report():
    files = get_scholarly_files()
    total_stats = {
        "bracketed_segments": 0,
        "inline_pinyin_chinese": 0,
        "added_headers": 0,
        "blockquotes": 0
    }
    
    report_lines = []
    report_lines.append("# Guketsu Translation Audit Report\n")
    report_lines.append(f"**Date:** {os.popen('date').read().strip()}\n")
    report_lines.append("This report enumerates elements added to the original Chinese text during the translation process. "
                        "These 'artifacts' include structural headers, bracketed interpolations for clarity, and inline glosses.\n")
    
    report_lines.append("| File | Added Headers | Bracketed Interpolations | Inline Chinese Glosses | Example Artifacts |")
    report_lines.append("|---|---|---|---|---|")
    
    for f in files:
        stats = analyze_file(f)
        
        # Aggregate
        total_stats["bracketed_segments"] += stats["bracketed_segments"]
        total_stats["inline_pinyin_chinese"] += stats["inline_pinyin_chinese"]
        total_stats["added_headers"] += stats["added_headers"]
        total_stats["blockquotes"] += stats["blockquotes"]
        
        examples = "; ".join(stats["examples"][:2]) # Just show a couple
        report_lines.append(f"| {f} | {stats['added_headers']} | {stats['bracketed_segments']} | {stats['inline_pinyin_chinese']} | {examples} |")

    report_lines.append("\n## Summary Statistics\n")
    report_lines.append(f"- **Total Files Analyzed**: {len(files)}")
    report_lines.append(f"- **Total Added Headers**: {total_stats['added_headers']}")
    report_lines.append(f"- **Total Bracketed Interpolations**: {total_stats['bracketed_segments']} (Words added for English grammar/context)")
    report_lines.append(f"- **Total Inline Chinese Glosses**: {total_stats['inline_pinyin_chinese']} (Original characters preserved for philological precision)")
    
    report_lines.append("\n## Analysis of Additions\n")
    report_lines.append("### 1. Structural Headers\n")
    report_lines.append("The original text is a continuous flow (fascicles). divide the text into 'Sections' and 'Parts' (e.g., 'The Ten Intentions') are modern editorial choices to facilitate reading.\n")
    report_lines.append("### 2. Bracketed Interpolations [...]\n")
    report_lines.append("Classical Chinese is telegraphic. The translator has added subjects (e.g., '[students]'), verbs (e.g., '[set forth]'), and connective particles to make the English grammatically complete.\n")
    report_lines.append("### 3. Inline Glosses (*pinyin* 漢字)\n")
    report_lines.append("These are retained source texts interspersed with translation to allow for philological verification. They are strictly additions to the *English target text* but represent the *original source*.\n")
    
    with open(OUTPUT_REPORT, 'w', encoding='utf-8') as f:
        f.writelines(report_lines)
    
    print(f"Report generated at {OUTPUT_REPORT}")

if __name__ == "__main__":
    generate_report()
