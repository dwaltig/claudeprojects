# Article 1: Data Gathering Checklist

**Purpose**: Collect all empirical data needed for Article 1 from Lotus Sutra project
**Status**: Ready to gather
**Timeline**: Week 1-2

---

## Data Sources (From Lotus Sutra Project)

### Primary Source Files
- `/Lotus_Sutra/04_AUDIO_PRODUCTION/AUDIO_PRODUCTION_MASTER_GUIDE.txt`
- `/Lotus_Sutra/04_AUDIO_PRODUCTION/chapters/*.txt` (30 chapter files)
- `/Lotus_Sutra/08_REFERENCE_MATERIALS/CHARACTER_VOICE_MAPPING_FINAL.txt`
- `/Lotus_Sutra/08_REFERENCE_MATERIALS/VOICE_CASTING_GUIDE.txt`
- `/Lotus_Sutra/documentation/DEVLOG.md`

---

## Data Collection Tasks

### ✅ COMPLETED (From Data Audit)

**Overall metrics**:
- [x] Total word count: ~200,000 words (blues interpretation)
- [x] Total chapters: 28
- [x] Voice tags total: 553
- [x] Distinct voices used: 15
- [x] Estimated audio duration: 18-22 hours
- [x] Estimated cost: $300-1,000

### 🔲 PENDING (Need to Extract)

#### 1. Voice Tag Distribution (For Table 1 & Figure 1)

**Need to count**:
- [ ] Charon tags: ___ (currently estimated 211, 38%)
- [ ] Iapetus tags: ___ (currently estimated 60, 11%)
- [ ] Rasalgethi tags: ___ (currently estimated 54, 10%)
- [ ] Orus tags: ___ (currently estimated 42, 8%)
- [ ] Puck tags: ___ (currently estimated 28, 5%)
- [ ] Other voices (10 remaining): ___ each

**Command to run**:
```bash
cd /Users/williamaltig/claudeprojects/Lotus_Sutra/04_AUDIO_PRODUCTION/chapters
grep -oh "\[Charon\]:" *.txt | wc -l
grep -oh "\[Iapetus\]:" *.txt | wc -l
# Repeat for each voice...
```

**Output format** (Table 1):
| Voice | Character(s) | Tags | % of Total | Dharma Role | Rationale |
|-------|-------------|------|------------|-------------|-----------|
| Charon | Narrator (Ānanda) | ___ | ___% | Cosmic presence | Deep baritone, weight of ages |
| ... | ... | ... | ... | ... | ... |

---

#### 2. Verse Optimization Examples (For Table 2)

**Need to extract**:
- [ ] 3-5 before/after verse examples
- [ ] Token count for each (pre-optimization)
- [ ] Token count for each (post-optimization)
- [ ] % reduction calculated

