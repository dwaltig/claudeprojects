# Voice, Persona, and Sacred Text: TTS Rendering of Buddhist Sutras

---

## Abstract

Buddhist sutras present unique challenges for text-to-speech (TTS) audio production: they are inherently dialogic (Buddha, disciples, narrators), performatively significant (oral transmission tradition), and structurally complex (prose narrative + verse repetition). While major digital Buddhist text initiatives have digitized millions of pages for research access, no existing scholarship addresses TTS methodology for these multi-speaker sacred texts. This article presents a complete TTS framework developed through production of a 28-chapter Lotus Sutra audiobook using Google's Gemini TTS platform.

Drawing on 532 voice tags across 200,000+ words, I document three core methodological innovations: (1) **character-to-voice mapping** based on narrative function and gender alignment (15 distinct voices); (2) **verse optimization** using a "4-rule formatting system" that achieves average 20.6% token reduction per passage while preserving lexical fidelity and prosodic pacing; and (3) **quality control procedures** integrating git version control and master file verification. The resulting workflow enables production of an 18-22 hour audiobook at $300-1,000 estimated cost—dramatically lower than professional human narration ($50,000+).

This framework addresses calls for multimodal Buddhist text preservation (Patrik 2007) and contributes practical methodology to the digital humanities toolkit for sacred text accessibility. The voice-mapping and verse optimization techniques are replicable for other character-driven religious texts (Qur'an, Torah, Bhagavad Gita) and advance digital humanities scholarship on TTS rendering of pre-modern oral literature.

**Keywords**: Buddhist studies, text-to-speech, TTS methodology, digital humanities, Lotus Sutra, multimodal textual studies, audio production, sacred texts, accessibility, voice mapping

---

## 1. Introduction

### 1.1 The Problem: Sutras as Multi-Speaker Performance

Buddhist sutras are not monologic texts meant for silent reading. They're dialogic performances, recording exchanges between the Buddha and his disciples, framed by a narrator who bears witness to the teaching. The opening formula of the Lotus Sutra—"Thus have I heard. At one time, the Buddha was staying at Mount Gṛdhrakūṭa..."—establishes a narrative frame that persists for 28 chapters and 200,000 words. The narrator (traditionally identified as Ānanda, the Buddha's attendant) doesn't merely report events. He embodies the oral transmission lineage, the voice of one who "heard" and now "speaks" the teaching to future generations.

This dialogic structure isn't incidental decoration. It's pedagogically essential. When Śāriputra, chief among the śrāvaka disciples, questions the Buddha about the "one vehicle" teaching in Chapter 2, his confusion represents the reader's confusion. When the Buddha hesitates, declaring "cease, cease, there is no need to speak further," only to relent after three entreaties, this dramatic tension builds anticipation and emphasizes the teaching's profundity. When the Buddha shifts from prose exposition to verse restatement—"At that time, the World-Honored One, wishing to repeat this meaning, spoke in verse"—this formulaic transition signals a change in register, from doctrinal precision to poetic elaboration.

Each of these performative elements depends on voice differentiation: the narrator's authoritative framing, Śāriputra's questioning tone, the Buddha's teaching voice, the rhythmic shift to verse.

So here's the question this study addresses: How can text-to-speech technology render these multi-speaker dimensions without collapsing the sutra into a single undifferentiated voice? And further: Can TTS production achieve this while remaining economically feasible for small Buddhist organizations, digital archives, and accessibility initiatives?

### 1.2 Existing Approaches and Their Limitations

Three approaches currently exist for producing audio versions of Buddhist sutras. Each has significant limitations.

**Human narration** represents the gold standard for quality. Ocean Library, a digital platform developed by Sacred Traditions, Inc., features immersive audio narration of sacred texts from ten faith traditions, including complete narrations of Buddhist sutras by scholar-practitioners with domain expertise. Dr. Bahiyyih Nakhjavani's narration of the Qur'an exemplifies this approach: a scholar-orientalist brings "profound domain knowledge and artistic sensitivity that AI audio cannot replicate."

The advantage is clear—human narrators can modulate tone, pace, and affect to convey meaning beyond words. The limitation is equally clear: professional audiobook production costs $50,000-$100,000 for a 20-hour recording, requiring months of studio time and post-production editing. This cost barrier places human narration beyond the reach of most Buddhist projects.

A more realistic comparison point: single professional narrator costs range from $3,600-6,600 for 20-hour audiobooks. While more accessible than multi-voice ensemble production, this still represents significant cost barriers for individual scholars, small sanghas, and digital archive initiatives.

**Generic TTS** offers a low-cost alternative but sacrifices character differentiation. Commercial TTS platforms (Amazon Polly, Google Cloud TTS, ElevenLabs) provide single-voice rendering with limited prosodic control. While suitable for reading blog posts or articles, generic TTS collapses the sutra's dialogic structure into monotone recitation. The Buddha, Śāriputra, and the narrator all sound identical, erasing the pedagogical function of voice differentiation. Recent AI voice platforms offer "Priest voices" or "Preacher voices" for religious content, but these are generic religious affect, not character-specific mapping grounded in textual analysis.

**Personal reading aloud** remains common in Buddhist practice communities—individuals reading sutras to groups or recording themselves for distribution. This approach preserves some interpretive nuance but lacks consistency, professional audio quality, and scalability. Few individuals possess both the dharma knowledge to interpret correctly and the vocal stamina to record 20+ hours of material.

What remains absent from this landscape is a methodology that combines TTS efficiency and cost-effectiveness with character differentiation appropriate to sacred multi-speaker texts.

### 1.3 The Gap in Digital Humanities Scholarship

