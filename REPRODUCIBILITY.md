# Reproducibility

Paper 05: AI and the Data Foundation: Provenance Before Verification: Timing, Repair Coverage, and Adoption

Run `python3 reproduce.py` from the repository root after installing `requirements.txt`.
It invokes these original scientific entry points in order:

```sh
python3 code/run_all.py
```

The wrapper stops on the first failed script. Scientific scripts are copied byte-for-byte from the complete research package; only the repository wrappers and documentation are new. Regeneration overwrites generated result tables and figures in the working tree. Retain a clean checkout or use a separate clone when comparing with the supplied outputs.

The current paper's LaTeX and supplied PDF are byte-identical to the checked F1 edition. Equations, proofs and scientific results were not rewritten for GitHub. Earlier internal review correspondence, chat references, editorial QA screenshots, build logs and full nested working archives are excluded. Supplementary scientific material required by the current article or reproduction is retained.

Some historical result metadata describe earlier scientific revisions. Those files are retained as recorded scientific outputs; editorial F1 changed the abstract and presentation. Runtime timestamps, environment metadata and floating-point display details can vary. See exact arithmetic assertions and stated numerical tolerances in each script.

`legacy/Paper_05_R7_Companion.pdf` and its editable sources preserve the earlier companion results referenced in Appendix C. They are supplementary and are distinct from the current paper. `code/field_estimator.py` is an estimator utility for the prospective design; only its synthetic unit check is part of the default suite.

Default Python entry points are the executed reference. Optional R files and unrun real-data estimator interfaces are documented separately and are not presented as executed empirical analyses.
