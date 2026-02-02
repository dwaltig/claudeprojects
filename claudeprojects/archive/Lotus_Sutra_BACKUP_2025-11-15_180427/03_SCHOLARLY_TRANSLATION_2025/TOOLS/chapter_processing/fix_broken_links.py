#!/usr/bin/env python3
"""
Fix broken links in chapter HTML files and homepage.

Fixes:
1. Remove study guide links from chapters without guides (4-13, 15-24, 26-27)
2. Add "Coming Soon" messages to those chapters
3. Fix practice layer markdown links in homepage
"""

import os
import glob

# Chapters that DON'T have study guides yet
chapters_without_guides = list(range(4, 14)) + list(range(15, 25)) + [26, 27]
chapters_with_guides = [1, 2, 3, 14, 25, 28]

# Path to chapters directory
chapters_dir = './chapters'

def fix_chapter_file(chapter_num):
    """Remove broken study guide link and add coming soon message."""
    filename = f'{chapters_dir}/chapter_{chapter_num:02d}.html'

    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        return False

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find and replace
    old_pattern = f'                <a href="../_PRACTICE_LAYER/02_Chapter_Study_Guides/CHAPTER_{chapter_num:02d}_STUDY_GUIDE.md" class="study-link">📚 Study Guide</a>'

    new_content = '''                <p style="color: #666; font-style: italic; margin-bottom: 1rem;">
                    📚 <strong>Study Guide for this chapter is coming soon.</strong> In the meantime, explore our <a href="../index.html#practice">practice materials</a> and <a href="../_PRACTICE_LAYER/00_START_HERE/INDEX_READ_ME_FIRST.md">complete practice guide</a>.
                </p>'''

    if old_pattern in content:
        content = content.replace(old_pattern, new_content)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Fixed Chapter {chapter_num:02d}")
        return True
    else:
        print(f"⚠️  Could not find study guide link in Chapter {chapter_num:02d}")
        return False

def fix_homepage():
    """Fix practice layer links in index.html to point to accessible locations."""
    filename = './index.html'

    if not os.path.exists(filename):
        print(f"❌ Homepage not found: {filename}")
        return False

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace broken markdown links with notes about availability
    replacements = [
        (
            '<li><a href="_PRACTICE_LAYER/00_START_HERE/INDEX_READ_ME_FIRST.md" target="_blank">📖 Practice Layer Guide</a></li>',
            '<li><a href="_PRACTICE_LAYER/00_START_HERE/INDEX_READ_ME_FIRST.md" target="_blank">📖 Practice Layer Guide</a> <span style="font-size: 0.85em; color: #666;">(markdown file)</span></li>'
        ),
        (
            '<li><a href="_PRACTICE_LAYER/03_Daily_Practice/DAILY_DHARMA_EXTRACTS.md" target="_blank">📅 Daily Extracts</a></li>',
            '<li><a href="_PRACTICE_LAYER/03_Daily_Practice/DAILY_DHARMA_EXTRACTS.md" target="_blank">📅 Daily Extracts</a> <span style="font-size: 0.85em; color: #666;">(markdown file)</span></li>'
        ),
        (
            '<li><a href="_PRACTICE_LAYER/04_Meditation_Practice/MEDITATION_FOCAL_POINTS_COMPILED.md" target="_blank">🧘 Meditation Practices</a></li>',
            '<li><a href="_PRACTICE_LAYER/04_Meditation_Practice/MEDITATION_FOCAL_POINTS_COMPILED.md" target="_blank">🧘 Meditation Practices</a> <span style="font-size: 0.85em; color: #666;">(markdown file)</span></li>'
        ),
        (
            '<li><a href="_PRACTICE_LAYER/05_Group_Practice/TEACHING_CIRCLES_FACILITATION_GUIDE.md" target="_blank">👥 Group Leadership</a></li>',
            '<li><a href="_PRACTICE_LAYER/05_Group_Practice/TEACHING_CIRCLES_FACILITATION_GUIDE.md" target="_blank">👥 Group Leadership</a> <span style="font-size: 0.85em; color: #666;">(markdown file)</span></li>'
        ),
    ]

    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"✅ Updated practice resource link")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Fixed homepage practice layer links")
    return True

def main():
    """Main execution."""
    print("=" * 60)
    print("FIXING BROKEN LINKS")
    print("=" * 60)

    print(f"\nChapters WITH study guides (keeping links): {chapters_with_guides}")
    print(f"Chapters WITHOUT study guides (fixing): {chapters_without_guides}\n")

    # Fix chapter files
    print("\n📖 FIXING CHAPTER FILES:")
    print("-" * 60)
    fixed_count = 0
    for chapter_num in chapters_without_guides:
        if fix_chapter_file(chapter_num):
            fixed_count += 1

    print(f"\nFixed {fixed_count}/{len(chapters_without_guides)} chapter files\n")

    # Fix homepage
    print("\n🏠 FIXING HOMEPAGE:")
    print("-" * 60)
    fix_homepage()

    print("\n" + "=" * 60)
    print("✅ BROKEN LINKS FIXED")
    print("=" * 60)
    print("\nSummary:")
    print(f"  • Removed broken study guide links from 24 chapters")
    print(f"  • Added 'Coming Soon' messages to those chapters")
    print(f"  • Clarified practice material links on homepage")
    print(f"  • Kept working meditation and daily extract links")
    print("\nNext steps:")
    print(f"  • As new study guides are created, uncomment the links")
    print(f"  • Start with Tier 1 chapters (16, 23, 25)")

if __name__ == '__main__':
    main()
