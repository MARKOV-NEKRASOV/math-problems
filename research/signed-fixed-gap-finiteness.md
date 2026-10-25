# Signed fixed-gap finiteness across Fermat–Catalan orientations

**Result: a restricted infinite-family finiteness theorem, not the full conjecture.** The earlier fixed-gap lemma treated positive `x^2+y^3=z^r`. The argument extends to every fixed pair of input exponents and to a signed difference, so it applies when the **varying exponent is on any one of the three coordinates**. The output base may have arbitrary moving prime factors.

## The polynomial construction

Fix integers `P,Q≥2`, a sign `ε∈{+1,−1}`, and a nonzero integer `D`. Put

`F(T)=T^P+ε(T−D)^Q`.

**Squarefree lemma.** `F` has no multiple root over `C`.

**Proof.** If `α` were a multiple root, put `β=α−D`. Both are nonzero because `D≠0`, while `F(0)=ε(−D)^Q≠0` and `F(D)=D^P≠0`. The equations `F(α)=F'(α)=0`, after multiplying the derivative by `αβ` and using `α^P=−εβ^Q`, give `Qα=Pβ`. If `P=Q`, this says `α=β`, contradicting `D≠0`. Otherwise, `α=PD/(P−Q)` and `β=QD/(P−Q)`. Let `M=max(P,Q)`, `m=min(P,Q)`, and `h=M−m>0`. Taking absolute values in `α^P=−εβ^Q` gives

`|D|^h = m^m h^h / M^M < 1`.

The strict inequality follows from `m<M` and `h<M`, so `m^m h^h < M^(m+h)=M^M`. But `|D|` is a positive integer. Contradiction. The sign `ε` disappears on taking absolute values. □

## Finiteness theorem

Fix `P,Q,ε,D` as above. There are only finitely many distinct powered-value triples from integer solutions

`m^P+ε n^Q=k^R>0`, `m,n,k≥1`, `m−n=D`, `R≥2`, `1/P+1/Q+1/R<1`.

No coprimality assumption is needed for this restricted theorem.

**Proof.** Substitute `m=T`, `n=T−D`; then `F(T)=k^R`. The squarefree lemma gives at least two distinct complex zeros. For `k≥2`, the Schinzel–Tijdeman theorem for polynomial perfect powers bounds `R` in terms of fixed `F`. For each remaining `R`, the smooth projective curve `Y^R=F(X)` has genus at least one under the displayed hyperbolicity hypothesis:

- If `ε=+1` or `P≠Q`, its degree is `d=max(P,Q)≥3`, except `P=Q=2`; the latter is never hyperbolic. A squarefree degree-`d≥3` polynomial gives genus `((R−1)(d−1)−gcd(R,d)+1)/2≥1` for every `R≥2`.
- If `ε=−1` and `P=Q`, its degree is `d=P−1`. For `P≥4`, `d≥3`. For `P=3`, `d=2`, but hyperbolicity forces `R≥4`, again giving genus at least one. For `P=2`, hyperbolicity is impossible.

Siegel's theorem then gives finitely many integral points `(T,k)` on each remaining curve. For `k=1`, the equation `F(T)=1` has finitely many integer `T`, and varying `R` repeats the same powered value `1`. Thus the union has finitely many distinct powered-value triples. □

This theorem includes the prior `(2,3,R)` positive fixed-gap result. The signed case adds genuine coverage: if `x^p+y^q=z^r` has one varying exponent, moving its powered term to the right writes the equation as a fixed-exponent positive sum **or difference** equal to a varying perfect power. If the other two coordinate exponents are fixed and their bases have a fixed nonzero difference `D`, only finitely many powered triples occur. Therefore, along an infinite all-prime family with exactly one diverging exponent and the other two fixed, the absolute difference of the fixed-exponent bases must tend to infinity (after discarding the finitely many unit-base triples). This restriction allows their prime supports to move and is independent of the fixed-support Siegel lemma.

The result does **not** rule out the full conjecture: the base gap can move with every solution, and the two supposedly fixed exponents can also move in other escape profiles. Schinzel–Tijdeman and Siegel give no uniform bound as `P,Q,D` vary. The cited Schinzel–Tijdeman hypotheses are restated in Pambuccian, arXiv:1410.8441v2 (abstract read in the repository); its original proof was not independently audited here.

## Checks on nearby proposed closures

The modular output-prime sieve only says that a fixed small prime cannot divide `c` for sufficiently large `p`; it does not bound the large primes. The project's Dirichlet–Hensel construction gives infinitely many local output-prime candidates satisfying the `27a1` divisibility test. Cyclotomic primitive divisors likewise give lower bounds on `a+b` while allowing the sum to grow with the exponent. Neither observation can replace a uniform theorem in this construction. The 2025 Mihăilescu cofactor preprint has a literal unit counterexample under its printed hypotheses, so no exclusion from it is used.

I independently checked two new **separate** finite-field and parity sieves. For positive primitive `(2,3,p)` and `p≥11`, `5|b` forces the globally selected FNS curve to have `a_5=0`, which among the seven is only `27a1`; `7|a` forces `a_7=0`, which only `288a1` has. The trace-zero statements follow from the `j=0` reduction at 5 and `j=1728` reduction at 7; the direct point counts in `research/output_prime_sieve_check.py` confirm the selector sets. Because the FNS curve is one globally selected curve, `5|b` and `7|a` cannot both occur. This is a genuine exclusion of an infinite base-divisibility family, while leaving cases avoiding one of those primes. Separately, for coprime odd signed `a,b` in `a^p+b^p=c^t` with odd `p`, `t≥2`, and `a+b>0`, the cofactor `V=(a^p+b^p)/(a+b)` is odd since `gcd(a+b,V)|p`. Therefore `v_2(a+b)=t v_2(c)`, so `2^t|a+b` and `a≠b (mod 4)`. This only excludes a base-residue family.

No complete Fermat–Catalan proof and no Lean formalization followed.
