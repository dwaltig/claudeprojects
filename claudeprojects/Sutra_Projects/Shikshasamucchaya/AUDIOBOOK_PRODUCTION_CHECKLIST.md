# Śikṣāsamuccaya Blues Audiobook Production Checklist

---

## Pre-Production Checklist

- [ ] Review complete manuscript: `SHIKSHASAMUCCHAYA_COMPLETE_BLUES_AUDIOBOOK.md`
- [ ] Verify all 19 chapters are included in correct order
- [ ] Check front matter (introduction, pronunciation guide, how to listen)
- [ ] Check back matter (epilogue, acknowledgments, colophon)
- [ ] Ensure Sanskrit diacriticals are preserved (Śāntideva, etc.)
- [ ] Create ElevenLabs account (Pro plan recommended: $99/month)
- [ ] Convert manuscript to .docx or .txt format:
  ```bash
  pandoc SHIKSHASAMUCCHAYA_COMPLETE_BLUES_AUDIOBOOK.md -o SHIKSHASAMUCCHAYA_ELEVENREADER.docx
  ```

---

## Voice Selection Checklist

- [ ] Test 3-5 voices with Chapter 17 (shortest chapter)
- [ ] Listen to each voice for:
  - [ ] Warmth and gravitas
  - [ ] Blues resonance (character, depth)
  - [ ] Clarity on Buddhist terms
  - [ ] Natural pacing
- [ ] Select final voice (recommended: **Adam**)
- [ ] Configure voice settings:
  - [ ] Stability: 60-70%
  - [ ] Clarity: 70-80%
  - [ ] Style Exaggeration: 30-40%

---

## TTS Generation Checklist

- [ ] Upload manuscript to ElevenReader
- [ ] Preview first chapter and verify:
  - [ ] Pronunciation of Buddhist terms (Śāntideva, bodhisattva, nirvāṇa)
  - [ ] Natural pacing and rhythm
  - [ ] Proper handling of verse sections
  - [ ] Chapter transitions
- [ ] Add pronunciation hints if needed (see Audio Production Guide)
- [ ] Generate full audiobook
- [ ] Download all audio files (MP3 or WAV)
- [ ] Verify file count: 19 chapters + front matter + back matter = 21 files

---

## Post-Production Checklist

### Audio Normalization
- [ ] Import all chapter files into Audacity or Adobe Audition
- [ ] Apply normalization to -3 dB peak level
- [ ] Apply compression (Threshold: -20 dB, Ratio: 3:1)
- [ ] Check for consistent volume across all chapters
- [ ] Remove any audio artifacts (clicks, pops, long pauses)

### Chapter Cleanup
- [ ] Add 0.5s silence at beginning and end of each chapter
- [ ] Verify chapter titles are clear and audible
- [ ] Check for mispronunciations and fix if needed
- [ ] Smooth chapter transitions

### Metadata
- [ ] Add ID3 tags to all MP3 files:
  - [ ] Title (chapter name)
  - [ ] Artist/Author (William Altig)
  - [ ] Album (The Śikṣāsamuccaya: A Compendium of Training)
  - [ ] Genre (Buddhism / Philosophy)
  - [ ] Year (2026)
  - [ ] Track numbers (01-21)

### Quality Assurance
- [ ] Listen to 5-minute samples from each chapter
- [ ] Verify loudness meets Audible standards (-18 to -23 dB RMS)
- [ ] Check for consistent audio quality throughout
- [ ] Test playback on multiple devices (phone, computer, car)

---

## Optional Audio Enhancement Checklist

(Only if pursuing advanced audio production)

- [ ] Add chapter transition sounds (singing bowl, temple bell)
- [ ] Add harmonic undertone to verse sections (136.1 Hz at -40 dB)
- [ ] Apply binaural beats for contemplative edition (8 Hz theta)
- [ ] Process with spatial audio plugin for immersive experience
- [ ] Create two versions: Standard and Contemplative

---

## Distribution Preparation Checklist

### Cover Art
- [ ] Design or commission audiobook cover art
- [ ] Minimum resolution: 2400x2400 pixels (Audible requirement)
- [ ] Verify text is readable at thumbnail size
- [ ] Include title, subtitle, author/translator name
- [ ] Save in multiple formats: JPG, PNG

### Platform Setup
- [ ] **Audible/ACX** (if using):
  - [ ] Create ACX account
  - [ ] Set up as Rights Holder
  - [ ] Prepare audio files in M4B format with chapter markers
  - [ ] Pass ACX audio quality check
  - [ ] Upload cover art and metadata
- [ ] **Findaway Voices** (recommended):
  - [ ] Create Findaway account
  - [ ] Upload MP3 chapters
  - [ ] Add metadata (title, description, categories)
  - [ ] Select distribution platforms