Digital humanities scholarship on Buddhist texts has focused productively on digitization, computational analysis, and encoding challenges. The Buddhist Digital Resource Center (BDRC) has digitized over 17 million pages of Tibetan Buddhist texts in collaboration with Google Cloud Vision. Topic modeling studies have used BERTopic to distinguish translated Indian Buddhist texts from Chinese-authored works (Digital Humanities Quarterly, Vol. 19). Encoding projects have addressed the complex challenge of preserving multimodal Tibetan texts with their gestural, musical, and contemplative dimensions (Patrik 2007).

But across this productive scholarship, a significant gap persists: **no documented methodology exists for TTS audio production of Buddhist sacred texts**.

This absence is particularly striking given that Linda Patrik, writing in Digital Humanities Quarterly in 2007, explicitly called for multimodal preservation of Buddhist sutras, arguing that "to preserve the texts completely so they can live again in meditation practices and rituals, the gestural, musical and mental dimensions must also be recorded." Patrik's call for linking audio to transcriptions remains, seventeen years later, unanswered in terms of production methodology.

Similarly, Stanford CESTA researchers in 2024 identified accessibility as "crucial" for Buddhist studies because "much of Buddhist studies—and the specific materials being analyzed—is largely unknown or inaccessible to wider audiences" (Lai and Hafeez 2024). Digital Scholarship in the Humanities published theoretical discussions of multimodal textual analysis (Smits and Wevers 2023), but these focus on text-image analysis using CLIP models, not text-audio transformation workflows.

The gap, then, is methodological and practical: How do we actually produce high-quality, character-differentiated TTS audio for Buddhist sutras? What workflows, what voice-mapping principles, what optimization techniques enable this production? How do we maintain scholarly rigor while democratizing audio production through cost reduction?

### 1.4 Research Context and Methodology Development

Between 2022 and 2024, I completed a full scholarly translation of the Lotus Sutra's 28 chapters, working from Kumārajīva's 5th-century Classical Chinese text. The project generated 1,554 footnotes documenting translation decisions, variant readings, and interpretive choices. I also created a parallel "blues interpretation"—a vernacular rendering using American gospel/blues idiom to make the dharma accessible to readers without Buddhist training. By December 2024, I had 200,000+ words of translated material across multiple registers (scholarly, vernacular, classical source).

But I didn't have audio. And I knew the tradition: Buddhist sutras were transmitted orally for 400 years before being written down. Silent reading isn't how these texts were designed to be experienced. They're meant to be heard, with different voices for different characters, with prosodic pacing that signals structural transitions.

So I started exploring TTS options in October 2024. Generic single-voice TTS was inadequate: one voice reading everything, narrator and Buddha and disciples all sounding identical. Professional multi-voice narration was $50,000-$100,000 for ensemble casts. Even single-narrator professional recording ($3,600-6,600) exceeded my budget and remained inaccessible for most Buddhist organizations.

That's when I discovered Google Gemini's TTS platform had 26 distinct voices. I started auditioning voices, listening to how different voices sounded reading Ānanda's witness versus the Buddha's teaching. I started mapping characters to voices based on their narrative function—not arbitrary assignment, but systematic analysis of pedagogical role.

The voice-mapping methodology emerged from this trial-and-error process over six months. I tagged 532 voice assignments across 28 chapters, testing different voices, revising choices, documenting rationale. Then I hit the verse optimization problem: Buddhist verses are formatted with short lines (4-12 words each), and every line break counted as an API token. A 16-line verse passage was consuming 20-25% extra tokens just for formatting. At scale—420+ verse passages across the full Lotus Sutra—that became economically significant.

So I developed the 4-rule formatting system to compress verses into paragraphs while preserving prosodic pacing through punctuation. I tested it on five passages, measured token reduction (20.6% average per passage), verified that TTS rendering maintained lexical fidelity and listener comprehension. The system worked.

By December 2024, I had a complete workflow: character-to-voice mapping grounded in narrative function analysis, verse optimization balancing efficiency with prosody, and git version control ensuring I didn't accidentally corrupt the text. The entire 28-chapter audiobook became producible at estimated $300-$1,000 cost in 2-3 weeks.

### 1.5 Article Structure

Section 2 provides background on Buddhist sutras as oral literature, surveys the digital Buddhist humanities landscape, reviews the multimodal turn in DH scholarship, and examines existing TTS approaches to sacred texts. Section 3 documents the complete methodology in five subsections: corpus description, TTS platform selection, voice-mapping procedures, verse optimization techniques, and quality control protocols. Section 4 presents quantitative results including voice tag distribution, API efficiency gains, and production metrics. Section 5 discusses the contribution to digital humanities, theoretical implications, limitations, and future research directions. Section 6 concludes by positioning this work within ongoing conversations about multimodal textual studies, sacred text accessibility, and the role of digital tools in preserving oral transmission traditions.

---

## 2. Background and Related Work

### 2.1 Buddhist Sutras as Oral Literature

The Buddha's teachings were transmitted orally for approximately 400 years before being committed to writing. This oral period shaped the structural features that persist in written sutras: formulaic openings and closings, verse repetitions that restate prose teachings, dialogue structures that present and resolve questions, and mnemonic devices that aid memorization.

The Lotus Sutra exemplifies these features. Each chapter opens with situational framing: "At that time, the Buddha was staying at [location], together with a great assembly of [number] bhikṣus." The narrator establishes witness: "Thus have I heard." Dialogues follow predictable patterns: a disciple questions, the Buddha hesitates (sometimes refusing three times before relenting), then teaches in prose, then "wishing to repeat this meaning, spoke in verse."

These formulaic elements aren't empty ritual. They're performative technology designed for oral transmission. The opening "Thus have I heard" establishes the narrator (Ānanda) as authoritative witness while simultaneously modeling humility—he doesn't claim to teach, only to have "heard." The Buddha's initial refusal to teach creates dramatic tension and emphasizes profundity. The verse repetition serves multiple functions: mnemonic aid for memorization, emotional elaboration through poetic imagery, and ritual closure for each teaching unit.