**Example passages to find**:
- Chapter 2 verse section (Expedient Means)
- Chapter 3 verse section (Burning House parable)
- Chapter 16 verse section (Buddha's Lifespan)

**Format needed**:
```
BEFORE (unoptimized):
The Buddha's wisdom is profound,
Difficult to understand.
All the śrāvakas and pratyekabuddhas
Cannot fathom it.

[Token count: X tokens]

AFTER (optimized):
The Buddha's wisdom is profound, difficult to understand. All the śrāvakas and pratyekabuddhas cannot fathom it.

[Token count: Y tokens]
[Reduction: Z%]
```

---

#### 3. Character Inventory (For Appendix A)

**Need to document**:
- [ ] All 50+ speaking characters across 28 chapters
- [ ] Which chapters they appear in
- [ ] Their dharma role/relationship to Buddha
- [ ] Gender (for voice alignment rationale)

**Major characters to include**:
- Buddha (multiple voices depending on context)
- Śāriputra (chief disciple)
- Mahākāśyapa (elder disciple)
- Mañjuśrī (Bodhisattva of Wisdom)
- Avalokiteśvara (Bodhisattva of Compassion)
- Maitreya (future Buddha)
- Narrator (Ānanda's voice)
- Parable characters (rich man, physician, etc.)

**Source**: `/Lotus_Sutra/08_REFERENCE_MATERIALS/CHARACTER_VOICE_MAPPING_FINAL.txt` (first 50 lines already read)

---

#### 4. Production Timeline Details (For Figure 3)

**Need to document from DEVLOG.md**:
- [ ] Phase 1: Initial optimization request (date range, chapters covered)
- [ ] Phase 2: Interpretation notes discovery (date, issue identified)
- [ ] Phase 3: File corruption correction (date, problem/solution)
- [ ] Phase 4: Extraction from master file (date, final solution)
- [ ] Phase 5: Voice tag insertion (estimated time)
- [ ] Phase 6: Verification and QC (estimated time)

**Total timeline**: Weeks or months?

---

#### 5. Cost Calculations (For Table 4)

**TTS costs (need to estimate)**:
- [ ] Average tokens per chapter: ___
- [ ] Gemini API cost per 1M tokens: $___
- [ ] Total chapters: 28
- [ ] Estimated total cost: $___

**Professional narration costs (research)**:
- [ ] Industry standard: $200-300 per finished hour (PFH)
- [ ] 18-22 hours × $200 = $3,600-6,600 (low end)
- [ ] 18-22 hours × $300 = $5,400-6,600 (high end)
- [ ] Voice talent + production + editing: $50,000+ (premium)

**Comparison**:
- TTS: $300-1,000
- Professional: $50,000+
- **Savings: 98-99%**

---

#### 6. Quality Control Incidents (For Discussion)

**Need to extract from DEVLOG.md and git log**:
- [ ] Encoding corruption incidents: ___ (zero expected based on audit)
- [ ] Content fidelity issues: ___ (zero expected)
- [ ] Git commits total: ___
- [ ] Revisions/iterations: ___ (mentioned "5 optimization rounds" in audit)

**Git commands to run**:
```bash
cd /Users/williamaltig/claudeprojects/Lotus_Sutra
git log --oneline --grep="audio" --grep="voice" --grep="chapter" | wc -l
git log --oneline --author="Claude" --since="2024-01-01" | wc -l
```

---

#### 7. Prose vs. Verse Ratio (For Methods Section Context)

**Need to calculate**:
- [ ] Approximate % of text that is verse (vs. prose narrative)
- [ ] Which chapters are verse-heavy vs. prose-heavy
- [ ] Implications for optimization impact

**Method**:
- Scan 3-5 sample chapters
- Count paragraphs that are verse vs. prose
- Estimate ratio

---

## Figures to Create

### Figure 1: Voice Tag Frequency Distribution
**Type**: Horizontal bar chart
**Data needed**: Voice name + tag count (from task #1 above)
**X-axis**: Number of tags (0-250 range)
**Y-axis**: Voice names (15 voices)
**Highlight**: Top 3 voices (Charon, Iapetus, Rasalgethi)

**Tools**: Excel, Google Sheets, Python matplotlib, or online chart maker

---

### Figure 2: API Efficiency Gains
**Type**: Before/after comparison chart
**Data needed**: Token counts from task #2
**Options**:
- Stacked bar chart (before/after for 5 sample verses)
- Line graph (token reduction trend)
- Percentage reduction summary (simple visual)

---

### Figure 3: Production Timeline
**Type**: Gantt chart or process flowchart
**Data needed**: Phase timeline from task #4
**Shows**:
- Week 1: Chapter extraction
- Week 2: Voice tag insertion
- Week 3: Verse optimization
- Week 4: Quality control
- Total: 1-2 weeks

---

## Tables to Create

### Table 1: Complete Voice Mapping
**Columns**: Voice | Character(s) | Tags | % | Dharma Role | Rationale
**Rows**: 15 voices
**Data source**: Task #1 + CHARACTER_VOICE_MAPPING_FINAL.txt

---

### Table 2: Verse Optimization Examples
**Columns**: Chapter | Before | After | Tokens Before | Tokens After | Reduction %
**Rows**: 3-5 example verses
**Data source**: Task #2

---

### Table 3: Quality Control Checklist
**Columns**: Check Item | Verification Method | Status
**Rows**: 5-7 QC items
**Data source**: Before/After checklist in OUTLINE_v1.md

---

### Table 4: Cost Comparison
**Columns**: Method | Cost Range | Timeline | Quality
**Rows**:
- TTS (our method)
- Professional human narration (Ocean Library model)
- DIY reading/recording

**Data source**: Task #5

---

## Quotes to Extract

### From AUDIO_PRODUCTION_MASTER_GUIDE.txt
- [ ] Quote on voice configuration
- [ ] Quote on production status ("READY FOR PROFESSIONAL RECORDING")
- [ ] Quote on manuscript status ("All 553 voice tags verified")

### From CHARACTER_VOICE_MAPPING_FINAL.txt
- [ ] Quote on voice philosophy ("Voice as Dharma Gateway")
- [ ] Quote on Charon's role ("cosmic gravitas, eternal presence")
- [ ] Quote on gender alignment rationale

### From DEVLOG.md
- [ ] Quote on 4-rule verse formatting system
- [ ] Quote on alignment requirement ("Please make sure the text for each chapter aligns with the master file")
- [ ] Quote on fidelity preservation ("100% - no words, meanings, or sacred terminology modified")

---

## Writing Resources Ready

**Dr. Amara Chen-Rothenberg Agent**: `/Lotus_Sutra/agents/02_scholarly-writer-agent_dr-amara-chen-rothenberg.md`

**Credentials to reference**:
- PhD Buddhist Studies (Harvard)
- MS Computational Linguistics (MIT)
- 40+ peer-reviewed articles
- Expertise: Buddhist translation theory, digital humanities, vernacular scripture

**Voice characteristics**:
- Scholarly but accessible
- Rigorous methodology
- Theoretical framing + empirical grounding
- Citations to establish authority

---

## Next Actions

**Week 1** (Data Gathering):
1. Run bash commands to count voice tags (task #1)
2. Extract verse examples with token counts (task #2)
3. Review CHARACTER_VOICE_MAPPING for full character list (task #3)
4. Extract timeline from DEVLOG.md (task #4)
5. Calculate cost estimates (task #5)

**Week 2** (Figure/Table Creation):
1. Create Figure 1 (voice frequency bar chart)
2. Create Figure 2 (API efficiency comparison)
3. Create Table 1 (complete voice mapping)
4. Create Table 2 (verse optimization examples)
5. Create Table 4 (cost comparison)

**Week 3-4** (Drafting):
1. Write Introduction (1,200 words)
2. Write Background (1,500 words)
3. Write Methods (2,000 words)
4. Write Results (1,500 words)
5. Write Discussion (1,500 words)
6. Write Conclusion (500 words)

**Total**: 8,200 words (within 6,000-8,000 target range after editing)

---

**Status**: Ready to begin data gathering
**Next Step**: Run bash commands to count voice tags (see task #1)
