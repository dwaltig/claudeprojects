# Wenju Scholarly Translation – Defect Register
## Autonomous Convergence System

**Purpose:** Structured defect log for compiler-based translation QA (CBETA‑anchored)
**Authority:** CBETA T.1718 (Taishō Tripiṭaka vol. 34, no. 1718)
**Target:** Zero open defects across all translation files
**Status:** AUDIT IN PROGRESS

---

## GLOBAL STATUS

- **Files audited:** 14 / 14
- **Files PASS:** 14 / 14
- **Files FAIL:** 0 / 14
- **Open defects:** 0
- **Repaired – Pending Re‑Audit:** 0
- **Closed defects:** 152

---

## DEFECT ENTRIES

### DEFECT-F01-001
- **File name:** Wenju_Fascicle_01_FULL_Scholarly.md
- **Fascicle:** 1
- **CBETA source file:** T1718_001.txt
- **CBETA line numbers:** 541–560
- **Chinese text (quoted):**
  - 「摩訶迦栴延」…「有外道執斷見謂無他世…凡有十番問答…」…「尊者前說日月而我已解…」
  - 「律中云：『善能教化歸戒…』又世典婆羅門…周利作十八變…」
  - 「約教論義者…」
  - 「阿㝹樓馱…昔於饑世…」
- **Translation excerpt:**
  - Summary bullets under **[541]**, **[548]**, **[553]**, **[559]** and truncated Dirgha/Vinaya dialogue.
- **Defect type:** Omission (summary/paraphrase)
- **Required correction:**
  - Replace the summary bullets from **[541]** through **[559]** with full CBETA text and line‑by‑line bilingual translation.
  - Preserve all Q/A exchanges and every analogy in the ten‑round Dirgha Agama debate.
  - Preserve Vinaya and World‑Classic Brahmin dialogue in full.
- **Status:** Closed

---

## XUANYI STATUS (FASCICLE 2)

- **Files audited:** 2 / 4
- **Files PASS:** 2 / 4
- **Files FAIL:** 0 / 4
- **Open defects:** 0
- **Repaired – Pending Re‑Audit:** 0
- **Closed defects:** 16

---

## XUANYI DEFECT ENTRIES (FASCICLE 2)

### DEFECT-X02-001
- **File name:** Xuanyi_Fascicle_02_Part_1_Three_Dharmas_SCHOLARLY.md
- **Fascicle:** 2 (Xuanyi)
- **CBETA source file:** T1716_002.txt
- **CBETA line numbers:** 19
- **Chinese text (quoted):**
  - 「《殃掘》云：「所謂彼眼根，於諸如來常，具足無減修，了了分明見。」」
  - 「乃至意根亦如是。」
  - 「眼尚不可得，何況有趣、有非趣？乃至一切法趣意，亦如是。」
- **Defect type:** Omission (missing citation block)
- **Required correction:**
  - Insert the missing *Aṅgulimālīya* citation and the “不可得” lines between the *Mahāparinirvāṇa* and *Mahāprajñāpāramitā* citations.
- **Post‑edit excerpt (Xuanyi_Fascicle_02_Part_1_Three_Dharmas_SCHOLARLY.md):**
  ```
  《殃掘》云：「所謂彼眼根，於諸如來常，具足無減修，了了分明見。」
  乃至意根亦如是。
  眼尚不可得，何況有趣、有非趣？乃至一切法趣意，亦如是。
  ```
- **Status:** Closed

### DEFECT-X02-002
- **File name:** Xuanyi_Fascicle_02_Part_1_Three_Dharmas_SCHOLARLY.md
- **Fascicle:** 2 (Xuanyi)
- **CBETA source file:** T1716_002.txt
- **CBETA line numbers:** 25–27
- **Chinese text (quoted):**
  - 「△今依三法，更廣分別。」
  - 「眾生法為二：先列法數，次解法相。」
  - 「或明二法攝一切法…或明三法攝一切法…如是等增數，乃至百千。」
- **Defect type:** Omission (missing transition + classification)
- **Required correction:**
  - Insert the “△今依三法…” transition and the “眾生法為二…” classification block before the Ten Suchnesses section.
- **Post‑edit excerpt (Xuanyi_Fascicle_02_Part_1_Three_Dharmas_SCHOLARLY.md):**
  ```
  △今依三法，更廣分別。
  眾生法為二：先列法數，次解法相。
  或明二法攝一切法…或明三法攝一切法…如是等增數，乃至百千。
  ```
- **Status:** Closed

### DEFECT-X02-003
- **File name:** Xuanyi_Fascicle_02_Part_1_Three_Dharmas_SCHOLARLY.md
- **Fascicle:** 2 (Xuanyi)
- **CBETA source file:** T1716_002.txt
- **CBETA line numbers:** 29
- **Chinese text (quoted):**
  - 「若依義便，作三意分別。」
  - 「若依讀便，當依偈文云：「如是大果報，種種性相義」(云云)。」
- **Defect type:** Omission (missing post‑reading clause)
- **Required correction:**
  - Restore both “依義便 / 依讀便” lines after the threefold reading section.
- **Post‑edit excerpt (Xuanyi_Fascicle_02_Part_1_Three_Dharmas_SCHOLARLY.md):**
  ```
  若依義便，作三意分別。
  若依讀便，當依偈文云：「如是大果報，種種性相義」(云云)。
  ```
- **Status:** Closed

### DEFECT-X02-004
- **File name:** Xuanyi_Fascicle_02_Part_1_Three_Dharmas_SCHOLARLY.md
- **Fascicle:** 2 (Xuanyi)
- **CBETA source file:** T1716_002.txt
- **CBETA line numbers:** 15
- **Chinese text (quoted):**
  - 「又乳經一種因果廣、高、長，一種因果狹、下、短，則一麁一妙(云云)。」
  - 「酪經唯一種因果狹、下、短，但麁無妙。」
- **Defect type:** Text divergence (omitted particles / altered line)
- **Required correction:**
  - Restore the “(云云)” and “酪經” in the Chinese linework.
- **Post‑edit excerpt (Xuanyi_Fascicle_02_Part_1_Three_Dharmas_SCHOLARLY.md):**
  ```
  又乳經一種因果廣、高、長，一種因果狹、下、短，則一麁一妙(云云)。
  酪經唯一種因果狹、下、短，但麁無妙。
  ```
- **Status:** Closed

### DEFECT-X02-005
- **File name:** Xuanyi_Fascicle_02_Part_1_Three_Dharmas_SCHOLARLY.md
- **Fascicle:** 2 (Xuanyi)
- **CBETA source file:** T1716_002.txt
- **CBETA line numbers:** 31–79
- **Chinese text (quoted):**
  - 「次判權實者…」
  - 「皆稱法界者，其意有三…」
  - 「通解者，相以據外…」
  - 「次別解者，取氣類相似…初四趣、次人天、次二乘、次菩薩佛也。」
- **Defect type:** Omission (large Ten‑Suchnesses exposition missing)
- **Required correction:**
  - Insert the full CBETA block from “次判權實者…” through “四十一地，皆有十法也。” with line‑by‑line bilingual translation.
- **Post‑edit excerpt (Xuanyi_Fascicle_02_Part_1_Three_Dharmas_SCHOLARLY.md):**
  ```
  次判權實者，光宅以前五如是為權，屬凡夫；次四如是為實，屬聖人；後一如是，總結權實。
  …
  次解十如是法。初、通解，後、別解。
  …
  四十一地，皆有十法也。
  ```
- **Status:** Closed

### DEFECT-X02-006
- **File name:** Xuanyi_Fascicle_02_Part_2_Relative_Absolute_SCHOLARLY.md
- **Fascicle:** 2 (Xuanyi)
- **CBETA source file:** T1716_002.txt
- **CBETA line numbers:** 117
- **Chinese text (quoted):**
  - 「復次，三藏但半字生滅門，不能通滿理，故名為麁…若不即空為通真方便，是故言麁；若能即空是通中方便…」
- **Defect type:** Omission (missing doctrinal paragraph)
- **Required correction:**
  - Insert the full paragraph on half‑word/full‑word, the Madhyamaka citation, and the “empty/provisional” distinctions between the Q/A about *Vaipulya/Prajñā* and the “milk‑to‑ghee” question.
- **Post‑edit excerpt (Xuanyi_Fascicle_02_Part_2_Relative_Absolute_SCHOLARLY.md):**
  ```
  復次，三藏但半字生滅門，不能通滿理，故名為麁…《中論》偈(云云)。
  若不即空為通真方便，是故言麁；若能即空是通中方便…不帶空假直通中者妙(云云)。
  ```
- **Status:** Closed

### DEFECT-X02-007
- **File name:** Xuanyi_Fascicle_02_Part_2_Relative_Absolute_SCHOLARLY.md
- **Fascicle:** 2 (Xuanyi)
- **CBETA source file:** T1716_002.txt
- **CBETA line numbers:** 119–123
- **Chinese text (quoted):**
  - 「問：乳至醍醐，同稱為滿，是譬云何？」
  - 「答：」
- **Defect type:** Omission (missing Q/A prompt)
- **Required correction:**
  - Restore the Q/A lines immediately before the “navigation metaphor” simile.
- **Post‑edit excerpt (Xuanyi_Fascicle_02_Part_2_Relative_Absolute_SCHOLARLY.md):**
  ```
  問：
  乳至醍醐，同稱為滿，是譬云何？
  答：
  ```
- **Status:** Closed

### DEFECT-X02-008
- **File name:** Xuanyi_Fascicle_02_Part_2_Relative_Absolute_SCHOLARLY.md
- **Fascicle:** 2 (Xuanyi)
- **CBETA source file:** T1716_002.txt
- **CBETA line numbers:** 137–149
- **Chinese text (quoted):**
  - 「妙悟之時…用是兩妙，妙上三法…」
  - 「若將上四種絕待約五味經者…」
  - 「問：何意以絕釋妙？答：…」
  - 「今將迹之絕妙…前四絕橫約四教；今三絕竪約圓教(云云)。」
- **Defect type:** Omission (missing doctrinal block + Q/A)
- **Required correction:**
  - Insert the full “妙悟之時…” block, the Five‑Flavor comparison, and the complete Q/A on why “absolute” explains “wonderful.”
- **Post‑edit excerpt (Xuanyi_Fascicle_02_Part_2_Relative_Absolute_SCHOLARLY.md):**
  ```
  妙悟之時…佛法、心法，亦具二妙，稱之為妙。
  若將上四種絕待約五味經者…此經但有一絕…
  問：何意以絕釋妙？答：秖喚妙為絕…故以絕為妙。
  今將迹之絕妙…前四絕橫約四教；今三絕竪約圓教(云云)。
  ```
- **Status:** Closed

### DEFECT-X02-009
- **File name:** Xuanyi_Fascicle_02_Part_2_Relative_Absolute_SCHOLARLY.md
- **Fascicle:** 2 (Xuanyi)
- **CBETA source file:** T1716_002.txt
- **CBETA line numbers:** 151–177
- **Chinese text (quoted):**
  - 「△別釋妙者，為三：若鹿苑三麁，鷲頭一妙…」
  - 「迹中十妙者：一、境妙…十、功德利益妙。」
  - 「釋十妙為五番：一、標章…五、結權實。」
  - 「○二引證者…『終不令一人獨得滅度…』即利益妙也。」
- **Defect type:** Omission (missing Ten‑Subtleties framework + citations)
- **Required correction:**
  - Replace summary/ellipsis blocks with the full CBETA text and line‑by‑line bilingual translation for the Ten‑Subtleties framework, definitions, and citation block.
- **Post‑edit excerpt (Xuanyi_Fascicle_02_Part_2_Relative_Absolute_SCHOLARLY.md):**
  ```
  △別釋妙者，為三：若鹿苑三麁，鷲頭一妙…若開麁顯妙，即用上絕待妙(云云)。
  迹中十妙者：一、境妙…十、功德利益妙。
  釋十妙為五番：一、標章。二、引證。三、生起。四、廣解。五、結權實。
  ○二引證者…「終不令一人獨得滅度…」即利益妙也。
  ```
- **Status:** Closed

---

## XUANYI STATUS (FASCICLE 1)

- **Files audited:** 4 / 4
- **Files PASS:** 4 / 4
- **Files FAIL:** 0 / 4
- **Open defects:** 0
- **Repaired – Pending Re‑Audit:** 0
- **Closed defects:** 18

---

## XUANYI DEFECT ENTRIES

### DEFECT-X01-001
- **File name:** Xuanyi_Fascicle_01_Part_2_Five_Chapters_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 66–68
- **Chinese text (quoted):**
  - 「若三界人見三界為異，二乘人見三界為如，菩薩人見三界亦如亦異，佛見三界非如非異、雙照如異。」
  - 「金剛藏說「佛甚微智」，辭異意同。其辭曰：「空有、不二、不異、不盡。」」
  - 「私謂實相之法，橫破凡夫之四執，竪破三聖之證得。」
- **Defect type:** Omission (missing doctrinal block)
- **Required correction:**
  - Insert the full CBETA block from “若三界人見三界為異…” through “況自行之實而非實耶！” between the Lifespan citation and Chapter 3.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_2_Five_Chapters_SCHOLARLY.md):**
  ```
  若三界人見三界為異，二乘人見三界為如，菩薩人見三界亦如亦異，佛見三界非如非異、雙照如異。

  金剛藏說「佛甚微智」，辭異意同。

  私謂實相之法，橫破凡夫之四執，竪破三聖之證得。
  ```
- **Status:** Closed

### DEFECT-X01-002
- **File name:** Xuanyi_Fascicle_01_Part_2_Five_Chapters_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 74
- **Chinese text (quoted):**
  - 「然諸因果，善須明識，尚不取別教因果，況餘因果！」
  - 「初修此實相之行，名為佛因，道場所得，名為佛果。」
- **Defect type:** Omission (missing “宗” paragraph)
- **Required correction:**
  - Insert the full CBETA paragraph beginning “然諸因果…” before the “論用” section.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_2_Five_Chapters_SCHOLARLY.md):**
  ```
  然諸因果，善須明識，尚不取別教因果，況餘因果！

  初修此實相之行，名為佛因，道場所得，名為佛果。
  ```
- **Status:** Closed

### DEFECT-X01-003
- **File name:** Xuanyi_Fascicle_01_Part_2_Five_Chapters_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 76
- **Chinese text (quoted):**
  - 「如薩婆悉達彎祖王弓滿，名為力；中七鐵鼓，貫一鐵圍山，洞地徹水輪，名為[A1]用。」
  - 「諸方便教，力用微弱，如凡人弓箭。」
- **CBETA apparatus (verbatim):**
  - [A1] 用【CB】，月【大】
- **Defect type:** Omission (missing “用” block + apparatus)
- **Required correction:**
  - Insert the missing “用” paragraph and the [A1] apparatus line in the Function section.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_2_Five_Chapters_SCHOLARLY.md):**
  ```
  如薩婆悉達彎祖王弓滿，名為力；中七鐵鼓，貫一鐵圍山，洞地徹水輪，名為[A1]用。

      [A1] 用【CB】，月【大】
  ```
- **Status:** Closed

### DEFECT-X01-004
- **File name:** Xuanyi_Fascicle_01_Part_2_Five_Chapters_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 80, 108–110
- **Chinese text (quoted):**
  - 「云何分別？如日初出，前照高山，厚殖善根，感斯頓說。」
  - 「次照幽谷，淺行偏明當分漸解，此如三藏。」
  - 「又異者，餘教當機益物，不說如來施化之意。」
- **CBETA apparatus (verbatim):**
  - [A2] 醍醐【CB】，醐醍【大】(cf. T49n2035_p0161c05; X29n0599_p0621b02)
- **Defect type:** Omission (missing “判教” expansions + apparatus)
- **Required correction:**
  - Insert “云何分別？” and the full Five Flavors exposition; append the [A2] apparatus and the two “又異者…” paragraphs before Section 2.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_2_Five_Chapters_SCHOLARLY.md):**
  ```
  云何分別？

  次照幽谷，淺行偏明當分漸解，此如三藏。

      [A2] 醍醐【CB】，醐醍【大】(cf. T49n2035_p0161c05; X29n0599_p0621b02)
  ```
- **Status:** Closed

### DEFECT-X01-005
- **File name:** Xuanyi_Fascicle_01_Part_4_Four_Siddhāntas_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 352
- **Chinese text (quoted):**
  - 「此法內、外、親、疎隔別…必須曉夜精勤、欣悅、無[A3]𣀇，此即世界悉檀起初觀也。」
  - 「若欲觀假入空，須識為人便宜。若宜修觀…若宜修止…」
- **CBETA apparatus (verbatim):**
  - [A3] 𣀇【CB】，[睪*支]【大】
- **Defect type:** Omission (missing “起觀教” details + apparatus)
- **Required correction:**
  - Insert the full “若欲觀假入空…” block and the [A3] apparatus line.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_4_Four_Siddhāntas_SCHOLARLY.md):**
  ```
  若欲觀假入空，須識為人便宜。
  若宜修觀，即用擇、精進、喜三覺分起之。

      [A3] 𣀇【CB】，[睪*支]【大】
  ```
- **Status:** Closed

### DEFECT-X01-006
- **File name:** Xuanyi_Fascicle_01_Part_4_Four_Siddhāntas_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 356
- **Chinese text (quoted):**
  - 「《大經》云：「生生不可說…亦可得說，十因緣法為生作因。」」
  - 「亦可得說十因緣者：從無明至有，此十成於眾生…」
- **Defect type:** Omission (missing “起教” expansion)
- **Required correction:**
  - Restore the full Mahāparinirvāṇa citation and the Ten‑Conditions explanation, plus the middle/upper‑grade clauses.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_4_Four_Siddhāntas_SCHOLARLY.md):**
  ```
  《大經》云：「生生不可說，乃至不生不生不可說」，又云：「亦可得說，十因緣法為生作因。」
  亦可得說十因緣者：從無明至有，此十成於眾生，具四根性，能感如來，說四種法。
  ```
- **Status:** Closed

### DEFECT-X01-007
- **File name:** Xuanyi_Fascicle_01_Part_4_Four_Siddhāntas_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 368
- **Chinese text (quoted):**
  - 「《淨名》杜口，《大集》無言菩薩不可智知，不可識識，言語道斷，心行亦訖，不生不滅，法如涅槃。」
- **Defect type:** Omission (missing “說默” clause)
- **Required correction:**
  - Restore the full “不可智知，不可識識…” clause in the “無言菩薩” line.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_4_Four_Siddhāntas_SCHOLARLY.md):**
  ```
  《淨名》杜口，《大集》無言菩薩不可智知，不可識識，言語道斷，心行亦訖，不生不滅，法如涅槃。
  ```
- **Status:** Closed

### DEFECT-X01-008
- **File name:** Xuanyi_Fascicle_01_Part_4_Four_Siddhāntas_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 384
- **Chinese text (quoted):**
  - 「假令用者，差機不當，故淨名訶滿願云：「不知人根，不應說法，無以穢食，置於寶器。」」
- **Defect type:** Omission (missing “得用不得用” quotation)
- **Required correction:**
  - Restore the full Vimalakīrti quotation in the “假令用者” line.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_4_Four_Siddhāntas_SCHOLARLY.md):**
  ```
  假令用者，差機不當，故淨名訶滿願云：「不知人根，不應說法，無以穢食，置於寶器。」
  ```
- **Status:** Closed

### DEFECT-X01-009
- **File name:** Xuanyi_Fascicle_01_Part_4_Four_Siddhāntas_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 386
- **Chinese text (quoted):**
  - 「若通教四諦明四悉檀，體法即真，其門則巧故。《釋論》云：「今欲說第一義悉檀故，說《摩訶般若波羅蜜經》。」」
- **Defect type:** Omission (missing “權實” clause)
- **Required correction:**
  - Restore the Śāstra citation and the full Common Teaching clause.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_4_Four_Siddhāntas_SCHOLARLY.md):**
  ```
  若通教四諦明四悉檀，體法即真，其門則巧故。《釋論》云：「今欲說第一義悉檀故，說《摩訶般若波羅蜜經》。」
  ```
- **Status:** Closed

### DEFECT-X01-010
- **File name:** Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 118
- **Chinese text (quoted):**
  - 「所以引二文者，古佛事定…若引者，「開、示、悟、入」，即其文也…「此異餘經」，證教也。」
- **Defect type:** Omission (missing rationale paragraph)
- **Required correction:**
  - Insert the full “所以引二文者…” paragraph and the fivefold evidentiary mapping.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md):**
  ```
  所以引二文者，古佛事定…若引者，「開、示、悟、入」，即其文也…
  「為大事因緣故」，證名；「佛之知見」，證體；「開示悟入」，證宗；「為令眾生」，證用；「此異餘經」，證教也。
  ```
- **Status:** Closed

### DEFECT-X01-011
- **File name:** Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 132
- **Chinese text (quoted):**
  - 「引諸譬喻，明教相最大…非但引文證教，餘義亦成。」
- **Defect type:** Omission (missing simile synthesis)
- **Required correction:**
  - Insert the full “引諸譬喻…” synthesis paragraph after the six similes.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md):**
  ```
  引諸譬喻，明教相最大…教相王中王，餘亦如是。
  非但引文證教，餘義亦成。
  ```
- **Status:** Closed

### DEFECT-X01-012
- **File name:** Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 136–140
- **Chinese text (quoted):**
  - 「〈神力品〉中，約教次第…故言甚深之事也。」
  - 「〈序品〉約行次第…分別同異，教相也。」
- **Defect type:** Omission (missing Section 3 expansions)
- **Required correction:**
  - Restore both paragraphs (神力品 + 序品) within the “生起” section.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md):**
  ```
  〈神力品〉中，約教次第…故言甚深之事也。
  〈序品〉約行次第…分別同異，教相也。
  ```
- **Status:** Closed

### DEFECT-X01-013
- **File name:** Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 144–146
- **Chinese text (quoted):**
  - 「釋名通論自行、化他…教相分別自、他。」
  - 「釋名通論說默…教相分別(云云)。」
  - 「十種者…三軌…三道…三德(云云)。」
- **Defect type:** Omission (missing Open/Combine sub‑sections)
- **Required correction:**
  - Insert the self/other, speech/silence, and ten‑kinds paragraphs under “開合”.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md):**
  ```
  釋名通論自行、化他…教相分別自、他。
  釋名通論說默…教相分別(云云)。
  十種者…三軌…三道…三德(云云)。
  ```
- **Status:** Closed

### DEFECT-X01-014
- **File name:** Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 166–238
- **Chinese text (quoted):**
  - 「文內從火宅至醫子，凡七譬…」
  - 「一切法皆佛法…」
  - 「何故雙用因果為宗…」
  - 「宗、用俱明智斷…」
  - 「經經各有異意…」
