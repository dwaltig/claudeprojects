#!/usr/bin/env python3
"""
Extract concept graph from GLOSSARY_BUDDHIST_TERMS.md
Builds lotus_concept_graph.json for Reader Mode + Scholar Mode

Process:
1. Parse glossary markdown
2. Extract all concepts with definitions, Sanskrit, chapters
3. Identify concept relationships
4. Cross-reference with chapter files for verse appearances
5. Output structured JSON
"""

import re
import json
from pathlib import Path
from collections import defaultdict

def parse_glossary():
    """Parse GLOSSARY_BUDDHIST_TERMS.md and extract concepts"""

    glossary_path = Path("GLOSSARY_BUDDHIST_TERMS.md")

    with open(glossary_path, 'r', encoding='utf-8') as f:
        content = f.read()

    concepts = []
    current_concept = None

    # Split by concept headers (### Term Name)
    concept_blocks = re.split(r'^### ', content, flags=re.MULTILINE)[1:]

    for block in concept_blocks:
        lines = block.split('\n')
        if not lines:
            continue

        # First line is the concept header
        header = lines[0].strip()

        # Extract term and description
        match = re.match(r'(.+?)\s*\((.+?)\)', header)
        if match:
            term = match.group(1).strip()
            english_desc = match.group(2).strip()
        else:
            term = header.strip()
            english_desc = ""

        # Create concept ID (lowercase, underscores)
        concept_id = re.sub(r'[^a-z0-9]+', '_', term.lower()).strip('_')

        # Extract Sanskrit
        sanskrit = ""
        definition = ""
        chapters_str = ""
        related_concepts = []

        content_section = '\n'.join(lines[1:])

        # Extract Sanskrit
        sanskrit_match = re.search(r'\*\*Sanskrit\*\*:\s*(.+?)(?:\n|$)', content_section)
        if sanskrit_match:
            sanskrit = sanskrit_match.group(1).strip()

        # Extract Definition
        definition_match = re.search(r'\*\*Definition\*\*:\s*(.+?)(?:\n\n|\n\*\*)', content_section, re.DOTALL)
        if definition_match:
            definition = definition_match.group(1).strip()
            # Clean up markdown links and extra whitespace
            definition = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', definition)
            definition = re.sub(r'\n\s+', ' ', definition)

        # Extract Chapters
        chapters_match = re.search(r'\*\*Chapters\*\*:\s*(.+?)(?:\n|$)', content_section)
        if chapters_match:
            chapters_str = chapters_match.group(1).strip()
            # Parse chapters: "1, 2, 3, 6, 7, 8"
            chapters = [int(x.strip()) for x in chapters_str.split(',') if x.strip().isdigit()]
        else:
            chapters = []

        # Extract Associated/Related Concepts
        related_match = re.search(r'\*\*(?:Associated|Related) Concepts?\*\*:\s*(.+?)(?:\n|$)', content_section)
        if related_match:
            related_str = related_match.group(1).strip()
            # Parse related: "Buddha-nature, enlightenment, bodhi, wisdom (prajñā)"
            related_concepts = [
                re.sub(r'\s*\(.+?\)', '', x.strip()).lower().replace(' ', '-')
                for x in related_str.split(',')
                if x.strip()
            ]

        # Determine concept depth/importance based on chapter count and glossary position
        depth = len(chapters)
        if depth >= 8:
            importance = "core"
        elif depth >= 4:
            importance = "central"
        else:
            importance = "supporting"

        concepts.append({
            'id': concept_id,
            'term': term,
            'english_desc': english_desc,
            'sanskrit': sanskrit,
            'definition': definition,
            'chapters': sorted(chapters),
            'related_concepts': related_concepts,
            'importance': importance,
            'depth': depth,
            'color': assign_color(importance)
        })

    return concepts

def assign_color(importance):
    """Assign color codes based on concept importance"""
    colors = {
        'core': '#16a085',        # Teal - primary
        'central': '#3498db',      # Blue - secondary
        'supporting': '#95a5a6'    # Gray - tertiary
    }
    return colors.get(importance, '#95a5a6')

def find_verse_references(concepts, chapters_dir='chapters'):
    """Cross-reference concepts with chapter HTML files to find verse appearances"""

    chapters_path = Path(chapters_dir)

    for concept in concepts:
        concept['verses'] = []

        for chapter_num in concept['chapters']:
            chapter_file = chapters_path / f'chapter_{chapter_num:02d}.html'

            if not chapter_file.exists():
                continue

            try:
                with open(chapter_file, 'r', encoding='utf-8') as f:
                    chapter_content = f.read()

                # Look for the concept term in verses
                # Match verse-line paragraphs containing the term
                term_variations = [
                    concept['term'],
                    concept['term'].replace('ā', 'a').replace('ī', 'i').replace('ū', 'u'),
                ]

                for variation in term_variations:
                    if variation.lower() in chapter_content.lower():
                        # Extract snippet around the occurrence
                        pattern = rf'<p class="verse-line">([^<]*{re.escape(variation)}[^<]*)</p>'
                        matches = re.findall(pattern, chapter_content, re.IGNORECASE)

                        if matches:
                            for match in matches[:2]:  # Limit to first 2 occurrences per chapter
                                # Clean HTML
                                verse_text = re.sub(r'<[^>]+>', '', match).strip()
                                concept['verses'].append({
                                    'chapter': chapter_num,
                                    'text': verse_text[:100] + '...' if len(verse_text) > 100 else verse_text,
                                    'full_text': verse_text
                                })
                        break

            except Exception as e:
                print(f"Warning: Could not read {chapter_file}: {e}")

    return concepts

