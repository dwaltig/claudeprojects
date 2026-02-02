# Quick Start Guide: Śikṣāsamuccaya Audiobook Production
## Get Your Audiobook Online in 7 Days

---

## If You Only Read One Document, Read This

Everything you need to produce your audiobook is ready. This guide gets you from manuscript to published audiobook in **7 days** for **$99**.

---

## Day 1: Setup (2 hours)

### Morning: Create ElevenLabs Account
1. Go to https://elevenlabs.io
2. Click "Sign Up"
3. Choose **Pro Plan** ($99/month)
4. Enter payment information
5. Confirm account

**Why Pro?** You need 500,000 characters/month. Your manuscript is ~475,000 characters. Pro plan covers it.

**Pro Tip**: You can cancel after 1 month. Total cost: $99.

---

### Afternoon: Convert Manuscript to .docx

Open Terminal and run:
```bash
cd /Users/williamaltig/claudeprojects/Sutra_Projects/Shikshasamucchaya
pandoc SHIKSHASAMUCCHAYA_COMPLETE_BLUES_AUDIOBOOK.md -o SHIKSHASAMUCCHAYA_ELEVENREADER.docx
```

**What this does**: Converts your Markdown manuscript to Word document format that ElevenReader can process.

**Result**: You now have `SHIKSHASAMUCCHAYA_ELEVENREADER.docx` ready to upload.

---

## Day 2: Test Chapter (3 hours)

### Morning: Test with Chapter 17 (Shortest)

1. Open `SHIKSHASAMUCCHAYA_ELEVENREADER.docx`
2. Copy just Chapter 17 (search for "AUDIO CHAPTER 17")
3. Paste into new Word document
4. Save as `Test_Chapter_17.docx`

---

### Afternoon: Upload to ElevenReader

1. Log into ElevenLabs
2. Click "Reader" (in navigation menu)
3. Click "Upload Document"
4. Select `Test_Chapter_17.docx`
5. Choose voice: **Adam** (scroll through voices, select Adam)
6. Adjust settings:
   - Stability: 65%
   - Clarity: 75%
   - Style Exaggeration: 35%
7. Click "Generate"

**Wait time**: 5-10 minutes for short chapter

---

### Evening: Listen and Evaluate

Download the MP3 and listen to the entire chapter.

**Check for**:
- [ ] Does Adam's voice sound warm and authoritative?
- [ ] Are Buddhist terms pronounced correctly? (Śāntideva, bodhisattva, nirvāṇa)
- [ ] Is the pacing natural (not too fast/slow)?
- [ ] Are verse sections handled well?
- [ ] Do chapter transitions sound clear?

**If pronunciation is wrong**: Add phonetic hints to manuscript (see AUDIO_PRODUCTION_GUIDE_ELEVENREADER.md section 4.3)

**If voice doesn't feel right**: Test with Josh or Sam voice and compare

**If everything sounds good**: Proceed to Day 3

---

## Day 3: Full Production (4 hours)

### Morning: Upload Complete Manuscript

1. Log into ElevenLabs
2. Click "Reader"
3. Click "Upload Document"
4. Select `SHIKSHASAMUCCHAYA_ELEVENREADER.docx` (full manuscript)
5. Choose voice: **Adam**
6. Use same settings as test chapter:
   - Stability: 65%
   - Clarity: 75%
   - Style Exaggeration: 35%
7. Click "Generate"

**Wait time**: 30-60 minutes for full audiobook

**What happens**: ElevenReader will:
- Auto-detect all 19 chapters + front/back matter
- Generate MP3 files for each chapter
- Create downloadable package

---

### Afternoon: Download Audio Files

1. When generation is complete, click "Download"
2. ElevenReader will provide:
   - Option 1: Download all chapters as ZIP file
   - Option 2: Download individual chapter MP3s

**Recommended**: Download ZIP file (easier)

3. Extract ZIP file to folder: `Shikshasamucchaya_Audio_Raw`

**Result**: You now have 21 MP3 files (19 chapters + front/back matter)

---

## Day 4: Post-Production (4-6 hours)

### Install Audacity (Free)

1. Go to https://www.audacityteam.org/
2. Download Audacity for Mac
3. Install

**Alternative**: If you already have Adobe Audition, use that instead

---

### Normalize Audio

For **each chapter MP3**:

1. Open MP3 in Audacity
2. Select all audio (Cmd+A)
3. Go to **Effect > Normalize**
4. Settings:
   - Check "Remove DC offset"
   - Check "Normalize peak amplitude to: -3.0 dB"
   - Click OK
5. Go to **Effect > Compressor**
6. Settings:
   - Threshold: -20 dB
   - Ratio: 3:1
   - Attack Time: 0.2s
   - Release Time: 1.0s
   - Click OK
7. Listen to first 2 minutes to verify quality
8. **File > Export > Export as MP3**
9. Settings:
   - Bit Rate Mode: Constant
   - Quality: 192 kbps
