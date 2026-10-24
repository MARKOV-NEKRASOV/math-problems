# Peer review of `research/attempt-height.md`

**Verdict:** The deductions and their conditional scope are sound. I found no mathematical error or claim of an unconditional Fermat–Catalan proof.

- The cited Stewart–Yu 2001 estimate is reproduced in the abc overview as `log C < K rad(ABC)^(1/3)(log rad(ABC))³`. Crossref confirms the paper's title, authors, journal, DOI, and abstract. I could not inspect the paywalled article text directly, so the exact displayed formulation is corroborated through that secondary source rather than the article itself.
- Substitution is arithmetically correct: `R^(1/3)<C^(41/126)` and `log R≤(41/42)log C`, giving (3). Its right side eventually exceeds `log C` for any fixed positive `K`, so (3) cannot bound `C`.
- The `R>(log C)^(3−δ)` consequence follows for every fixed `δ>0` and sufficiently large `C`: if the reverse inequality held for `0<δ<3`, Stewart–Yu would give `log C=O((log C)^(1−δ/3)(log log C)³)=o(log C)`. For `δ≥3`, the claim is immediate from `R≥2`.
- The fixed-support argument correctly applies the classical two-variable `S`-unit theorem to `A/C+B/C=1`. Pairwise coprimality makes the positive primitive integer triple uniquely recoverable from `A/C`; hence finitely many `S`-unit pairs give finitely many powered-value triples.
- A fixed radical bound indeed limits prime support to finitely many subsets of the primes at most that bound. The power estimate `C≤K R^(42/41−η)` with a single uniform `K` would force a bound on `C`; conversely a finite set of non-unit solutions admits such a `K`. The equivalence claim is therefore correct **within the stated non-unit universe**.

**Suggested precision edit:** In the final paragraph, specify `0<η<42/41` and emphasize that `K` is uniform across all exponent signatures. This makes the intended positive exponent and uniformity explicit; the existing argument already uses both correctly.