- **Defect type:** Omission (missing Q/A block)
- **Required correction:**
  - Insert all missing Q/A exchanges in the 料簡 section between the flower‑hut question and the “五章” question, and append the final “經經各有異意” Q/A.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md):**
  ```
  問：文內從火宅至醫子…何以取此為題？答：七譬是別…
  問：一切法皆佛法…答：若開權顯實…
  問：何故雙用因果為宗？答：由因致果…
  問：宗、用俱明智斷…答：自行以智德為宗…
  問：經經各有異意…答：若經經別釋…
  ```
- **Status:** Closed

### DEFECT-X01-015
- **File name:** Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 240–262
- **Chinese text (quoted):**
  - 「○六明觀心者，從標章至料簡，悉明觀心。」
  - 「觀心引證者…」
  - 「觀心生起者…」
  - 「觀心開合者…」
  - 「觀心料簡者…」
  - 「若欲免貧窮…六即…」
  - 「妙法蓮華經玄義卷第一上 / 第一下」
- **Defect type:** Omission (missing Observing‑Mind blocks + fascicle boundaries)
- **Required correction:**
  - Restore the complete Observing‑Mind sub‑sections (引證/生起/開合/料簡), the Six‑Identity list, and the fascicle boundary lines.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md):**
  ```
  ○六明觀心者，從標章至料簡，悉明觀心。
  觀心引證者…觀心生起者…觀心開合者…觀心料簡者…
  若欲免貧窮，當勤三觀；欲免上慢，當聞六即。
  …唯佛與佛究盡實相，究竟即也。
  妙法蓮華經玄義卷第一上
  妙法蓮華經玄義卷第一下
  ```
- **Status:** Closed

### DEFECT-X01-016
- **File name:** Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 268–350
- **Chinese text (quoted):**
  - 「七、會異者。」
  - 「問：何不次第？…」
  - 「《論》專釋《大品》…」
  - 「次解四悉檀為十重…」
  - 「釋名者…」
  - 「私十五番釋其相令易解…」
  - 「三、釋成者…四、對諦者…」
- **Defect type:** Omission (missing Four‑Siddhāntas exposition)
- **Required correction:**
  - Restore the full “會異” section including order Q/A, ten‑layer list, name‑definition paragraph, fifteen‑fold analysis, and the “釋成 / 對諦” blocks.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md):**
  ```
  七、會異者。
  問：何不次第？…答：悉檀是佛智慧…
  次解四悉檀為十重：一、釋名…十、通經
  釋名者，悉檀，天竺語…
  私十五番釋其相令易解…
  三、釋成者…四、對諦者…
  ```
- **Status:** Closed

### DEFECT-X01-017
- **File name:** Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 112, 134, 142, 150
- **Chinese text (quoted):**
  - 「○二、引證者，如文殊答問偈云「我見燈明佛，本光瑞如此，以是知今佛，欲說《法華經》」。」
  - 「○三、生起者，能生為生，所生為起。前後有次第，麁細不相違。」
  - 「○四、開合者，五章共釋一經，種種分別，令易解故。凡三種開合，謂五種、十種、譬喻。」
  - 「○五料簡者，」
- **Defect type:** Omission (missing section header lines)
- **Required correction:**
  - Restore the missing section header phrases at the starts of Sections 2–5.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md):**
  ```
  ○二、引證者，如文殊答問偈云「我見燈明佛，本光瑞如此，以是知今佛，欲說《法華經》」。

  ○三、生起者，能生為生，所生為起。前後有次第，麁細不相違。

  ○四、開合者，五章共釋一經，種種分別，令易解故。凡三種開合，謂五種、十種、譬喻。

  ○五料簡者，
  ```
- **Status:** Closed

### DEFECT-X01-018
- **File name:** Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md
- **Fascicle:** 1 (Xuanyi)
- **CBETA source file:** T1716_001.txt
- **CBETA line numbers:** 150–152; 240–242; 268–270; 350 (end of fascicle)
- **Chinese text (quoted):**
  - N/A (non‑CBETA additions in English only)
- **Translation excerpt (non‑CBETA additions removed):**
  - “This section presents a series of questions and answers addressing potential objections.”
  - “This is the practical core of the Seven Interpretations—transforming doctrine into meditation.”
  - “This section harmonizes the Five‑Chapter system with the Four Siddhāntas.”
  - “*Fascicle 1 Upper translation complete. Fascicle 1 Lower continues with the detailed Four Siddhāntas exposition...*”
- **Defect type:** Addition (non‑CBETA editorial lines)
- **Required correction:**
  - Remove all non‑CBETA editorial sentences inserted between CBETA blocks or appended after the fascicle.
- **Post‑edit excerpt (Xuanyi_Fascicle_01_Part_3_Seven_Interpretations_SCHOLARLY.md):**
  ```
  ○五料簡者，

  > Fifth, critical discrimination.

  ### Q1: Doesn't "flower for the lotus" imply cause contains effect?
  ```
  ```
  ○六明觀心者，從標章至料簡，悉明觀心。

  > Section Six clarifies observing the mind: from the establishing of headings through critical discrimination, all of it clarifies observing the mind.
  ```
  ```
  七、會異者。

  > Seven: reconciling differences.

  ### The Four Siddhāntas and the Five Chapters
  ```
  ```
  四、對諦者，直對一番四諦，如前說。廣對四種四諦者，四種四諦，一一以四悉檀對之。復總對者，生滅四諦對世界，無生四諦對為人，無量四諦對對治，無作四諦對第一義。

  > Four, corresponding to the truths: directly correspond to one set of Four Truths, as previously explained. Broadly corresponding to the four kinds of Four Truths: each kind of Four Truths is matched with the Four Siddhāntas. In overall correspondence: the Four Truths of arising‑and‑ceasing correspond to Worldly; the Four Truths of non‑arising correspond to For‑Each‑Person; the immeasurable Four Truths correspond to Therapeutic; the Four Truths of non‑fabrication correspond to First Principle.
  ```
- **Status:** Closed

### DEFECT-F01-002
- **File name:** Wenju_Fascicle_01_FULL_Scholarly.md
- **Fascicle:** 1
- **CBETA source file:** T1718_001.txt
- **CBETA line numbers:** 541–560
- **Chinese text (quoted):**
  - [4] 好【大】，名好【甲】
  - [5] 若【大】，答【甲】
  - [6] 見人【大】，人見【甲】
  - [7] 得歸【大】，可歸【甲】
  - [8] 屠【大】，屠者【甲】
  - [1] 男即【大】，即男【甲】
- **Translation excerpt:**
  - No apparatus lines for the above variants appear in the translation around **[541]–[559]**.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert all missing apparatus lines exactly where the CBETA variants occur, in the scholarly apparatus format used elsewhere in the file.
- **Status:** Closed

### DEFECT-F01-003
- **File name:** Wenju_Fascicle_01_FULL_Scholarly.md
- **Fascicle:** 1
- **CBETA source file:** T1718_001.txt
- **CBETA line numbers:** 561–600
- **Chinese text (quoted):**
  - 「姓者，劫初大水風吹結構以成世界…」
  - 「《十二遊經》云…」
  - 「仁賢劫初…」
  - 「《賢愚經》云…」
  - 「阿那律精進…」
  - 「約教者…」
  - 「劫賓那…」
  - 「約教者…約本迹者…觀心者…」
- **Translation excerpt:**
  - The “Protocol Map: Fascicle 1 (Lines 561–600)” block is a non‑CBETA insertion.
- **Defect type:** Addition (non‑CBETA)
- **Required correction:**
  - Remove the entire “Protocol Map: Fascicle 1 (Lines 561–600)” block.
- **Status:** Closed

### DEFECT-F01-004
- **File name:** Wenju_Fascicle_01_FULL_Scholarly.md
- **Fascicle:** 1
- **CBETA source file:** T1718_001.txt
- **CBETA line numbers:** 561–600
- **Chinese text (quoted):**
  - 「姓者，劫初大水風吹結構以成世界…」 through 「…觀五陰舍即中，與法佛同宿(云云)。[5]」
- **Translation excerpt:**
  - Summary bullets and short paraphrases for **[561]–[591]** replace the full CBETA narrative.
- **Defect type:** Omission (summary/paraphrase)
- **Required correction:**
  - Replace all summaries from **[561]** through **[591]** with full CBETA text and line‑by‑line bilingual translation.
  - Preserve all causal sequences, genealogy details, and quoted sūtra passages.
- **Status:** Closed

### DEFECT-F01-005
- **File name:** Wenju_Fascicle_01_FULL_Scholarly.md
- **Fascicle:** 1
- **CBETA source file:** T1718_001.txt
- **CBETA line numbers:** 561–600
- **Chinese text (quoted):**
  - [2] 一十【大】，十一【甲】
  - [3] 名【大】，言【甲】
  - [4] 名【大】，〔－〕【甲】
  - [5] 末法時世【大】，末世時【甲】
  - [6] 見【大】，見人【甲】
  - [7] 債【大】，責【甲】
  - [1] 音秀【大】，〔－〕【甲】
  - [2] 星【大】，宿【甲】
  - [3] 在【大】，即在【甲】
  - [4] 音夙【大】，〔－〕【甲】
  - [5] 不分卷【甲】
- **Translation excerpt:**
  - No apparatus lines for the above variants appear in the translation around **[561]–[591]**.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert all missing apparatus lines exactly where the CBETA variants occur, using the same scholarly apparatus format.
- **Status:** Closed


### DEFECT-F01-006
- **File name:** Wenju_Fascicle_01_FULL_Scholarly.md
- **Fascicle:** 1
- **CBETA source file:** T1718_001.txt
- **CBETA line numbers:** 289
- **Chinese text (quoted):**
  - 《釋論》云：「怖魔、破惡、乞士，魔樂生死，其既出家復化餘人，俱離三界乖於魔意，魔用力制翻被五繫，但愁懼而已，故名怖魔。出家人必破身、口[8]七惡，故言破惡。夫在家三種如法，一田、二商、三仕，用養身命；出家人佛不許此，唯乞自濟，身安道存，福利檀越，三義相成即比丘義也。」
- **Translation excerpt:**
  - “Mara delights in Birth and Death… acting contrary to Mara’s intent… (ellipsis)”
- **Defect type:** Paraphrase / Ellipsis
- **Required correction:**
  - Replace the ellipsis‑based English bullet with a full literal translation of the entire quoted passage.
- **Status:** Closed

### DEFECT-F01-007
- **File name:** Wenju_Fascicle_01_FULL_Scholarly.md
- **Fascicle:** 1
- **CBETA source file:** T1718_001.txt
- **CBETA line numbers:** 355
- **Chinese text (quoted):**
  - 「…若能知色非淨乃至識非常，又能知色無常、苦、空、不淨，乃至識無常、苦、無我、不淨者，是為不生，非是生。」
- **Translation excerpt:**
  - “If one can know Form is not Pure… up to Consciousness is not Permanent; and also know Form is Impermanent, Suffering, Empty, Impure… up to Consciousness is Impermanent, Suffering, Non‑Self, Impure—This is No‑Birth, not Birth.”
- **Defect type:** Paraphrase / Ellipsis
- **Required correction:**
  - Expand the ellipses and translate all five skandhas explicitly (Form, Feeling, Conception, Volition, Consciousness) in both clauses.
- **Status:** Closed

### DEFECT-F01-008
- **File name:** Wenju_Fascicle_01_FULL_Scholarly.md
- **Fascicle:** 1
- **CBETA source file:** T1718_001.txt
- **CBETA line numbers:** 367
- **Chinese text (quoted):**
  - 「耳、鼻、舌、身、意亦如是，是眼界乃至法界亦如是。」
- **Translation excerpt:**
  - “Ear… up to Mind; Eye Realm… up to Dharma Realm are also thus.”
- **Defect type:** Paraphrase / Ellipsis
- **Required correction:**
  - Replace ellipses with full explicit enumeration of ear, nose, tongue, body, mind; and eye‑realm through dharma‑realm.
- **Status:** Closed

### DEFECT-F02-001
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** 6–11
- **CBETA locator:** T1718_002.txt [6]–[11], [＊7-1], [＊7-2], [＊10-1]
- **CBETA apparatus (verbatim):**
  - [6] 不分卷【甲】
  - [7] 笑【大】＊，咲【甲】＊
  - [＊7-1] 笑【大】＊，咲【甲】＊
  - [＊7-2] 笑【大】＊，咲【甲】＊
  - [8] 羅【大】，阿羅【甲】
  - [9] 追【大】，召【甲】
  - [10] 和尚【大】＊，和上【甲】＊
  - [11] 偈【大】，偈言【甲】
  - [＊10-1] 和尚【大】＊，和上【甲】＊
- **Translation excerpt:**
  - No apparatus lines present after the Gavāmpati section.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering all variants above at the end of the Gavāmpati block.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  **Four streams [from his body] flowed to the place of Mahākāśyapa, and the water spoke a verse: "Since the great elephant has departed, the young elephant follows. Since the World Honored One and the Preceptor have entered extinction, why should I remain here now?" This is also the *Ultimate Siddhānta*.**
  *[Critical apparatus: 不分卷【甲】; 笑【大】＊，咲【甲】＊; [＊7-1] 笑【大】＊，咲【甲】＊; [＊7-2] 笑【大】＊，咲【甲】＊; 羅【大】，阿羅【甲】; 追【大】，召【甲】; 和尚【大】＊，和上【甲】＊; 偈【大】，偈言【甲】; [＊10-1] 和尚【大】＊，和上【甲】＊]*
  ```
- **Status:** Closed

### DEFECT-F02-002
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** 12–13, [A1]
- **CBETA locator:** T1718_002.txt [12], [A1], [13]
- **CBETA apparatus (verbatim):**
  - [12] 辰【大】，神【甲】
  - [A1] 己【CB】，已【大】
  - [13] 道【大】，道也【甲】
- **Translation excerpt:**
  - No apparatus line appears after the Revata section.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering [12], [A1], and [13] immediately after the Revata block.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  **The multitude of monks said: "This person is easily liberated." They told him: "Your body was originally the remnants of another; it is not your own possession." He immediately attained the Way. The *Ekottara Āgama* says: "Among those who sit in meditation (*dhyāna*) entering samādhi with a mind not inverted or scattered, the Bhikṣu Revata is foremost."**
  *[Critical apparatus: [12] 辰【大】，神【甲】; [A1] 己【CB】，已【大】; [13] 道【大】，道也【甲】]*
  ```
- **Status:** Closed

### DEFECT-F02-003
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [＊7-3]
- **CBETA locator:** T1718_002.txt [＊7-3]
- **CBETA apparatus (verbatim):**
  - [＊7-3] 笑【大】＊，咲【甲】＊
- **Translation excerpt:**
  - No apparatus line appears after the Pilindavatsa “assembly laughed” paragraph.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering [＊7-3] after the Pilindavatsa block.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  **The River Goddess parted the stream for him. The spirit went to complain to the Buddha. The Buddha ordered him to apologize. He immediately joined his palms: "Little Maid, do not be angry." The great assembly laughed at him—apologizing yet scolding again! The Buddha said: "His original habit is like this; effectively he has no arrogant mind." The *Ekottara Āgama* says: "Among those who sit in bitter practice under trees, avoiding neither wind nor rain, the Bhikṣu Vatsa is foremost."**
  *[Critical apparatus: [＊7-3] 笑【大】＊，咲【甲】＊]*
  ```
- **Status:** Closed

### DEFECT-F02-004
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** 1–4
- **CBETA locator:** T1718_002.txt [1]–[4]
- **CBETA apparatus (verbatim):**
  - [1] 槃【大】，盤【甲】
  - [2] 火水【大】，水火【甲】
  - [3] 也【大】，〔－〕【甲】
  - [4] 薄【大】，婆【甲】
- **Translation excerpt:**
  - No apparatus line appears after the Vakkula section.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering [1]–[4] after the Vakkula block.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  **King Aśoka paid homage to the stupas of the Arhats. When he came next to [Vakkula's] stupa, he spoke a verse: "Although he trained himself in [removing] ignorance, he was of little benefit to the world." He offered twenty cowrie shells. The *Ekottara Āgama* says: "He offered one coin [cowrie], and the cowrie flew out from the stupa and attached itself to the King's foot. The ministers were astonished—even his stupa had such power of leisure, stillness, and few desires." The *Ekottara* says: "Among those of extremely long life never cut short, constantly delighting in leisure dwelling and not abiding in crowds, Vakkula is foremost."**
  *[Critical apparatus: [1] 槃【大】，盤【甲】; [2] 火水【大】，水火【甲】; [3] 也【大】，〔－〕【甲】; [4] 薄【大】，婆【甲】]*
  ```
- **Status:** Closed

### DEFECT-F02-005
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [5a]
- **CBETA locator:** T1718_002.txt [5a]
- **CBETA apparatus (verbatim):**
  - [5a] （而真…寂靜）二十字【大】，而入真通寂靜離二邊而入中圓寂靜【甲】
- **Translation excerpt:**
  - No apparatus line appears after the Vakkula “According to the Teachings” block.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering [5a] after the Vakkula teachings block.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  *   **Perfect:** The extremes *are* the Middle (*jí biān ér zhōng*)—Perfect Stillness.
  *[Critical apparatus: [5a] （而真…寂靜）二十字【大】，而入真通寂靜離二邊而入中圓寂靜【甲】]*
  ```
- **Status:** Closed

### DEFECT-F02-006
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [5b]
- **CBETA locator:** T1718_002.txt [5b]
- **CBETA apparatus (verbatim):**
  - [5b] （本者…定）八字【大】，本迹者本住大寂定【甲】
- **Translation excerpt:**
  - No apparatus line appears after the Vakkula Fundamental paragraph.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering [5b] after the Vakkula Fundamental block.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  **According to *Fundamental*: He abides in the Great Quiescent Samādhi (Mahāparinirvāṇa). Long life is **Permanence**; no sickness is **Bliss**; no premature death is **Self**; stillness is **Purity**. Dwelling in the root of these Four Virtues, his trace demonstrates the stillness of the six sense faculties.**
  *[Critical apparatus: [5b] （本者…定）八字【大】，本迹者本住大寂定【甲】]*
  ```
- **Status:** Closed

### DEFECT-F02-007
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [＊7-4], [6]
- **CBETA locator:** T1718_002.txt [＊7-4], [6]
- **CBETA apparatus (verbatim):**
  - [＊7-4] 笑【大】＊，咲【甲】＊
  - [6] 留【大】，婁【甲】
- **Translation excerpt:**
  - No apparatus line appears after the Mahākauṣṭhila narrative paragraph.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering [＊7-4] and [6] after the Mahākauṣṭhila narrative.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  **The Buddha asked: "Do you 'accept' this accepting [or not accepting]?" Here he fell into a double defeat: if I say, "I accept [this]," earlier I already said, "I do not accept all [dharmas]." If I say, "I do not accept [this]," then I have no way to defeat the Buddha. He immediately lowered his head and attained the Purity of the Dharma Eye. Śāriputra, who was fanning the Buddha and heard his uncle's debate, attained the fruit of Arhatship. The *Ekottara Āgama* says: "Among those who attain the Four Eloquences and, when confronted with difficulties, are able to answer, Kauṣṭhila is foremost." The Southern Heavenly King Virūpākṣa constantly came to attend him.**
  *[Critical apparatus: [＊7-4] 笑【大】＊，咲【甲】＊; [6] 留【大】，婁【甲】]*
  ```
- **Status:** Closed

### DEFECT-F02-008
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [7], [8]
- **CBETA locator:** T1718_002.txt [7], [8]
- **CBETA apparatus (verbatim):**
  - [7] 本【大】＊，本迹【甲】＊
  - [8] 示【大】，〔－〕【甲】
- **Translation excerpt:**
  - No apparatus line appears after the Mahākauṣṭhila Fundamental paragraph.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering [7] and [8] after the Mahākauṣṭhila Fundamental block.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  **According to *Fundamental*: He abides in the Secret of the Mouth, the inconceivable transformation of the Voice Wheel, Great Concentration and Great Wisdom. His trace manifests as "Big Knee."**
  *[Critical apparatus: [7] 本【大】＊，本迹【甲】＊; [8] 示【大】，〔－〕【甲】]*
  ```
- **Status:** Closed

### DEFECT-F02-009
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [9], [10]
- **CBETA locator:** T1718_002.txt [9], [10]
- **CBETA apparatus (verbatim):**
  - [9] 偪【大】＊，逼【甲】＊
  - [10] 陀【大】，陀也【甲】
- **Translation excerpt:**
  - No apparatus line appears after the Nanda opening paragraph.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering [9] and [10] immediately after the Nanda opening paragraph.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  **"Nanda" (難陀 *Nántuó*): Also called "Cowherding Nanda." Translated as "Good Joy" (*Shàn Huānxǐ*) or "Delight" (*Xīnlè*). King Śuddhodana forced ten thousand Śākyas to leave home [to become monks]; he was one of them. Some masters say: "This is the Upananda (*Bá-nántuó*) mentioned in the Vinaya."**
  *[Critical apparatus: [9] 偪【大】＊，逼【甲】＊; [10] 陀【大】，陀也【甲】]*
  ```
- **Status:** Closed

### DEFECT-F02-010
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [＊7-1]
- **CBETA locator:** T1718_002.txt [＊7-1]
- **CBETA apparatus (verbatim):**
  - [＊7-1] 本【大】＊，本迹【甲】＊
- **Translation excerpt:**
  - No apparatus line appears after the Nanda Fundamental paragraph.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering [＊7-1] after the Nanda Fundamental block.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  **According to *Fundamental*: He abides in the **Reality Limit** (*shíjì*), neither joy nor non-joy; his trace is named "Joy."**
  *[Critical apparatus: [＊7-1] 本【大】＊，本迹【甲】＊]*
  ```
- **Status:** Closed

### DEFECT-F02-011
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [11], [＊9-1], [12]
- **CBETA locator:** T1718_002.txt [11], [＊9-1], [12]
- **CBETA apparatus (verbatim):**
  - [11] 拳【大】，惓【甲】
  - [＊9-1] 偪【大】＊，逼【甲】＊
  - [12] 走【大】，〔－〕【甲】
- **Translation excerpt:**
  - No apparatus line appears after the Sundarananda narrative block.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering [11], [＊9-1], and [12] after the Sundarananda narrative.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  **The Buddha then returned to the Nyagrodha Garden and said to Ānanda: "Have Nanda bring the meal." Ānanda proclaimed the Buddha's instruction and had him deliver the food as an offering to the Buddha. The Buddha then ordered his head to be shaved. [Nanda] clenched his fist and said to the barber: "Do not bring a knife near the crown of the King of Jambudvīpa!" The Buddha pressed him and he could not stop it; thus his head was shaved.**
  *[Critical apparatus: [11] 拳【大】，惓【甲】; [＊9-1] 偪【大】＊，逼【甲】＊; [12] 走【大】，〔－〕【甲】]*
  ```
- **Status:** Closed

### DEFECT-F02-012
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [13]
- **CBETA locator:** T1718_002.txt [13]
- **CBETA apparatus (verbatim):**
  - [13] 云云【大】＊，〔－〕【甲】＊
- **Translation excerpt:**
  - No apparatus line appears after “本迹觀心如前(云云)。”
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering [13] immediately after the “本迹觀心如前(云云)” line.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  **As for *Fundamental/Trace* and *Contemplating the Mind*: they are as above (and so on).**
  *[Critical apparatus: [13] 云云【大】＊，〔－〕【甲】＊]*
  ```
