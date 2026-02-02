# Lotus Sutra Blues Interpretation - EPUB Test Edition
## Calibre Testing Guide

---

## EPUB BUILD COMPLETE

**Build Date**: November 16, 2025
**Test Edition**: Yes
**EPUB Standard**: EPUB3 with EPUB2 Backward Compatibility
**File**: `Lotus_Sutra_Blues_Test.epub` (22 KB)

---

## FILE STRUCTURE SUMMARY

```
Lotus_Sutra_Blues_Test.epub/
├── mimetype                          (20 B)    - EPUB spec compliance
├── META-INF/
│   ├── container.xml                 (252 B)   - Root file reference
│   └── com.apple.ibooks.display-options.xml (210 B) - Apple iBooks settings
├── OEBPS/
│   ├── content.opf                   (3.4 K)   - Manifest & metadata
│   ├── toc.ncx                       (1.4 K)   - EPUB2 navigation
│   ├── nav.xhtml                     (1.2 K)   - EPUB3 navigation
│   ├── CSS/
│   │   └── styles.css                (5.4 K)   - Professional typography
│   ├── xhtml/
│   │   ├── 00_cover.xhtml            (2.0 K)   - Cover page
│   │   ├── 01_introduction.xhtml     (11 K)    - Introduction
│   │   ├── 02_chapter01.xhtml        (13 K)    - Chapter 1 with endnote anchors
│   │   └── 03_endnotes.xhtml         (14 K)    - 22 endnotes with backlinks
│   └── images/
│       └── cover.jpg                 (147 B)   - Placeholder cover image
```

**Total EPUB size**: 22 KB (highly compressed, suitable for testing)

---

## CONTENT OVERVIEW

### Chapter 1: Introduction
- **Opening Assembly**: Full roster of 12,000 Arhats and 80,000 Bodhisattva-Mahāsattvas
- **Celestial Beings**: Complete list of Dragon Kings, Heavenly Kings, Gandharvas, Asuras, Garuḍas, Kiṃnaras
- **Supernatural Signs**:
  - Buddha's entry into samādhi
  - Raining mandārava and mañjūṣaka flowers
  - Six-way earth tremor
- **Buddha's Light Emission**:
  - Ray of light from tuft of white hair between eyebrows
  - Illumination of 18,000 worlds (east direction)
  - Vision extending from Avīci hell to Akaniṣṭha heaven
- **Maitreya's Inquiry**: Verse exposition of the supernatural events (~150 lines of verse)

