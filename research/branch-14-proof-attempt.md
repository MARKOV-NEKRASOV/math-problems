# Branch proof attempt, cycle 14: residual-prime correction

**30 October 2026. Status: incomplete.** Four roles revisited the fixed-`(2,r)` F2 laboratory, with a primary PDF audit of arXiv:2605.02632v1 and an independent adversarial check. No infinite F2, F1, or F0 profile has been closed, and no Lean formalization was started.

## G14-S: correction of the even-base irreducibility lemma

Fix an odd prime `r≥7`. For a positive primitive solution `a²+b^r=c^p` with `b` even and prime `p` sufficiently large depending on `r`, the Jacobian `J_{2,r}` of Cazorla García–Koutsianas–Villagra Torcomian has irreducible residual two-dimensional representation at primes over `p`, provided `c` has a prime factor `ℓ∤2r`. **No assumption `p∤ab` is needed.** The proof applies their arXiv:2605.02632v1 Theorem 6.1 with a prime of `K_r=Q(ζ_r)^+` over 2. Proposition 5.6 gives potentially good reduction there because `v₂(b^r)≥r≥7`. Theorem 3.3 gives GL2 type; Proposition 5.2 and the paper's Corollary 6.1 proof supply the endomorphism-descent condition when `ℓ|c`.

The disputed semistability hypothesis is resolved directly from the *printed* source, p. 10: Proposition 5.1 requires `q∤2rAB(Aa²+Bb^r)` for good reduction. With coefficients `A=B=C=1`, residual `p>2r`, and `p∤c`, this holds even when `p|a` or `p|b`. If `p|c`, Proposition 5.2 gives multiplicative reduction. Thus every prime over `p` is semistable. Cycle 13 mistakenly added `p∤ab` by reading an input-base factor into Proposition 5.1; the [earlier note](branch-13-geometric-irreducibility.md) now carries this correction. The source Theorem 6.1 says *irreducible*; its Corollary 6.1 says *absolutely irreducible*. We retain the weaker printed conclusion until the underlying 2017 theorem is checked.

If `supp(c)⊆{2,r}`, the project's [fixed-output-support lemma](fixed-output-support.md) gives finitely many distinct powered-value triples for this fixed `(2,r)` pair. Because `b` even implies `c` odd, this exception consists of `r`-power bases. Consequently the entire even-`b` slice has residual irreducibility for sufficiently large `p`. This is only an entrance condition for the modular method: no comparison-newform elimination or upper bound on `p` follows. The threshold depends on `K_r`, its degree and Jacobian dimension `(r−1)/2`, and the chosen prime over 2; it is not uniform as `r→∞`.

## B14-W: exact input-divisibility condition

Let `p>r≥3` be odd primes and let `a²+b^r=c^p` be primitive with positive bases. If `p|b`, then `p∤ac` and `c^p≡a² (mod p²)` because `r≥3`. Euler's theorem gives `c^{p(p−1)}≡1 (mod p²)`. Therefore `a^{2(p−1)}≡1 (mod p²)`. Writing `a^{p−1}≡1+kp (mod p²)` and using that `p` is odd yields `k≡0 (mod p)`, so `a^{p−1}≡1 (mod p²)`. If `p|a`, the same argument gives `b^{r(p−1)}≡1 (mod p²)` and, because `p∤r`, `b^{p−1}≡1 (mod p²)`. These are necessary Wieferich-type conditions, **not** exclusions. The known primitive solution `2213459²+1414³=65⁷` has `7|1414` and `2213459⁶≡1 (mod 49)`; thus the first condition is attained in a genuine Fermat–Catalan solution.

## A closed subcase from an existing theorem

The earlier [factorization](branch-13-factorization.md) sends the opposite-parity slice of `x^p+y⁴=z⁴` to `(u²)^p+(v²)^p=2w^p`, with `u<v` coprime odd and `p≥3`. Ratcliffe–Grechuk, arXiv:2412.11933v2, p. 16, Theorem 3.6, states that `U^n+V^n=2W^n` has no nontrivial primitive solution with `|UVW|>1` for `n≥3`, citing Darmon–Merel. Here `U=u²`, `V=v²` are coprime and unequal, so the survey theorem excludes the entire opposite-parity slice. **This is an application of a known result**, not a new proof. The original 1997 Darmon–Merel article was unavailable; the theorem scope has been checked in the survey but its original proof has not been audited. The both-odd slice remains, and a closed slice does not close F2-QR.

## Bounds and seven-profile state

| Profile | This cycle's result | Status |
| --- | --- | --- |
| F2-PQ | For the fixed pair `(2,r)`, even-`b` residual irreducibility no longer needs `p∤ab`; input-divisibility has the B14-W condition. No height upper bound or newform elimination. | OPEN |
| F2-PR | No new uniform bound. | OPEN |
| F2-QR | The opposite-parity `(p,4,4)` slice is excluded by the secondary-source statement of Darmon–Merel; the both-odd slice and the full profile remain. | OPEN |
| F1-P | The threshold and field degree grow with `r`. | OPEN |
| F1-Q | Same unresolved dependence. | OPEN |
| F1-R | No new uniform bound. | OPEN |
| F0 | No upper inequality uniform in all exponents. | OPEN |

For fixed `(2,r)`, the sufficient radical slope would be `κ<2r/(r+2)` in an inequality `log C≤κ log rad(abc)+o(p)`. G14-S and B14-W provide no such upper bound. The next falsifiable task is to compute the level-lowered comparison forms in the entire even-`b` family, identify every surviving ghost or congruence class, and prove their elimination with constants tracked in `r`. The odd-`b`, `r|c` slice still lacks the same fixed potentially-good place from Proposition 5.6.

## Source and review boundary

The G14-S proof uses checked theorem statements and proof lines from the cached primary arXiv:2605.02632v1 PDF (pp. 8, 10–12, 22). The adversarial [source audit](branch-14-adversarial-review.md) independently checked Propositions 5.1/5.2/5.6 and B14-W. The [literature watch](branch-14-literature.md) checked cached primary and survey PDFs at opening and closing; live arXiv queries returned HTTP 403, so no claim is made about newer versions. The original 2017 Billerey et al. Corollary 1 and 1997 Darmon–Merel text were unavailable. The source's endomorphism-descent inference is cited, not independently reproved. The previous `p∤ab` restriction is explicitly retracted; this is a correction to an application of an existing theorem, not a proof of an escape branch.
