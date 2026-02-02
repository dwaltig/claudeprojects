#!/usr/bin/env python3
"""
Scholarly Agent CLI - Command-line interface for running custom tasks

Usage:
    python3 scripts/agent_cli.py "Your task prompt here"

Examples:
    python3 scripts/agent_cli.py "Analyze terminology in Lotus Sutra"
    python3 scripts/agent_cli.py "Check diacriticals in Diamond Sutra"
    python3 scripts/agent_cli.py "Find inconsistent Buddhist terms in all projects"
"""

import sys
from pathlib import Path
from scholarly_agent import ScholarlyAgent


def main():
    if len(sys.argv) < 2:
        print("📖 Scholarly Agent CLI")
        print("=" * 80)
        print()
        print("Usage:")
        print("    python3 scripts/agent_cli.py \"Your task prompt here\"")
        print()
        print("Examples:")
        print("    python3 scripts/agent_cli.py \"Analyze terminology in Lotus Sutra\"")
        print("    python3 scripts/agent_cli.py \"Check diacriticals in Diamond Sutra\"")
        print("    python3 scripts/agent_cli.py \"Find inconsistent terms in Dhammapada\"")
        print()
        print("Supported task types:")
        print("  • Terminology analysis (finds variant spellings, capitalization issues)")
        print("  • Diacritical validation (checks UTF-8 encoding, Sanskrit marks)")
        print("  • General file analysis")
        print()
        print("Project detection:")
        print("  Mention any project name in your prompt:")
        print("  - Dhammapada, Lotus (Sutra), Diamond (Sutra), Surangama, Vimalakirti")
        print()
        print("File type filters:")
        print("  - 'scholarly' → Only scholarly translations")
        print("  - 'blues' → Only blues interpretations")
        print()
        return

    # Get task from command line
    task = " ".join(sys.argv[1:])

    print("🤖 Scholarly Agent CLI")
    print("=" * 80)
    print(f"📋 Task: {task}")
    print("=" * 80)
    print()

    # Initialize agent
    workspace = Path("/Users/williamaltig/claudeprojects")
    agent = ScholarlyAgent(workspace)

    # Execute task
    try:
        output = agent.execute_task(task)

        # Display report
        print()
        print(output['report'])

        # Save results
        output_dir = workspace / "scripts"

        # Save JSON results
        import json
        output_path = output_dir / "agent_output.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            serializable_output = {
                'plan': output['plan'],
                'results': {
                    k: v for k, v in output['results'].items()
                    if k not in ['terms_by_file']  # Skip large nested data
                },
                'execution_log': output['execution_log']
            }
            json.dump(serializable_output, f, indent=2, ensure_ascii=False)

        print(f"\n💾 Detailed results saved to: {output_path}")

        # Save text report
        report_path = output_dir / "agent_report.txt"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(output['report'])

        print(f"📄 Report saved to: {report_path}")

    except Exception as e:
        print(f"\n❌ Error executing task: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
