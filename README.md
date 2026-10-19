# vax_frog

## Expert system for weather forecasting from observations in the OPS5 production system language

See my [blog post](https://lardel.li/2024/03/first-encounter-with-ai.html) about this project for details.

Written in [OPS5](https://en.wikipedia.org/wiki/OPS5), a production system computer language to create expert systems.

Unfortunately I have only the printed version left. Therefore PDF only. Sorry.


## Update 19.10.26: Source code extracted by claude Opus 5.5

### Here the comments from claude:


I extracted the full VAXfrog source from Part 2. `vaxfrog.ops` (2,582 lines) is now in your repo folder, and it runs.

**How I checked it**
- **Proofreading:** I OCR'd every page of the listing and compared each one line by line against the scan. That fixed hundreds of misreads, like `;` read as `:` or `j`, `^` read as `*`, `<rc>` read as `<re>`, and `-->` read as random characters. The star banners and the ASCII title logo came out garbled in OCR, so I retyped them from the scan.
- **Structure:** all 165 rules plus the declarations and startup block have balanced parentheses and exactly one `-->` each. Every attribute a rule uses is declared.
- **Running it:** I loaded it into the public-domain CMU OPS5 interpreter and ran a complete forecast. It shows the title screen and asks its questions, then fires 6 prognosis rules (falling pressure, nimbostratus, a follow-up question about morning fog, and so on). After that it prints the forecast in German sentences, the rule explanations and the tables with certainty percentages.

**Running it yourself:** CMU OPS5 can't read a few VAX-specific constructs, mainly arithmetic like `(compute <t> - 1)` inside a rule's conditions. A small converter makes a compatible test copy for the interpreter and leaves `vaxfrog.ops` exactly as printed. The steps are in `run_with_cmu_ops5/README.md`.

**Bugs in the 1986 original, kept as printed**
- The rule `sommer/waerme-gewitter` uses `^rtask` where it should use `^gtask`, so it can never fire.
- One rule sets the cloud-density certainty (`^wd`) twice. The second was probably meant to be wind strength (`^ws`).
- One prompt reads "vor 0 Stunden".

The original spelling quirks ("Milibar", "Spetzielle", …) are also kept. All of this is listed in `TRANSCRIPTION_NOTES.md`.

**Files added to your repo folder:**
- `vaxfrog.ops`
- `TRANSCRIPTION_NOTES.md`
- `run_with_cmu_ops5/` (the converter, the load script, a script that plays a sample session, and a recorded transcript)

They're uncommitted, and I didn't touch your README. I also deleted the temporary `_ocr_tmp` folder. A natural next step would be updating the README line "Unfortunately I have only the printed version left" to point at the new source.