- [ ] **Free Distribution**:
  - [ ] Upload to Archive.org
  - [ ] Submit to Dharma Seed (if accepted)
  - [ ] Create download page on personal website
- [ ] **Direct Sales**:
  - [ ] Set up Gumroad product listing
  - [ ] Set price ($9.99-14.99 or pay-what-you-want)
  - [ ] Create download delivery system

### Metadata & Description
- [ ] Write compelling audiobook description (150-300 words)
- [ ] Select categories:
  - [ ] Buddhism
  - [ ] Philosophy
  - [ ] Religious Studies
  - [ ] Spiritual Growth
- [ ] Add keywords: Buddhist training, Śāntideva, Mahāyāna, Blues translation, dharma
- [ ] Prepare author bio (100-150 words)

---

## Final QA Checklist

- [ ] Listen to complete audiobook from start to finish (or spot-check 20%)
- [ ] Verify all chapters play in correct order
- [ ] Check that chapter markers work correctly (if using M4B)
- [ ] Test on multiple platforms/devices:
  - [ ] Smartphone
  - [ ] Computer
  - [ ] Tablet
  - [ ] Car audio system (if available)
- [ ] Verify metadata displays correctly on all platforms
- [ ] Confirm cover art appears properly

---

## Launch Checklist

### Pre-Launch (1 week before)
- [ ] Announce upcoming release on social media / email list
- [ ] Prepare promotional materials (excerpt clips, quotes, images)
- [ ] Reach out to Buddhist podcasts / dharma centers for potential features
- [ ] Create landing page with "coming soon" message

### Launch Day
- [ ] Publish on all selected platforms
- [ ] Post announcement with purchase/download links
- [ ] Share on social media
- [ ] Email subscribers / dharma community
- [ ] Submit to relevant Buddhist subreddits (if appropriate)

### Post-Launch (1-2 weeks after)
- [ ] Monitor reviews and feedback
- [ ] Respond to listener comments/questions
- [ ] Track downloads/sales across platforms
- [ ] Gather testimonials for future marketing

---

## Budget Tracking

| Item | Estimated Cost | Actual Cost | Notes |
|------|----------------|-------------|-------|
| ElevenLabs Pro (1 month) | $99 | | Required for TTS generation |
| Cover art design | $0-200 | | Optional if DIY |
| ISBN (if needed) | $125 | | Only if required by platform |
| Audio editing software | $0-99 | | Audacity free, Audition $20/month |
| Distribution fees | $0 | | Most platforms free to upload |
| Marketing / promotion | Variable | | Optional |
| **TOTAL** | **$99-423** | | |

---

## Timeline Tracking

| Phase | Estimated Duration | Start Date | End Date | Status |
|-------|-------------------|------------|----------|--------|
| Pre-Production | 1-2 days | | | ⬜ Not Started |
| Voice Selection & Testing | 1 day | | | ⬜ Not Started |
| TTS Generation | 1-3 days | | | ⬜ Not Started |
| Post-Production | 2-4 days | | | ⬜ Not Started |
| Distribution Setup | 1-2 days | | | ⬜ Not Started |
| Platform Review | 2-4 weeks | | | ⬜ Not Started |
| **TOTAL** | **1-5 weeks** | | | ⬜ Not Started |

**Status Legend**:
- ⬜ Not Started
- 🔄 In Progress
- ✅ Complete

---

## Notes & Observations

Use this section to track issues, insights, or adjustments during production:

### Voice Selection Notes:
- Tested voices:
- Final choice:
- Reason:

### Audio Quality Issues:
- Mispronunciations to fix:
- Technical problems:
- Solutions applied:

### Platform-Specific Notes:
- ACX review feedback:
- Findaway approval status:
- Archive.org upload notes:

### Listener Feedback:
- Early reviews:
- Common comments:
- Improvements for future editions:

---

## Contact Information for Support

**ElevenLabs Support**: support@elevenlabs.io
**ACX Support**: https://www.acx.com/help/contact-us
**Findaway Support**: https://www.findawayvoices.com/support
**Archive.org Support**: info@archive.org

---

## Key Files Reference

- **Consolidated Manuscript**: `SHIKSHASAMUCCHAYA_COMPLETE_BLUES_AUDIOBOOK.md`
- **Audio Production Guide**: `AUDIO_PRODUCTION_GUIDE_ELEVENREADER.md`
- **Chapter Files**: `01_TRANSLATIONS/Chapter_*_Blues.md`
- **Completion Status**: `03_DOCUMENTATION/COMPLETION_STATUS.md`

---

**Last Updated**: January 2026
**Project**: Śikṣāsamuccaya Blues Audiobook
**Translator**: William Altig
