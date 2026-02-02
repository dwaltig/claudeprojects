#!/usr/bin/env python3
"""
Scholarly Agent MVP - Autonomous Buddhist Text Analysis
Built on agentic loop architecture similar to Claude Cowork

This minimal viable agent demonstrates:
- Autonomous task planning and execution
- Multi-file analysis capabilities
- Terminology consistency checking
- Automated report generation
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict, Counter
from datetime import datetime


class ScholarlyAgent:
    """
    Autonomous agent for Buddhist scholarly work.

    Architecture:
    1. Planning: Decompose user request into actionable tasks
    2. Execution: Process files and analyze content
    3. Verification: Validate results and generate report
    """

    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.results = {}
        self.execution_log = []

    def log(self, message: str):
        """Log execution steps for transparency"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.execution_log.append(log_entry)
        print(log_entry)

    def execute_task(self, prompt: str) -> Dict:
        """
        Main agentic loop: Plan → Execute → Verify

        Args:
            prompt: Natural language task description

        Returns:
            Results dictionary with analysis and reports
        """
        self.log(f"🤖 Agent activated with task: {prompt}")

        # Phase 1: Planning
        plan = self._create_plan(prompt)
        self.log(f"📋 Created plan with {len(plan['steps'])} steps")

        # Phase 2: Execution
        results = self._execute_plan(plan)
        self.log(f"✅ Executed {len(results)} tasks")

        # Phase 3: Verification
        verified_results = self._verify_results(results)
        self.log(f"🔍 Verification complete")

        # Phase 4: Report Generation
        report = self._generate_report(verified_results)
        self.log(f"📄 Report generated")

        return {
            'plan': plan,
            'results': verified_results,
            'report': report,
            'execution_log': self.execution_log
        }

    def _create_plan(self, prompt: str) -> Dict:
        """
        Planning phase: Decompose task into steps

        For MVP, we support terminology analysis tasks
        """
        # Simple pattern matching for MVP
        # In production, this would use Claude API for intelligent planning

        if "terminology" in prompt.lower() or "consistency" in prompt.lower():
            return {
                'task_type': 'terminology_analysis',
                'steps': [
                    {'id': 1, 'action': 'scan_files', 'target': 'translation_files'},
                    {'id': 2, 'action': 'extract_terms', 'target': 'buddhist_terms'},
                    {'id': 3, 'action': 'analyze_consistency', 'target': 'term_usage'},
                    {'id': 4, 'action': 'identify_issues', 'target': 'inconsistencies'},
                    {'id': 5, 'action': 'generate_report', 'target': 'consistency_report'}
                ],
                'scope': self._detect_scope(prompt)
            }

        elif "diacritic" in prompt.lower() or "encoding" in prompt.lower():
            return {
                'task_type': 'diacritical_validation',
                'steps': [
                    {'id': 1, 'action': 'scan_files', 'target': 'all_text_files'},
                    {'id': 2, 'action': 'check_encoding', 'target': 'utf8_validation'},
                    {'id': 3, 'action': 'validate_diacriticals', 'target': 'sanskrit_marks'},
                    {'id': 4, 'action': 'identify_errors', 'target': 'encoding_issues'},
                    {'id': 5, 'action': 'generate_report', 'target': 'validation_report'}
                ],
                'scope': self._detect_scope(prompt)
            }

        else:
            # Default: general file analysis
            return {
                'task_type': 'general_analysis',
                'steps': [
                    {'id': 1, 'action': 'scan_files', 'target': 'all_files'},
                    {'id': 2, 'action': 'analyze_content', 'target': 'content_summary'},
                    {'id': 3, 'action': 'generate_report', 'target': 'analysis_report'}
                ],
                'scope': self._detect_scope(prompt)
            }

    def _detect_scope(self, prompt: str) -> Dict:
        """Detect which project/files to analyze from prompt"""
        scope = {
            'projects': [],
            'file_patterns': []
        }

        # Detect project mentions
        projects = ['dhammapada', 'lotus', 'diamond', 'surangama', 'vimalakirti']
        for project in projects:
            if project.lower() in prompt.lower():
                scope['projects'].append(project)

        # Default to all if none specified
        if not scope['projects']:
            scope['projects'] = ['dhammapada']  # Start with Dhammapada for MVP

        # Detect file type preferences
        if 'scholarly' in prompt.lower():
            scope['file_patterns'].append('*Scholarly*.md')
        if 'blues' in prompt.lower():
            scope['file_patterns'].append('*Blues*.md')

        # Default patterns
        if not scope['file_patterns']:
            scope['file_patterns'] = ['*.md', '*.txt']

        return scope

    def _execute_plan(self, plan: Dict) -> Dict:
        """Execute the planned steps"""
        results = {}

        if plan['task_type'] == 'terminology_analysis':
            results = self._execute_terminology_analysis(plan)
        elif plan['task_type'] == 'diacritical_validation':
            results = self._execute_diacritical_validation(plan)
        else:
            results = self._execute_general_analysis(plan)

        return results

    def _execute_terminology_analysis(self, plan: Dict) -> Dict:
        """Execute terminology consistency analysis"""
        self.log("🔍 Starting terminology analysis...")

        # Step 1: Scan and collect files
        files = self._scan_files(plan['scope'])
        self.log(f"📁 Found {len(files)} files to analyze")

        # Step 2: Extract Buddhist terms
        terms_by_file = {}
        all_terms = Counter()

        for file_path in files:
            terms = self._extract_buddhist_terms(file_path)
            terms_by_file[file_path] = terms
            all_terms.update(terms)

        self.log(f"📚 Extracted {len(all_terms)} unique terms")

        # Step 3: Analyze consistency
        inconsistencies = self._analyze_term_consistency(terms_by_file, all_terms)
        self.log(f"⚠️  Found {len(inconsistencies)} potential issues")

        # Step 4: Categorize issues
        categorized = self._categorize_issues(inconsistencies)

        return {
            'files_analyzed': len(files),
            'unique_terms': len(all_terms),
            'total_term_occurrences': sum(all_terms.values()),
            'terms_by_file': terms_by_file,
            'all_terms': dict(all_terms.most_common(50)),  # Top 50 terms
            'inconsistencies': inconsistencies,
            'categorized_issues': categorized
        }

    def _scan_files(self, scope: Dict) -> List[Path]:
        """Scan workspace for relevant files"""
        files = []

        for project in scope['projects']:
            project_patterns = [
                f"{project.capitalize()}*/**/*.md",
                f"{project.capitalize()}*/**/*.txt",
                f"*{project}*/**/*.md",
                f"*{project}*/**/*.txt"
            ]

            for pattern in project_patterns:
                files.extend(self.workspace.glob(pattern))

        # Filter by scope patterns if specified
        if scope['file_patterns']:
            filtered = []
            for f in files:
                for pattern in scope['file_patterns']:
                    if f.match(pattern):
                        filtered.append(f)
                        break
            files = filtered

        # Remove duplicates and sort
        return sorted(list(set(files)))

    def _extract_buddhist_terms(self, file_path: Path) -> Counter:
        """Extract Buddhist terminology from a file"""
        terms = Counter()

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Define Buddhist term patterns
            term_patterns = [
                # Sanskrit/Pali with diacriticals
                r'\b[A-ZĀĪŪṂṆŚṢŁāīūṃṇśṣł][a-zāīūṃṇśṣł]+(?:[-][A-ZĀĪŪṂṆŚṢŁāīūṃṇśṣł][a-zāīūṃṇśṣł]+)*\b',
                # Common Buddhist terms (capitalized)
                r'\b(?:Buddha|Dharma|Sangha|Nirvana|Karma|Samsara|Bodhisattva|Tathagata|Arhat)\b',
                r'\b(?:Nirvāṇa|Saṃsāra|Dhamma|Kamma|Arahant)\b',
                # Character names
                r'\b(?:Śāriputra|Maudgalyāyana|Ānanda|Mahākāśyapa|Subhūti|Mañjuśrī|Avalokiteśvara)\b',
            ]

            for pattern in term_patterns:
                matches = re.findall(pattern, content)
                terms.update(matches)

        except Exception as e:
            self.log(f"⚠️  Error reading {file_path.name}: {e}")

        return terms

    def _analyze_term_consistency(self, terms_by_file: Dict, all_terms: Counter) -> List[Dict]:
        """Analyze terminology for consistency issues"""
        issues = []

        # Check for variant spellings (simplified for MVP)
        variants = self._find_variant_spellings(all_terms)

        for base_term, variant_list in variants.items():
            if len(variant_list) > 1:
                # Found inconsistency
                issue = {
                    'type': 'variant_spelling',
                    'severity': 'medium',
                    'base_term': base_term,
                    'variants': variant_list,
                    'occurrences': {v: all_terms[v] for v in variant_list},
                    'recommendation': f"Standardize to most common variant: {max(variant_list, key=lambda x: all_terms[x])}"
                }
                issues.append(issue)

        # Check for capitalization inconsistencies
        cap_issues = self._find_capitalization_issues(all_terms)
        issues.extend(cap_issues)

        return issues

    def _find_variant_spellings(self, terms: Counter) -> Dict[str, List[str]]:
        """Find variant spellings of the same term"""
        variants = defaultdict(list)

        # Group terms by normalized form
        for term in terms:
            # Normalize: lowercase, remove diacriticals for comparison
            normalized = term.lower()
            # Simple normalization (could be more sophisticated)
            normalized = normalized.replace('ā', 'a').replace('ī', 'i').replace('ū', 'u')
            normalized = normalized.replace('ṃ', 'm').replace('ṇ', 'n').replace('ś', 's')

            variants[normalized].append(term)

        # Filter to only those with actual variants
        return {k: v for k, v in variants.items() if len(v) > 1}

    def _find_capitalization_issues(self, terms: Counter) -> List[Dict]:
        """Find inconsistent capitalization"""
        issues = []

        # Group by case-insensitive comparison
        grouped = defaultdict(list)
        for term in terms:
            grouped[term.lower()].append(term)

        for lower_term, variants in grouped.items():
            if len(variants) > 1:
                # Found capitalization inconsistency
                issue = {
                    'type': 'capitalization',
                    'severity': 'low',
                    'term': lower_term,
                    'variants': variants,
                    'occurrences': {v: terms[v] for v in variants},
                    'recommendation': f"Standardize capitalization (suggest: {max(variants, key=lambda x: terms[x])})"
                }
                issues.append(issue)

        return issues

    def _categorize_issues(self, issues: List[Dict]) -> Dict:
        """Categorize issues by severity and type"""
        categorized = {
            'high_priority': [],
            'medium_priority': [],
            'low_priority': [],
            'by_type': defaultdict(list)
        }

        for issue in issues:
            severity = issue.get('severity', 'low')
            issue_type = issue.get('type', 'unknown')

            if severity == 'high':
                categorized['high_priority'].append(issue)
            elif severity == 'medium':
                categorized['medium_priority'].append(issue)
            else:
                categorized['low_priority'].append(issue)

            categorized['by_type'][issue_type].append(issue)

        return categorized

    def _execute_diacritical_validation(self, plan: Dict) -> Dict:
        """Execute diacritical mark validation"""
        self.log("🔍 Starting diacritical validation...")

        files = self._scan_files(plan['scope'])
        issues = []

        # Expected Sanskrit diacriticals
        valid_diacriticals = set('āīūṃṇśṣṭḍḥṛṝḷḹ')

        for file_path in files:
            try:
                with open(file_path, 'rb') as f:
                    raw_bytes = f.read()

                # Check encoding
                try:
                    content = raw_bytes.decode('utf-8')
                except UnicodeDecodeError as e:
                    issues.append({
                        'file': str(file_path),
                        'type': 'encoding_error',
                        'severity': 'high',
                        'message': f"File is not valid UTF-8: {e}"
                    })
                    continue

                # Check for suspicious character sequences
                # (e.g., combining diacritics vs precomposed)
                if '\u0301' in content or '\u0302' in content:  # Combining diacritics
                    issues.append({
                        'file': str(file_path),
                        'type': 'combining_diacritics',
                        'severity': 'medium',
                        'message': 'File contains combining diacritics instead of precomposed characters'
                    })

            except Exception as e:
                self.log(f"⚠️  Error checking {file_path.name}: {e}")

        return {
            'files_checked': len(files),
            'issues_found': len(issues),
            'issues': issues
        }

    def _execute_general_analysis(self, plan: Dict) -> Dict:
        """Execute general file analysis"""
        files = self._scan_files(plan['scope'])

        return {
            'files_found': len(files),
            'file_list': [str(f) for f in files]
        }

    def _verify_results(self, results: Dict) -> Dict:
        """Verification phase: Check results are valid"""
        self.log("🔍 Verifying results...")

        verified = results.copy()
        verified['verification'] = {
            'timestamp': datetime.now().isoformat(),
            'checks_passed': True,
            'warnings': []
        }

        # Basic sanity checks
        if 'files_analyzed' in results and results['files_analyzed'] == 0:
            verified['verification']['warnings'].append("No files were analyzed - check scope")

        if 'inconsistencies' in results and len(results['inconsistencies']) > 100:
            verified['verification']['warnings'].append(f"Large number of inconsistencies ({len(results['inconsistencies'])}) - may need refinement")

        return verified

    def _generate_report(self, results: Dict) -> str:
        """Generate human-readable report"""
        report_lines = [
            "=" * 80,
            "SCHOLARLY AGENT - ANALYSIS REPORT",
            "=" * 80,
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "SUMMARY",
            "-" * 80
        ]

        if 'files_analyzed' in results:
            report_lines.extend([
                f"Files analyzed: {results['files_analyzed']}",
                f"Unique terms found: {results.get('unique_terms', 0)}",
                f"Total term occurrences: {results.get('total_term_occurrences', 0)}",
                ""
            ])

        if 'inconsistencies' in results and results['inconsistencies']:
            report_lines.extend([
                "ISSUES FOUND",
                "-" * 80,
                f"Total issues: {len(results['inconsistencies'])}",
                ""
            ])

            categorized = results.get('categorized_issues', {})

            # High priority issues
            if categorized.get('high_priority'):
                report_lines.extend([
                    "HIGH PRIORITY:",
                    ""
                ])
                for issue in categorized['high_priority'][:10]:  # Top 10
                    report_lines.append(f"  • {issue['type']}: {issue.get('recommendation', 'Review needed')}")
                report_lines.append("")

            # Medium priority issues
            if categorized.get('medium_priority'):
                report_lines.extend([
                    "MEDIUM PRIORITY:",
                    ""
                ])
                for issue in categorized['medium_priority'][:10]:  # Top 10
                    report_lines.append(f"  • {issue['type']}: {issue.get('base_term', 'N/A')}")
                    if 'variants' in issue:
                        report_lines.append(f"    Variants: {', '.join(issue['variants'])}")
                    report_lines.append(f"    → {issue.get('recommendation', 'Review needed')}")
                    report_lines.append("")

        if 'all_terms' in results:
            report_lines.extend([
                "",
                "TOP TERMS (by frequency)",
                "-" * 80
            ])
            for term, count in list(results['all_terms'].items())[:20]:
                report_lines.append(f"  {term}: {count}")

        if 'verification' in results:
            report_lines.extend([
                "",
                "VERIFICATION",
                "-" * 80,
                f"Status: {'✅ PASSED' if results['verification']['checks_passed'] else '❌ FAILED'}"
            ])
            if results['verification']['warnings']:
                report_lines.append("Warnings:")
                for warning in results['verification']['warnings']:
                    report_lines.append(f"  ⚠️  {warning}")

        report_lines.extend([
            "",
            "=" * 80,
            "END OF REPORT",
            "=" * 80
        ])

        return "\n".join(report_lines)


def main():
    """Demo the agent with a sample task"""
    print("🤖 Scholarly Agent MVP - Initializing...\n")

    # Initialize agent with workspace path
    workspace = Path("/Users/williamaltig/claudeprojects")
    agent = ScholarlyAgent(workspace)

    # Example task
    task = "Analyze terminology consistency in Dhammapada translations"

    print(f"📋 Task: {task}\n")
    print("=" * 80)

    # Execute task
    output = agent.execute_task(task)

    # Display report
    print("\n")
    print(output['report'])

    # Save detailed results to JSON
    output_path = workspace / "scripts" / "agent_output.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        # Convert non-serializable objects
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

    # Save report to text file
    report_path = workspace / "scripts" / "agent_report.txt"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(output['report'])

    print(f"📄 Report saved to: {report_path}")


if __name__ == "__main__":
    main()
