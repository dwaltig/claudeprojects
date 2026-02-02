# Convergence Criteria Templates

Templates for evaluating when Ralph Loop iterations should terminate.

---

## Translation Convergence

**When to use:** Professor ↔ Bluesman translation cycles

### Success Criteria
| Criterion | Threshold | Weight |
|-----------|-----------|--------|
| Both agents sign off | Required | — |
| Character delta | < 5% | High |
| No doctrinal flags | 0 flags | Critical |
| No ghost characters | 0 flagged | Critical |
| Confidence scores | ≥ 8/10 avg | Medium |

### Sign-Off Phrases
The loop watches for these signals from agents:
- "No further changes recommended"
- "Translation approved as-is"
- "Satisfied with current rendering"
- "Sign-off complete"

### Interrupt Phrases
These phrases halt the loop for human review:
- "Doctrinal concern"
- "Requires human judgment"
- "Unresolvable tension between..."
- "Recommend expert consultation"

---

## Manuscript Review Convergence

**When to use:** JAR reviewer cycles

### Success Criteria
| Criterion | Threshold | Weight |
|-----------|-----------|--------|
| Reviewer score | ≥ 7/10 | Required |
| Recommendation | Accept or Minor Revisions | Required |
| Priority issues | All addressed | High |
| Word count | Within target ± 3% | Medium |

### Score Progression
Track improvement across iterations:
- Iteration 1: Score X
- Iteration 2: Score Y (expect Y > X)
- Stagnation: 3 iterations with < 0.5 point improvement

---

## Philological Audit Convergence

**When to use:** DeepSeek audit cycles

### Success Criteria
| Criterion | Threshold | Weight |
|-----------|-----------|--------|
| Sentence confidence | ≥ 8/10 all sentences | Required |
| Ghost characters | 0 flagged | Critical |
| Over-translation | 0 flagged | High |
| Source coverage | 100% | Required |

### Audit Signal Phrases
- "Philologically sound"
- "Source text fully represented"
- "No semantic drift detected"

---

## Convergence Calculation

### Character Delta Formula
```
delta = |chars_current - chars_previous| / chars_previous * 100
```

### Weighted Score
```python
def calculate_convergence_score(iteration_data):
    weights = {
        'signoff': 0.3,
        'delta': 0.25,
        'flags': 0.25,
        'confidence': 0.2
    }
    
    signoff_score = 1.0 if both_signed_off else 0.0
    delta_score = max(0, 1 - (delta / 10))  # 0-10% mapped to 1-0
    flag_score = 1.0 if no_critical_flags else 0.0
    conf_score = avg_confidence / 10
    
    return sum(weights[k] * v for k, v in scores.items())
```

**Converged when:** Weighted score ≥ 0.85

---

*Template created: January 10, 2026*
*For use with: Ralph Loop Orchestrator*
