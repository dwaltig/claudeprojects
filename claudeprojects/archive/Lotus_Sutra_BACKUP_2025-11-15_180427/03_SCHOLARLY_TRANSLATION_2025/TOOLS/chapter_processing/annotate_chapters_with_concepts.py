#!/usr/bin/env python3
"""
Annotate chapter HTML files with data-concept attributes
Makes all concept mentions clickable in Reader Mode and Scholar Mode

Strategy:
1. Load lotus_concept_graph.json (Phase 1 concepts only)
2. For each chapter HTML file:
   - Find all occurrences of concept terms
   - Wrap in <span class="concept-link" data-concept="id">term</span>
   - Handle variant spellings (with/without diacritics)
3. Output annotated chapters
4. Track which concepts were found in which chapters
"""

import re
import json
from pathlib import Path
from html.parser import HTMLParser

def load_concept_graph():
    """Load lotus_concept_graph.json and extract Phase 1 concepts"""

    with open('lotus_concept_graph.json', 'r', encoding='utf-8') as f:
        graph = json.load(f)

    # Extract only Phase 1 concepts for this phase
    phase1_concepts = [c for c in graph['concepts'] if c['phase'] == 'phase1']

    # Sort by term length (longest first) to avoid partial matching issues
    phase1_concepts.sort(key=lambda x: len(x['term']), reverse=True)

    return phase1_concepts

def create_variant_spellings(term):
    """Create variant spellings for Sanskrit terms with diacritics"""

    variants = [term]

    # Common diacritic simplifications
    diacritic_map = {
        'ā': 'a', 'ī': 'i', 'ū': 'u', 'ē': 'e', 'ō': 'o',
        'ṃ': 'm', 'ṇ': 'n', 'ś': 's', 'ṣ': 's',
        'ñ': 'n', 'č': 'c', 'ř': 'r'
    }

    # Create simplified variant
    simplified = term
    for accented, plain in diacritic_map.items():
        simplified = simplified.replace(accented, plain)

    if simplified != term:
        variants.append(simplified)

    return variants

def annotate_chapter_file(chapter_path, concepts):
    """Annotate a single chapter file with concept links"""

    with open(chapter_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    annotations_made = 0
    concepts_found = {}

    # Process each concept
    for concept in concepts:
        term = concept['term']
        concept_id = concept['id']
        variants = create_variant_spellings(term)

        # Create pattern that matches the term but avoids already-wrapped spans
        # Pattern: word boundary + term + word boundary, but NOT if already in span.concept-link
        for variant in variants:
            # Escape special regex characters in the variant
            escaped_variant = re.escape(variant)

            # Pattern: match the variant if it's not already inside a span.concept-link
            # Use negative lookbehind/lookahead to avoid matching inside tags
            pattern = rf'(?<!</span>)(?<![>"])\b({escaped_variant})\b(?![^<]*</span>)'

            def replace_func(match):
                nonlocal annotations_made
                original_text = match.group(1)

                # Skip if already wrapped in a span
                # Check context
                start_pos = match.start()
                surrounding = content[max(0, start_pos - 100):start_pos + 100]

                if 'data-concept=' in surrounding:
                    return original_text

                annotations_made += 1
                if concept_id not in concepts_found:
                    concepts_found[concept_id] = 0
                concepts_found[concept_id] += 1

                return f'<span class="concept-link" data-concept="{concept_id}">{original_text}</span>'

            # Use re.sub to replace all occurrences
            content = re.sub(pattern, replace_func, content, flags=re.IGNORECASE)

            # Only use first variant if it matched
            if annotations_made > 0:
                break

    # Check if changes were made
    if content != original_content:
        with open(chapter_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return annotations_made, concepts_found

def annotate_all_chapters(concepts, chapters_dir='chapters'):
    """Annotate all chapter files"""

    chapters_path = Path(chapters_dir)
    chapters_files = sorted(chapters_path.glob('chapter_*.html'))

    total_annotations = 0
    all_concepts_found = {}

    for chapter_file in chapters_files:
        chapter_num = int(chapter_file.stem.split('_')[1])

        annotations, found = annotate_chapter_file(chapter_file, concepts)
        total_annotations += annotations

        # Track which concepts were found
        for concept_id, count in found.items():
            if concept_id not in all_concepts_found:
                all_concepts_found[concept_id] = {}
            all_concepts_found[concept_id][chapter_num] = count

    return total_annotations, all_concepts_found

def create_annotation_report(concepts, annotations_report):
    """Create a report of annotation coverage"""

    concept_map = {c['id']: c for c in concepts}

    annotated_count = len(annotations_report)
    unannotated_count = len(concepts) - annotated_count

    print(f"\n{'='*80}")
    print(f"CHAPTER ANNOTATION COMPLETE")
    print(f"{'='*80}\n")

    print(f"📊 Annotation Summary:")
    print(f"   Total Phase 1 Concepts: {len(concepts)}")
    print(f"   Concepts Found in Text: {annotated_count}")
    print(f"   Concepts Not Yet Found: {unannotated_count}")

    # Show unannotated concepts
    unannotated = [c for c in concepts if c['id'] not in annotations_report]
    if unannotated:
        print(f"\n⚠️  Concepts without annotations (may need manual checking):")
        for concept in unannotated[:20]:  # Show first 20
            print(f"   - {concept['term']:30s} (Chapters: {concept['chapters']})")
        if len(unannotated) > 20:
            print(f"   ... and {len(unannotated) - 20} more")

    # Show top annotated concepts
    print(f"\n🎯 Top 15 Most Annotated Concepts:")
    top_concepts = sorted(
        annotations_report.items(),
        key=lambda x: sum(x[1].values()),
        reverse=True
    )[:15]

    for i, (concept_id, chapters) in enumerate(top_concepts, 1):
        concept = concept_map.get(concept_id)
        if concept:
            total_count = sum(chapters.values())
            chapter_list = ', '.join(map(str, sorted(chapters.keys())))
            print(f"   {i:2d}. {concept['term']:25s} ({total_count:3d} occurrences) Chapters: {chapter_list}")

    print(f"\n{'='*80}\n")

    return annotated_count, unannotated_count

def main():
    print("\n" + "="*80)
    print("ANNOTATING CHAPTERS WITH CONCEPT LINKS")
    print("="*80 + "\n")

    print("Step 1: Loading concept graph...")
    concepts = load_concept_graph()
    print(f"  ✓ Loaded {len(concepts)} Phase 1 concepts")

    print("\nStep 2: Creating variant spellings for matching...")
    print(f"  ✓ Ready to match Sanskrit and English terms")

    print("\nStep 3: Annotating chapter files...")
    total_annotations, annotations_report = annotate_all_chapters(concepts)
    print(f"  ✓ Created {total_annotations} concept links across all chapters")

    print("\nStep 4: Generating annotation report...")
    annotated_count, unannotated_count = create_annotation_report(concepts, annotations_report)

    print("✅ All chapters annotated with data-concept attributes!")
    print(f"   Ready for Reader Mode and Scholar Mode implementation.")

if __name__ == "__main__":
    main()