def rank_concepts_by_importance(concepts):
    """Rank concepts for Phase 1 launch (core + high-depth concepts)"""

    # Scoring: importance + depth + chapter variety
    for concept in concepts:
        score = 0

        # Importance scoring
        importance_score = {'core': 3, 'central': 2, 'supporting': 1}
        score += importance_score.get(concept['importance'], 0) * 10

        # Depth scoring (appears in many chapters)
        score += min(concept['depth'], 10) * 2

        # Relationship scoring (has many related concepts)
        score += len(concept['related_concepts'])

        concept['launch_score'] = score

    # Sort by score
    ranked = sorted(concepts, key=lambda x: x['launch_score'], reverse=True)

    # Mark top 75-100 for Phase 1
    for i, concept in enumerate(ranked):
        if i < 75:
            concept['phase'] = 'phase1'
        elif i < 150:
            concept['phase'] = 'phase2'
        else:
            concept['phase'] = 'phase3'

    return concepts

def build_relationships_graph(concepts):
    """Build concept relationship graph"""

    relationships = []
    concept_map = {c['id']: c for c in concepts}

    for concept in concepts:
        for related_id in concept['related_concepts']:
            if related_id in concept_map:
                relationships.append({
                    'from': concept['id'],
                    'to': related_id,
                    'type': 'related_to',
                    'bidirectional': True
                })

    return relationships

def output_concept_graph(concepts, relationships, output_file='lotus_concept_graph.json'):
    """Output structured JSON concept graph"""

    # Summary stats
    phase1_count = len([c for c in concepts if c['phase'] == 'phase1'])
    phase2_count = len([c for c in concepts if c['phase'] == 'phase2'])
    phase3_count = len([c for c in concepts if c['phase'] == 'phase3'])

    graph = {
        'metadata': {
            'title': 'Lotus Sutra Concept Graph',
            'description': '186 Buddhist concepts with relationships, Sanskrit terms, and chapter references',
            'total_concepts': len(concepts),
            'phase1_launch': phase1_count,
            'phase2_expansion': phase2_count,
            'phase3_completion': phase3_count,
            'total_relationships': len(relationships),
            'version': '1.0'
        },
        'concepts': concepts,
        'relationships': relationships
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)

    return graph

def print_summary(graph):
    """Print extraction summary"""

    metadata = graph['metadata']

    print(f"\n{'='*80}")
    print(f"CONCEPT GRAPH EXTRACTION COMPLETE")
    print(f"{'='*80}\n")

    print(f"📚 Total Concepts Extracted: {metadata['total_concepts']}")
    print(f"🔗 Total Relationships: {metadata['total_relationships']}")
    print(f"\n📊 Phase Distribution:")
    print(f"   Phase 1 (Launch):    {metadata['phase1_launch']} concepts - Ready for immediate use")
    print(f"   Phase 2 (Expansion): {metadata['phase2_expansion']} concepts - Add after launch feedback")
    print(f"   Phase 3 (Complete):  {metadata['phase3_completion']} concepts - Long-term growth")

    # Show top Phase 1 concepts
    phase1 = [c for c in graph['concepts'] if c['phase'] == 'phase1']
    phase1_sorted = sorted(phase1, key=lambda x: x['launch_score'], reverse=True)

    print(f"\n🎯 Top 10 Phase 1 Concepts (by importance):")
    for i, concept in enumerate(phase1_sorted[:10], 1):
        print(f"   {i:2d}. {concept['term']:30s} (Score: {concept['launch_score']:3d}, Chapters: {concept['depth']})")

    # Verse coverage
    verse_count = sum(len(c['verses']) for c in phase1)
    print(f"\n📖 Verse References (Phase 1):")
    print(f"   Total verse appearances: {verse_count}")

    # Concept importance distribution
    importance_dist = {'core': 0, 'central': 0, 'supporting': 0}
    for c in phase1:
        importance_dist[c['importance']] += 1

    print(f"\n📈 Phase 1 Importance Distribution:")
    print(f"   Core concepts:       {importance_dist['core']}")
    print(f"   Central concepts:    {importance_dist['central']}")
    print(f"   Supporting concepts: {importance_dist['supporting']}")

    print(f"\n✅ Output: {metadata['title']} (lotus_concept_graph.json)")
    print(f"\nReady for Reader Mode + Scholar Mode implementation!")
    print(f"{'='*80}\n")

def main():
    print("\n" + "="*80)
    print("EXTRACTING CONCEPT GRAPH FROM GLOSSARY")
    print("="*80 + "\n")

    print("Step 1: Parsing glossary markdown...")
    concepts = parse_glossary()
    print(f"  ✓ Extracted {len(concepts)} concepts")

    print("\nStep 2: Finding verse references in chapters...")
    concepts = find_verse_references(concepts)
    print(f"  ✓ Cross-referenced with chapter files")

    print("\nStep 3: Ranking concepts by importance...")
    concepts = rank_concepts_by_importance(concepts)
    print(f"  ✓ Scored and phased for launch")

    print("\nStep 4: Building relationship graph...")
    relationships = build_relationships_graph(concepts)
    print(f"  ✓ Built {len(relationships)} concept relationships")

    print("\nStep 5: Outputting JSON structure...")
    graph = output_concept_graph(concepts, relationships)
    print(f"  ✓ Generated lotus_concept_graph.json")

    print_summary(graph)

if __name__ == "__main__":
    main()