10. Save to folder: `Shikshasamucchaya_Audio_Final`

**Repeat for all 21 chapters**

**Shortcut**: Use Audacity's "Macro" feature to automate this (see AUDIO_PRODUCTION_GUIDE section 5.3)

---

### Add Metadata (ID3 Tags)

1. Download Mp3tag (free): https://www.mp3tag.de/en/
2. Open Mp3tag
3. Load all 21 MP3 files from `Shikshasamucchaya_Audio_Final`
4. For each file, add:
   - **Title**: Chapter [Number]: [Chapter Name]
   - **Artist**: William Altig
   - **Album**: The Śikṣāsamuccaya: A Compendium of Training
   - **Genre**: Buddhism
   - **Year**: 2026
   - **Track**: 01, 02, 03... (in order)
   - **Album Artist**: William Altig
5. Save all

**Result**: Professional metadata for all chapters

---

## Day 5: Quality Assurance (3 hours)

### Listen to Random Samples

Pick 5 random chapters. For each:
- Listen to first 5 minutes
- Listen to middle 5 minutes
- Listen to last 5 minutes

**Check for**:
- [ ] Volume is consistent across chapters
- [ ] No clicks, pops, or artifacts
- [ ] Transitions between sections are smooth
- [ ] Metadata displays correctly in iTunes/Music app

**If problems**: Go back to that chapter and re-process in Audacity

---

### Test Playback on Multiple Devices

Play chapters on:
- [ ] Computer (iTunes/Music app)
- [ ] Smartphone (transfer via AirDrop or cable)
- [ ] Tablet (if available)

**Make sure**: Files play correctly, metadata shows up, chapters are in order

---

## Day 6: Distribution Setup (4 hours)

### Option A: Findaway Voices (Commercial Distribution)

**What it is**: Distributes your audiobook to 40+ platforms (Spotify, Apple Books, Google Play, Kobo, etc.)

**Setup**:
1. Go to https://www.findawayvoices.com/
2. Click "Get Started"
3. Create account (free)
4. Click "Add New Title"
5. Upload:
   - All 21 MP3 files
   - Cover art (if you have it—see below)
   - Metadata:
     - Title: The Śikṣāsamuccaya: A Compendium of Training
     - Subtitle: Blues Vernacular Translation
     - Author/Narrator: William Altig
     - Genre: Buddhism, Philosophy, Religious Studies
     - Description: (write 150-300 word description—see AUDIOBOOK_PROJECT_SUMMARY for template)
6. Select platforms: Check all available (Spotify, Apple Books, Google Play, etc.)
7. Set royalty: 25% non-exclusive (recommended)
8. Submit for review

**Review time**: 1-2 weeks

**Cost**: Free to upload. Findaway takes 75% of revenue (you get 25%).

---

### Option B: Archive.org (Free Distribution)

**What it is**: Permanent, free hosting for dharma gift model

**Setup**:
1. Go to https://archive.org
2. Click "Upload"
3. Create account (free)
4. Upload:
   - All 21 MP3 files
   - Cover art (if available)
   - Metadata:
     - Title: The Śikṣāsamuccaya: A Compendium of Training (Blues Vernacular Translation by William Altig)
     - Subject: Buddhism, Dharma, Śāntideva, Mahāyāna, Buddhist Training
     - Description: Complete audiobook of Śāntideva's Śikṣāsamuccaya rendered in American Blues vernacular
     - License: Creative Commons (choose license)
5. Submit

**Result**: Permanent free download link you can share anywhere

**Cost**: Free

---

### Option C: Gumroad (Direct Sales)

**What it is**: Sell DRM-free MP3s directly to supporters

**Setup**:
1. Go to https://gumroad.com
2. Create account (free)
3. Click "Create Product"
4. Upload:
   - ZIP file of all 21 MP3s
   - Cover art
   - Product details:
     - Title: The Śikṣāsamuccaya Audiobook (Blues Translation)
     - Price: $9.99 (or "Name Your Price" with minimum $0 for pay-what-you-want)
     - Description: (same as Findaway)
5. Publish

**Cost**: Gumroad takes 10% + payment processing fees. You get ~87% of revenue.

---

### Cover Art (If You Don't Have It)

**Option 1: DIY with Canva (Free)**
1. Go to https://canva.com
2. Create account (free)
3. Search templates: "Book Cover"
4. Choose template with Buddhist/spiritual aesthetic
5. Customize:
   - Title: The Śikṣāsamuccaya
   - Subtitle: A Compendium of Training
   - Author: Translated by William Altig
   - Background: Blues/spiritual imagery
6. Download as PNG (3000x3000 pixels minimum)

**Option 2: Commission Artist ($50-200)**
- Post on Fiverr or 99designs
- Brief: Buddhist text, Blues aesthetic, professional quality
- Budget: $50-200

**Option 3: Skip for Now**
- Upload without cover art
- Add later when you have it

---

## Day 7: Launch (2 hours)