- **Status:** Closed

### DEFECT-F02-013
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [14], [15]
- **CBETA locator:** T1718_002.txt [14], [15]
- **CBETA apparatus (verbatim):**
  - [14] 諸【大】，請【甲】
  - [15] 此從【大】，從此【甲】
- **Translation excerpt:**
  - No apparatus line appears after the Pūrṇa naming paragraph.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering [14] and [15] after the Pūrṇa naming paragraph.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  **This name is obtained from the two conditions of father and mother, therefore he is called "Full-Compassion Son." He was good at knowing: among internal and external scriptures and books there was nothing he did not know. Because his knowledge was "full," he was again named "Full."**
  *[Critical apparatus: [14] 諸【大】，請【甲】; [15] 此從【大】，從此【甲】]*
  ```
- **Status:** Closed

### DEFECT-F02-014
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [1]
- **CBETA locator:** T1718_002.txt [1]
- **CBETA apparatus (verbatim):**
  - [1] 也【大】，〔－〕【甲】
- **Translation excerpt:**
  - No apparatus line appears after the Pūrṇa Fundamental/Trace paragraph.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering [1] after the Pūrṇa Fundamental/Trace block.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ```
  **According to *Fundamental/Trace*: His fundamental wish was fulfilled long ago; his trace is "Foremost in Preaching Dharma," demonstrating a Good Friend (*kalyāṇamitra*) to sentient beings.**
  *[Critical apparatus: [1] 也【大】，〔－〕【甲】]*
  ```
- **Status:** Closed


---

## FILE STATUS

- **Fascicle 1:** PASS
- **Fascicle 2:** PASS
- **Fascicle 3 Part 1:** PASS
- **Fascicle 3 Part 2:** PASS
- **Fascicle 3:** PASS (Boundary PASS)
- **Fascicle 4 Part 1:** PASS
- **Fascicle 4 Part 2:** PASS
- **Fascicle 4:** PASS (Boundary PASS)
- **Fascicle 5:** PASS
- **Fascicle 6 Part 1:** PASS
- **Fascicle 6 Part 2:** PASS
- **Fascicle 6:** PASS (Boundary PASS)
- **Fascicle 7 Part 1:** PASS
- **Fascicle 7 Part 2:** PASS
- **Fascicle 7:** PASS (Boundary PASS)
- **Fascicle 8 Part 1:** PASS
- **Fascicle 8 Part 2:** PASS
- **Fascicle 8:** PASS (Boundary PASS)
- **Fascicle 9:** PASS

---

## FASCICLE 3 BOUNDARY (Preflight Mapping)

- **Part1 ends at CBETA:** T1718_003.txt [5] 「權、一是實；次空有二智，觀空不證離二乘，涉有無染出凡夫；次空有內靜為實，外用為權；次金剛前後常、無常為權實…」
- **Part2 begins at CBETA:** T1718_003.txt [2] 「一切法非權非實者，文云：「非如非異」又云：「亦復不行上中下法，有為無為、實不實法，非虛非實如實相也。」…」
- **Boundary Integrity Test:** **F03_BOUNDARY_CONTINUITY**  
  - **Fail condition:** any missing/duplicate CBETA line at the seam between the entries above  
  - **Result (preflight):** **PASS** (no gap, no overlap; contiguous order index 48→49 in CBETA parsing)


## FASCICLE 4 BOUNDARY (Preflight Mapping)

- **Part1 ends at CBETA:** T1718_004.txt [229] 「妙法蓮華經文句卷第四上」
- **Part2 begins at CBETA:** T1718_004.txt [231] 「妙法蓮華經文句卷第四下」
- **Boundary Integrity Test:** **F04_BOUNDARY_CONTINUITY**  
  - **Fail condition:** any missing/duplicate CBETA line at the seam between the entries above  
  - **Result (preflight):** **PASS** (no gap, no overlap; contiguous order index 229→231 in CBETA parsing)


## FASCICLE 5 BOUNDARY (Preflight Mapping)

- **Full file begins at CBETA:** T1718_005.txt 「妙法蓮華經文句卷第五上」
- **Full file ends at CBETA:** T1718_005.txt 「妙法蓮華經文句卷第五下」
- **Boundary Integrity Test:** **F05_BOUNDARY_CONTINUITY**  
  - **Fail condition:** missing/duplicate CBETA anchor at file start or end  
- **Result (preflight):** **PASS** (start/end anchors present; full fascicle coverage)

## FASCICLE 6 BOUNDARY (Preflight Mapping)

- **Part1 ends at CBETA:** T1718_006.txt 「妙法蓮華經文句卷第六上」
- **Part2 begins at CBETA:** T1718_006.txt 「妙法蓮華經文句卷第六下」
- **Boundary Integrity Test:** **F06_BOUNDARY_CONTINUITY**  
  - **Fail condition:** any missing/duplicate CBETA line at the seam between the entries above  
  - **Result (preflight):** **PASS** (no gap, no overlap; contiguous upper→lower roll transition)



## FASCICLE 7 BOUNDARY (Preflight Mapping)

- **Part1 ends at CBETA:** T1718_007.txt 「妙法蓮華經文句卷第七上」
- **Part2 begins at CBETA:** T1718_007.txt 「妙法蓮華經文句卷第七下」
- **Boundary Integrity Test:** **F07_BOUNDARY_CONTINUITY**  
  - **Fail condition:** any missing/duplicate CBETA line at the seam between the entries above  
  - **Result (preflight):** **PASS** (no gap, no overlap; contiguous upper→lower roll transition)



## FASCICLE 8 BOUNDARY (Preflight Mapping)

- **Part1 ends at CBETA:** T1718_008.txt 「妙法蓮華經文句卷第八上」
- **Part2 begins at CBETA:** T1718_008.txt 「妙法蓮華經文句卷第八下」
- **Boundary Integrity Test:** **F08_BOUNDARY_CONTINUITY**  
  - **Fail condition:** any missing/duplicate CBETA line at the seam between the entries above  
  - **Result (preflight):** **PASS** (no gap, no overlap; contiguous upper→lower roll transition)



## FASCICLE 9 BOUNDARY (Preflight Mapping)

- **Full file begins at CBETA:** T1718_009.txt 「妙法蓮華經文句卷第九上」
- **Full file ends at CBETA:** T1718_009.txt 「妙法蓮華經文句卷第九下」
- **Boundary Integrity Test:** **F09_BOUNDARY_CONTINUITY**  
  - **Fail condition:** missing/duplicate CBETA anchor at file start or end  
  - **Result (preflight):** **PASS** (start/end anchors present; full fascicle coverage)


### DEFECT-F02-015
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [9], [10]
- **CBETA locator:** T1718_002.txt [9], [10]
- **CBETA apparatus (verbatim):**
  - [9] 偪【大】＊，逼【甲】＊
  - [10] 陀【大】，陀也【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**According to the *Teachings*:**
*[Critical apparatus: [9] 偪【大】＊，逼【甲】＊; [10] 陀【大】，陀也【甲】]*
``
- **Status:** Closed


### DEFECT-F02-016
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [＊7-2], [6], [7]
- **CBETA locator:** T1718_002.txt [＊7-2], [6], [7]
- **CBETA apparatus (verbatim):**
  - [＊7-2] 本【大】＊，本迹【甲】＊
  - [6] 法【大】，法相【甲】
  - [7] 見【大】，現【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**According to *Fundamental*: He abides in the Reality Mark Dharma Body; his trace demonstrates "Being Born from Seeing Emptiness."**
*[Critical apparatus: [＊7-2] 本【大】＊，本迹【甲】＊; [6] 法【大】，法相【甲】; [7] 見【大】，現【甲】]*
``
- **Status:** Closed


### DEFECT-F02-017
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [8]
- **CBETA locator:** T1718_002.txt [8]
- **CBETA apparatus (verbatim):**
  - [8] 不【大】，心不【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**As for *Contemplating the Mind*: it is not within, not without, and not in-between; it is not self-possessed. This is called the *Contemplating-the-Mind* Dharma-body.**
*[Critical apparatus: [8] 不【大】，心不【甲】]*
``
- **Status:** Closed


### DEFECT-F02-018
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [＊13-1]
- **CBETA locator:** T1718_002.txt [＊13-1]
- **CBETA apparatus (verbatim):**
  - [＊13-1] 云云【大】＊，〔－〕【甲】＊
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Contemplating-the-mind is as in the preceding cases and can be understood (and so on).**
*[Critical apparatus: [＊13-1] 云云【大】＊，〔－〕【甲】＊]*
``
- **Status:** Closed


### DEFECT-F02-019
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [4]
- **CBETA locator:** T1718_002.txt [4]
- **CBETA apparatus (verbatim):**
  - [4] 秖【大】＊，只【甲】＊
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Sixth, "Conclusion": "Such assemblies are what the multitude knows as [good] friends." Some say "knowing" (*zhī*) is simply "recognition" (*shí*). Some say: hearing the name is "knowing" and seeing the form is "recognition"; seeing the form is "knowing" and seeing the mind is "recognition."**
*[Critical apparatus: [4] 秖【大】＊，只【甲】＊]*
``
- **Status:** Closed


### DEFECT-F02-020
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [＊7-3]
- **CBETA locator:** T1718_002.txt [＊7-3]
- **CBETA apparatus (verbatim):**
  - [＊7-3] 本【大】＊，本迹【甲】＊
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**According to *Fundamental/Trace*: fundamentally [they] act for sentient beings as a "full-word" good friend; in trace [they] act as a "half-word" good friend (and so on).**
*[Critical apparatus: [＊7-3] 本【大】＊，本迹【甲】＊]*
``
- **Status:** Closed


### DEFECT-F02-021
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [5]
- **CBETA locator:** T1718_002.txt [5]
- **CBETA apparatus (verbatim):**
  - [5] 觀【大】，觀心【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**As for the "contemplation-and-practice" [meaning of] good friends: it is as in the *Mohe Zhiguan*.**
*[Critical apparatus: [5] 觀【大】，觀心【甲】]*
``
- **Status:** Closed


### DEFECT-F02-022
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [6]
- **CBETA locator:** T1718_002.txt [6]
- **CBETA apparatus (verbatim):**
  - [6] 為【大】，名【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**As for "Learner/No-Learner": in the Tripiṭaka there are eighteen kinds of Learners and nine kinds of No-Learners. In the Shared Teaching, the Five Grounds are all called Learner and the Sixth Ground is called No-Learner; also, in the Shared Teaching the Ninth Ground is called Learner and the Buddha-ground is No-Learner. In the Distinct and Perfect [Teachings], one may clarify Learner/No-Learner either in terms of "with effort" and "without effort," or in terms of "complete" and "not yet complete."**
*[Critical apparatus: [6] 為【大】，名【甲】]*
``
- **Status:** Closed


### DEFECT-F02-023
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [7]
- **CBETA locator:** T1718_002.txt [7]
- **CBETA apparatus (verbatim):**
  - [7] 迹【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Fundamentally, [she] abides in the Dharma-gate of wisdom-transcendence; in trace, [she is] the mother of a thousand Buddhas, a teacher who gives birth and nurtures.**
*[Critical apparatus: [7] 迹【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-024
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [8]
- **CBETA locator:** T1718_002.txt [8]
- **CBETA apparatus (verbatim):**
  - [8] 寶【大】，昔寶【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**According to *Fundamental/Trace*: as wives, they are equal - how could one of vast ground [a great bodhisattva] be the Crown Prince's wife? Therefore we know that fundamentally she abides in quiescent samādhi and subtle Dharma-joy; in trace she is the Buddha's wife. The *Sūtra of the Sorrowful Flower* says: "In the presence of the Buddha Ratnagarbha (Treasure-Store), [she] vowed only to be a wife."**
*[Critical apparatus: [8] 寶【大】，昔寶【甲】]*
``
- **Status:** Closed


### DEFECT-F02-025
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [9], [1], [2]
- **CBETA locator:** T1718_002.txt [9], [1], [2]
- **CBETA apparatus (verbatim):**
  - [9] 革【大】＊，隔【甲】＊
  - [1] 以【大】，之【甲】
  - [2] 佛【大】，道【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Above, we should have clearly distinguished the Fundamental/Trace and Contemplating-the-Mind. Now we further present a general discussion, manifesting the subtle ingenuity of good provisional expedients and clarifying the subtlety of contemplative practice.**
*[Critical apparatus: [9] 革【大】＊，隔【甲】＊; [1] 以【大】，之【甲】; [2] 佛【大】，道【甲】]*
``
- **Status:** Closed


### DEFECT-F02-026
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [＊9-1]
- **CBETA locator:** T1718_002.txt [＊9-1]
- **CBETA apparatus (verbatim):**
  - [＊9-1] 革【大】＊，隔【甲】＊
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**To sum up contemplations: what the above teacher and disciples do - the workings of the dharmakāya that bestows transformation - if one does not make it into a contemplating expedient, it is of no benefit to the practitioner. It is like a poor man counting another's treasure; it is like a blind man holding a lamp.**
*[Critical apparatus: [＊9-1] 革【大】＊，隔【甲】＊]*
``
- **Status:** Closed


### DEFECT-F02-027
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [3], [＊3-1]
- **CBETA locator:** T1718_002.txt [3], [＊3-1]
- **CBETA apparatus (verbatim):**
  - [3] 旃【大】＊，栴【甲】＊
  - [＊3-1] 旃【大】＊，栴【甲】＊
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Further, take the ten universal factors of the great earth that arise together with the mind-king, entering good and entering evil and pervading all: conceptualization, desire, contact, wisdom, mindfulness, intention, liberation, recollection, concentration, and feeling.**
*[Critical apparatus: [3] 旃【大】＊，栴【甲】＊; [＊3-1] 旃【大】＊，栴【甲】＊]*
``
- **Status:** Closed


### DEFECT-F02-028
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [4]
- **CBETA locator:** T1718_002.txt [4]
- **CBETA apparatus (verbatim):**
  - [4] 法數【大】，數法【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Now contemplating the mind is also like this: within each and every mind, the king and the factors are all present. In order to accomplish contemplation, king and factors mutually support one another and thereby obtain awakening. One may enter the path through the conceptualization-factor, or enter the path through the desire-factor - according to what is appropriate. Mind-king and mind-factors together apply themselves, transforming and taking the dusty-labors of the various minds and making them into Buddha-work.**
*[Critical apparatus: [4] 法數【大】，數法【甲】]*
``
- **Status:** Closed


### DEFECT-F02-029
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [5], [6]
- **CBETA locator:** T1718_002.txt [5], [6]
- **CBETA apparatus (verbatim):**
  - [5] 眾【大】，〔－〕【甲】
  - [6] 名【大】，名為【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Second is listed the Bodhisattva assembly. The *Treatise* says: "Bodhisattvas are included within the four assemblies of those who have left home and those who remain at home; why then are they listed separately? Answer: 'Some bodhisattvas fall within the four assemblies, but some members of the four assemblies do not fall within the bodhisattvas, because they have not aroused the aspiration to become Buddhas. Therefore, they are now listed separately.'" Those who equally arouse the mind and seek to become Buddhas are called the Bodhisattva assembly. The text has six parts: (1) type; (2) great number; (3) rank; (4) praising virtues; (5) listing names; (6) concluding phrase.**
*[Critical apparatus: [5] 眾【大】，〔－〕【甲】; [6] 名【大】，名為【甲】]*
``
- **Status:** Closed


### DEFECT-F02-030
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [＊3-2], [1]
- **CBETA locator:** T1718_002.txt [＊3-2], [1]
- **CBETA apparatus (verbatim):**
  - [＊3-2] 旃【大】＊，栴【甲】＊
  - [1] 蘇【大】，熟蘇【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**1. Type: This is precisely the Bodhisattva-Mahāsattvas. If preserved in full, it should be "bodhi-sattva-mahā-sattva"; Master Kumārajīva considered it verbose and abbreviated it, only mentioning the two characters *sattva* (*duò*). "Bodhi" means the Path; "sattva" means mind; "mahā" means great. These people all seek the broad, vast Great Path, and also mature sentient beings; thus they are the type of those with the "path-mind" and the "great-path-mind."**
*[Critical apparatus: [＊3-2] 旃【大】＊，栴【甲】＊; [1] 蘇【大】，熟蘇【甲】]*
``
- **Status:** Closed


### DEFECT-F02-031
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [2], [3]
- **CBETA locator:** T1718_002.txt [2], [3]
- **CBETA apparatus (verbatim):**
  - [2] 迦【大】，尊【甲】
  - [3] 鎚【大】，槌【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**According to *Fundamental and Trace*: the fundamental ground is hard to fathom - some dwell at the level of equal awakening; some are equal to the Dharma King. For example, when Sudhana enters the Dharma-realm and sees that Manjuśrī's form and images are boundless and his Dharma-gates deep and far, [this shows they] are fundamentally adjacent to the Buddhas. In trace, they assist Śākyamuni as bodhisattvas. By the power of the samādhi of universally manifesting form-bodies, they scatter their traces and let their appearances descend. By the inconceivable transformations of the "wheel of speech," they speak broadly as is appropriate. This can be known by meaning, but cannot be fully debated by words.**
*[Critical apparatus: [2] 迦【大】，尊【甲】; [3] 鎚【大】，槌【甲】]*
``
- **Status:** Closed


### DEFECT-F02-032
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [4], [5]
- **CBETA locator:** T1718_002.txt [4], [5]
- **CBETA apparatus (verbatim):**
  - [4] 密【大】，蜜【甲】
  - [5] 率【大】，變【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**"Eighty thousand": this is a number. Other sutras gather assemblies in very large numbers - why is this sutra's [number] comparatively small? Perhaps it is speaking of the assembly's greatness by number; or it is like a king discussing secret matters, which cannot be planned together with the entire land (and so on).**
*[Critical apparatus: [4] 密【大】，蜜【甲】; [5] 率【大】，變【甲】]*
``
- **Status:** Closed


### DEFECT-F02-033
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [6]
- **CBETA locator:** T1718_002.txt [6]
- **CBETA apparatus (verbatim):**
  - [6] 三【大】，此三【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**As for "All are irreversible from unsurpassed awakening": this clarifies rank/position. "Anuttara" means "unsurpassed." The "path" is as explained in the Wondrous of Objects; the "rank" is as explained in the Wondrous of Position.**
*[Critical apparatus: [6] 三【大】，此三【甲】]*
``
- **Status:** Closed


### DEFECT-F02-034
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [7], [8]
- **CBETA locator:** T1718_002.txt [7], [8]
- **CBETA apparatus (verbatim):**
  - [7] 歎【大】，歎往【甲】
  - [8] 歎【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**According to *Fundamental/Trace*: the quiescent-destruction of the fundamental ground is still not the Ten Grounds - how much less is it the First Abode? If it is still not even the First Abode's non-retrogression, how much less can it be the Distinct or Shared? The Distinct and Shared ranks are appropriate for explaining other sutras' assembly lists. The Perfect Teaching rank is precisely in this sutra. Since the treatise-masters of other sutras do not recognize the trace, how can they know the fundamental? When what is praised is already mistaken, condemnation is contained within it; it turns into the two slanders of increasing and decreasing - how could this be called praising virtue?**
*[Critical apparatus: [7] 歎【大】，歎往【甲】; [8] 歎【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-035
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [9], [10], [＊10-1], [11], [＊10-2], [＊10-3], [12], [1]
- **CBETA locator:** T1718_002.txt [9], [10], [＊10-1], [11], [＊10-2], [＊10-3], [12], [1]
- **CBETA apparatus (verbatim):**
  - [9] 禪【大】，禪故【甲】
  - [10] 董【大】＊，薰【甲】＊
  - [＊10-1] 董【大】＊，薰【甲】＊
  - [11] 為【大】，為諸【甲】
  - [＊10-2] 董【大】＊，薰【甲】＊
  - [＊10-3] 董【大】＊，薰【甲】＊
  - [12] 地【大】，地也【甲】
  - [1] 或【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Now, using thirteen clauses, [Zhiyi] dissolves the text by "vertical" and "horizontal" [interpretations]: (1) the vertical - in terms of the Ten Grounds - is convenient; (2) the horizontal - in terms of the First Abode - is convenient.**
*[Critical apparatus: [9] 禪【大】，禪故【甲】; [10] 董【大】＊，薰【甲】＊; [＊10-1] 董【大】＊，薰【甲】＊; [11] 為【大】，為諸【甲】; [＊10-2] 董【大】＊，薰【甲】＊; [＊10-3] 董【大】＊，薰【甲】＊; [12] 地【大】，地也【甲】; [1] 或【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-036
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [＊9-2], [2], [3]
- **CBETA locator:** T1718_002.txt [＊9-2], [2], [3]
- **CBETA apparatus (verbatim):**
  - [＊9-2] 革【大】＊，隔【甲】＊
  - [2] 供【大】，能供【甲】
  - [3] 能【大】，有【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Next, in terms of the "horizontal" praise: it directly explains it in terms of the First Abode; by analogy, the other ranks can be understood. In the First Abode of initial arousing of the mind, one arouses once and everything is aroused; one goes beyond the two extremes, transforms the ordinary and surpasses the sage, entering the Middle Way. The mind is quiescent, and thought after thought flows into the sea of omniscience; therefore it is said to attain non-retrogression.**
*[Critical apparatus: [＊9-2] 革【大】＊，隔【甲】＊; [2] 供【大】，能供【甲】; [3] 能【大】，有【甲】]*
``
- **Status:** Closed


### DEFECT-F02-037
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [4], [5]
- **CBETA locator:** T1718_002.txt [4], [5]
- **CBETA apparatus (verbatim):**
  - [4] 位【大】，住【甲】
  - [5] 空【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Answer: The other ranks are also like this - why only the First Abode? The old [interpretation] said that the Eighth Ground has various virtues, and did not take it as doubtful. Now, when the Perfect Teaching praises the First Abode, what virtue would it not encompass? If even the First Abode is like this, how much more the later ranks?**
*[Critical apparatus: [4] 位【大】，住【甲】; [5] 空【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-038
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [6], [7], [＊4-1]
- **CBETA locator:** T1718_002.txt [6], [7], [＊4-1]
- **CBETA apparatus (verbatim):**
  - [6] 名【大】，〔－〕【甲】
  - [7] 字語言【大】，空言語【甲】
  - [＊4-1] 秖【大】＊，只【甲】＊
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**In terms of contemplating-the-mind and interpreting the praise of virtues: non-retrogression is as discussed above. As for dhāraṇī: the emptiness contemplation is the "revolving dhāraṇī"; the provisional contemplation is the "hundreds-and-thousands revolving dhāraṇī"; the middle contemplation is the "Dharma-sound expedient dhāraṇī."**
*[Critical apparatus: [6] 名【大】，〔－〕【甲】; [7] 字語言【大】，空言語【甲】; [＊4-1] 秖【大】＊，只【甲】＊]*
``
- **Status:** Closed


### DEFECT-F02-039
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [1], [2]
- **CBETA locator:** T1718_002.txt [1], [2]
- **CBETA apparatus (verbatim):**
  - [1] 稱【大】，稱對治【甲】
  - [2] 不分卷【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
***The Words and Phrases of the Lotus Sutra of the Wonderful Dharma*, Fascicle Two, Part One**
*[Critical apparatus: [1] 稱【大】，稱對治【甲】; [2] 不分卷【甲】]*
``
- **Status:** Closed


### DEFECT-F02-040
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [3]
- **CBETA locator:** T1718_002.txt [3]
- **CBETA apparatus (verbatim):**
  - [3] 不分卷【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Interpreted by contemplating the mind: the three wisdoms are called "observing"; the three truths are called "world"; the three contemplations are the "speech" and, as the root, are therefore called "sound."**
*[Critical apparatus: [3] 不分卷【甲】]*
``
- **Status:** Closed


### DEFECT-F02-041
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [4], [5]
- **CBETA locator:** T1718_002.txt [4], [5]
- **CBETA apparatus (verbatim):**
  - [4] 勢【大】，勢至【甲】
  - [5] 世【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Interpreted by contemplating the mind: the three cessations are the feet; they step upon the ground of the Three Truths and move the Ten Dharma Realms; all places where views and craving abide are all shaken and overturned (and so on).**
*[Critical apparatus: [4] 勢【大】，勢至【甲】; [5] 世【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-042
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [6]
- **CBETA locator:** T1718_002.txt [6]
- **CBETA apparatus (verbatim):**
  - [6] 億【大】，萬【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**As for contemplating the mind: in contemplating emptiness, one does not abide in emptiness; in going out into the provisional, one does not abide in the provisional; and in entering the middle, one does not abide in the middle. Simultaneously illuminating the Two Truths is called Never Resting.**
*[Critical apparatus: [6] 億【大】，萬【甲】]*
``
- **Status:** Closed


### DEFECT-F02-043
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [7]
- **CBETA locator:** T1718_002.txt [7]
- **CBETA apparatus (verbatim):**
  - [7] 志【大】，悉【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**As for contemplating the mind: the inconceivable Three Truths are called jewels; the one-mind three contemplations are called the palm. With this contemplative palm holding these truth-jewels, benefiting self and benefiting others, therefore it is called Jeweled Palm.**
*[Critical apparatus: [7] 志【大】，悉【甲】]*
``
- **Status:** Closed


### DEFECT-F02-044
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [8]
- **CBETA locator:** T1718_002.txt [8]
- **CBETA apparatus (verbatim):**
  - [8] 來【大】，來也【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**In terms of contemplation and understanding: rightly contemplating the Middle Way is foremost among all goods; therefore it is called Good Guard.**
*[Critical apparatus: [8] 來【大】，來也【甲】]*
``
- **Status:** Closed


### DEFECT-F02-045
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [9]
- **CBETA locator:** T1718_002.txt [9]
- **CBETA apparatus (verbatim):**
  - [9] 下【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**In terms of contemplation and understanding: the wondrous wisdom of the Three Contemplations guides all practices, not falling into the two extremes, and all enter right contemplation; therefore it is named Guide. Those not yet explained will be supplemented later in annotations (and so on).**
*[Critical apparatus: [9] 下【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-046
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [12], [1]
- **CBETA locator:** T1718_002.txt [12], [1]
- **CBETA apparatus (verbatim):**
  - [12] 旃【大】下同，栴【甲】下同
  - [1] 本【大】，天本【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**The *Saṃyukta Āgama*, fascicle 40, says: "A bhikṣu asked the Buddha: 'Why is he named Śakra Devānām Indra?' [The Buddha] answered: 'When he was a human, he practiced sudden giving and was capable of acting as a lord; therefore he is named Śakra Devānām Indra.' 'Why is he named Purandara?' 'Because as a human he repeatedly practiced giving.' 'Why is he named Maghavan?' 'Because it was his name when he was a human.' 'Why is he named Śabara?' 'Because as a human he gave this robe-cloth.' 'Why is he named Kauśika?' 'Because it was his clan name when he was a human.' 'Why is he named Śacīpati?' 'Śacī is the wife; pati is the husband.' 'Why is he named Thousand-Eyed?' 'Because as a human he was clever and in one sitting could think a thousand meanings, observe and weigh them; therefore he is named Thousand-Eyed.' 'Why is he named Indriya?' 'Because he is lord of the thirty-two heavens.'" The *Yingluo*, fascicle 3, says: "The name of the Heavenly Emperor is Kōyoku."**
*[Critical apparatus: [12] 旃【大】下同，栴【甲】下同; [1] 本【大】，天本【甲】]*
``
- **Status:** Closed


### DEFECT-F02-047
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [2], [3]
- **CBETA locator:** T1718_002.txt [2], [3]
- **CBETA apparatus (verbatim):**
  - [2] 觀【大】，觀心【甲】
  - [3] 二【大】，三【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**In terms of contemplation and understanding: the Three Contemplations are the Two Wisdoms; the Three Wisdoms are the Three Luminaries. From the Three Truths arise the Three Wisdoms: the truths are the devas, and the wisdoms are the sons (and so on).**
*[Critical apparatus: [2] 觀【大】，觀心【甲】; [3] 二【大】，三【甲】]*
``
- **Status:** Closed


### DEFECT-F02-048
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [4]
- **CBETA locator:** T1718_002.txt [4]
- **CBETA apparatus (verbatim):**
  - [4] 大論云妙善【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**In terms of contemplation and understanding: contemplating the wisdom of the Four Truths is precisely the Four Kings. Under a single truth, removing the two afflictions of craving and views is protecting the eight cravings and views. Next, above Trāyastriṃśa there is Yāma, translated as "Good Times"; the *Great Treatise* calls it "Wondrous Good." It is 3,360,000 *lǐ* above Trāyastriṃśa. Above Good Times is Tuṣita, translated as "Wondrous Contentment," as far above Yāma as the earth [is below]. That they are not listed is simply abbreviation. Why? The lower heavens are dull and the higher heavens are attached to pleasures - yet they still know to come and gather. How much more would those who are neither attached nor dull fail to come?**
*[Critical apparatus: [4] 大論云妙善【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-049
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [5]
- **CBETA locator:** T1718_002.txt [5]
- **CBETA apparatus (verbatim):**
  - [5] 如【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Dwelling between dhyānas: internally there is vitarka and vicāra, and externally there is speech; attaining lordship, he is king. Those who cultivate dhyāna alone are Brahmā citizens; those who add the Four Immeasurables are kings. The first dhyāna has the Brahmā assembly, Brahmā ministers, and Great Brahmā; now it raises the king to include them all.**
*[Critical apparatus: [5] 如【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-050
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [6]
- **CBETA locator:** T1718_002.txt [6]
- **CBETA apparatus (verbatim):**
  - [6] 之【大】，之云云【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**There are also the five Anāgāmins: No-Affliction, No-Heat, Good-View, Good-Manifestation, and Form's Ultimate - also Great Mastery, namely Maheśvara. The sutra text is abbreviated and does not fully list them; it only says "and so on," meaning these various heavens. By analogy there are teaching-gate, Fundamental/Trace, and contemplating-the-mind interpretations - reflect on them yourself.**
*[Critical apparatus: [6] 之【大】，之云云【甲】]*
``
- **Status:** Closed


### DEFECT-F02-051
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [7], [8]
- **CBETA locator:** T1718_002.txt [7], [8]
- **CBETA apparatus (verbatim):**
  - [7] 於【大】，〔－〕【甲】
  - [8] 也【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Fundamentally, [it] abides in coolness and in Eternity, Bliss, Self, and Purity; in trace it dwells at the cool lake. In terms of contemplation: the wondrous wisdom of the Three Contemplations purifies the gnawing afflictions of the Five Abodes and avoids the hot sands of the two deaths (and so on).**
*[Critical apparatus: [7] 於【大】，〔－〕【甲】; [8] 也【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-052
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [9], [10], [11]
- **CBETA locator:** T1718_002.txt [9], [10], [11]
- **CBETA apparatus (verbatim):**
  - [9] 現【大】，視【甲】
  - [10] 涼【大】，源【甲】
  - [11] 云云【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Fundamentally, [it] abides in coolness and in Eternity, Bliss, Self, and Purity; in trace it dwells at the cool lake. In terms of contemplation: the wondrous wisdom of the Three Contemplations purifies the gnawing afflictions of the Five Abodes and avoids the hot sands of the two deaths (and so on).**
*[Critical apparatus: [9] 現【大】，視【甲】; [10] 涼【大】，源【甲】; [11] 云云【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-053
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [1]
- **CBETA locator:** T1718_002.txt [1]
- **CBETA apparatus (verbatim):**
  - [1] 魚龍【大】，龍魚【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Further, when the sun emits light and shines on its eyes, it cannot see; it raises its hand and palm to obstruct the sun. People all say there is a strange and dangerous solar eclipse - various wrong theories. Covering the moon is also so. Sometimes it makes a great sound; people say heavenly beasts roar and that danger and disorder mean kings decline - various wrong theories. When it frightens the sun and moon, it doubles its body and exhales energy at the sun and moon, and the sun and moon lose their light. It came to complain to the Buddha. The Buddha told Rāhu: "Do not swallow the sun and moon." Rāhu's joints trembled and his body flowed with white sweat; it immediately released the sun and moon. By the power of the sun and moon, the power of sentient beings, and the power of the Buddha, by the many causal conditions it could not do harm.**
*[Critical apparatus: [1] 魚龍【大】，龍魚【甲】]*
``
- **Status:** Closed


### DEFECT-F02-054
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [2]
- **CBETA locator:** T1718_002.txt [2]
- **CBETA apparatus (verbatim):**
  - [2] 云【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Further, when the sun emits light and shines on its eyes, it cannot see; it raises its hand and palm to obstruct the sun. People all say there is a strange and dangerous solar eclipse - various wrong theories. Covering the moon is also so. Sometimes it makes a great sound; people say heavenly beasts roar and that danger and disorder mean kings decline - various wrong theories. When it frightens the sun and moon, it doubles its body and exhales energy at the sun and moon, and the sun and moon lose their light. It came to complain to the Buddha. The Buddha told Rāhu: "Do not swallow the sun and moon." Rāhu's joints trembled and his body flowed with white sweat; it immediately released the sun and moon. By the power of the sun and moon, the power of sentient beings, and the power of the Buddha, by the many causal conditions it could not do harm.**
*[Critical apparatus: [2] 云【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-055
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [3], [4], [＊4-1]
- **CBETA locator:** T1718_002.txt [3], [4], [＊4-1]
- **CBETA apparatus (verbatim):**
  - [3] 不爾【大】，不爾者【甲】
  - [4] 邪【大】＊，耶【甲】＊
  - [＊4-1] 邪【大】＊，耶【甲】＊
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Further, when the sun emits light and shines on its eyes, it cannot see; it raises its hand and palm to obstruct the sun. People all say there is a strange and dangerous solar eclipse - various wrong theories. Covering the moon is also so. Sometimes it makes a great sound; people say heavenly beasts roar and that danger and disorder mean kings decline - various wrong theories. When it frightens the sun and moon, it doubles its body and exhales energy at the sun and moon, and the sun and moon lose their light. It came to complain to the Buddha. The Buddha told Rāhu: "Do not swallow the sun and moon." Rāhu's joints trembled and his body flowed with white sweat; it immediately released the sun and moon. By the power of the sun and moon, the power of sentient beings, and the power of the Buddha, by the many causal conditions it could not do harm.**
*[Critical apparatus: [3] 不爾【大】，不爾者【甲】; [4] 邪【大】＊，耶【甲】＊; [＊4-1] 邪【大】＊，耶【甲】＊]*
``
- **Status:** Closed


### DEFECT-F02-056
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [5]
- **CBETA locator:** T1718_002.txt [5]
- **CBETA apparatus (verbatim):**
  - [5] 此【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Next are listed four garuḍas. This is translated as "golden-winged": their wing-feathers are golden in color. They dwell atop the great trees of the four continents. The two wings are 3,360,000 *lǐ* apart. Some say that in the *Zhuangzi* they are called the *péng*; when the *péng* travels, the myriad birds wing alongside it, and it is also called a phoenix. Privately, [Zhiyi] says: the phoenix does not tread on living grass, eats bamboo fruit, and perches on paulownia; the golden-winged bird eats dragons - how could they be the same kind?**
*[Critical apparatus: [5] 此【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-057
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [6], [7], [＊7-1], [1], [2]
- **CBETA locator:** T1718_002.txt [6], [7], [＊7-1], [1], [2]
- **CBETA apparatus (verbatim):**
  - [6] 翻【大】，此翻【甲】
  - [7] 者【大】＊，〔－〕【甲】＊
  - [＊7-1] 者【大】＊，〔－〕【甲】＊
  - [1] 時【大】，世時【甲】
  - [2] 而惑【大】，或【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Next are listed the humans: "Vaidehī" is the mother; it is translated as "Concentration/Contemplation." "Bimbisāra" is translated as "Modeled Reality"; he is the father. "Ajātaśatru" means "unborn enemy." He is also called Vāruci, translated as "No Finger." The inner attendants who nursed him called him Good-View; Good-View is the fundamental name, and "No Finger" is the trace designation.**
*[Critical apparatus: [6] 翻【大】，此翻【甲】; [7] 者【大】＊，〔－〕【甲】＊; [＊7-1] 者【大】＊，〔－〕【甲】＊; [1] 時【大】，世時【甲】; [2] 而惑【大】，或【甲】]*
``
- **Status:** Closed


### DEFECT-F02-058
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [3]
- **CBETA locator:** T1718_002.txt [3]
- **CBETA apparatus (verbatim):**
  - [3] 以下斷缺【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**This meaning should now be distinguished. The rising and sinking of the destinies depends on whether precepts are upheld or violated; seeing the Buddha or not seeing the Buddha depends on whether the vehicle is slow or swift. Upholding precepts has coarse and fine, therefore the recompense is superior or inferior; upholding the vehicle has small and great, therefore seeing the Buddha has provisional and real. Briefly judging both precepts and vehicle each as three grades, and by one line from the *Nirvāṇa* unfolding them into four statements, the meaning becomes clear: (1) both precepts and vehicle are swift; (2) precepts are lax and vehicle is swift; (3) precepts are swift and vehicle is lax; (4) both precepts and vehicle are lax.**
*[Critical apparatus: [3] 以下斷缺【甲】]*
``
- **Status:** Closed


### DEFECT-F02-059
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [4]
- **CBETA locator:** T1718_002.txt [4]
- **CBETA apparatus (verbatim):**
  - [4] 法華文句卷第三首，卷首題下無天台智者大師說七字【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**From below the words "At that time the World-Honored One..." up to the end of the chapter is called the Distinct Sequence. The text has five parts: (1) the assembly gathering; (2) the manifestation of omens; (3) doubt and pondering; (4) raising the question; (5) answering the question.**
*[Critical apparatus: [4] 法華文句卷第三首，卷首題下無天台智者大師說七字【甲】]*
``
- **Status:** Closed


### DEFECT-F02-060
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [5], [6], [7]
- **CBETA locator:** T1718_002.txt [5], [6], [7]
- **CBETA apparatus (verbatim):**
  - [5] 合【大】，各合【甲】
  - [6] 集【大】，眾集【甲】
  - [7] 古往【大】，往古【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**As for the "four assemblies": the old [interpretation] said: "Those who have left home and those who remain at home each have two; together they make the four assemblies." This name is narrow and the intent is not comprehensive. Now, taking it as one assembly and further opening it as four, they are: the initiating assembly, the responsive assembly, the shadow-and-influence assembly, and the karmic-connection assembly.**
*[Critical apparatus: [5] 合【大】，各合【甲】; [6] 集【大】，眾集【甲】; [7] 古往【大】，往古【甲】]*
``
- **Status:** Closed


### DEFECT-F02-061
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [1], [2]
- **CBETA locator:** T1718_002.txt [1], [2]
- **CBETA apparatus (verbatim):**
  - [1] 並【大】，普【甲】
  - [2] 秖【大】下同，只【甲】下同
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**From the words "expounded the Great Vehicle Sutra for the sake of all bodhisattvas" down to "using the Buddha's relics to raise a seven-jeweled stupa" is the Manifestation Sequence. Master Yao explains seven omens: in this land six are opened, and in that land they are combined as one. Guangzhai says there are six omens here and six there.**
*[Critical apparatus: [1] 並【大】，普【甲】; [2] 秖【大】下同，只【甲】下同]*
``
- **Status:** Closed


### DEFECT-F02-062
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [3]
- **CBETA locator:** T1718_002.txt [3]
- **CBETA apparatus (verbatim):**
  - [3] 僧【大】，阿僧【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Master Sheng says: \"The markless empty principle is the root of the Great Vehicle. The sealing of the Three has been long; if one suddenly says \"no three,\" people cannot accept it. Therefore one speaks marklessness as the *Lotus* preface.\" Master Guan's intent is the same. If so, then the Prajñā sutras and the *Vimalakīrti* should all be prefaces; why only the *Infinite Meaning*? Their explanation says: \"Because of the Five Periods, later teachings can arise.\" We further ask: if so, then *Infinite Meaning* and the other sutras all mutually generate one another along the common road; that has nothing to do with a distinct preface.**[^6]
*[Critical apparatus: [3] 僧【大】，阿僧【甲】]*
``
- **Status:** Closed


### DEFECT-F02-063
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [4], [5], [6], [7], [8], [9], [10], [1]
- **CBETA locator:** T1718_002.txt [4], [5], [6], [7], [8], [9], [10], [1]
- **CBETA apparatus (verbatim):**
  - [4] 宋【大】，宗【甲】
  - [5] 與【大】，與歸【甲】
  - [6] 若【大】，善【甲】
  - [7] 序正【大】，正序【甲】
  - [8] 耳【大】，也【甲】
  - [9] 無【大】，出無【甲】
  - [10] 佛【大】，佛也【甲】
  - [1] 亦【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Master Sheng says: \"The markless empty principle is the root of the Great Vehicle. The sealing of the Three has been long; if one suddenly says \"no three,\" people cannot accept it. Therefore one speaks marklessness as the *Lotus* preface.\" Master Guan's intent is the same. If so, then the Prajñā sutras and the *Vimalakīrti* should all be prefaces; why only the *Infinite Meaning*? Their explanation says: \"Because of the Five Periods, later teachings can arise.\" We further ask: if so, then *Infinite Meaning* and the other sutras all mutually generate one another along the common road; that has nothing to do with a distinct preface.**[^6]
*[Critical apparatus: [4] 宋【大】，宗【甲】; [5] 與【大】，與歸【甲】; [6] 若【大】，善【甲】; [7] 序正【大】，正序【甲】; [8] 耳【大】，也【甲】; [9] 無【大】，出無【甲】; [10] 佛【大】，佛也【甲】; [1] 亦【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-064
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [2]
- **CBETA locator:** T1718_002.txt [2]
- **CBETA apparatus (verbatim):**
  - [2] 住【CB】【甲】，在【大】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**As for \"That which the Buddha protects and keeps in mindfulness\": the Meaning-Place of Infinite Meanings is what the Buddha himself has realized; therefore it is what the Tathāgata protects and keeps in mindfulness. Below it says: \"The Buddha himself abides in the Great Vehicle. Although he wishes to open and reveal [it], sentient beings' faculties are dull; for a long time he kept this essential point silent, not hastening to speak.\" Therefore it says \"protected and kept in mindfulness.\"**
*[Critical apparatus: [2] 住【CB】【甲】，在【大】]*
``
- **Status:** Closed


### DEFECT-F02-065
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [3], [4]
- **CBETA locator:** T1718_002.txt [3], [4]
- **CBETA apparatus (verbatim):**
  - [3] 實【大】，寶【甲】
  - [4] 迦【大】，金【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**As for \"Heaven rains four flowers\": the old explanation says, \"Small and great white; small and great red.\" The *Zhengfa-hua* says: \"Meaning-flower; Great-meaning-flower; Pǔxiàng-flower; Great-Pǔxiàng-flower.\" The *Treatise* (99) says: \"Heavenly flowers, when wondrous, are called māndārava.\" And again (79) says: \"Eight hundred bhikṣus become Buddhas in their lands, where five-colored māndārava flowers constantly rain.\" The old explanation takes the raining of small and great white to represent the two lay assemblies, and small and great red to represent the two renunciant assemblies, signifying their former causes but not yet their fruits.**
*[Critical apparatus: [3] 實【大】，寶【甲】; [4] 迦【大】，金【甲】]*
``
- **Status:** Closed


### DEFECT-F02-066
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [5]
- **CBETA locator:** T1718_002.txt [5]
- **CBETA apparatus (verbatim):**
  - [5] 以【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**As for the phrase "the entire Buddha-world's earth moves in six ways": the old explanation says it is the six fixed attachments of the three-vehicle people's cause-and-fruit. This breaks the Tripiṭaka school's three vehicles' six attachments, but does not break the Shared Teaching's three vehicles' six attachments. In the Shared Teaching, if one speaks in terms of dharmas, the three people's cause-and-fruit are the same; if one speaks in terms of persons, the three people's cause-and-fruit differ. Both this sameness and difference are broken, yet the old school's intent of breaking does not break this. In the Distinct Teaching, since there is no name of \"three vehicles,\" there are then no six attachments - which the old [explanation] does not break. Now we clarify that in the Distinct school, at the time of cause the three dharmas interweave horizontally and vertically, and at the time of fruit the three dharmas also interweave horizontally and vertically - this too must be broken.**
*[Critical apparatus: [5] 以【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-067
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [1]
- **CBETA locator:** T1718_002.txt [1]
- **CBETA apparatus (verbatim):**
  - [1] 滅【大】，滅也【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**In terms of contemplating practice, it is the moving of the six sense faculties. The earth-characteristic is firm and solid, like the six faculties' watery clinging. [Since one] has never entered the Great Vehicle's path, the \"hard-to-move\" earth is moved, signifying faculties that are pure-yet-not-pure.**
*[Critical apparatus: [1] 滅【大】，滅也【甲】]*
``
- **Status:** Closed


### DEFECT-F02-068
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [2], [3], [4], [5]
- **CBETA locator:** T1718_002.txt [2], [3], [4], [5]
- **CBETA apparatus (verbatim):**
  - [2] 而【大】，而今【甲】
  - [3] 喜【大】，歡喜【甲】
  - [4] 藏【大】，是藏【甲】
  - [5] 義【大】，意【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Answer: Heavenly flowers delight the eyes; earth-shaking shakes the mind. The *Mahā-sūtra* says: \"When it moves, it can cause sentient beings' minds to move.\" Flowers and earth are external omens; mind-joy is an internal omen. It is not ordinary joy. Though such joy has existed in the past, [one] was not moved by joy and yet could contemplate the Buddha with one mind - how could it not be an omen? If one says joy moves the defiled (skandha) mind, that is the human-and-heaven meaning. If joy moves the undefiled mind of the True Truth, that is the Tripiṭaka/Shared meaning. If joy moves the Provisional mind, that is the Distinct meaning. If joy moves the mind of the Real Aspect, that is the Perfect meaning.**[^14]
*[Critical apparatus: [2] 而【大】，而今【甲】; [3] 喜【大】，歡喜【甲】; [4] 藏【大】，是藏【甲】; [5] 義【大】，意【甲】]*
``
- **Status:** Closed


### DEFECT-F02-069
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [6]
- **CBETA locator:** T1718_002.txt [6]
- **CBETA apparatus (verbatim):**
  - [6] 牽【大】，毫【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Next, explaining the omen of the Buddha emitting light: it signifies establishing teaching in response to capacities, breaking delusion and removing doubt. The white curl possesses various merits. The *Contemplation of the Buddha-Sea Samādhi Sutra* says: \"When the Buddha was first born, it was drawn out to be five *chǐ* long; when practicing asceticism it was one *zhàng* four *chǐ* long; when he attained Buddhahood it was one *zhàng* five *chǐ* long. Within the hair, inside and outside are both empty, like a white beryl tube, pure within and without. From the first arousing of the mind, through the various practices and various appearances in the middle, up to entering nirvāṇa, all merits are displayed within the hair.\" The curl is between the two eyebrows, symbolizing the Middle Way's permanence; its softness symbolizes bliss; its free rolling and unrolling symbolizes self; its whiteness symbolizes purity. Emitting light breaks darkness, symbolizing that from the Middle Way wisdom arises. The light illuminating this land and other lands symbolizes self-enlightenment and enlightening others.**[^15]
*[Critical apparatus: [6] 牽【大】，毫【甲】]*
``
- **Status:** Closed


### DEFECT-F02-070
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [7], [8]
- **CBETA locator:** T1718_002.txt [7], [8]
- **CBETA apparatus (verbatim):**
  - [7] 緣宜【大】，宜緣【甲】
  - [8] 今【大】，此【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Furthermore: the sutras describe \"emitting light\" differently. In the *Great Prajñā*, it is from the thousand-spoked wheel-mark beneath the feet up to the topknot; each emits sixty thousand myriads of millions of rays, as explained there in detail. The *Mahā-sūtra* has light emitted from the face; this sutra has light emitted from the white curl; it is simply that conditions and suitability differ.**[^16]
*[Critical apparatus: [7] 緣宜【大】，宜緣【甲】; [8] 今【大】，此【甲】]*
``
- **Status:** Closed


### DEFECT-F02-071
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [9], [10], [11], [12]
- **CBETA locator:** T1718_002.txt [9], [10], [11], [12]
- **CBETA apparatus (verbatim):**
  - [9] 眾【大】，之眾【甲】
  - [10] 經【大】，經法【甲】
  - [11] 竟【大】，竟日【甲】
  - [12] 出【大】，生出【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Next, explaining the Six Omens of the light illuminating other lands: (1) seeing the six destinies; (2) seeing the Buddhas - this is the pair of superior sages and inferior ordinary beings; (3) hearing the Buddhas expound the Dharma; (4) seeing the four assemblies attain the Way - this is the pair of person and Dharma; (5) seeing bodhisattvas practicing conduct; (6) seeing Buddhas' nirvāṇa - this is the pair of beginning and end. Since there are sentient beings to be transformed, there are Buddhas who can transform; having Buddhas, there is preaching; having preaching, there are disciples; disciples are the beginning of practice; practice must reach the end.**
*[Critical apparatus: [9] 眾【大】，之眾【甲】; [10] 經【大】，經法【甲】; [11] 竟【大】，竟日【甲】; [12] 出【大】，生出【甲】]*
``
- **Status:** Closed

### DEFECT-F03-001
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3 (Part 1)
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** N/A
- **CBETA locator:** N/A (non‑CBETA insertion)
- **CBETA apparatus (verbatim):** N/A
- **Translation excerpt:**
  - Non‑CBETA editorial block: “OVERVIEW: WHY MAITREYA ASKS”.
- **Defect type:** Addition (non‑CBETA)
- **Required correction:**
  - Remove the entire overview block so CBETA text resumes immediately.
- **Post‑edit excerpt (Wenju_Fascicle_03_Part1_Scholarly.md):**
  ```
  ## 13. MAITREYA'S VERSES

  **從「爾時彌勒欲自決疑」下訖偈...**
  ```
- **Status:** Closed

### DEFECT-F03-002
- **File name:** Wenju_Fascicle_03_Part2_Scholarly.md
- **Fascicle:** 3 (Part 2)
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** N/A
- **CBETA locator:** N/A (non‑CBETA insertion)
- **CBETA apparatus (verbatim):** N/A
- **Translation excerpt:**
  - Non‑CBETA block: “TIANTAI TRANSLATION PROTOCOL (STRICT)”.
- **Defect type:** Addition (non‑CBETA)
- **Required correction:**
  - Remove the full protocol block from the translation body.
- **Post‑edit excerpt (Wenju_Fascicle_03_Part2_Scholarly.md):**
  ```
  **Spoken by the Tiantai Great Master Zhizhe.**

  ## Translation: Fascicle 3, Part 2
  ```
- **Status:** Closed

### DEFECT-F03-003
- **File name:** Wenju_Fascicle_03_Part2_Scholarly.md
- **Fascicle:** 3 (Part 2)
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** N/A
- **CBETA locator:** N/A (non‑CBETA insertion)
- **CBETA apparatus (verbatim):** N/A
- **Translation excerpt:**
  - Non‑CBETA block: “Structural Map: The Dialectic of Conveniences (Lines 195-End)”.
- **Defect type:** Addition (non‑CBETA)
- **Required correction:**
  - Remove the entire structural map block.
- **Post‑edit excerpt (Wenju_Fascicle_03_Part2_Scholarly.md):**
  ```
  **Spoken by the Tiantai Great Master Zhizhe.**

  ## Translation: Fascicle 3, Part 2
  ```
- **Status:** Closed


### DEFECT-F02-072
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [6], [7], [＊7-1], [＊7-2], [8], [9], [10], [11], [＊10-1]
- **CBETA locator:** T1718_002.txt [6], [7], [＊7-1], [＊7-2], [8], [9], [10], [11], [＊10-1]
- **CBETA apparatus (verbatim):**
  - [6] 不分卷【甲】
  - [7] 笑【大】＊，咲【甲】＊
  - [＊7-1] 笑【大】＊，咲【甲】＊
  - [＊7-2] 笑【大】＊，咲【甲】＊
  - [8] 羅【大】，阿羅【甲】
  - [9] 追【大】，召【甲】
  - [10] 和尚【大】＊，和上【甲】＊
  - [11] 偈【大】，偈言【甲】
  - [＊10-1] 和尚【大】＊，和上【甲】＊
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**In the past, among five hundred wild geese, one goose always obtained flowers and fruits to offer to the Goose King. [Later,] when the Buddha accepted the invitation of King Agnidatta regarding the summer retreat, five hundred bhikṣus all ate horse-fodder, yet Gavāmpati alone was in the Śirīṣa Garden[^2] in the heavens, receiving offerings from the Heavenly King.**
*[Critical apparatus: [6] 不分卷【甲】; [7] 笑【大】＊，咲【甲】＊; [＊7-1] 笑【大】＊，咲【甲】＊; [＊7-2] 笑【大】＊，咲【甲】＊; [8] 羅【大】，阿羅【甲】; [9] 追【大】，召【甲】; [10] 和尚【大】＊，和上【甲】＊; [11] 偈【大】，偈言【甲】; [＊10-1] 和尚【大】＊，和上【甲】＊]*
``
- **Status:** Closed


### DEFECT-F02-073
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [2], [3], [4], [5]
- **CBETA locator:** T1718_002.txt [2], [3], [4], [5]
- **CBETA apparatus (verbatim):**
  - [2] 住【大】，往【甲】
  - [3] 佛【大】，佛佛【甲】
  - [4] 石【大】，石空【甲】
  - [5] 汝【大】，我汝【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Because he constantly cultivated the practice of emptiness, he is called "Good Deeds/Good Practice." Because those who make offerings obtain immediate recompense, he is also called "Good Auspiciousness."**
*[Critical apparatus: [2] 住【大】，往【甲】; [3] 佛【大】，佛佛【甲】; [4] 石【大】，石空【甲】; [5] 汝【大】，我汝【甲】]*
``
- **Status:** Closed


### DEFECT-F02-074
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [9], [10], [11]
- **CBETA locator:** T1718_002.txt [9], [10], [11]
- **CBETA apparatus (verbatim):**
  - [9] 信【大】，使【甲】
  - [10] 大【大】，太【甲】
  - [11] 頸【大】，頸云云【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Then a deva came and said: "Your son has become a Buddha." The King had not yet resolved his doubt. In a moment a trusted report arrived: "Last night heaven and earth shook greatly; the Crown Prince has become a Buddha." The King had great joy. King Śuklodana reported: "A son has been born." The whole country was delighted; because of this he was named "Joy." This is the name given by his parents.**
*[Critical apparatus: [9] 信【大】，使【甲】; [10] 大【大】，太【甲】; [11] 頸【大】，頸云云【甲】]*
``
- **Status:** Closed


### DEFECT-F02-075
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [12], [13], [1], [2], [3]
- **CBETA locator:** T1718_002.txt [12], [13], [1], [2], [3]
- **CBETA apparatus (verbatim):**
  - [12] 翻此【大】，此翻【甲】
  - [13] 輪【大】，輪王【甲】
  - [1] 云【大】，睺【甲】
  - [2] 當【大】，當廣【甲】
  - [3] 法【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Paramārtha Tripiṭaka Master said: "Rāhu originally refers to [A]sura, who can obstruct the sun and moon with his hand; this should be translated as 'Obstructing the Moon'." The Buddha said: "My Dharma is like the moon; this child obstructed me from immediately leaving home. In lifetime after lifetime he obstructed me; in lifetime after lifetime I was able to renounce, so he is called Obstacle."**
*[Critical apparatus: [12] 翻此【大】，此翻【甲】; [13] 輪【大】，輪王【甲】; [1] 云【大】，睺【甲】; [2] 當【大】，當廣【甲】; [3] 法【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-076
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [10], [11]
- **CBETA locator:** T1718_002.txt [10], [11]
- **CBETA apparatus (verbatim):**
  - [10] 呼【大】，呼報【甲】
  - [11] 之【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Third is listed the "mixed assembly." The old [interpretations] said it is an assembly of ordinary people, yet here there are sages; said it is a worldly assembly, yet here there is the Way; said it is a deva-and-human assembly, yet here there are dragons and ghosts - all of these are unsuitable. Now it is called the mixed assembly, because the meaning includes them all: namely, the five destinies, the two realms, and eight groupings - therefore it is called "mixed." Vaipulya sutras also list hell; the *Intermediate-State Sutra* also teaches the formless - all of these appear in accord with capacities; one cannot make a single rule and line them up, and one also cannot fix their sequence.**
*[Critical apparatus: [10] 呼【大】，呼報【甲】; [11] 之【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F02-077
- **File name:** Wenju_Fascicle_02_FULL_Scholarly.md
- **Fascicle:** 2
- **CBETA source file:** T1718_002.txt
- **CBETA line numbers:** [1]
- **CBETA locator:** T1718_002.txt [1]
- **CBETA apparatus (verbatim):**
  - [1] 不分卷【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_02_FULL_Scholarly.md):**
  ``
**Answer: Catalyst (*Jī*) exists or not. Although positions are equal, Host and Guest have different suitabilities. The Sage responds to the Catalyst; if there is no questioner, he cannot answer.**
*[Critical apparatus: [1] 不分卷【甲】]*
``
- **Status:** Closed


### DEFECT-F03-004
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [9], [10]
- **CBETA locator:** T1718_003.txt [9], [10]
- **CBETA apparatus (verbatim):**
  - [9] 佛【大】，諸佛【甲】
  - [10] 生【大】，生者【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From "Also seeing the Buddhas" downwards, the second part (4 lines) asks about Seeing those Buddha Lands and directly Seeing the Buddhas Expound Dharma. This broadly clarifies the marks of expounding Dharma, meaning expounding the **Sudden Teaching** (*Dùn Jiào*) to meet the **Great Root Nature** (*Dà Gēn Xìng*). "Sage Lord Lions" is like **This Land** manifesting the image of **Vairocana** (*Lúshěnuó*)[^3].**
*[Critical apparatus: [9] 佛【大】，諸佛【甲】; [10] 生【大】，生者【甲】]*
``
- **Status:** Closed


### DEFECT-F03-005
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [1], [2], [3]
- **CBETA locator:** T1718_003.txt [1], [2], [3]
- **CBETA apparatus (verbatim):**
  - [1] 人【大】，〔－〕【甲】
  - [2] 供【大】，供養【甲】
  - [3] 故【大】，佛故【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From "If persons encounter suffering" downwards, the third part (3 lines) asks about the Four Assemblies of That Land. This is after the Sudden Preaching, next clarifying the **Tripiṭaka Teaching** (*Sānzàng Jiào*).**
*[Critical apparatus: [1] 人【大】，〔－〕【甲】; [2] 供【大】，供養【甲】; [3] 故【大】，佛故【甲】]*
``
- **Status:** Closed


### DEFECT-F03-006
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [4], [5]
- **CBETA locator:** T1718_003.txt [4], [5]
- **CBETA apparatus (verbatim):**
  - [4] 文殊【大】，次文殊師利【甲】
  - [5] 有【大】＊，〔－〕【甲】＊
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From "Manjuśrī, I abide/see" downwards, the fourth part (1.5 lines) concludes the previous and opens the subsequent.[^27][^28] "Seeing and hearing like this" concludes the previous. "Thus vast and many" opens the subsequent.**
*[Critical apparatus: [4] 文殊【大】，次文殊師利【甲】; [5] 有【大】＊，〔－〕【甲】＊]*
``
- **Status:** Closed


### DEFECT-F03-007
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [6], [7], [8], [9]
- **CBETA locator:** T1718_003.txt [6], [7], [8], [9]
- **CBETA apparatus (verbatim):**
  - [6] 第【大】，〔－〕【甲】
  - [7] 目【大】，眼【甲】
  - [8] 一行【大】，〔－〕【甲】
  - [9] 也【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From "I see that land" downwards, the fifth part has thirty-one and a half lines, asking about the various practices cultivated by bodhisattvas in that other land.**
*[Critical apparatus: [6] 第【大】，〔－〕【甲】; [7] 目【大】，眼【甲】; [8] 一行【大】，〔－〕【甲】; [9] 也【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F03-008
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [1], [＊1-1]
- **CBETA locator:** T1718_003.txt [1], [＊1-1]
- **CBETA apparatus (verbatim):**
  - [1] 兕【大】＊，光【甲】＊
  - [＊1-1] 兕【大】＊，光【甲】＊
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From "Manjuśrī, there are also Bodhisattvas" downwards, the sixth part (7 lines) clarifies raising Stupas for Relics after the Buddha's Extinction. This praises [recounts] the fact that the Buddha of that Land appeared in the Five Turbidities, opened Gradual and Sudden Teachings from the One Markless Dharma, hence there are Two Dharmas, Three Paths, and various different marks of practice as seen above.**
*[Critical apparatus: [1] 兕【大】＊，光【甲】＊; [＊1-1] 兕【大】＊，光【甲】＊]*
``
- **Status:** Closed


### DEFECT-F03-009
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [2]
- **CBETA locator:** T1718_003.txt [2]
- **CBETA apparatus (verbatim):**
  - [2] 從【大】，從諸【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From "At that time Manjuśrī said to Maitreya" down to the end of the verses is called the **Preface of Answering Questions**. It has prose and verses.**
*[Critical apparatus: [2] 從【大】，從諸【甲】]*
``
- **Status:** Closed


### DEFECT-F03-010
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [7], [8]
- **CBETA locator:** T1718_003.txt [7], [8]
- **CBETA apparatus (verbatim):**
  - [7] 說【大】，疑【甲】
  - [8] 記【大】，說記【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From "At that time there was a Bodhisattva" downwards, the fifth part "Bestowing Prediction Same." Anciently bestowed prediction on **Virtue Store** (*Dé Zàng*) Bodhisattva. Current Sutra bestows prediction on Śrāvakas. How can this be Same?**
*[Critical apparatus: [7] 說【大】，疑【甲】; [8] 記【大】，說記【甲】]*
``
- **Status:** Closed


### DEFECT-F03-011
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [5]
- **CBETA locator:** T1718_003.txt [5]
- **CBETA apparatus (verbatim):**
  - [5] 自【大】，若自【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**If arousing the true [path] is natural, why is there need for the buddhas to preach Dharma?**
*[Critical apparatus: [5] 自【大】，若自【甲】]*
``
- **Status:** Closed


### DEFECT-F03-012
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [6]
- **CBETA locator:** T1718_003.txt [6]
- **CBETA apparatus (verbatim):**
  - [6] 成【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**It is like a boat going with the current: if it meets wind and adds oar-assistance, it quickly reaches its destination. The wind is a metaphor for seeing the Buddha and hearing Dharma; the oars are a metaphor for cultivation.**
*[Critical apparatus: [6] 成【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F03-013
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [7]
- **CBETA locator:** T1718_003.txt [7]
- **CBETA apparatus (verbatim):**
  - [7] 等【大】，等教【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From "In each and every Buddha-land, the śrāvaka assembly" downwards: fourth, three lines. This takes people in terms of Dharma. Since the people are the two vehicles, one must know it is opening the Tripiṭaka preaching. That is: it versifies the above about preaching dharmas that accord with the Four Truths for śrāvaka people. Although it does not versify pratyekabuddhas explicitly, they are included within it. Practicing giving, patience, and so on corresponds to the four pāramitās. This single line versifies the above Mahāyāna of the Six Pāramitās.**
*[Critical apparatus: [7] 等【大】，等教【甲】]*
``
- **Status:** Closed


### DEFECT-F03-014
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [8], [9], [10], [＊5-1], [1], [2]
- **CBETA locator:** T1718_003.txt [8], [9], [10], [＊5-1], [1], [2]
- **CBETA apparatus (verbatim):**
  - [8] 二【大】，二有【甲】
  - [9] 四偈【大】，我見下四行偈【甲】
  - [10] 燈【大】，燈明【甲】
  - [＊5-1] 有【大】＊，〔－〕【甲】＊
  - [1] 召【大】，名【甲】
  - [2] 美【大】，義美【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**Next, from "At that time the fourfold assembly" downwards: second, one and a half lines. This retrospectively versifies the past Buddha's fourfold assembly harboring doubts, as in the text.**
*[Critical apparatus: [8] 二【大】，二有【甲】; [9] 四偈【大】，我見下四行偈【甲】; [10] 燈【大】，燈明【甲】; [＊5-1] 有【大】＊，〔－〕【甲】＊; [1] 召【大】，名【甲】; [2] 美【大】，義美【甲】]*
``
- **Status:** Closed


### DEFECT-F03-015
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [4]
- **CBETA locator:** T1718_003.txt [4]
- **CBETA apparatus (verbatim):**
  - [4] 皆【大】，皆是【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**They are distinguished in four sentences: there are those in which skillful means break provisionality and provisionality breaks skillful means; skillful means cultivate provisionality and provisionality cultivates skillful means; skillful means are provisionality and provisionality is skillful means; provisionality is skillful means with no two and no difference.**
*[Critical apparatus: [4] 皆【大】，皆是【甲】]*
``
- **Status:** Closed


### DEFECT-F03-016
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [5]
- **CBETA locator:** T1718_003.txt [5]
- **CBETA apparatus (verbatim):**
  - [5] 權【大】，權後【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**Further, some use the four kinds of two wisdoms: first, one is provisional and one is real; next, the two knowledges of empty and existent—contemplating emptiness without realizing it departs from the two vehicles, engaging existence without defilement departs from ordinary beings; next, inner quiescence of empty and existent is real and outer functioning is provisional; next, permanence/impermanence before/after the diamond are provisional/real.**
*[Critical apparatus: [5] 權【大】，權後【甲】]*
``
- **Status:** Closed


### DEFECT-F03-017
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [1]
- **CBETA locator:** T1718_003.txt [1]
- **CBETA apparatus (verbatim):**
  - [1] 不分卷【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**Now, clarifying provisional and real: first make four sentences: (1) all dharmas are provisional; (2) all dharmas are real; (3) all dharmas are both provisional and real; (4) all dharmas are neither provisional nor real.**
*[Critical apparatus: [1] 不分卷【甲】]*
``
- **Status:** Closed


### DEFECT-F03-018
- **File name:** Wenju_Fascicle_03_Part2_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [2]
- **CBETA locator:** T1718_003.txt [2]
- **CBETA apparatus (verbatim):**
  - [2] 不分卷【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**"All dharmas are neither provisional nor real," as the text states: "It is neither like nor different." And again: "It also does not practice superior, medium, or inferior dharmas, conditioned or unconditioned, real or unreal dharmas; it is neither empty nor real, but like the Real Mark [Reality itself]."**
*[Critical apparatus: [2] 不分卷【甲】]*
``
- **Status:** Closed


### DEFECT-F03-019
- **File name:** Wenju_Fascicle_03_Part2_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [4], [1]
- **CBETA locator:** T1718_003.txt [4], [1]
- **CBETA apparatus (verbatim):**
  - [4] 為【大】，〔－〕【甲】
  - [1] 檀【大】，〔－〕【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**3. Explanation:**
*[Critical apparatus: [4] 為【大】，〔－〕【甲】; [1] 檀【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F03-020
- **File name:** Wenju_Fascicle_03_Part2_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [2]
- **CBETA locator:** T1718_003.txt [2]
- **CBETA apparatus (verbatim):**
  - [2] 已下斷缺【甲】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**4. Citation of Proof: These ten meanings pervasively cover the Great and Small Teachings, spanning all dharmas. We tentatively cite this sutra: "Not seeing the Three Realms as the Three Realms [are usually seen]"—**
*[Critical apparatus: [2] 已下斷缺【甲】]*
``
- **Status:** Closed


### DEFECT-F03-021
- **File name:** Wenju_Fascicle_03_Part2_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [A1]
- **CBETA locator:** T1718_003.txt [A1]
- **CBETA apparatus (verbatim):**
  - [A1] 從【CB】，縱【大】
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From this chapter down to the 19 verses of the *Distinctions in Merit Chapter*, or up to the end of the text on the "Four Faiths of Disciples in the Present," is named the Main Discourse Division (*Zhengshuo Fen*).**
*[Critical apparatus: [A1] 從【CB】，縱【大】]*
``
- **Status:** Closed


### DEFECT-F03-022
- **File name:** Wenju_Fascicle_03_Part2_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [A2]
- **CBETA locator:** T1718_003.txt [A2]
- **CBETA apparatus (verbatim):**
  - [A2] 莫【CB】，茣【大】(cf. X30n0600_p0043c12)
- **Translation excerpt:**
  - Missing apparatus near anchor line.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert a critical‑apparatus line covering the variants above at the correct position.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From "Sariputra, the Tathāgata is able to make various distinctions" Old interpretations take this to conclude the previous Power/Real. Now we use it to start the later section; intending to Transcend Words (*Jueyan*), we again bring up Power/Real as the cause for the "Praise Transcending Words."**
*[Critical apparatus: [A2] 莫【CB】，茣【大】(cf. X30n0600_p0043c12)]*
``
- **Status:** Closed


### DEFECT-F03-023
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [2]
- **CBETA locator:** T1718_003.txt [2]
- **CBETA apparatus (verbatim):**
  - [2] 不分卷【甲】
- **Translation excerpt:**
  - Inline apparatus embedded in Chinese line.
- **Defect type:** Formatting / Addition (inline apparatus)
- **Required correction:**
  - Move apparatus to a standalone critical‑apparatus line and remove inline commentary.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From "At that time Maitreya wished to resolve his doubts" down to the end of the verses, this is the **Preface of Asking Questions** (*Fā Wèn Xù*). The text has two parts: Prose and Verses.[^15]**
*[Critical apparatus: 不分卷【甲】]*
``
- **Status:** Closed


### DEFECT-F03-024
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [3]
- **CBETA locator:** T1718_003.txt [3]
- **CBETA apparatus (verbatim):**
  - [3] 問【大】，〔－〕【甲】
- **Translation excerpt:**
  - Inline apparatus embedded in Chinese line.
- **Defect type:** Formatting / Addition (inline apparatus)
- **Required correction:**
  - Move apparatus to a standalone critical‑apparatus line and remove inline commentary.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**In the questioning,[^16] [the doubts regarding] This Land and That Land are as in the text. Why is there a Verse Section (*Gāthā*)?**
*[Critical apparatus: 問【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F03-025
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [4], [5]
- **CBETA locator:** T1718_003.txt [4], [5]
- **CBETA apparatus (verbatim):**
  - [4] 問【大】，答問【甲】
  - [5] 兩【大】，二【甲】
- **Translation excerpt:**
  - Inline apparatus embedded in Chinese line.
- **Defect type:** Formatting / Addition (inline apparatus)
- **Required correction:**
  - Move apparatus to a standalone critical‑apparatus line and remove inline commentary.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**Regarding the **Questioning**,[^17] there are two[^18] parts: The first four lines ask about **This Land**; the latter fifty lines ask about **That [Other] Land**.**
*[Critical apparatus: 問【大】，答問【甲】; 兩【大】，二【甲】]*
``
- **Status:** Closed


### DEFECT-F03-026
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [6]
- **CBETA locator:** T1718_003.txt [6]
- **CBETA apparatus (verbatim):**
  - [6] 光【大】，光明【甲】
- **Translation excerpt:**
  - Inline apparatus embedded in Chinese line.
- **Defect type:** Formatting / Addition (inline apparatus)
- **Required correction:**
  - Move apparatus to a standalone critical‑apparatus line and remove inline commentary.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From "Brow Light"[^19] downwards, next there are fifty lines [of verse] that versify the questions about the Six Omens of Other Lands.**
*[Critical apparatus: 光【大】，光明【甲】]*
``
- **Status:** Closed


### DEFECT-F03-027
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [7]
- **CBETA locator:** T1718_003.txt [7]
- **CBETA apparatus (verbatim):**
  - [7] 次【大】，五【甲】
- **Translation excerpt:**
  - Inline apparatus embedded in Chinese line.
- **Defect type:** Formatting / Addition (inline apparatus)
- **Required correction:**
  - Move apparatus to a standalone critical‑apparatus line and remove inline commentary.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**Next:[^20] thirty-one and a half lines ask about cultivating Bodhisattva practices in Other Lands.**
*[Critical apparatus: 次【大】，五【甲】]*
``
- **Status:** Closed


### DEFECT-F03-028
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [8]
- **CBETA locator:** T1718_003.txt [8]
- **CBETA apparatus (verbatim):**
  - [8] 次【大】，六【甲】
- **Translation excerpt:**
  - Inline apparatus embedded in Chinese line.
- **Defect type:** Formatting / Addition (inline apparatus)
- **Required correction:**
  - Move apparatus to a standalone critical‑apparatus line and remove inline commentary.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**Next:[^21] seven lines ask about offerings to relics; this is precisely asking about the Buddha's Nirvana.**
*[Critical apparatus: 次【大】，六【甲】]*
``
- **Status:** Closed


### DEFECT-F03-029
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [9], [10]
- **CBETA locator:** T1718_003.txt [9], [10]
- **CBETA apparatus (verbatim):**
  - [9] 佛【大】，諸佛【甲】
  - [10] 生【大】，生者【甲】
- **Translation excerpt:**
  - Inline apparatus embedded in Chinese line.
- **Defect type:** Formatting / Addition (inline apparatus)
- **Required correction:**
  - Move apparatus to a standalone critical‑apparatus line and remove inline commentary.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**"Illuminating Buddha Dharmas,[^22] opening and awakening sentient beings"[^23] is like **This Land** beginning to see the Buddha Body and entering the Tathāgata Wisdom.**
*[Critical apparatus: 佛【大】，諸佛【甲】; 生【大】，生者【甲】]*
``
- **Status:** Closed


### DEFECT-F03-030
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [1]
- **CBETA locator:** T1718_003.txt [1]
- **CBETA apparatus (verbatim):**
  - [1] 人【大】，〔－〕【甲】
- **Translation excerpt:**
  - Inline apparatus embedded in Chinese line.
- **Defect type:** Formatting / Addition (inline apparatus)
- **Required correction:**
  - Move apparatus to a standalone critical‑apparatus line and remove inline commentary.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**If persons encounter suffering and create evil karma, suffering cannot be exhausted—these are the "Bottom" sentient beings. If persons[^24] encounter suffering and create good karma, suffering is also not exhausted; they loathe the lower and climb to the higher [heavens], like Nanda holding precepts for the sake of desire.**
*[Critical apparatus: 人【大】，〔－〕【甲】]*
``
- **Status:** Closed


### DEFECT-F03-031
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [2]
- **CBETA locator:** T1718_003.txt [2]
- **CBETA apparatus (verbatim):**
  - [2] 供【大】，供養【甲】
- **Translation excerpt:**
  - Inline apparatus embedded in Chinese line.
- **Defect type:** Formatting / Addition (inline apparatus)
- **Required correction:**
  - Move apparatus to a standalone critical‑apparatus line and remove inline commentary.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From "If a person has blessings"—the next single line—this opens the Middle Vehicle. If one makes few offerings to a Buddha, one encounters suffering and is afflicted. If one makes many[^25] offerings to a Buddha, although one encounters suffering one has blessings. Therefore it says: a śrāvaka plants blessings over three lifetimes; a pratyekabuddha plants blessings over a hundred kalpas. In comparison with those śrāvakas, therefore it says "has blessings."**
*[Critical apparatus: 供【大】，供養【甲】]*
``
- **Status:** Closed


### DEFECT-F03-032
- **File name:** Wenju_Fascicle_03_Part1_Scholarly.md
- **Fascicle:** 3
- **CBETA source file:** T1718_003.txt
- **CBETA line numbers:** [3]
- **CBETA locator:** T1718_003.txt [3]
- **CBETA apparatus (verbatim):**
  - [3] 故【大】，佛故【甲】
- **Translation excerpt:**
  - Inline apparatus embedded in Chinese line.
- **Defect type:** Formatting / Addition (inline apparatus)
- **Required correction:**
  - Move apparatus to a standalone critical‑apparatus line and remove inline commentary.
- **Post‑edit excerpt (Wenju_Fascicle_03):**
  ``
**From "If there are Buddha-sons" downwards, this opens the Mahāyāna of the Six Pāramitās. True compassion can continue the Buddha-seed, therefore they are called "Buddha-sons." They cultivate the Six Pāramitās, therefore it says "various practices." Because they aspire and seek,[^26] therefore it says "unsurpassed wisdom." Within the Six Pāramitās there are no six hindrances; like medicine that contains no disease, therefore it is called the "pure path"—it is not ultimately pure.**
*[Critical apparatus: 故【大】，佛故【甲】]*
``
- **Status:** Closed



### DEFECT-F04-001
- **File name:** Wenju_Fascicle_04_Part1_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 9–227
- **CBETA locator:** T1718_004.txt [1]–[2], [3], [4], [1], [＊1-1], [2], [3], [4], [＊4-1], [1], [2], [＊4-2]–[＊4-4], [＊4-5], [＊4-6], [1]–[4], [1], [2], [＊1-2], [＊1-3], [＊1-4], [1], [2]
- **CBETA apparatus (verbatim):**
  - [1] 妙法蓮華經【大】，法華【甲】
  - [2] 上【大】，〔－〕【甲】
  - [3] 天台智者大師說【大】，〔－〕【甲】
  - [4] 揀【大】＊，簡【甲】＊
  - [1] 二【大】，第二【甲】
  - [1] 優【大】＊，〔－〕【甲】＊
  - [＊1-1] 優【大】＊，〔－〕【甲】＊
  - [2] 胡【大】，梵【甲】
  - [3] 九【大】，第九【甲】
  - [4] 正【大】，止【甲】
  - [＊4-1] 揀【大】＊，簡【甲】＊
  - [1] 秖【大】＊，只【甲】＊
  - [2] 諳【大】，識【甲】
  - [＊4-2] 揀【大】＊，簡【甲】＊
  - [3] 是【大】，〔－〕【甲】
  - [4] 是【大】，此【甲】
  - [＊4-3] 揀【大】＊，簡【甲】＊
  - [＊4-4] 揀【大】＊，簡【甲】＊
  - [＊4-5] 揀【大】＊，簡【甲】＊
  - [＊4-6] 揀【大】＊，簡【甲】＊
  - [1] 解【大】，知【甲】
  - [＊1-1] 秖【大】＊，只【甲】＊
  - [2] 引【大】，胤【甲】
  - [1] 矛【大】，桙【甲】
  - [2] 若【大】，答【甲】
  - [3] 來【大】，未【甲】
  - [4] 為【大】，為示無量義為【甲】
  - [1] 知【大】，〔－〕【甲】
  - [2] 體【大】，體顯【甲】
  - [＊1-2] 秖【大】＊，只【甲】＊
  - [＊1-3] 秖【大】＊，只【甲】＊
  - [＊1-4] 秖【大】＊，只【甲】＊
  - [1] 結【大】，結成諸佛四一文也【甲】
  - [2] 不分卷【甲】
- **Translation excerpt:**
  - CBETA markers appear in the Chinese linework, but no critical‑apparatus lines were present in Part 1.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert critical‑apparatus lines at each marker location using the standard scholarly format.
- **Post‑edit excerpt (Wenju_Fascicle_04_Part1_Scholarly.md):**
  ```
  [1]妙法蓮華經文句卷第四[2]上<br>
  [3]天台智者大師說
  *[Critical apparatus: [1] 妙法蓮華經【大】，法華【甲】; [2] 上【大】，〔－〕【甲】; [3] 天台智者大師說【大】，〔－〕【甲】]*
  ```
- **Status:** Closed


### DEFECT-F04-002
- **File name:** Wenju_Fascicle_04_Part2_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 235–414
- **CBETA locator:** T1718_004.txt [3], [4], [5], [＊4-1], [1], [2], [3], [4], [＊2-1], [＊4-2]–[＊4-4], [5], [6], [1], [2], [3], [＊4-5], [＊4-6], [4], [5], [1], [2], [3], [4], [5], [＊2-2], [6], [1], [2], [3], [＊2-3], [4], [5], [A1], [1]–[7], [A2], [5]–[7], [8], [1]–[5], [＊3-1], [＊3-2], [6]
- **CBETA apparatus (verbatim):**
  - [3] 不分卷【甲】
  - [4] 揀【大】＊，簡【甲】＊
  - [5] 秖【大】，只【甲】
  - [＊4-1] 揀【大】＊，簡【甲】＊
  - [1] 是【大】，是也【甲】
  - [2] 邪【大】＊，耶【甲】＊
  - [3] 執【大】，〔－〕【甲】
  - [4] 作是思惟【大】，即生此念【甲】
  - [＊2-1] 邪【大】＊，耶【甲】＊
  - [＊4-2] 揀【大】＊，簡【甲】＊
  - [＊4-3] 揀【大】＊，簡【甲】＊
  - [＊4-4] 揀【大】＊，簡【甲】＊
  - [5] 一【大】，一也【甲】
  - [6] 入【大】，應入【甲】
  - [1] 將【大】，用【甲】
  - [2] 云【大】，言【甲】
  - [3] 有【大】，〔－〕【甲】
  - [＊4-5] 揀【大】＊，簡【甲】＊
  - [＊4-6] 揀【大】＊，簡【甲】＊
  - [4] 我有方便下【大】，有【甲】
  - [5] 小【大】，少【甲】
  - [1] 人【大】，上人【甲】
  - [2] 中【大】，中亦二內心外色【甲】
  - [3] 心【大】，心次一行舉外色【甲】
  - [4] 誓【大】，誓願【甲】
  - [5] 障【大】，障大【甲】
  - [＊2-2] 邪【大】＊，耶【甲】＊
  - [6] 秖【大】，〔－〕【甲】
  - [1] 酥【大】，蘇【甲】
  - [2] 四【大】，疱【甲】
  - [3] 蟲【大】，虫【甲】
  - [＊2-3] 邪【大】＊，耶【甲】＊
  - [4] 或【大】，或云【甲】
  - [5] 劫【大】，佛【甲】
  - [A1] 二【CB】，一【大】
  - [1] 二【大】，六【甲】
  - [2] 古【大】，古時【甲】
  - [3] 皮【大】，膠【甲】
  - [4] 墮【大】，隨【甲】
  - [5] 盤【大】，槃【甲】
  - [6] 次【大】，〔－〕【甲】
  - [7] 也【大】，〔－〕【甲】
  - [1] 龍【大】，籠【甲】
  - [2] 互【大】，更互【甲】
  - [1] 末【大】，未【甲】
  - [2] 本【大】，作本【甲】
  - [3] 始【大】，〔－〕【甲】
  - [4] 大【大】，大寢【甲】
  - [A2] 派【CB】，泒【大】(cf. X29n0597_p0528c03)
  - [5] 觀【大】，〔－〕【甲】
  - [6] 得【大】，同【甲】
  - [7] 原【大】，元【甲】
  - [8] 用【大】，之【甲】
  - [1] 曜【大】，耀【甲】
  - [2] 在【大】，在天【甲】
  - [3] 胡【大】＊，梵【甲】＊
  - [4] 味【大】，無味【甲】
  - [5] 變【大】，反【甲】
  - [＊3-1] 胡【大】＊，梵【甲】＊
  - [＊3-2] 胡【大】＊，梵【甲】＊
  - [6] 不分卷【甲】
- **Translation excerpt:**
  - CBETA markers appear throughout Part 2, but no critical‑apparatus lines were present.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert critical‑apparatus lines at each marker location using the standard scholarly format.
- **Post‑edit excerpt (Wenju_Fascicle_04_Part2_Scholarly.md):**
  ```
  [3]第二、廣釋迦章，於六義中，無歎法希有，初開權，次顯實，三舉五濁釋方便，四[4]揀偽敦信一實，五無虛妄。
  *[Critical apparatus: [3] 不分卷【甲】; [4] 揀【大】＊，簡【甲】＊]*
  ```
- **Status:** Closed


### DEFECT-F04-003
- **File name:** Wenju_Fascicle_04_Part2_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 235, 256
- **CBETA text (quoted):**
  - 「[3]第二、廣釋迦章，於六義中，無歎法希有，初開權，次顯實，三舉五濁釋方便，四[4]揀偽敦信一實，五無虛妄。…況有單三、單五之權？[5]秖為五濁障重實不得宣…」
  - 「…根鈍遮重，此則成障，不聞小乘、不得度者[1]。」
- **Translation excerpt:**
  - The opening line lacked the leading [3] marker, the “秖為五濁…” line used [＊4-5] instead of [5], and the small‑vehicle Q&A line omitted the trailing [1].
- **Defect type:** Marker omission / mismatch
- **Required correction:**
  - Insert [3] at the start of the “第二、廣釋迦章” line, correct [＊4-5] → [5] in “秖為五濁…”, and add the trailing [1] at the end of the small‑vehicle Q&A line.
- **Post‑edit excerpt (Wenju_Fascicle_04_Part2_Scholarly.md):**
  ```
  [3]第二、廣釋迦章，於六義中，無歎法希有，初開權，次顯實，三舉五濁釋方便，四[4]揀偽敦信一實，五無虛妄。
  [5]秖為五濁障重實不得宣，須施單五、單三之權，亦施帶二、帶三之權，故言「於一佛乘分別說三」，分別說於若帶二、帶三之三，若單五、單三之三也。
  …
  答：此就小乘，應四句分別：小乘根利遮輕，障不能障，身子是也；根利遮重，障亦不能障，央掘是也；根鈍遮輕亦不為障，槃特是也；根鈍遮重，此則成障，不聞小乘、不得度者是。[1]
  ```
- **Status:** Closed


### DEFECT-F04-004
- **File name:** Wenju_Fascicle_04_Part1_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 87–88
- **CBETA text (quoted):**
  - 「十、明待時不待時，爾前不悟必待《法華》悟者，名為待時；《法華》前教已解者，名不待時。何故爾？佛有顯密二說。若密教為論，未必具待五味在法華方會，爾前密有入者故名不待時，此乃大判時不時。若就三周，亦是待時、不待時，迹本二門，亦是待時、不待時，致有前後悟入，即此意也。」
- **Translation excerpt:**
  - The Chinese source used ellipses (“顯密二說…”, “此乃大判時不時…”) that truncated the CBETA line, and the English quote used ellipsis within the direct citation.
- **Defect type:** Omission / Ellipsis
- **Required correction:**
  - Restore the full CBETA line (no ellipses) and render the quoted line without ellipsis.
- **Post‑edit excerpt (Wenju_Fascicle_04_Part1_Scholarly.md):**
  ```
  十、明待時不待時，爾前不悟必待《法華》悟者，名為待時；《法華》前教已解者，名不待時。何故爾？佛有顯密二說。
  若密教為論，未必具待五味在法華方會，爾前密有入者故名不待時，此乃大判時不時。若就三周，亦是待時、不待時，迹本二門，亦是待時、不待時，致有前後悟入，即此意也。
  Therefore it says: "Because the Time for speaking had not yet arrived, now is exactly the Time; I decisively speak the Great Vehicle." This is **Waiting for Time**.
  ```
- **Status:** Closed


### DEFECT-F04-005
- **File name:** Wenju_Fascicle_04_Part1_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 58, 173–179
- **CBETA text (quoted):**
  - 「其求緣覺者，比丘、比丘尼。」
  - 「《金光明》中，時閻浮提有二種人，亦是斯例意。」
- **Translation excerpt:**
  - English citations used ellipses: “Bhikṣus and Bhikṣuṇīs.” and “there were two kinds of people.”
- **Defect type:** Paraphrase / Ellipsis
- **Required correction:**
  - Remove ellipses and render the quoted phrases fully.
- **Post‑edit excerpt (Wenju_Fascicle_04_Part1_Scholarly.md):**
  ```
  Therefore, in Śāriputra’s request verse, it says: "Those seeking the Pratyekabuddha Vehicle, Bhikṣus and Bhikṣuṇīs." Relying on this text, we know that Pratyekabuddhas are gathered within the Four Assemblies.
  …
  In the *Suvarṇaprabhāsa Sūtra* (*Golden Light*), it says in Jambudvīpa there were two kinds of people; this is also the meaning of this example.
  ```
- **Status:** Closed


### DEFECT-F04-006
- **File name:** Wenju_Fascicle_04_Part1_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 42–56
- **CBETA locator:** T1718_004.txt 42–56
- **Chinese text (quoted):**
  - 「問：三根入初住位，猶有利鈍不？」
  - 「答：真修體顯則無差降。」
  - 「問：若爾，初住已上更起緣修，有優劣不？」
  - 「答：此同位人無復勝負，真修體融寧得有異耶？」
- **Translation excerpt:**
  - The Q/A block is missing between the “three knives chopping wood” paragraph and the “Meanings 5: Roots have Awakening or Do Not Have Awakening” heading.
- **Defect type:** Omission (missing Q/A block)
- **Required correction:**
  - Insert the missing four Q/A lines with bilingual translation in Meaning 4, immediately after the “three knives chopping wood” paragraph and before Meaning 5.
- **Post‑edit excerpt (Wenju_Fascicle_04_Part1_Scholarly.md):**
  ```
  問：<br><br>
  三根入初住位，猶有利鈍不？
  **Question:** When the three roots enter the first abode, is there still sharpness and dullness?
  …
  答：<br><br>
  此同位人無復勝負，真修體融寧得有異耶？
  **Answer:** For those in the same level there is no longer victory or defeat; once the substance of true cultivation is fused, how could there be differences?
  ```
- **Status:** Closed


### DEFECT-F04-007
- **File name:** Wenju_Fascicle_04_Part2_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 256
- **CBETA text (quoted):**
  - 「此就小乘，應四句分別：小乘根利遮輕，障不能障，身子是也；根利遮重，障亦不能障，央掘是也；根鈍遮輕亦不為障，槃特是也；根鈍遮重，此則成障，不聞小乘、不得度者[1]是。」
- **Translation excerpt:**
  - 「…根鈍遮重，此則成障，不聞小乘、不得度者是。[1]」
- **Defect type:** Marker misplacement (apparatus anchor)
- **Required correction:**
  - Move the [1] marker to match CBETA placement: immediately after 「者」 and before 「是」.
- **Post‑edit excerpt (Wenju_Fascicle_04_Part2_Scholarly.md):**
  ```
  答：此就小乘，應四句分別：小乘根利遮輕，障不能障，身子是也；根利遮重，障亦不能障，央掘是也；根鈍遮輕亦不為障，槃特是也；根鈍遮重，此則成障，不聞小乘、不得度者[1]是。
  ```
- **Status:** Closed


### DEFECT-F04-008
- **File name:** Wenju_Fascicle_04_Part2_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 393
- **CBETA text (quoted):**
  - 「…「種種法門」即對不種種，為下唯有一門譬作本；…」
- **Translation excerpt:**
  - 「…「種種法門」即對不種種，為下唯一門譬作本；…」
- **Defect type:** Omission (single character)
- **Required correction:**
  - Insert 「有」 to match CBETA: 「唯有一門」.
- **Post‑edit excerpt (Wenju_Fascicle_04_Part2_Scholarly.md):**
  ```
  又安隱者，即是安隱法，還對不安隱法，不安隱法即五濁法也，為下火起譬作本；「種種法門」即對不種種，為下唯有一門譬作本；「知眾生性欲」者，即是五道根性有三乘差別，為下三十子譬作本。
  ```
- **Status:** Closed


### DEFECT-F04-009
- **File name:** Wenju_Fascicle_04_Part1_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 75–84
- **CBETA text (quoted):**
  - 「七、得記不得記者，若同皆領解，何故聲聞得記，不見緣覺、菩薩受記？此亦三意：一者、昔明二乘入正位不能發心，何由得記？今既悟大，欣斯別決，故為記劫國也。」
- **Translation excerpt:**
  - “This also has **three meanings**: 1. **The Surprise Factor:** …”
- **Defect type:** Addition (interpretive label not in source)
- **Required correction:**
  - Remove the editorial label “The Surprise Factor” and render 「一者」 with a neutral ordinal (e.g., “First,” / “First meaning:”).
- **Post‑edit excerpt (Wenju_Fascicle_04_Part1_Scholarly.md):**
  ```
  This also has **three meanings**:
  1.  **First:** Formerly, it was explained that Two Vehicles entering the **Correct Position** (*zhèng wèi*) could not generate the [Bodhi] Mind.
  ```
- **Status:** Closed


### DEFECT-F04-010
- **File name:** Wenju_Fascicle_04_Part1_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 110–114
- **CBETA text (quoted):**
  - 「問：身子初周為四眾三根請，譬周為中下請，云何言佛各為三根人三周說法耶？」
- **Translation excerpt:**
  - “Why then do we say the Buddha speaks Dharma in Three Weeks, each for the people of the Three Roots? **If the request was specific, why is the response general?**”
- **Defect type:** Addition (non‑source sentence)
- **Required correction:**
  - Remove the added sentence “If the request was specific, why is the response general?”
- **Post‑edit excerpt (Wenju_Fascicle_04_Part1_Scholarly.md):**
  ```
  **Question:** In the First Week, Śāriputra requested on behalf of the Three Roots of the Four Assemblies. In the Parable Week, he requested for the Intermediate and Inferior [Roots].
  Why then do we say the Buddha speaks Dharma in Three Weeks, each for the people of the Three Roots?
  ```
- **Status:** Closed


### DEFECT-F04-011
- **File name:** Wenju_Fascicle_04_Part1_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 118–122
- **CBETA text (quoted):**
  - 「答：經無文，義推應爾。引三歸一，三望一，一則是當；舉事為譬，譬即是現。準後望前，應如所問。」
- **Translation excerpt:**
  - “Measuring the Back (Future) and looking at the Front (Past), it should be as you asked. **[Thus: Past = Causes/Conditions, Present = Parable, Future = Dharma/One Vehicle Result].**”
- **Defect type:** Addition (editorial summary not in source)
- **Required correction:**
  - Remove the bracketed summary sentence and keep a literal rendering of the source line.
- **Post‑edit excerpt (Wenju_Fascicle_04_Part1_Scholarly.md):**
  ```
  Guiding the Three to return to the One: The Three look toward the One; the One is the **Future**.
  Raising affairs to make a Parable: The Parable is the **Present**.
  Measuring the Back (Future) and looking at the Front (Past), it should be as you asked.
  ```
- **Status:** Closed


### DEFECT-F04-012
- **File name:** Wenju_Fascicle_04_Part2_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 240–241
- **CBETA text (quoted):**
  - 「…如水奔昏風波鼓努魚龍攪撓，無一憀賴時使之然。」
- **Translation excerpt:**
  - English block ends after “the Multitude of Corruptions gather together (*jiāocòu*).” (no rendering for 「無一憀賴時使之然」)
- **Defect type:** Omission (untranslated clause)
- **Required correction:**
  - Add a translation for 「無一憀賴時使之然」 after the existing English sentence.
- **Post‑edit excerpt (Wenju_Fascicle_04_Part2_Scholarly.md):**
  ```
  Coarse and vile Form and Mind, evil names and filthy designations, destroying years and reducing lifespan—the Multitude of Corruptions gather together (*jiāocòu*).
  There is not a single moment of respite; time makes it so.
  ```
- **Status:** Closed


### DEFECT-F04-013
- **File name:** Wenju_Fascicle_04_Part2_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 299–331
- **CBETA text (quoted):**
  - 「故文云：「喜稱南無佛」。」
- **Translation excerpt:**
  - “Therefore the text says: **‘Joyfully称 “Namo Buddha.”’**”
- **Defect type:** Translation error (untranslated character)
- **Required correction:**
  - Replace the mixed Chinese character with an English verb (e.g., “Joyfully say/call ‘Namo Buddha.’”).
- **Post‑edit excerpt (Wenju_Fascicle_04_Part2_Scholarly.md):**
  ```
  …therefore the text says: “Joyfully say ‘Namo Buddha.’”
  ```
- **Status:** Closed


### DEFECT-F04-014
- **File name:** Wenju_Fascicle_04_Part1_Scholarly.md
- **Fascicle:** 4
- **CBETA source file:** T1718_004.txt
- **CBETA line numbers:** 87
- **CBETA text (quoted):**
  - 「…名不待時。何故爾？佛有顯密二說，若顯說為論，《法華》之前二乘未悟大道…」
- **Translation excerpt:**
  - 「…名不待時。何故爾？佛有顯密二說。」 (full stop used instead of CBETA comma)
- **Defect type:** Punctuation mismatch (CBETA comma)
- **Required correction:**
  - Change the punctuation after 「佛有顯密二說」 to a comma to match CBETA.
- **Post‑edit excerpt (Wenju_Fascicle_04_Part1_Scholarly.md):**
  ```
  十、明待時不待時，爾前不悟必待《法華》悟者，名為待時；《法華》前教已解者，名不待時。何故爾？佛有顯密二說，
  ```
- **Status:** Closed


### DEFECT-F05-001
- **File name:** Wenju_Fascicle_05_FULL_Scholarly.md
- **Fascicle:** 5
- **CBETA source file:** T1718_005.txt
- **CBETA line numbers:** 55
- **CBETA text (quoted):**
  - 「咸以恭敬心，皆來至我所」者，一云：「耻小慕大，大機感佛故云至佛所。」今明非但機至佛所，亦乃身到，如無量義中四眾圍繞，合掌敬心，欲聞具足道也。「曾從諸佛聞，方便所說法」者，此中初味調伏，受行三藏、六度，通、別等三教方便，由此調熟故，使障除機發而求大也。從「我即作是念」下，二行一句，明障除佛喜。佛為佛慧故出，昔障重無機，不得即說佛慧；中間雖障除又未得說；今機發正是說時。昔眾生根鈍智小，恐其謗法墮惡，故未是說時；今根利志大，聞必信解故佛歡喜。「無畏」者，不畏執小謗大起罪墮惡，故言無畏。「於菩薩中」下三句，正顯實也。五乘是曲而非直，通別偏傍而非正，今皆捨彼偏曲，但說正直一道也。「菩薩聞是法」下一行，明受行悟入，六度通二菩薩，初聞略說，動舊執致新疑，今悉已除；非獨菩薩，二乘亦爾。而云「聲聞皆當作佛」者，昔教不說二乘作佛，今行與授記，授記豈獨二乘？除疑豈獨菩薩？互存則兩備。
- **Translation excerpt:**
  - Paragraph missing between the Q/A on “seeking one” and the “Resolving the Bodhisattva’s Doubt” heading.
- **Defect type:** Omission (missing CBETA paragraph)
- **Required correction:**
  - Insert the full CBETA paragraph with bilingual translation immediately after the “昔出宅索三…” Q/A block.
- **Post‑edit excerpt (Wenju_Fascicle_05_FULL_Scholarly.md):**
  ```
  「咸以恭敬心，皆來至我所」者，一云：「耻小慕大，大機感佛故云至佛所。」…
  As for “All with respectful minds, all came to my place,” one says: “Ashamed of the small and admiring the great, their great capacity moved the Buddha…”
  ```
- **Status:** Closed


### DEFECT-F05-002
- **File name:** Wenju_Fascicle_05_FULL_Scholarly.md
- **Fascicle:** 5
- **CBETA source file:** T1718_005.txt
- **CBETA line numbers:** 141–145
- **CBETA text (quoted):**
  - 「爾時佛告舍利」下，第二，佛答，文為三：一、發起；二、譬喻；三、勸信。
  - 發起為二：一抑、二引，抑令憤勇，引令速進。「我先不言」下，指上明權皆為菩提，指上顯實皆為化菩薩者，若權若實，皆入佛道無住涅槃，上已明言，云何執教迷闇不解，如此責謂是抑文也。「然舍利弗今當」下，[2]是引接安慰。前斥既切，恐鄙懟自沈，今許其譬喻更明此義，若能解者猶稱智也。
  - [2] 是引【大】，引是【甲】
- **Translation excerpt:**
  - The “佛答/發起” paragraph and its [2] marker/apparatus line were absent before the parable section.
- **Defect type:** Omission / Variant missing
- **Required correction:**
  - Insert the missing paragraph, restore the [2] marker, and add the critical‑apparatus line for [2].
- **Post‑edit excerpt (Wenju_Fascicle_05_FULL_Scholarly.md):**
  ```
  「爾時佛告舍利」下，第二，佛答，文為三：一、發起；二、譬喻；三、勸信。
  發起為二：…「然舍利弗今當」下，[2]是引接安慰。…
  *[Critical apparatus: [2] 是引【大】，引是【甲】]*
  ```
- **Status:** Closed


### DEFECT-F05-003
- **File name:** Wenju_Fascicle_05_FULL_Scholarly.md
- **Fascicle:** 5
- **CBETA source file:** T1718_005.txt
- **CBETA line numbers:** 122–124
- **CBETA text (quoted):**
  - 從「汝於未來」下，是大段第四，授記段。前自陳佛印竟，是故與記，若得大解自知得佛，何俟須記？記有四意：一、昔未記二乘而今須記；二、中下未悟，以記勉勵之；三、令聞者結緣；四、滿其本願，是故記也。…「宜應自欣慶」者，成初入歡喜位之解也，初住能百佛世界作佛，行地倍是。
  - 第五，四眾領解，有長行、偈頌。初經家敘眾喜；次陳供養。「作是言」下，正領解。初領開權，今乃復轉下，領顯實也。偈有六行半，為二：初二行，頌上開權顯實；後四行半，自述得解隨喜迴向也。「我等亦如是」者，如身子之領解，如身子被述成，如身子之得記也。
- **Translation excerpt:**
  - The prediction section and the four‑assemblies understanding paragraph were missing before the Q&A section.
- **Defect type:** Omission (missing CBETA paragraphs)
- **Required correction:**
  - Insert both paragraphs with bilingual translation before the “Q&A: Why Shariputra First?” section.
- **Post‑edit excerpt (Wenju_Fascicle_05_FULL_Scholarly.md):**
  ```
  從「汝於未來」下，是大段第四，授記段。…
  第五，四眾領解，有長行、偈頌。…
  ```
- **Status:** Closed


### DEFECT-F05-004
- **File name:** Wenju_Fascicle_05_FULL_Scholarly.md
- **Fascicle:** 5
- **CBETA source file:** T1718_005.txt
- **CBETA locator:** T1718_005.txt apparatus entries (all)
- **CBETA apparatus (verbatim):**
  - [7] 不分卷【甲】
  - [1] 益【大】，蓋【甲】
  - [2] 秖【大】＊，只【甲】＊
  - [3] 變【大】，反【甲】
  - [4] 七【大】，七日【甲】
  - [5] 行【大】，行悟入【甲】
  - [6] 導【大】，道【甲】
  - [1] 習習【大】，集集【甲】
  - [1] 行【大】，一行【甲】
  - [2] 揀【大】＊，簡【甲】＊
  - [＊2-1] 揀【大】＊，簡【甲】＊
  - [＊2-2] 揀【大】＊，簡【甲】＊
  - [＊2-3] 揀【大】＊，簡【甲】＊
  - [＊2-4] 揀【大】＊，簡【甲】＊
  - [＊2-5] 揀【大】＊，簡【甲】＊
  - [3] 法華經文句卷第四終【甲】，法隆寺本奧書云康治元年壬戌八月十八日奉寫已了南都法隆寺五師大法師覺印之一校了（朱書）同二年癸亥六月五日移點已了為令法久住往生極樂也覺印
  - [4] 法華文句卷第五首【甲】
  - [5] 遣【大】，達【甲】
  - [1] 又【大】，又云【甲】
  - [2] 圓【大】，員【甲】
  - [3] （二初…三）十一字【大】，三名身喜聞此法音依於佛口聞而歡喜故【甲】
  - [4] 二【大】，次【甲】
  - [＊2-1] 秖【大】＊，只【甲】＊
  - [5] 甞【大】，常【甲】
  - [6] 知見【大】，見知【甲】
  - [7] 實權【大】，權實【甲】
  - [1] 得【大】，待【甲】
  - [2] 願即【大】，〔－〕【甲】
  - [1] 輩【大】＊，背【甲】＊
  - [＊1-1] 輩【大】＊，背【甲】＊
  - [2] 是引【大】，引是【甲】
  - [3] 中【大】，〔－〕【甲】
  - [4] 儀【大】，議【甲】
  - [5] 贍【大】，瞻【甲】
  - [1] 統【大】，繞【甲】
  - [2] 車門【大】，門車【甲】
  - [3] 頹【大】＊，隤【甲】＊
  - [＊3-1] 頹【大】＊，隤【甲】＊
  - [4] 不分卷【甲】
  - [5] 不分卷【甲】
  - [6] 名【大】，為【甲】
  - [1] 秖【大】＊，只【甲】＊
  - [1] 設權【大】，權設【甲】
  - [2] 第【大】，〔－〕【甲】
  - [1] 說【大】，因緣【甲】
  - [2] 機【大】，〔－〕【甲】
  - [3] 豈【大】，蚩【甲】
  - [4] 聞【大】，見【甲】
  - [1] 酥【大】＊，蘇【甲】＊
  - [＊1-1] 酥【大】＊，蘇【甲】＊
  - [＊1-1] 秖【大】＊，只【甲】＊
  - [2] 師【大】，〔－〕【甲】
  - [3] 車【大】，〔－〕【甲】
  - [4] 者【大】，者小果者【甲】
  - [5] 矛盾【大】，鉾楯【甲】
  - [6] 人【大】，有【甲】
  - [7] 授【大】，受【甲】
  - [1] 救【大】，拔【甲】
  - [1] 外德【大】，〔－〕【甲】
  - [2] 力【大】，力者【甲】
  - [3] 也【大】＊，〔－〕【甲】＊
  - [4] 已【大】，〔－〕【甲】
  - [5] 者【大】，〔－〕【甲】
  - [6] 所【大】，〔－〕【甲】
  - [＊3-1] 也【大】＊，〔－〕【甲】＊
  - [＊3-2] 也【大】＊，〔－〕【甲】＊
  - [A1] 繫【CB】，繁【大】
  - [1] 推【大】，惟【甲】
  - [2] 不分卷【甲】
- **Translation excerpt:**
  - Apparatus appeared as standalone bilingual “Variant:” rows; no critical‑apparatus lines were present.
- **Defect type:** Variant missing / Apparatus format
- **Required correction:**
  - Remove apparatus‑only rows and insert critical‑apparatus lines in the scholarly format after each relevant block.
- **Post‑edit excerpt (Wenju_Fascicle_05_FULL_Scholarly.md):**
  ```
  *[Critical apparatus: [7] 不分卷【甲】]*
  ```
- **Status:** Closed


### DEFECT-F05-005
- **File name:** Wenju_Fascicle_05_FULL_Scholarly.md
- **Fascicle:** 5
- **CBETA source file:** T1718_005.txt
- **CBETA line numbers:** 94
- **CBETA text (quoted):**
  - 「…是故歡喜，此對治釋也。[1]又佛子所應得者皆已得之…」
  - [1] 又【大】，又云【甲】
- **Translation excerpt:**
  - “此對治釋也” lacked the [1] marker and no critical‑apparatus line appeared.
- **Defect type:** Marker omission / Variant missing
- **Required correction:**
  - Restore [1] in the Chinese line and insert the critical‑apparatus line for [1].
- **Post‑edit excerpt (Wenju_Fascicle_05_FULL_Scholarly.md):**
  ```
  …是故歡喜，此對治釋也。[1]
  *[Critical apparatus: [1] 又【大】，又云【甲】]*
  ```
- **Status:** Closed


### DEFECT-F06-001
- **File name:** Wenju_Fascicle_06_Part2_Scholarly.md
- **Fascicle:** 6 (Lower)
- **CBETA source file:** T1718_006.txt
- **CBETA line numbers:** 224
- **CBETA text (quoted):**
  - 「從「父遙見之」，即是第三，放捨勸誡息大乘化。」
- **Translation excerpt:**
  - 「從「父遙見」下，即是第三，放捨勸誡息大乘化。」
- **Defect type:** Omission (single character in quoted line)
- **Required correction:**
  - Restore 「之」 inside the quoted phrase to match CBETA: 「父遙見之」.
- **Post‑edit excerpt (Wenju_Fascicle_06_Part2_Scholarly.md):**
  ```
  從「父遙見之」，即是第三，放捨勸誡息大乘化。
  ```
- **Status:** Closed


### DEFECT-F06-002
- **File name:** Wenju_Fascicle_06_Part2_Scholarly.md
- **Fascicle:** 6 (Lower)
- **CBETA source file:** T1718_006.txt
- **CBETA line numbers:** 241
- **CBETA text (quoted):**
  - 「「語諸作人」下，第四，親教子作譬也，即是道品中七科法門，以顯除糞之相，領上諸子心各勇銳互相推排競共馳走爭出火宅也。一者語作人譬，譬四念處是外凡位；二、令勤作勿得懈息譬，譬四正勤；三、「咄男子」，勿復餘去譬，譬四如意足；四、「好自安意」下，名安慰譬，譬五根；五、「所以者何」下，名無五過譬，譬五力。此前四句是第二內凡位。六、即時長者字以為子譬，譬八正。七、「雖欣此遇」下，名教常令除糞譬，譬七覺。此二句是第三聖位也。」
- **Translation excerpt:**
  - The Chinese source moves from 「狀有所畏」… to the next section header and begins at 「今初語諸作人者…」 without the 「語諸作人」 summary line and the seven‑item list.
- **Defect type:** Omission (missing CBETA block)
- **Required correction:**
  - Insert the missing 「語諸作人」 line and its seven‑item list (with bilingual translation) between the sentence ending 「狀有所畏…」 and the subsequent 「今初語諸作人者…」 block.
- **Post‑edit excerpt (Wenju_Fascicle_06_Part2_Scholarly.md):**
  ```
  「語諸作人」下，第四，親教子作譬也，即是道品中七科法門，以顯除糞之相，領上諸子心各勇銳互相推排競共馳走爭出火宅也。一者語作人譬，譬四念處是外凡位；二、令勤作勿得懈息譬，譬四正勤；三、「咄男子」，勿復餘去譬，譬四如意足；四、「好自安意」下，名安慰譬，譬五根；五、「所以者何」下，名無五過譬，譬五力。此前四句是第二內凡位。六、即時長者字以為子譬，譬八正。七、「雖欣此遇」下，名教常令除糞譬，譬七覺。此二句是第三聖位也。
  ```
- **Status:** Closed


### DEFECT-F07-001
- **File name:** Wenju_Fascicle_07_Part2_Scholarly.md
- **Fascicle:** 7 (Lower)
- **CBETA source file:** T1718_007.txt
- **CBETA line numbers:** 213–240 (approx.)
- **CBETA locator:** T1718_007.txt 「將導眾人」…「汝證一切智十力等佛法」
- **Chinese text (quoted):**
  - 「將導眾人」下，是第二，將導譬…「若入是城快得安[1]樂」…「但作[2]二乘亦好」…「適[3]子願勇銳推排出宅」…
- **Translation excerpt:**
  - The entire **Leading/Conducting Parable** analysis block (and its doctrinal mapping) was missing in English.
- **Defect type:** Omission
- **Required correction:**
  - Insert the full CBETA block beginning at 「將導眾人」 through the end of the parable/doctrinal mapping, with a complete bilingual translation and its apparatus notes.
- **Post‑edit excerpt (Wenju_Fascicle_07_Part2_Scholarly.md):**
  ```
  「將導眾人」下，是第二，將導譬…「若入是城快得安[1]樂」…「但作[2]二乘亦好」…「適[3]子願勇銳推排出宅」…
  *[Critical apparatus: [1] 樂【大】，隱【甲】; [2] 二【大】，三【甲】; [3] 子【大】，〔－〕【甲】]*
  ```
- **Status:** Closed

### DEFECT-F07-002
- **File name:** Wenju_Fascicle_07_Part2_Scholarly.md
- **Fascicle:** 7 (Lower)
- **CBETA source file:** T1718_007.txt
- **CBETA line numbers:** 241–260 (approx.)
- **CBETA locator:** T1718_007.txt 「爾時導師知此」…「[5]我令脫苦縛逮得涅槃」
- **Chinese text (quoted):**
  - 「爾時導師知此」下，第三，滅化引至寶所…「唯佛與佛乃能究[4]竟諸法實相」…
  - 「寶處在近，向者大城我所化作」…「[5]我令脫苦縛逮得涅槃」…
- **Translation excerpt:**
  - The entire extinguish‑magic/treasure‑place analysis was missing in English.
- **Defect type:** Omission
- **Required correction:**
  - Insert the missing CBETA paragraphs with full bilingual translation and apparatus notes [4] and [5].
- **Post‑edit excerpt (Wenju_Fascicle_07_Part2_Scholarly.md):**
  ```
  「爾時導師知此」下…「唯佛與佛乃能究[4]竟諸法實相」…
  「寶處在近，向者大城我所化作」…「[5]我令脫苦縛逮得涅槃」…
  *[Critical apparatus: [4] 竟【大】，盡【甲】; [5] 我【大】，〔－〕【甲】]*
  ```
- **Status:** Closed

### DEFECT-F07-003
- **File name:** Wenju_Fascicle_07_Part2_Scholarly.md
- **Fascicle:** 7 (Lower)
- **CBETA source file:** T1718_007.txt
- **CBETA line numbers:** 261–293 (approx.)
- **CBETA locator:** T1718_007.txt 「時十六王子」…「諸佛之導師」
- **Chinese text (quoted):**
  - 「時十六王子」下，五行半…[2]頌二萬劫中間說方等《般若》…
  - 「是諸沙彌[3]等」下，二十七行…「見諸求[12]道者」…
- **Translation excerpt:**
  - The entire gāthā‑analysis sub‑blocks for the “sixteen princes” and “sramaneras” verses were missing, along with their apparatus lines.
- **Defect type:** Omission
- **Required correction:**
  - Insert the two missing gāthā‑analysis paragraphs with full bilingual translation and the apparatus lines [1], [2], [3]–[12].
- **Post‑edit excerpt (Wenju_Fascicle_07_Part2_Scholarly.md):**
  ```
  *[Critical apparatus: [1] 時【大】，〔－〕【甲】]*
  「時十六王子」下…
  *[Critical apparatus: [2] 頌【大】，頌第四【甲】]*
  「是諸沙彌[3]等」下…「見諸求[12]道者」…
  *[Critical apparatus: [3] 等【大】，〔－〕【甲】; [4] 次【大】，〔－〕【甲】; [5] 後【大】，〔－〕【甲】; [6] 三【大】，一【甲】; [7] 日【大】，日還【甲】; [8] 文【大】，文有【甲】; [9] 二【大】，兩【甲】; [10] 直【大】，真【甲】; [11] 第四【大】，〔－〕【甲】; [12] 道【大】，導【甲】]*
  ```
- **Status:** Closed

### DEFECT-F07-004
- **File name:** Wenju_Fascicle_07_Part2_Scholarly.md
- **Fascicle:** 7 (Lower)
- **CBETA source file:** T1718_007.txt
- **CBETA line numbers:** [1], [2], [A2], [3]
- **CBETA locator:** T1718_007.txt [1] 詮 / [2] 秖 / [A2] 昔 / [3] 譬 / [1] 也 / [2] 本 / [3] 次頁[01]
- **CBETA apparatus (verbatim):**
  - [1] 詮【大】，論【甲】
  - [2] 秖【大】，只【甲】
  - [A2] 昔【CB】，音【大】
  - [3] 譬【大】，喻【甲】
  - [1] 也【大】，〔－〕【甲】
  - [2] 本【大】＊，〔－〕【甲】＊
  - [3] 次頁[01]不分卷【甲】
- **Translation excerpt:**
  - Multiple apparatus lines were missing in the Magic‑City Q/A, Five‑Places analysis, and prediction sections.
- **Defect type:** Variant missing
- **Required correction:**
  - Insert the missing apparatus lines at each respective location.
- **Post‑edit excerpt (Wenju_Fascicle_07_Part2_Scholarly.md):**
  ```
  *[Critical apparatus: [1] 詮【大】，論【甲】; [2] 秖【大】，只【甲】]*
  *[Critical apparatus: [A2] 昔【CB】，音【大】; [3] 譬【大】，喻【甲】]*
  *[Critical apparatus: [1] 也【大】，〔－〕【甲】]*
  *[Critical apparatus: [2] 本【大】＊，〔－〕【甲】＊]*
  *[Critical apparatus: [3] 次頁[01]不分卷【甲】]*
  ```
- **Status:** Closed

### DEFECT-F07-005
- **File name:** Wenju_Fascicle_07_Part1_Scholarly.md
- **Fascicle:** 7 (Upper)
- **CBETA source file:** T1718_007.txt
- **CBETA line numbers:** 48–50 (approx.)
- **CBETA locator:** T1718_007.txt 「迦葉當知如來」…「第一，合密雲」…「於大眾中而唱」
- **Chinese text (quoted):**
  - 「迦葉當知如來」下，合譬也…合譬次第者…得潤是同不無差別增長(云云)。
  - 第一，合密雲…五陰合上山川谿谷也。「於大眾中而唱」下，即是第二，合上第四注雨譬…
- **Translation excerpt:**
  - The file places **「第一，合密雲」** before **「迦葉當知如來」**, then resumes with **「於大眾中而唱」**, breaking CBETA order.
- **Defect type:** Misordering (sequence error)
- **Required correction:**
  - Move the **「迦葉當知如來」下，合譬也…** block to precede **「第一，合密雲…」**, restoring CBETA sequence so **「合密雲」** flows into **「於大眾中而唱」**.
- **Post‑edit excerpt (Wenju_Fascicle_07_Part1_Scholarly.md):**
  ```
  「迦葉當知如來」下，合譬也…得潤是同不無差別增長(云云)。
  第一，合密雲…五陰合上山川谿谷也。「於大眾中而唱」下，即是第二，合上第四注雨譬…
  ```
- **Status:** Closed

### DEFECT-F07-006
- **File name:** Wenju_Fascicle_07_Part1_Scholarly.md
- **Fascicle:** 7 (Upper)
- **CBETA source file:** T1718_007.txt
- **CBETA line numbers:** 59 (approx.)
- **CBETA locator:** T1718_007.txt 「五乘者」…「隨緣不同耳」
- **Chinese text (quoted):**
  - 「五乘者，五戒乘出三途苦，十善乘出人道八苦，聲聞乘出三界無常苦，緣覺乘出從他聞法苦，菩薩乘出內無利智外無相好苦，是為五乘。問：但應以人天為世間乘，餘是出世間乘。又佛為實乘，餘是權乘。又佛為果乘，餘是因乘。又應為三乘，人天為下、二乘為中、佛為上。又人天名不斷煩惱乘，二乘名斷煩惱乘，佛名非斷非不斷乘。又人天名不斷，佛名斷，二乘名亦斷亦不斷。又凡夫、賢聖、非凡非聖，有、空、非有非空等乘(云云)。《大論》明五善根，《勝鬘》辨四藏，與三草二木云何？人天為二善，二乘為一，佛菩薩為五，開大合小，五乘開小合大，四藏合凡開聖，五乘則凡聖俱開，隨緣不同耳。」
- **Translation excerpt:**
  - The Chinese source jumps from 「任力所堪漸得入道，即後世以道受樂。」 directly to 「如彼大雲」 without the **五乘** paragraph.
- **Defect type:** Omission (missing CBETA block)
- **Required correction:**
  - Insert the missing **「五乘者…隨緣不同耳」** block with full bilingual translation between 「即後世以道受樂。」 and 「如彼大雲」.
- **Post‑edit excerpt (Wenju_Fascicle_07_Part1_Scholarly.md):**
  ```
  「任力所堪漸得入道」，即後世以道受樂。
  五乘者，五戒乘出三途苦…五乘則凡聖俱開，隨緣不同耳。
  「如彼大雲」下，第二，提譬帖合六意者…
  ```
- **Status:** Closed

### DEFECT-F07-007
- **File name:** Wenju_Fascicle_07_Part1_Scholarly.md
- **Fascicle:** 7 (Upper)
- **CBETA source file:** T1718_007.txt
- **CBETA line numbers:** 66 (approx.)
- **CBETA locator:** T1718_007.txt 「地雖無差別，而能生桃梅卉木差別等異」
- **Chinese text (quoted):**
  - 「地雖無差別，而能生桃梅卉木差別等異；桃[1]李卉木雖差，而同是一堅相。」
- **Translation excerpt:**
  - 「地雖無差別，而能生桃梅卉木差別等異；桃[1]李卉木雖差，而同是一堅相。」
- **Defect type:** Omission (missing character)
- **Required correction:**
  - Restore **「梅」** so the phrase reads **「桃梅卉木差別等異」**, and align the **[1]** marker to **「桃[1]李」** per CBETA.
- **Post‑edit excerpt (Wenju_Fascicle_07_Part1_Scholarly.md):**
  ```
  地雖無差別，而能生桃梅卉木差別等異；桃[1]李卉木雖差，而同是一堅相。
  ```
- **Status:** Closed

### DEFECT-F07-008
- **File name:** Wenju_Fascicle_07_Part1_Scholarly.md
- **Fascicle:** 7 (Upper)
- **CBETA source file:** T1718_007.txt
- **CBETA line numbers:** 80 (approx.)
- **CBETA locator:** T1718_007.txt 「究竟涅槃終歸於空」
- **Chinese text (quoted):**
  - 「究竟涅槃終歸於空」，即是無量中一。
- **Translation excerpt:**
  - 「究竟涅槃終歸於空」，即是無量中一。
- **Defect type:** Omission (missing character)
- **Required correction:**
  - Restore **「於」** so it reads **「究竟涅槃終歸於空」**, and move **[1]** to **「終歸[1]空」** per CBETA.
- **Post‑edit excerpt (Wenju_Fascicle_07_Part1_Scholarly.md):**
  ```
  「究竟涅槃終歸於空」，即是無量中一。
  …壽盡終歸灰斷，故言終歸[1]空。
  ```
- **Status:** Closed

### DEFECT-F07-009
- **File name:** Wenju_Fascicle_07_Part1_Scholarly.md
- **Fascicle:** 7 (Upper)
- **CBETA source file:** T1718_007.txt
- **CBETA line numbers:** 66 (approx.)
- **CBETA locator:** T1718_007.txt 「究竟至於一切種智」者…
- **Chinese text (quoted):**
  - 「究竟至於一切種智」者，若得二邊滅相，即是通、別二惑盡，入佛知見，以一切種智心中行般若，初發、畢竟二不別，故言「究竟」，此即佛之智慧，故言「一切種智」也。
- **Translation excerpt:**
  - The explanatory sentence beginning **「究竟至於一切種智」者…** was missing after 「準一相可解。」.
- **Defect type:** Omission (missing CBETA sentence)
- **Required correction:**
  - Insert the missing sentence with full bilingual translation immediately after 「準一相可解。」.
- **Post‑edit excerpt (Wenju_Fascicle_07_Part1_Scholarly.md):**
  ```
  句句例作[2]差無差別義，準一相可解。「究竟至於一切種智」者，若得二邊滅相，即是通、別二惑盡，入佛知見，以一切種智心中行般若，初發、畢竟二不別，故言「究竟」，此即佛之智慧，故言「一切種智」也。
  ```
- **Status:** Closed


### DEFECT-F07-010
- **File name:** Wenju_Fascicle_07_Part2_Scholarly.md
- **Fascicle:** 7 (Lower)
- **CBETA source file:** T1718_007.txt
- **CBETA line numbers:** 221–235 (approx.)
- **CBETA locator:** T1718_007.txt 「又明二乘，六義同、十義別」…「佛道雖長如萬里行，但五百是難、餘者則易」
- **Chinese text (quoted):**
  - 「又明二乘，六義同、十義別，同出三界、同盡無生…同名小乘，所以合為一化城。」
  - 「別開十義：行因久近…聲聞不定。」
  - 「火宅三車今為二百…佛道雖長如萬里行，但五百是難、餘者則易。」
- **Translation excerpt:**
  - The Six-Shared-Meanings / Ten-Differences analysis and the Fire-House/Three-Carts-as-200 explanation were missing in English.
- **Defect type:** Omission (missing doctrinal analysis block)
- **Required correction:**
  - Insert the full bilingual translation of the "Six Shared Meanings / Ten Differences" block and the subsequent Fire-House/Three-Carts discussion before "Zhiyi's Determination."
- **Post‑edit excerpt (Wenju_Fascicle_07_Part2_Scholarly.md):**
  ```
  **Two Vehicles: Six Shared Meanings, Ten Differences:**
  Shared six: both exit the Three Realms… therefore they are combined as one Magic City.
  Ten differences:
  1. Length of causal practice (60 kalpas vs 100).
  …
  Fire-House three carts are now 200… the 500 are the difficulty; the rest are easy.
  ```
- **Status:** Closed

### DEFECT-F07-011
- **File name:** Wenju_Fascicle_07_Part2_Scholarly.md
- **Fascicle:** 7 (Lower)
- **CBETA source file:** T1718_007.txt
- **CBETA line numbers:** 235–238 (approx.)
- **CBETA locator:** T1718_007.txt 「問：二百是二乘難…《大論》六十六云」…「若過五百即入佛道」
- **Chinese text (quoted):**
  - 「問：二百是二乘難…既求車出，何不為二百所障(云云)？」
  - 「《大論》六十六云「險道是世間，一百由旬是欲界…四百是二乘。」…此經明五百由旬即菩薩道，若過五百即入佛道(云云)。」
- **Translation excerpt:**
  - The Q&A and Great Treatise (fascicle 66) citation were missing from the English block.
- **Defect type:** Omission (missing Q&A + citation)
- **Required correction:**
  - Insert the Q&A and the Great Treatise citation (fasc. 66) with full bilingual translation before "Zhiyi's Determination."
- **Post‑edit excerpt (Wenju_Fascicle_07_Part2_Scholarly.md):**
  ```
  **Q&A on the 200 Yojanas (Great Treatise, Fascicle 66):**
  **Q:** If 200 is the Two-Vehicle difficulty… why are they not obstructed by the 200? (etc.)
  **A:** The *Great Treatise* (*Da Lun*) fascicle 66 says: the perilous road is the world; 100 yojanas = Desire Realm… This sutra clarifies that 500 yojanas are the bodhisattva path; passing beyond 500 one enters the Buddha path. (etc.)
  ```
- **Status:** Closed


### DEFECT-F09-001
- **File name:** Wenju_Fascicle_09_FULL_Scholarly.md
- **Fascicle:** 9
- **CBETA source file:** T1718_009.txt
- **CBETA line numbers:** [6]
- **CBETA locator:** T1718_009.txt [6]
- **CBETA apparatus (verbatim):**
  - [6] 法華文句卷第八終【甲】，法隆寺本奧書云康治元年壬戌六月三十日寫之法隆寺僧覺印一校了（朱書）康治二年六月二十八日移點已了
- **Translation excerpt:**
  - Apparatus line present only in a nonstandard label (“Critical apparatus (A-text colophon)”), missing the CBETA [6] locator.
- **Defect type:** Variant missing / apparatus format
- **Required correction:**
  - Replace the nonstandard line with a standard critical‑apparatus line including the [6] locator.
- **Post‑edit excerpt (Wenju_Fascicle_09_FULL_Scholarly.md):**
  ```
  *[Critical apparatus: [6] 法華文句卷第八終【甲】，法隆寺本奧書云康治元年壬戌六月三十日寫之法隆寺僧覺印一校了（朱書）康治二年六月二十八日移點已了]*
  ```
- **Status:** Closed


### DEFECT-F08-001
- **File name:** Wenju_Fascicle_08_Part1_Scholarly.md
- **Fascicle:** 8
- **CBETA source file:** T1718_008.txt
- **CBETA line numbers:** 1–186 (Upper Roll)
- **CBETA locator:** T1718_008.txt (卷第八上) from 「妙法蓮華經文句[A1]卷第八上」 through the upper‑roll closing line 「妙法蓮華經文句卷第八上」
- **Chinese text (quoted):**
  - 「妙法蓮華經文句[A1]卷第八上」
  - 「[1]「漸漸具足菩薩」下，第二，授記。文為七：一、明因圓…」
  - 「釋法師品」
  - 「妙法蓮華經文句卷第八上」
- **CBETA apparatus (verbatim):**
  - [A1] 卷【CB】，［－］【大】
  - [1] 前頁[03]不分卷【甲】
  - [2] 是【大】，知【甲】
  - [3] 別分【大】，分別【甲】
  - [4] 也【大】，〔－〕【甲】
  - [5] 淫【大】，婬【甲】
  - [6] 記【大】，說【甲】
  - [7] 以【大】，〔－〕【甲】
  - [1] 智【大】，知【甲】
  - [2] 學【大】＊，覺【甲】＊
  - [3] 人【大】，〔－〕【甲】
  - [4] 雲【大】＊，云【甲】＊
  - [＊4-1] 雲【大】＊，云【甲】＊
  - [＊2-1] 學【大】＊，覺【甲】＊
  - [＊2-2] 學【大】＊，覺【甲】＊
  - [5] 法華文句卷第七終【甲】，法隆寺本奧書云□四年十月二日初舟後圓河上之䉼堂勝法寺□□萬壽五年二月十六日□為令法久住書寫了僧琳兌之本法隆寺五師大法師覺印修複之康治元年五月日傳得之
  - [6] 法華文句卷第八首【甲】，但卷題下無天台智者大師七字
  - [1] 以【大】，〔－〕【甲】
  - [2] 亡【大】，忌【甲】
  - [3] 空【大】，坐【甲】
  - [4] 空【大】，空座【甲】
  - [5] 忍【大】，悲【甲】
  - [6] 所【大】，門【甲】
  - [7] 一【大】，而【甲】
  - [8] 覓【大】，觀【甲】
  - [9] 美【大】，善美【甲】
  - [10] 語【大】，諸【甲】
  - [11] 揀【大】＊，簡【甲】＊
  - [＊11-1] 揀【大】＊，簡【甲】＊
  - [＊11-2] 揀【大】＊，簡【甲】＊
  - [1] 喜【大】，之【甲】
  - [2] 譚【大】＊，談【甲】＊
  - [＊2-1] 譚【大】＊，談【甲】＊
  - [3] 況【大】，況有人【甲】
  - [4] 於【大】，〔－〕【甲】
  - [5] 種【大】，權【甲】
  - [1] 下【大】，〔－〕【甲】
  - [2] 半【大】，半行【甲】
  - [3] 棲【大】＊，栖【甲】＊
  - [＊3-1] 棲【大】＊，栖【甲】＊
  - [＊11-3] 揀【大】＊，簡【甲】＊
  - [1] 般【大】＊，波【甲】＊
  - [＊1-1] 般【大】＊，波【甲】＊
  - [2] 詺【大】，名【甲】
  - [3] 世【大】，世諸【甲】
  - [4] 算【大】，弄【甲】
  - [5] 實【大】，實真【甲】
  - [6] 物【大】，總【甲】
  - [7] 章【大】，章互【甲】
  - [8] 問【大】，問門【甲】
  - [＊11-4] 揀【大】＊，簡【甲】＊
  - [1] 就【大】，〔－〕【甲】
  - [2] 荷【大】，荷檐【甲】
  - [3] 見【大】，見況見佛【甲】
  - [4] 知【大】，知下【甲】
  - [＊11-5] 揀【大】＊，簡【甲】＊
  - [5] 軌【大】，軌方軌【甲】
  - [6] 不分卷【甲】
- **Translation excerpt:**
  - “## Explanation of the Prophecy for Five Hundred Disciples Chapter”
  - “### 1. Title Explanation”
  - Summary bullet blocks replacing line‑by‑line CBETA translation.
- **Defect type:** Omission (summary/paraphrase)
- **Required correction:**
  - Replace all summary/outline blocks with full CBETA text and line‑by‑line bilingual translation for the entire upper roll.
  - Insert every CBETA apparatus line in the standard scholarly critical‑apparatus format at the correct positions.
  - Preserve the upper‑roll boundary line at the end (“妙法蓮華經文句卷第八上”).
- **Post‑edit excerpt (Wenju_Fascicle_08_Part1_Scholarly.md):**
  ```
  妙法蓮華經文句[A1]卷第八上

  The Words and Phrases of the Lotus Sutra, Fascicle Eight (Upper).

  *[Critical apparatus: [A1] 卷【CB】，［－］【大】]*
  ```
- **Status:** Closed


### DEFECT-F08-002
- **File name:** Wenju_Fascicle_08_Part2_Scholarly.md
- **Fascicle:** 8
- **CBETA source file:** T1718_008.txt
- **CBETA line numbers:** 188–360 (Lower Roll)
- **CBETA locator:** T1718_008.txt (卷第八下) from 「妙法蓮華經文句卷第八下」 through the lower‑roll closing line 「妙法蓮華經文句卷第八下」
- **Chinese text (quoted):**
  - 「妙法蓮華經文句卷第八下」
  - 「[7]釋見寶塔品」
  - 「釋安樂行品」
  - 「妙法蓮華經文句卷第八下」
- **CBETA apparatus (verbatim):**
  - [7] 不分卷【甲】
  - [8] 或【大】，或言【甲】
  - [9] 倚切【大】，荷反【甲】
  - [10] 秖【大】＊，只【甲】＊
  - [1] 涌【大】下同，踊【甲】下同
  - [2] 雲【大】，云【甲】
  - [＊10-1] 秖【大】＊，只【甲】＊
  - [3] 此【大】，是【甲】
  - [4] 般【大】，波【甲】
  - [5] 子【大】，〔－〕【甲】
  - [1] 也【大】，者【甲】
  - [2] 言【大】，〔－〕【甲】
  - [3] 三【大】，三問【甲】
  - [4] 當【大】，當知【甲】
  - [5] 同【大】，〔－〕【甲】
  - [6] 病【大】，病之【甲】
  - [7] 法【大】，〔－〕【甲】
  - [8] 百【大】，百八【甲】
  - [1] 四【大】，〔－〕【甲】
  - [2] 示【大】，亦【甲】
  - [3] 經【大】，縛【甲】
  - [4] 多【大】，〔－〕【甲】
  - [5] 達【大】，達多【甲】
  - [6] 般【大】，波【甲】
  - [7] 伏慳【大】，慳伏【甲】
  - [8] 熟【大】，就【甲】
  - [9] 不【大】，〔－〕【甲】
  - [10] 悔恨【大】，恨悔【甲】
  - [1] 足【大】，足下【甲】
  - [A2] 膞【CB】【北藏-CB】，膊【大】(cf. P159n1654_p0617b09)
  - [2] 相【大】，二相【甲】
  - [3] 拘【大】，物【甲】
  - [4] 如【大】，如文【甲】
  - [1] 歎【大】，讚【甲】
  - [＊10-2] 秖【大】＊，只【甲】＊
  - [2] 然【大】，〔－〕【甲】
  - [3] 煩【大】，繁【甲】
  - [4] 加【大】，知【甲】
  - [5] 抖擻【大】，斗藪【甲】
  - [6] 自既【大】，既自【甲】
  - [7] 茶【大】，荼【甲】
  - [8] 能【大】，〔－〕【甲】
  - [9] 瘳【大】，聊【甲】
  - [10] 不善【大】，惡【甲】
  - [1] 毘【大】，〔－〕【甲】
  - [2] 諸【大】，〔－〕【甲】
  - [3] 慈與【大】，與慈【甲】
  - [1] 先【大】，光【甲】
  - [2] 已【大】，〔－〕【甲】
  - [3] 眾【大】，眾生【甲】
  - [4] 空【大】，室【甲】
  - [5] （初一…二）二十四字【大】，〔－〕【甲】
  - [6] 棲【大】，栖【甲】
  - [7] 也【大】，〔－〕【甲】
  - [8] 窮二【大】，二窮【甲】
  - [1] 心【大】，心亦【甲】
  - [2] 邪【大】，耶【甲】
  - [3] 旃【大】，栴【甲】
  - [4] 不分卷【甲】
- **Translation excerpt:**
  - “## Explanation of the Vision of the Jeweled Stupa Chapter”
  - “### 1. Title Explanation”
  - Summary bullet blocks replacing line‑by‑line CBETA translation.
- **Defect type:** Omission (summary/paraphrase)
- **Required correction:**
  - Replace all summary/outline blocks with full CBETA text and line‑by‑line bilingual translation for the entire lower roll.
  - Insert every CBETA apparatus line in the standard scholarly critical‑apparatus format at the correct positions.
  - Preserve the lower‑roll boundary line at the end (“妙法蓮華經文句卷第八下”).
- **Post‑edit excerpt (Wenju_Fascicle_08_Part2_Scholarly.md):**
  ```
  妙法蓮華經文句卷第八下

  The Words and Phrases of the Lotus Sutra, Fascicle Eight (Lower).

  *[Critical apparatus: [7] 不分卷【甲】]*
  ```
- **Status:** Closed