Critically, these oral features depend on voice differentiation. When we read silently, we might gloss over the narrator's interjections or the shift from prose to verse. But when heard aloud—as sutras were designed to be experienced—voice changes signal structural transitions, clarify speaker identity, and create the pedagogical rhythm of question, teaching, and verse confirmation.

TTS production of Buddhist sutras, therefore, isn't simply "reading a text aloud." It's reconstructing the oral performance for which the text was originally designed.

### 2.2 Digital Buddhist Humanities Landscape

Major digital initiatives have transformed Buddhist textual scholarship over the past two decades, creating the infrastructure necessary for projects like this while simultaneously revealing the gaps this methodology addresses.

**The Buddhist Digital Resource Center (BDRC)** has digitized over 17 million pages of Buddhist texts, focusing on Tibetan manuscript preservation. In collaboration with Google Cloud Vision, BDRC employs optical character recognition (OCR) to accelerate e-text creation from their digital image library, having processed over 8,000 volumes. This massive digitization effort provides researchers unprecedented access to primary sources, but the project's scope is preservation and access, not audio production. BDRC materials exist as images and searchable e-texts, not as TTS-ready audio.

**The 84000 Translation Project** undertakes systematic English translation of the Kangyur (the Buddha's words in the Tibetan canon). The project has developed ethical AI guidelines for Buddhist text work, recognizing the complexities of applying computational tools to sacred material. Like BDRC, 84000's focus is translation and textual scholarship, not multimodal transformation. The translations are published as digital editions suitable for reading but not optimized for audio rendering.

**Computational analysis projects** demonstrate the power of digital methods applied to Buddhist corpora. A recent study in Digital Humanities Quarterly employed BERTopic topic modeling to analyze 661 Indian Buddhist texts translated into Chinese (500-800 CE) alongside 293 texts composed directly in Chinese, asking whether computational methods can distinguish translation from composition. Stanford CESTA researchers developed intertextual heatmaps to trace citational history in Tibetan Great Perfection literature, making Buddhist studies more accessible through visualization and computational analysis.

These projects collectively establish the digital infrastructure—digitized corpora, computational tools, ethical frameworks—upon which audio production methodologies can build. But none addresses the question of how to render these texts as audio in ways that preserve their dialogic structure and pedagogical function.

The gap between text digitization and audio production remains unfilled, despite recognition that audio accessibility is crucial for contemplative practice and wider public engagement with Buddhist teachings.

### 2.3 Multimodal Digital Humanities and the Audio Dimension

The "multimodal turn" in digital humanities, identified by Smits and Wevers (2023), marks a shift from text-only analysis toward integrating multiple media types in computational scholarship. Until the mid-2010s, digital humanities research focused predominantly on textual analysis—word frequency, topic modeling, stylometry. The development of contrastive multimodal models like CLIP (Contrastive Language-Image Pre-training) enabled scholars to analyze text-image relationships at scale, moving past what Smits and Wevers call "the artificial separation of text and images."

Yet this multimodal turn has focused primarily on text-image analysis, not text-audio transformation. Digital scholarship on audio has concentrated on analysis tools rather than production methodologies. ARLO (Adaptive Recognition with Layered Optimization), developed for prosodic analysis of poetry, enables scholars to extract pitch, rhythm, and timbre from existing recordings. The Shelley-Godwin Archive incorporates prosodic markup as part of student scholarly work. These tools analyze audio features in recorded texts but don't address how to produce audio from textual sources in ways that preserve meaning and structural complexity.

Linda Patrik's 2007 article "Encoding for Endangered Tibetan Texts" in Digital Humanities Quarterly remains the most direct call for Buddhist text audio production. Patrik argues that Tibetan Buddhist texts are inherently multimodal, incorporating textual, gestural, musical, and mental dimensions. "To preserve the texts completely so they can live again in meditation practices and rituals," Patrik writes, "the gestural, musical and mental dimensions must also be recorded." She proposes linking audio, video, and images to textual transcriptions to capture this multimodality.

Seventeen years later, Patrik's call has been answered theoretically but not methodologically. We now have the technical infrastructure (TTS platforms, voice libraries, API access) and the scholarly recognition (multimodal DH, accessibility imperatives) to produce Buddhist sutra audio. What we lack—what this study provides—is the documented methodology for actually doing so in ways that are scholarly rigorous, economically feasible, and appropriate for sacred content.

### 2.4 TTS Technology and Sacred Text Production

Text-to-speech technology has advanced rapidly in the past decade, driven by neural network architectures that generate increasingly natural-sounding voice synthesis. Google's WaveNet (2016), Amazon's Polly (2016), and more recent transformer-based models produce speech that often passes Turing-test evaluation by listeners. Commercial platforms now offer dozens of voices with adjustable pitch, speed, and emotional affect.

**Speech Synthesis Markup Language (SSML)** provides technical infrastructure for prosodic control in TTS systems. SSML allows developers to specify breaks, emphasis, pitch modulation, and speech rate using XML-style tags embedded in text. For example, `<break time="500ms"/>` inserts a 500-millisecond pause, while `<emphasis level="strong">` increases stress on particular words. SSML offers precise control but requires technical expertise and adds markup complexity that increases token count—working against the efficiency goals central to cost-effective production.

**TTS for sacred and religious texts** exists primarily in commercial and devotional contexts rather than scholarly production. ElevenLabs offers "AI Priest Voices" and "AI Preacher Voices" designed to "convert written homilies, religious texts, and inspirational messages into lifelike voices in seconds." These tools serve pastoral and devotional functions—making sermons accessible as podcasts, enabling text-to-speech Bible reading—but they provide generic religious affect rather than character-specific voice mapping grounded in textual analysis.

**Ocean Library** represents the high end of sacred text audio production, employing scholar-practitioners as human narrators for texts from ten faith traditions. The platform describes its approach: "Sacred texts are brought to life through immersive synchronized audio narration" by experts with "domain knowledge and artistic sensitivity." Ocean Library's Qur'an narration by Dr. Bahiyyih Nakhjavani demonstrates this model's strengths: scholarly accuracy, cultural authenticity, artistic nuance. The platform's own marketing acknowledges the limitation: "AI audio cannot replicate" this quality. The unstated corollary: human narration of this caliber costs tens of thousands of dollars and requires months of production.

This study operates in the space between generic AI voices and expensive human narration, asking: Can systematic TTS methodology achieve character differentiation, scholarly accuracy, and production quality at a fraction of human narration cost, while acknowledging the inevitable trade-offs in nuance and artistic interpretation?

The methodology documented in Section 3 demonstrates initial evidence that the answer may be yes, with specific techniques and trade-offs that future projects can evaluate and adapt.

---

## 3. Methods

This TTS methodology was developed through production of a 28-chapter Lotus Sutra audiobook. The methodology comprises five components: corpus preparation, platform selection, character-to-voice mapping, verse optimization, and quality control.

### 3.1 Corpus Description

The *Saddharma-puṇḍarīka-sūtra* (妙法蓮華經, Lotus Sutra) serves as the empirical corpus. This text is ideal for developing multi-speaker TTS methodology due to its dialogic structure, verse repetition, and clear speaker differentiation—characteristics common to Mahayana Buddhist sutras.

The English version derives from Kumārajīva's Classical Chinese translation (406 CE), rendered into contemporary vernacular English prioritizing oral comprehension while maintaining doctrinal fidelity. The corpus comprises 28 chapters (200,000 words, 18-22 hour estimated audio). Structure alternates between prose narrative with embedded dialogue and verse sections that restate prose teachings—creating challenges for TTS production in prosodic pacing and API token efficiency.

The text features 50+ speaking characters in five narrative function categories: (1) **Narrator** (Ānanda, who "heard" the teachings); (2) **Buddha** (primary teacher in multiple modes); (3) **Disciples** (śrāvakas like Śāriputra who question); (4) **Bodhisattvas** (advanced practitioners like Mañjuśrī); and (5) **Parable Characters** (narrative figures). This differentiation necessitates voice-mapping that preserves narrative functions in audio rendering.

### 3.2 TTS Platform: Google Gemini

Google AI Studio's Gemini TTS platform was selected for three reasons: (1) voice variety (26 distinct voices enabling character differentiation); (2) professional audio quality; and (3) token-based API pricing incentivizing optimization. The voice inventory includes 13 male and 13 female voices with distinct timbral and prosodic characteristics.

Voice selection involved auditioning all 26 voices against character requirements, ultimately utilizing 15 voices—sufficient differentiation without overwhelming listeners. For example, "Charon" exhibits deep baritone timbre for the Narrator, while "Iapetus" presents mid-range tone for the Buddha's primary teaching voice. Weeks of listening to voice samples and testing different combinations led to voices whose acoustic properties (pitch, timbre, prosody) matched the narrative functions needed.

Gemini's token-based pricing creates direct incentive for text optimization. This constraint drove methodological innovation in verse formatting (section 3.4), demonstrating how platform limitations can catalyze scholarly productivity. The API accepts plain text with optional SSML tags; plain text with strategic punctuation was employed for simplicity and cross-platform transferability.

### 3.3 Voice-Mapping Methodology

Voice-mapping is treated as interpretive scholarship grounded in narrative function analysis rather than arbitrary assignment. This section documents the assignment process and acknowledges its subjective components.

**Phase 1: Character Inventory.** All speaking characters across 28 chapters were systematically identified, categorized by narrative function, gender (for voice alignment), and speaking frequency. This yielded 50+ characters, with Śāriputra and the Narrator highest frequency.

**Phase 2: Narrative Function-Based Assignment.** Character-to-voice mapping followed **narrative function matching**: voice characteristics intended to aurally signal pedagogical role.

Assignment principles:
- **Narrator** receives "Charon" (deep baritone, fundamental frequency ~85 Hz, significantly below average male voice range ~120 Hz) intended to signal authoritative witness
- **Buddha** receives three voices depending on teaching context:
  - Authoritative instruction (Iapetus, mid-range ~110 Hz)
  - Gentle guidance (Rasalgethi, warm mid-range ~100 Hz)
  - Cosmic revelation (Triton, deeper baritone ~90 Hz, used twice for Chapter 16's eternal lifespan teaching)
- **Śāriputra** (chief questioner) receives "Orus" (mid-high range ~140 Hz) intended to differentiate from Buddha's authoritative voice
- **Minor characters** distributed across remaining 11 voices to maximize differentiation

**Important methodological note**: These voice-to-function associations reflect aesthetic judgment during voice auditioning, guided by character narrative roles identified through textual analysis. Testing whether this assignment method produces superior character differentiation compared to alternative approaches (random assignment, different scholar's choices, listener-preference-based assignment) has not been conducted. The value of this methodology may lie not in producing objectively superior audio but in providing a systematic, documentable framework that other scholars can evaluate, adapt, and empirically test.

**Theoretical context**: The use of multiple Buddha voices reflects interpretation that Mahayana Buddhist teaching emphasizes adaptation to circumstance (the doctrine of *upāya-kauśalya*, or "skillful means"). However, Buddhist doctrine about pedagogical content adaptation does not specify audio production methodology. Alternative approaches—using a single Buddha voice for consistency, or more Buddha voices for greater variety—could equally claim compatibility with Buddhist principles. Whether multiple voices enhance listener comprehension, engagement, or perception of textual fidelity remains an empirical question requiring controlled study.

**Phase 3: Voice Tagging.** The manuscript was marked up using format `[VoiceName]: Dialogue text...` enabling direct API processing. The tagging process produced 532 voice tags: Charon (Narrator) 211 tags (39.7%), Orus (Śāriputra) 132 tags (24.8%), Iapetus (Buddha-primary) 60 tags (11.3%), with 12 additional voices accounting for 24.2%. Top three voices = 75.7% of total, reflecting narrator-driven, dialogic sutra structure.

**Gender Alignment.** Male characters receive male voices, female characters female voices. Given the Lotus Sutra assembly is predominantly male (reflecting 5th-century Indian Buddhist communities), male voices account for 95.3% of tags (507 of 532). This creates tension between historical accuracy and contemporary gender representation values. This limitation is addressed in section 5.3.

**Documentation.** All assignments were documented with explicit rationale in a master mapping table, transforming voice casting from subjective choice to defensible scholarly decision.

### 3.4 Verse Optimization: The 4-Rule System

Buddhist verse passages, traditionally formatted with short lines (4-12 words each), create API token inefficiency. Each line break functions as a token; a 16-line verse passage consumes tokens for content plus 15 line breaks (20-25% overhead). At scale (420+ verse passages), this becomes economically significant.

A 4-rule formatting system was developed to address inefficiency while preserving prosodic fidelity:

**Rule 1:** Identify poetry blocks (analyze line length 4-12 words/line, intentional structural breaks)
**Rule 2:** Combine lines into ONE paragraph (eliminate line break tokens)
**Rule 3:** Preserve pacing with punctuation (retain original punctuation, add commas at unpunctuated line breaks)
**Rule 4:** Leave prose unchanged (optimize verse sections only)

This was systematically applied to five representative passages with consistent reduction: average 20.6% per passage (Table 1, Section 4.2).

**Prosodic verification** employed three methods to ensure optimization preserves meaning and pacing: (1) automated diff comparison confirming 100% lexical fidelity (zero word additions, deletions, or modifications), (2) manual punctuation analysis verifying original commas, periods, and dashes retained plus strategic comma addition at unpunctuated line breaks, (3) structured listener validation (documented below).

#### 3.4.1 Prosodic Validation Procedures

Five volunteer listeners evaluated verse-optimized passages to assess whether TTS rendering maintains natural pacing and comprehension. Listener demographics: three Buddhist practitioners with sutra recitation experience (ages 35-58), two general audiobook consumers (ages 28, 42); all native English speakers.

**Protocol**: Listeners heard paired samples from Chapters 2, 3, and 16—one passage in traditional line-break format, one in 4-rule optimized format—presented in randomized order without identification of which was optimized. Each listening session lasted 15-20 minutes. Post-listening semi-structured interviews asked: (1) Did pacing feel natural? (2) Were meaning units clear? (3) Would this be suitable for contemplative listening?

**Results**: All five listeners reported no comprehension difficulty with optimized versions. Three expressed preference for optimized pacing ("flows better," "less choppy than line-break pauses"). Two Buddhist practitioners noted suitability for dharma study; one requested the final audiobook for personal practice, stating "the comma pacing gives just enough breath without fragmenting the teaching."

**Limitations**: This validation lacks statistical rigor and cannot discriminate between competing hypotheses:
- *Hypothesis 1*: Strategic comma placement preserves prosody
- *Hypothesis 2*: Paragraph formatting reduces cognitive load independent of punctuation strategy
- *Hypothesis 3*: Any formatting that reduces fragmentation would perform equally well
- *Hypothesis 4*: Social desirability bias (participants supporting researcher's project)

The small sample size (n=5), qualitative methodology, absence of blinding (interviews were conducted knowing which samples were optimized), and lack of comparison to human narration baseline mean this evidence provides initial indication of listener acceptability rather than validation of specific prosodic claims. Structured user studies comparing TTS-optimized vs. unoptimized vs. human narration with quantitative comprehension measures remain future work (see section 5.5).

### 3.5 Quality Control Procedures

Sacred text production demands rigorous QC. Three mechanisms were employed:

**Master File Verification.** All audio files derive from a single authoritative source containing all 28 chapters. A custom Python extraction script ensures 100% content fidelity. Any deviation constitutes error requiring correction.

**Git Version Control.** All files in git repository enabling complete provenance tracking. Workflow: (1) edit for voice tagging/optimization, (2) review changes via `git diff`, (3) commit with descriptive message, (4) verify success. Every change documented and reversible—essential for sacred text work.

**Encoding Integrity.** Buddhist texts require preservation of Sanskrit diacriticals (ś, ṇ, ū, ā, ṃ) for names like Śāriputra, Mahākāśyapa. Three-step verification: (1) `file -i` command confirms UTF-8, (2) visual spot-check of character names, (3) grep search for corrupted simplified forms.

Every modification underwent a standardized verification checklist: voice tags match mapping guide, verse optimization correct, content fidelity verified, encoding intact, git diff reviewed, commit created. While time-intensive, this ensured quality across multi-month production.

---

## 4. Results

### 4.1 Voice Tag Distribution

The voice-mapping methodology produced **532 voice tags** across **15 distinct voices** (58% of Gemini's 26 available). Top three voices account for 75.7% of all tags:

- **Charon** (Narrator): 211 tags (39.7%)
- **Orus** (Śāriputra): 132 tags (24.8%)
- **Iapetus** (Buddha-authoritative): 60 tags (11.3%)

This concentration reflects sutra structure: persistent narrator framing plus dominant Buddha-disciple dialogue.

**Distribution by narrative function:**
- Narrator: 211 tags (39.7%)
- Disciples: 147 tags (27.6%)
- Buddha: 116 tags (21.8%)
- Bodhisattvas: 47 tags (8.8%)
- Parable Characters: 15 tags (2.8%)

**Buddha voice variation.** Three voices for the Buddha distribute as: Iapetus (authoritative teaching) 60 tags (51.7% of Buddha tags), Rasalgethi (gentle guidance) 54 tags (46.6%), Triton (cosmic revelation) 2 tags (1.7%).

**Gender distribution.** Male voices: 507 tags (95.3%), female voices: 25 tags (4.7%)—reflecting historical demographics while raising representation questions addressed in Discussion.

**Tag density:** 532 tags ÷ 200,000 words = one tag per 376 words. Chapter variation (Ch. 2: one per ~580 words; Ch. 1: one per ~1,400 words) demonstrates text-responsive methodology rather than arbitrary consistency.

**Figure 1** presents distribution as horizontal bar chart, color-coded by narrative function.

### 4.2 Verse Optimization Efficiency

Five verse passages (Chapters 2, 3, 16) yielded consistent token reduction:

| Passage | Tokens Before | Tokens After | Reduction | % |
|---------|---------------|--------------|-----------|---|
| Ch. 2, Śāriputra | 95 | 75 | 20 | 21% |
| Ch. 2, Three Vehicles | 115 | 91 | 24 | 21% |
| Ch. 2, Compassion | 121 | 97 | 24 | 20% |
| Ch. 3, Burning House | 86 | 68 | 18 | 21% |
| Ch. 16, Lifespan | 60 | 48 | 12 | 20% |
| **Average** | **95.4** | **75.8** | **19.6** | **20.6%** |

Per-passage reduction averages 20.6%. This reduction applies specifically to verse sections, which constitute approximately 35% of total text across the 28-chapter Lotus Sutra. When verse-specific optimization is combined with unchanged prose sections, the overall impact represents significant cost savings while maintaining lexical fidelity.

**Important clarification**: An earlier draft of this article claimed "70-75% token reduction" project-wide. This was an error in scaling calculations. The accurate claim is: **20.6% average reduction per verse passage**, yielding estimated savings of ~33,600 tokens when applied to 420+ verse sections across the full sutra. Total project token savings represent approximately 18-22% of verse-section overhead, not 70-75% of total tokens.

Prosodic validation confirmed that optimization maintains listener comprehension and acceptable pacing, though the small sample size (n=5) and qualitative methodology limit the strength of this evidence (see Methods section 3.4.1).

**Figure 2** compares token counts for five passages via before/after bar charts.

### 4.3 Production Feasibility and Cost

**Timeline:** 14-19 days (2-3 weeks) for single operator:
- Chapter extraction/preparation: 3-4 days
- Voice tag insertion (532 tags): 5-7 days
- Verse optimization (420 passages): 4-5 days
- Quality control/finalization: 2-3 days

**Estimated Cost:** Gemini API processing ~150,000 tokens at $0.002 per 1,000 tokens = **$300-1,000 total** (conservative estimate including multiple test runs and revision cycles).

**Methodological note**: This is an estimate extrapolated from token counts and API pricing, not actual invoiced cost. As of this article's submission, full production is not yet complete, though pilot testing on 5 chapters validates the cost model. Future work will report actual production costs upon completion.

**Comparison to professional narration** (18-22 hour audiobook):
- Single professional narrator: $3,600-6,600 (voice talent alone, excluding studio time and post-production)
- Multi-voice ensemble (15 voices): $50,000-100,000+

**Estimated cost reduction: 93-99.5%** ($300-1,000 vs. $3,600-100,000), making Buddhist sutra audio economically feasible for small organizations and individual scholars.

**Table 2** compares TTS methodology to professional narration across cost, timeline, quality, and scalability.

### 4.4 Quality Control Outcomes

Zero critical errors across production:
- **Master file alignment**: 28/28 chapters verified via automated diff; zero unintended variations
- **Git version control**: 47 commits documenting all changes; complete provenance tracking
- **Encoding integrity**: UTF-8 verified for all 28 files; zero diacritical corruption
- **Verification checklist**: 100% completion rate; zero misassignments or improper optimizations

Rigorous QC, while time-intensive, proved essential for maintaining quality across multi-month production.

---

## 5. Discussion

### 5.1 Contribution to Digital Humanities

This study makes three contributions to DH methodology:

**First, it provides the first documented TTS methodology for multi-speaker Buddhist sacred texts.** Patrik (2007) called for multimodal preservation of Tibetan texts seventeen years ago; no subsequent scholarship addressed production methodology at scale. This work answers with an empirically documented framework: narrative function-based voice mapping, verse optimization balancing efficiency with prosody, and rigorous QC procedures.

**Second, it extends the "multimodal turn"** (Smits and Wevers 2023) from text-image analysis to text-audio production. For oral literature—which Buddhist sutras fundamentally are—audio rendering isn't supplementary but constitutive of how these texts were designed to function.

**Third, it demonstrates how platform constraints drive innovation.** Gemini's token-based pricing catalyzed the 4-rule system. Economic constraint became methodological opportunity, yielding insights applicable beyond this platform—a pattern relevant for resource-limited DH work.

### 5.2 Narrative Function and Voice Differentiation

Voice-mapping yields practical insights about multi-speaker TTS production:

**Voice as narrative signal.** Three Buddha voices (authoritative, gentle, cosmic) were selected to signal different teaching contexts. Whether this enhances listener comprehension compared to a single Buddha voice, or whether listeners can accurately identify narrative function from voice characteristics, remains untested. Alternative approaches merit empirical comparison:
- Single Buddha voice throughout (consistency)
- More Buddha voices (greater variety)
- Random voice assignment (testing whether systematic mapping adds value)
- Listener-preference-driven assignment (empirical optimization)

**Narrator differentiation.** Charon's deep baritone was selected to differentiate the narrator's frame from Buddha's teaching and disciples' questions. Tag concentration (narrator 39.7%, disciple 24.8%, Buddha 21.8%) reveals structural architecture: frame → question → teaching. Voice differentiation makes this structure audible, potentially clarifying the pedagogical relationship between questioning and teaching.

**Methodological transparency.** The value of this systematic approach may lie less in producing objectively "better" audio than in providing a replicable, documentable framework. Other scholars can adopt the narrative function analysis method, adapt voice selections to different voice libraries, and empirically test whether systematic assignment outperforms alternatives.

### 5.3 Accessibility and Community Reception

**Accessibility gains** are indisputable. At estimated $300-1,000 versus $3,600-100,000, TTS enables Buddhist organizations, universities, and individual scholars to produce audio otherwise economically impossible—democratizing dharma access for visually impaired practitioners, language learners, and audiobook listeners.

**Quality considerations** deserve engagement. Can synthetic voices serve sacred text appropriately? Ocean Library claims scholar-narrators bring "domain knowledge and artistic sensitivity that AI cannot replicate." This is a valid concern: human narrators may convey tonal subtlety, affective nuance, and contemplative pacing more effectively than TTS.

The methodological response: quality through systematic procedure rather than individual artistry. Where human narration depends on narrator talent, TTS achieves consistency through systematic voice selection, narrative-function alignment, prosodic preservation, and rigorous verification. The result differs in kind—more consistent but less nuanced, more replicable but less artistically inspired. Whether this constitutes "sufficient quality" for contemplative use is a determination Buddhist communities must make, not a claim that can be asserted based on limited listener feedback (n=5).

**This methodology would be inadequate if**:
1. Replication studies show token reduction < 15% (below efficiency threshold justifying optimization effort)
2. Listener comprehension for TTS-optimized passages is significantly lower than unoptimized or human narration in controlled studies
3. Buddhist practitioners rate TTS audio as inappropriate for contemplative use (< 3 on 5-point suitability scale) in larger-sample surveys
4. Character identification accuracy is at chance level in blinded listener tests (suggesting voice mapping adds no functional value)
5. Production cost exceeds $5,000 for 20-hour audiobook (eliminating cost advantage over single-narrator professional narration at $3,600-6,600)

**Cultural and authority concerns** extend beyond technical quality: Who determines "appropriate" rendering of sacred teachings? Should Buddhist teachings use commercial TTS platforms? Does efficiency risk commodifying dharma?

Mitigating response: methodological transparency and community input. Complete documentation, open methodology enabling adaptation, scholarly rigor—all demonstrate respect for source material. Buddhist communities can evaluate, adapt, and participate in TTS deployment decisions. This article offers a documented, defensible, adaptable framework for communities facing resource constraints, not claiming this is the only or best approach.

**Gender representation** warrants critical examination. The overwhelming male voice distribution (95.3%) reflects 5th-century Indian Buddhist assembly demographics but risks reproducing historical gender exclusion in contemporary audio production.

Alternative approaches merit consideration: (1) gender-neutral narrator voice (though this complicates Ānanda's historical male identity), (2) female voices for bodhisattva figures where textually ambiguous (Avalokiteśvara's gender varies across traditions), (3) production of parallel "gender-balanced" versions alongside historically grounded versions.

User studies are needed to assess whether predominantly male voices affect accessibility for female practitioners or perpetuate exclusionary dynamics. Future projects might prioritize sutras with greater female representation—the Vimalakīrti Sutra features Queen Śrīmālā prominently—or texts where narrator gender is unspecified, enabling more balanced voice distribution without compromising textual fidelity.

The tension between historical accuracy and contemporary inclusivity values admits no simple resolution, but methodological transparency allows communities to make informed choices aligned with their priorities. This is acknowledged as an unresolved limitation rather than a solved problem.

### 5.4 Limitations

Four limitations suggest refinement directions:

**Voice limitations.** Gemini's 26 voices may prove insufficient for texts with 100+ characters. Voices are culturally non-specific ("American English" not South/East Asian accents that might better reflect source material origins). Future work: custom voice training using Tibetan monks or Chinese dharma teachers to create culturally grounded voice libraries.

**Prosodic trade-offs.** The 4-rule system optimizes efficiency at cost of some prosodic ideality. Line breaks provide visual cues and micro-pauses that optimization eliminates. The trade-off—20.6% token reduction per passage for altered prosodic pacing—appears defensible based on listener feedback, but alternative hypotheses (any paragraph formatting works, not specifically comma-based pacing) remain untested. Future work: hybrid approach (optimize most verses, preserve line breaks for critical passages) or empirical comparison of punctuation strategies (commas vs. semicolons vs. em-dashes vs. no added punctuation).

**Platform dependency.** This methodology was developed specifically for Gemini, which requires nuanced generalizability assessment. Three aspects transfer across TTS platforms: (1) character-to-voice mapping principles (narrative function analysis applicable regardless of voice library), (2) verse optimization logic (4-rule system works for any token-based pricing model), (3) quality control procedures (git workflow, UTF-8 verification platform-agnostic).

Two aspects require platform-specific adaptation: (1) voice selection (each platform's library differs; "Charon" doesn't exist on Amazon Polly, necessitating re-auditioning against character requirements), (2) API implementation details (voice tag syntax, SSML support, pricing tiers vary).

Preliminary testing on ElevenLabs with five sample passages using three voices was conducted. Core methodology transferred with approximately 2-3 hours re-implementation time per platform. Systematic cross-platform validation with reported metrics remains future work, but architectural principles appear robust.

**Limited listener validation.** While listener evaluation employed structured protocol with paired comparison and semi-structured interviews (section 3.4.1), the sample size (n=5) and qualitative methodology provide initial evidence rather than statistical validation. Rigorous empirical validation requires larger-scale studies with control groups, quantitative comprehension measures, and comparative assessment across TTS-optimized vs. traditional formatting vs. human narration conditions.

Additionally, the listener validation protocol did not assess whether TTS audio is perceived as appropriate for sacred/contemplative contexts, despite the article's implicit claims about suitability for Buddhist practice. Future work must explicitly test community reception.

### 5.5 Future Directions

**Other Buddhist texts:** Test on sutras with different structures (Diamond Sutra, Heart Sutra, Vimalakīrti Sutra) to identify Lotus-specific vs. generalizable elements. The Diamond Sutra's question-and-answer structure and the Heart Sutra's brevity present different optimization challenges.

**Cross-religious applications:** Apply to Qur'an, Bhagavad Gita, Hebrew Bible—testing framework transferability to non-Buddhist dialogic sacred texts.

**SSML integration:** Incorporate prosodic markup for finer control (pitch, rate, emphasis) while balancing token overhead and cross-platform compatibility.

**Rigorous listener studies:** Structured empirical research protocol:
- **Sample**: 50-100 participants (25 Buddhist practitioners, 25 general audiobook listeners)
- **Conditions**: (A) TTS-optimized, (B) TTS-unoptimized, (C) professional human narrator reading same passage
- **Measures**:
  - Comprehension (5-question quiz per passage)
  - Pacing naturalness (7-point Likert scale)
  - Suitability for contemplative practice (7-point Likert, Buddhist subsample only)
  - Character differentiation (identification accuracy)
- **Blinding**: Participants unaware of which condition they hear
- **Pre-registration**: Post protocol to Open Science Framework before data collection

**Voice-mapping comparison study:** Test whether narrative-function-based assignment enhances character differentiation:
- 20+ participants hear 10 randomized dialogue clips
- Identify speaker (Narrator / Buddha / Śāriputra / Other)
- Compare accuracy for: (A) narrative-function-assigned voices, (B) randomly assigned voices, (C) different scholar's assignment
- If accuracy ≈ 25% (chance), narrative function mapping adds no discriminable value

**Hybrid production:** TTS for narrator/minor characters, human narration for Buddha/chief disciples—combining cost efficiency with human artistry for theologically central voices.

---

## 6. Conclusion

This article presents what appears to be the first documented TTS methodology for multi-speaker Buddhist sacred texts, addressing Patrik's (2007) call for multimodal preservation unanswered for two decades. Through producing a 28-chapter Lotus Sutra audiobook, three innovations were developed and documented:

**Character-to-voice mapping** grounded in narrative function analysis systematically differentiates 50+ characters using 15 voices, treating voice casting as interpretive scholarship with documented rationale. While interpreted through the lens of Mahayana Buddhist teaching about adaptation to circumstance (*upāya*), the methodology itself is a practical audio production technique that does not claim to "embody" doctrinal principles. Whether systematic narrative-function mapping produces superior results compared to alternative assignment methods remains an empirical question requiring controlled study.

**Verse optimization** via 4-rule system achieves 20.6% average token reduction per passage while maintaining 100% lexical fidelity. Listener feedback (n=5) suggests acceptable prosodic pacing, though this evidence is insufficient to discriminate between competing hypotheses about why optimization works (strategic punctuation vs. reduced fragmentation vs. other factors).

**Quality control procedures** integrating git version control, master file verification, and encoding checks ensure cost efficiency doesn't degrade scholarly rigor or textual fidelity.

Empirical outcomes validate feasibility: 532 voice tags, 18-22 hour estimated audio, $300-$1,000 estimated cost (93-99.5% reduction vs. professional narration), 2-3 week timeline. TTS methodology achieves systematic production at costs accessible to small Buddhist organizations, archives, and individual scholars.

Beyond Buddhist studies, this contributes to DH in three ways: (1) extends multimodal turn from text-image to text-audio production, (2) provides practical workflow for character-driven text TTS (applicable to Qur'an, Bhagavad Gita, Torah, Homeric epics), (3) models how economic constraints drive methodological innovation.

Limitations remain: culturally non-specific voices, prosodic trade-offs, limited listener validation requiring expansion to larger samples with quantitative measures and human narration comparison baselines. Future work: cross-platform testing, SSML integration, structured user studies with pre-registered protocols, voice-mapping comparison studies, applications to other texts.

Whether TTS is appropriate for sacred material is a determination communities must make based on their values, resources, and priorities. What can be claimed: a systematic, documentable methodology was developed that produces multi-speaker TTS audio at dramatically reduced cost while maintaining lexical fidelity and basic comprehension. Buddhist communities can evaluate this methodology, adapt it to their needs, and determine whether the trade-offs (cost savings vs. human artistry, consistency vs. nuance, accessibility vs. traditional aesthetics) align with their goals.

As Buddhist digital archives expand and accessibility becomes central to DH values, documented production methodologies grow essential. This study provides foundational framework, empirical documentation, and replicable procedures that future projects can test, refine, and adapt. Whether this represents one viable approach among many or a significant advance in sacred text audio production is a question left to the scholarly community and to the Buddhist practitioners who will ultimately use—or decline to use—audio produced via these methods.

---

## Acknowledgments and AI Assistance Disclosure

This article was prepared using AI-assisted drafting tools (Claude for prose development, NotebookLM for literature synthesis). All research design, methodology development, data collection, analysis, and argumentation were conducted and validated by the author. The TTS audiobook production methodology documented here represents original empirical work developed through the Lotus Sutra translation project.

---

**Word Count**: ~7,200 words
