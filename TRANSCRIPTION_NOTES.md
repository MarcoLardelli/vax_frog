# Transcription notes for vaxfrog.ops

Source: `VAXfrog-OPS-5_Expertensystem_Marco_Lardelli_1986_Teil_2.pdf` (listing, scan pages 2-45).
OCR with Tesseract, then every page proofread by eye against the scan.
Indentation and comments follow the printout. The `*` banner boxes and the ASCII-art title screen
were re-typed from the scan because the OCR scrambled them.

Checks done on the result:
* parentheses balance, every rule has exactly one `-->`
* every `^attribute` used is declared in the matching `literalize`
* all 165 productions compile in CMU OPS5, and a full forecasting session runs end-to-end
  (see `run_with_cmu_ops5/`)

## Quirks that are in the original printout (kept as-is)
* `sommer/waerme-gewitter`: `(next-group ^rtask prognose )`, so `next-group` has no
  `^rtask` attribute (should be `^gtask`), and the rule can never fire.
* `altocumulus-langsam-ziehend`: RHS sets `^wd` twice; the second was probably meant to be `^ws`.
* `cirrus-wolken-oder-cirrostratus/fallender-druck`: tests `^temperatur`/`^t` twice in one CE.
* `zeit 3` has `^zeit-sym 0`, so the fog question reads "vor 0 Stunden".
* Typos in texts kept: "Milibar", "Spetzielle", "Morgennbel", "RERSTART", "gestelllt".
