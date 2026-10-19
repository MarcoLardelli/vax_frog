# Running VAXfrog on a modern machine

`vaxfrog.ops` (one level up) is the faithful transcription of the 1986 VAX OPS5 listing.
VAX OPS5 is long gone, so this folder lets it run on the public-domain CMU OPS5
interpreter (Common Lisp) under SBCL.

```sh
git clone https://github.com/sharplispers/ops5.git     # interpreter, into ./ops5
python3 xform.py ../vaxfrog.ops test.ops               # make a CMU-compatible copy
sbcl --load load.lisp --eval '(ops::run-vaxfrog "test.ops")'
```

`xform.py` changes only what CMU OPS5 cannot parse; the rules keep their meaning:

* `:` in rule names → `_` (Lisp reads `:` as a package marker)
* `(compute <t> + 1)` inside a condition (allowed in VAX OPS5, not in CMU OPS5) →
  a fresh variable plus a lookup in a small `zz-arith` table appended at the end of the LHS
  (so the element numbers used by `modify`/`remove` don't shift)

`load.lisp` adds the rest of the VAX dialect: `'?'` quoting, `(startup ...)`,
`(disable ...)`, and `//` as integer division.

`drive.py` (needs `pexpect`) plays a full session with sample weather data;
`sample_session.txt` is the transcript of such a run.
