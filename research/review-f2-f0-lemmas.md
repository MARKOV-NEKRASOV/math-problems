# Independent cross-review of A12 and B12

**25 October 2026. Verdict:** A12-G, A12-F, B12.1, and B12.2 are valid within their written hypotheses. They are structural barriers and sufficient criteria, not a full Fermat–Catalan proof. I found no arithmetic error requiring retraction. The qualifications below matter before integrating them into an F2→F0 claim.

## A12-G: non-Galois monodromy barrier

The exact setup is essential: a connected degree-`n` cover of `P¹_C` with exactly three branch points, whose *local monodromy permutations themselves* have pairwise-coprime exact orders `e1,e2,e3>1`. Monodromy is a faithful transitive subgroup of `S_n`. The branch-cycle relation and coprimality kill all three generator images in its abelianization, hence `G` is perfect. Lagrange gives `e1e2e3| |G|`; faithfulness gives `|G|≤n!`. Therefore `n!≥e1e2e3` is correct. It does not give a genus bound for the original non-Galois cover.

**Scope clarification:** A local permutation's order is the lcm of the ramification indices of points above that branch value. A construction specifying some individual cycle lengths `e_i` has not yet established the hypothesis that the whole permutation has exact order `e_i`. In the distinct-prime case, the immediate permutation fact `n≥max(e1,e2,e3)` is stronger as a degree lower bound than `n!≥e1e2e3`; thus (G′)'s main value is the perfect-monodromy restriction, not the numerical size of `n`. The source HGM in A12-F has local monodromy orders `{q,∞,r}` at the three points, so A12-G's finite pairwise-coprime-index hypothesis does **not** apply directly to it. The note already states this boundary in substance.

## A12-F: field degree and discriminant

For distinct odd primes `q,r`, `K_q=Q(ζ_q+ζ_q^{-1})` has degree `(q−1)/2` and discriminant `q^((q−3)/2)`, including the trivial `q=3` edge. The two fields ramify at disjoint finite primes, so their intersection is `Q`; their discriminants are coprime. Hence `F=K_qK_r` has degree `(q−1)(r−1)/4` and discriminant magnitude `q^((q−3)(r−1)/4) r^((r−3)(q−1)/4)`. Sanity check `q=5,r=7`: degrees `2·3=6`, discriminant `5³7⁴`, matching the formula. I directly rechecked the Cazorla García–Villagra Torcomian v2 PDF, §6.4: it does say the cited HGMs are defined over `F=Q(ζ_q)^+Q(ζ_r)^+`, with local monodromy `{q,∞,r}`. Thus the formula applies to that **chosen field**. No lower bound for every possible Frey construction or motive follows.

**Old→new bound and threshold gap:** A12-G supplies a finite-cover design filter; A12-F gives exact field growth `(qr)/4` and log-discriminant of order `qr(log q+log r)` for the cited rank-two HGM as both primes grow. Neither yields the protocol's upper `log C≤((1−δ)m/3)log R+o(m log m)` or an F2/F1 radical power bound. No branch is closed. Tracking field degree alone does not prove that associated modularity constants grow too fast; those constants must be explicitly bounded or shown to obstruct uniformity.

## B12.1: slack lemma and F2/F1 implications

Write `L=log C`, `T=log R`, `M=max(p,q,r)` with all bases at least 2. If `M` occurs on either input, its powered value is strictly below `C`, and if on the output then `C≥2^M`. Thus `L≥M log2`. The radical inequality `T≤σL` and a proposed `L≤κ T+E` with `s=1−κσ>0` give `E≥sL≥sM log2`. Therefore an estimate with `E=o(sM)` along an infinite nonunit family is impossible. For F2 with fixed `a,b` and `κ<ab/(a+b)`, `s` eventually has a fixed positive lower bound, so `E_{a,b}(w)=o(w)` suffices to contradict `M≥w`. For F1 with fixed `a` and `κ<a`, `E_a(w)=o(w)` likewise suffices. These are **sufficient targets**, not established upper bounds. All constants must remain independent of the moving bases and exponents as specified.

## B12.2/B12.3: F0 error budget and Pastén

B12.2 correctly specializes the reported Stewart–Yu inequality `L≤K e^(T/3)T³` together with `T≤3L/m`: setting `u=L/m` yields `m≤27K e^u u²`, hence `L≥m(log m−2loglog m−O_K(1))`. Combining it with `L≥M log2` gives `L≥c max{M,m log m}` for large `m`. The unproved proposed upper `L≤((1−δ)m/3)T+E` would imply `δL≤E`; the refined uniform budget `E=o(max{M,m log m})` would be contradictory. I directly read Héctor Pastén, arXiv:2312.03566v1, introduction p.2: it states the Stewart–Yu form with an absolute constant. The original Stewart–Yu article was not read here, so record Pastén as a later primary-research restatement rather than a proof audit of the 2001 theorem.

Pastén's Theorem 1.4(2) on p.2 states `L≤q_* exp(κ sqrt((log R) log_2 R))` for `q_*=min(P(A),P(B),P(C))` and an absolute κ, consistent with B12.3's `q_* exp(κ sqrt(T log T))`. This bound does not supply a linear-in-`T` coefficient below the F0 threshold. The abstract scale `L=m²,T=m,q_*≥2` is a legitimate logical consistency check of inequalities only, not a candidate integer solution.

## Seven-branch impact and next test

All seven F2/F1/F0 branches remain open. A12-F shows why a fixed-rank motive over `F=K_qK_r` is not automatically uniform when `q,r` move. B12.1 permits a sublinear error in a hypothetical F2 upper bound, refining the earlier fixed-constant target; B12.2 permits `o(max{M,m log m})` in F0 if the slope is genuinely `(1−δ)m/3`. The next falsifiable target is to derive an upper inequality from a specific F2 construction with **explicit** dependence on `[F:Q]`, `disc(F)`, conductor, motive rank, and residual-image hypotheses, then check whether its slope and error survive F1 and F0. If it only gives fixed-`q,r` constants or an error at least comparable to the moving-exponent budget, it has not crossed the bridge.

**Source/reading status:** Cazorla García–Villagra Torcomian arXiv:2503.21568v2 §6.4 was rechecked in extracted PDF text; Pastén arXiv:2312.03566v1 introduction and Theorem 1.4(2) were directly read in its PDF. Theorem G's proof and A12-G were checked algebraically, not against a claimed originality source. No Lean formalization is justified.