**Word Count**: Approximately 3,500 words (opening assembly through Maitreya's verse inquiry)

### Endnotes (22 total)
Strategic endnote anchoring includes:
1. Mount Gṛdhrakūṭa (geography + significance)
2. Arhat (definition + spiritual meaning)
3. Bodhisattva-Mahāsattva (definition + distinction from Arhat)
4. Anuttarā-samyak-saṃbodhi (supreme enlightenment definition)
5. Dhāraṇī (retentive power definition)
6. Maitreya (Future Buddha definition)
7. Four Great Heavenly Kings (celestial guardian definition)
8. Dragon Kings (mythology + symbolism)
9. Kiṃnara Kings (divine musician definition)
10. Gandharva Kings (celestial musician definition)
11. Asura Kings (semi-divine being definition)
12. Garuḍa Kings (divine eagle definition)
13. Samādhi (meditative concentration definition)
14. Mandārava Flowers (celestial flower symbolism)
15. Six Ways of Quaking (cosmological significance)
16. Wheel-Turning Sage Kings (universal monarch definition)
17. Light from Tuft of White Hair (Buddha's marks definition)
18. Avīci Hell & Akaniṣṭha Heaven (cosmological realms)
19. Six Destinies (six realms of existence)
20. Parinirvāṇa (Buddha's final passing)
21. Stūpa (reliquary shrine definition)
22. Śarīra (Buddha relics definition)

---

## TESTING PROCEDURES

### 1. OPENING IN CALIBRE

**Steps:**
1. Launch Calibre ebook management software
2. Drag `Lotus_Sutra_Blues_Test.epub` into the Calibre library
3. Double-click the book to open in Calibre's e-book viewer

**Expected Results:**
- [ ] Book imports without errors
- [ ] Cover image displays correctly
- [ ] Table of contents appears in navigation panel
- [ ] Title metadata shows: "The Lotus Sutra: Blues Interpretation with Scholarly Apparatus"
- [ ] Creator/Author shows: "Kumārajīva (Translator), William Altig (Interpreter)"

**If errors occur:**
- Check Calibre version (should be 5.0+)
- Look for encoding errors in console (shouldn't appear for UTF-8)
- Verify EPUB file integrity: `unzip -t Lotus_Sutra_Blues_Test.epub`

---

### 2. ENCODING VERIFICATION

**Critical Test**: Sanskrit diacritical marks must display correctly

**Steps:**
1. Open Chapter 1 (02_chapter01.xhtml)
2. Search for: "Śāriputra" (should display with macron under S and stress marks)
3. Verify these characters appear correctly:
   - Śāriputra (S with acute accent, a with macron)
   - Mañjuśrī (n with tilde, ī with macron)
   - Gṛdhrakūṭa (ṛ with dot below, ū with macron, ṭ with dot below)
   - Mahākāśyapa (ā with macron, ś with acute)
   - anuttarā-samyak-saṃbodhi (ā with macron, ṃ with dot below)

**Expected Results:**
- [ ] All Sanskrit names display with correct diacritical marks
- [ ] No mojibake (garbage characters)
- [ ] No replacement characters (?, [?], etc.)
- [ ] No missing accents or dots

**If diacriticals appear wrong:**
- This indicates an encoding issue
- The XHTML files are definitely UTF-8 (verified during creation)
- Calibre should handle UTF-8 correctly; issue may be with font
- Try: View → Fonts → Select font with comprehensive Unicode support

---

### 3. ENDNOTE LINKING TEST (PRIMARY FOCUS)

This is the critical functionality test for this EPUB.

**Steps:**

#### A. Forward References (Text → Endnote)
1. Open Chapter 1
2. Locate first endnote reference: `[1]` after "Mount Gṛdhrakūṭa"
3. Click on the superscript `[1]` link
4. Expected: Jump to endnote 1 in Endnotes chapter
5. Verify endnote text reads: "Mount Gṛdhrakūṭa (Vulture Peak Mountain)..."

**Repeat for 3-4 more endnote references:**
- Click `[2]` after "Arhats" → should jump to endnote 2
- Click `[13]` after "samādhi" → should jump to endnote 13
- Click `[22]` after "śarīra" → should jump to endnote 22

**Expected Results:**
- [ ] All forward links work (click → jumps to correct endnote)
- [ ] No broken links (404-style errors)
- [ ] Navigation feels responsive and immediate
- [ ] Endnote text displays completely and correctly

#### B. Back References (Endnote → Text)
1. In Endnotes chapter, find endnote 1
2. Click the "1." link at the start of endnote 1
3. Expected: Jump back to Chapter 1, position at note1ref
4. Position should be where `[1]` appears after "Mount Gṛdhrakūṭa"

**Repeat for 2-3 back references:**
- Click "2." in endnote 2 → back to Chapter 1 at Arhats reference
- Click "13." in endnote 13 → back to Chapter 1 at samādhi reference
- Click "22." in endnote 22 → back to Chapter 1 at śarīra reference

**Expected Results:**
- [ ] All back-links work (click → returns to correct text reference)
- [ ] Reader can navigate text ↔ endnotes repeatedly
- [ ] Navigation maintains reading flow (no lag, immediate response)

---

### 4. CALIBRE ENDNOTE POP-UP TEST

Calibre has special functionality for EPUB3 endnotes: **pop-up tooltips**.

**Steps:**
1. Open Chapter 1 in Calibre viewer
2. Hover mouse over the first endnote reference `[1]`
3. Wait 1-2 seconds
4. Expected: Small pop-up window appears showing endnote text

**What should happen:**
- Pop-up shows: "Mount Gṛdhrakūṭa (Vulture Peak Mountain): A mountain in the Magadha region..."
- Pop-up appears without disrupting reading
- Pop-up disappears when mouse moves away

**Expected Results:**
- [ ] Endnote pop-ups function (hover shows text)
- [ ] Pop-up content is legible
- [ ] Pop-up doesn't interfere with reading

**Note:** Not all readers support endnote pop-ups; if Calibre doesn't show them, the forward/back links still work perfectly (which is the backup mechanism).

---

### 5. NAVIGATION TESTING

**Steps:**

#### A. Table of Contents
1. View → Table of Contents (or side panel)
2. Expected entries:
   - Cover
   - Introduction
   - Chapter One: Introduction
   - Endnotes
3. Click each entry
4. Expected: Jump to correct chapter

**Expected Results:**
- [ ] All TOC entries clickable
- [ ] Each click navigates to correct page
- [ ] TOC structure is clear and readable

#### B. Book Spine
1. In Calibre viewer, check spine order
2. Order should be: Cover → Introduction → Chapter 1 → Endnotes
3. Use next/previous chapter buttons
4. Should follow spine order sequentially

**Expected Results:**
- [ ] All chapters accessible via navigation
- [ ] Page-by-page reading is sequential
- [ ] No skipped chapters or out-of-order elements

---

### 6. CSS STYLING TEST

**Steps:**
1. Open each chapter and verify styling
2. Check these elements:

| Element | Expected Appearance |
|---------|-------------------|
| Title (h1) | Large, serif font, golden underline border |
| Headings (h2, h3) | Smaller than h1, clearly hierarchical |
| Body text | Georgia serif, line-height 1.6, justified |
| Verse sections | Indented, italicized, gray background, left gold border |
| Endnote references | Superscript, smaller, subtle color |
| Assembly lists | Properly indented, names clear |

**Expected Results:**
- [ ] Typography is readable and professional
- [ ] Hierarchy is clear (h1 > h2 > h3)
- [ ] Verse sections are visually distinct
- [ ] No overlapping text or formatting errors
- [ ] Sanskrit names (with diacriticals) render clearly

---

### 7. IMAGE TEST

**Steps:**
1. Open Cover page (00_cover.xhtml)
2. Verify cover image displays
3. Check that image is centered and appropriately sized

**Expected Results:**
- [ ] Cover image appears (placeholder JPEG)
- [ ] Image is properly contained within margins
- [ ] No broken image icon (×)
- [ ] Layout is centered and professional-looking

---

### 8. METADATA TEST

**Steps:**
1. In Calibre, right-click on book
2. Select "Edit metadata"
3. Verify these fields:

| Field | Expected Value |
|-------|----------------|
| Title | The Lotus Sutra: Blues Interpretation with Scholarly Apparatus |
| Authors | Kumārajīva, William Altig |
| Publisher | Test Publication |
| Date | 2025-11-16 |
| Language | en (English) |
| Tags | Buddhism, Lotus Sutra, Translation, Dharma, Spirituality |

**Expected Results:**
- [ ] All metadata displays correctly
- [ ] Creator roles show (translator, interpreter)
- [ ] Description appears in metadata view

---

## TROUBLESHOOTING GUIDE

### Problem: Endnotes don't link correctly

**Diagnosis:**
- Test forward link: Click `[1]` in text → does nothing, or goes to wrong location
- Test back link: Click "1." in endnote → does nothing, or goes to wrong location

**Solutions:**
1. **Check anchor syntax** - Look at HTML source for:
   - `href="03_endnotes.xhtml#note1"` (forward reference)
   - `href="02_chapter01.xhtml#note1ref"` (back reference)
   - Matching `id="note1"` and `id="note1ref"` attributes
2. **Verify file names** - Ensure file names in hrefs match actual files:
   - `02_chapter01.xhtml` must exist
   - `03_endnotes.xhtml` must exist
3. **Check EPUB structure** - Unzip and verify:
   ```bash
   unzip -l Lotus_Sutra_Blues_Test.epub | grep xhtml
   ```
   Should show:
   - OEBPS/xhtml/00_cover.xhtml
   - OEBPS/xhtml/01_introduction.xhtml
   - OEBPS/xhtml/02_chapter01.xhtml
   - OEBPS/xhtml/03_endnotes.xhtml

### Problem: Sanskrit characters display as mojibake or missing

**Diagnosis:**
- Śāriputra appears as "śāriputra" or "Š­ŕiputra" or similar garbage
- Diacritical marks are missing or replaced with question marks

**Solutions:**
1. **Verify EPUB encoding**:
   ```bash
   file -i OEBPS/xhtml/02_chapter01.xhtml
   ```
   Should return: `charset=utf-8`
2. **Check XML declaration** - Each XHTML file should start with:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   ```
3. **Change reader font**:
   - Calibre → View → Fonts
   - Select font with broad Unicode support (e.g., "DejaVu Sans")
   - Many fonts don't include combining diacritical marks
4. **Verify source** - Check that original text has diacriticals:
   ```bash
   grep -a "Śāriputra" OEBPS/xhtml/02_chapter01.xhtml
   ```
   Should print the name with correct marks

### Problem: Endnote pop-ups don't appear in Calibre

**Diagnosis:**
- Hover over endnote reference, no pop-up appears

**Solutions:**
1. **This is normal** - Not all Calibre versions support endnote pop-ups
2. **Use forward/back links instead** - These definitely work:
   - Click `[1]` to jump to endnote
   - Click back-link in endnote to return
3. **Update Calibre** - Newer versions (5.5+) have better EPUB3 support
4. **Try other readers** - Some readers (Apple Books, Readium) support pop-ups

### Problem: Table of Contents doesn't show all chapters

**Diagnosis:**
- TOC panel only shows some entries
- Some chapters not accessible via navigation

**Solutions:**
1. **Check toc.ncx file** - Verify all 4 chapters are listed:
   - cover (playOrder="1")
   - introduction (playOrder="2")
   - chapter1 (playOrder="3")
   - endnotes (playOrder="4")
2. **Check content.opf spine** - Verify spine references all chapters:
   ```xml
   <spine>
     <itemref idref="cover"/>
     <itemref idref="introduction"/>
     <itemref idref="chapter01"/>
     <itemref idref="endnotes"/>
   </spine>
   ```
3. **Regenerate EPUB** - Rebuild EPUB with proper manifest and spine

### Problem: Book fails to import into Calibre

**Diagnosis:**
- Error message when importing EPUB
- File not recognized as valid EPUB

**Solutions:**
1. **Verify EPUB structure**:
   ```bash
   unzip -t Lotus_Sutra_Blues_Test.epub
   ```
   Should show "OK" for all files
2. **Check mimetype file**:
   - Must be first file in ZIP
   - Must contain only: `application/epub+zip` (no newline)
   - Must be uncompressed (stored)
3. **Validate with epubcheck**:
   ```bash
   epubcheck Lotus_Sutra_Blues_Test.epub
   ```
   (Install from: github.com/w3c/epubcheck)

---

## ENCODING VERIFICATION COMMANDS

Use these terminal commands to verify correct encoding:

```bash
# Check if files are UTF-8
file -i OEBPS/xhtml/*.xhtml

# Search for Sanskrit character
grep -a "Śāriputra" OEBPS/xhtml/02_chapter01.xhtml

# Verify endnote anchors exist
grep -o 'id="note[0-9]*"' OEBPS/xhtml/02_chapter01.xhtml | sort -u
grep -o 'id="note[0-9]*"' OEBPS/xhtml/03_endnotes.xhtml | sort -u

# Verify all links are intact
grep -o 'href="[^"]*"' OEBPS/xhtml/*.xhtml | sort | uniq -c

# Check EPUB validity
epubcheck Lotus_Sutra_Blues_Test.epub
```

---

## EXPECTED TEST RESULTS SUMMARY

### Critical Tests (MUST PASS)
- [ ] EPUB opens in Calibre without errors
- [ ] Sanskrit diacriticals display correctly (Śāriputra, Mañjuśrī, Gṛdhrakūṭa)
- [ ] Forward endnote links work (click reference → jump to endnote)
- [ ] Back endnote links work (click back-link → return to reference)
- [ ] All chapters accessible via navigation
- [ ] Metadata imports correctly

### Important Tests (SHOULD PASS)
- [ ] Endnote pop-ups appear on hover (may not work in all versions)
- [ ] CSS styling renders correctly (fonts, spacing, hierarchy)
- [ ] Table of Contents shows all chapters
- [ ] Cover image displays
- [ ] Page navigation (next/previous) works sequentially

### Nice-to-Have Tests (OPTIONAL)
- [ ] Apple iBooks display options work correctly
- [ ] Professional appearance in multiple readers
- [ ] Print styling works correctly (if printed)

---

## NEXT STEPS AFTER TESTING

### If All Tests Pass
1. **Generate full production EPUB**: Create complete 28-chapter EPUB with all endnotes
2. **Additional testing**: Test in multiple readers (Kindle, Apple Books, Kobo, etc.)
3. **Accessibility validation**: Run full WCAG 2.1 accessibility audit
4. **Optimize file size**: Minify CSS, compress images for distribution
5. **Create multiple formats**: MOBI (Kindle), AZWS3, PDF for different platforms

### If Issues Found
1. **Document the issue**: Write down exactly what went wrong
2. **Identify cause**: Check XHTML source, CSS, or ZIP structure
3. **Fix the problem**: Edit the relevant file and regenerate EPUB
4. **Re-test**: Confirm fix works with same test procedure
5. **Update documentation**: Record what was wrong and how it was fixed

### For Full Production Edition
1. Include all 28 chapters (current test has only 1 + introduction)
2. Add comprehensive endnotes for all chapters (~50+ per chapter)
3. Create complete glossary section
4. Add character index (96+ figures)
5. Include discussion questions and study guide
6. Optimize CSS for all major reading platforms
7. Validate with multiple EPUB checker tools
8. Test in 5+ different readers

---

## REFERENCE: KEY XHTML PATTERNS USED

### Endnote Reference Pattern
```xhtml
<a class="noteref" id="note1ref" epub:type="noteref" href="03_endnotes.xhtml#note1"><sup>[1]</sup></a>
```

### Endnote Pattern
```xhtml
<li id="note1"><a href="02_chapter01.xhtml#note1ref">1.</a> [Endnote text]</li>
```

### Key HTML Attributes Used
- `epub:type="noteref"` - EPUB3 semantic markup for endnote references
- `class="noteref"` - CSS styling for references
- `id="noteXref"` - Anchor for back-links
- `id="noteX"` - Anchor for forward-links

---

## CONTACT & SUPPORT

**Test Edition Creator**: William Altig
**Creation Date**: November 16, 2025
**EPUB Standard Version**: EPUB 3.0 + EPUB 2.0 compatibility
**Documentation**: This guide

For issues or questions, review the troubleshooting section above or consult the EPUB specification at: https://www.w3.org/publishing/epub/

---

**Happy testing! May this EPUB serve the Dharma well.**