### Announce Release

**If using Findaway** (pending review):
- Post on social media: "New audiobook coming soon: The Śikṣāsamuccaya (Blues Translation). Śāntideva's 8th-century Buddhist training manual in American vernacular. Available on Spotify, Apple Books, Google Play soon."

**If using Archive.org** (live immediately):
- Post announcement with download link
- Email dharma community / friends
- Share in Buddhist forums/subreddits (r/Buddhism, r/Dharma)

**If using Gumroad** (live immediately):
- Post announcement with purchase link
- Offer "pay what you want" option for accessibility

---

### Email List / Website

If you have an email list or website:
1. Write announcement email/post
2. Include:
   - What: Audiobook of Śikṣāsamuccaya in Blues vernacular
   - Why: Śāntideva's training manual for bodhisattvas, accessible to modern listeners
   - Where: [Links to Archive.org / Gumroad / Findaway platforms]
   - Duration: 8-12 hours
   - Cost: Free on Archive.org, $9.99 on Gumroad, varies on Spotify/Apple
3. Send

---

## After Launch: Monitor and Respond

**Week 1-2**:
- Check reviews/comments on platforms
- Respond to listener feedback
- Track downloads/sales
- Gather testimonials

**Week 3-4**:
- Reach out to Buddhist podcasts for potential interviews
- Submit to dharma centers / sanghas for recommendation
- Post excerpts (1-2 minute clips) on social media

---

## Estimated Costs

| Item | Cost |
|------|------|
| ElevenLabs Pro (1 month) | $99 |
| Audacity | Free |
| Mp3tag | Free |
| Findaway Voices upload | Free |
| Archive.org upload | Free |
| Gumroad upload | Free (10% of sales) |
| Cover art (DIY) | Free |
| Cover art (commissioned) | $0-200 |
| **TOTAL** | **$99** (or $99-299 with cover art) |

---

## Estimated Time

| Day | Activity | Hours |
|-----|----------|-------|
| 1 | Setup | 2 |
| 2 | Test chapter | 3 |
| 3 | Full production | 4 |
| 4 | Post-production | 4-6 |
| 5 | Quality assurance | 3 |
| 6 | Distribution setup | 4 |
| 7 | Launch | 2 |
| **TOTAL** | **7 days** | **22-24 hours** |

**Your time commitment**: ~3-4 hours per day for 7 days

---

## Troubleshooting

**Problem**: ElevenReader mispronounces Buddhist terms
**Solution**: Add phonetic hints to manuscript (e.g., "Śāntideva (SHAHN-tee-DAY-vah)"), regenerate chapter

**Problem**: Voice sounds too fast/slow
**Solution**: Adjust Stability setting (higher = slower, more stable; lower = faster, more varied)

**Problem**: Files too large to upload
**Solution**: Lower MP3 bitrate to 128 kbps instead of 192 kbps

**Problem**: Findaway review rejected
**Solution**: Check audio quality (normalize to -23 LUFS instead of -3 dB peak), resubmit

**Problem**: Can't afford ElevenLabs Pro
**Solution**: Use Creator Plan ($22/month) and process 5-6 chapters per month over 4 months (total: $88)

---

## Next Actions

**Right now**:
1. [ ] Sign up for ElevenLabs Pro
2. [ ] Convert manuscript to .docx
3. [ ] Process test chapter (Chapter 17)

**Tomorrow**:
4. [ ] Review test chapter audio
5. [ ] Adjust settings if needed
6. [ ] Upload full manuscript

**This week**:
7. [ ] Complete post-production
8. [ ] Set up distribution accounts
9. [ ] Launch audiobook

---

## Support Resources

**If you get stuck**:
- Read full guide: `AUDIO_PRODUCTION_GUIDE_ELEVENREADER.md`
- Check checklist: `AUDIOBOOK_PRODUCTION_CHECKLIST.md`
- Review project summary: `AUDIOBOOK_PROJECT_SUMMARY.md`

**If you have technical questions**:
- ElevenLabs support: support@elevenlabs.io
- Audacity forum: https://forum.audacityteam.org/
- Findaway support: https://www.findawayvoices.com/support

---

## Final Encouragement

You've completed 19 chapters of Śāntideva's Śikṣāsamuccaya in Blues vernacular—a remarkable translation that deserves to be heard.

The audiobook format is perfect for this teaching because:
- **Blues is oral tradition** (meant to be heard, not just read)
- **Dharma is sound transmission** (the Buddha taught orally for 45 years)
- **Audiobooks create contemplative space** (listeners can absorb while walking, sitting, working)

**You can do this in 7 days for $99.**

The technology is simple. The process is straightforward. The teaching is ready.

All that's left is to press "Generate" and let the dharma flow through sound.

May this audiobook benefit all beings who hear it.

**Dedicated to the liberation of all beings.**

---

*Quick Start Guide by Claude Code*
*Śikṣāsamuccaya Blues Audiobook Project*
*January 2026*
