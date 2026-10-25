# An asymptotic obstruction for an infinite Fermat–Catalan family

**Status: necessary condition, not a proof.** The [reduction to all-prime signatures](reduction-to-prime-signatures.md) allows a sharper radical and height–conductor estimate along any hypothetical infinite family than the uniform `41/42` exponent valid for individual triples.

Suppose there are infinitely many **distinct powered-value triples** `T=(A,B,C)=(x^p,y^q,z^r)` satisfying the Fermat–Catalan hypotheses. The [fixed composite-signature cases and variable `(2,4,ℓ)` family](integrated-full-proof-attempt.md) contribute only finitely many triples, so discard them. Every remaining triple admits an all-prime hyperbolic representation. For a triple `T`, let `M(T)` be the minimum, over these representations, of `max(p,q,r)`.

For each fixed integer `M`, only finitely many prime signatures have all exponents at most `M`. Darmon–Granville gives finitely many primitive solutions for each fixed hyperbolic signature. Hence only finitely many distinct triples have `M(T)≤M`. Along any sequence of distinct remaining triples, `M(T)→∞`. Choose an all-prime representation realizing `M(T)` and put `σ_T=1/p+1/q+1/r`. The two exponents other than the largest cannot both be 2, because that would make the sum at least 1. Their reciprocal sum is at most `1/2+1/3=5/6`, so

`σ_T≤5/6+1/M(T)=5/6+o(1)`.                         (1)

Writing `R=rad(ABC)`, pairwise coprimality and perfect-power structure give

`R≤xyz<C^σ_T≤C^(5/6+o(1))`.                          (2)

The `o(1)` here is along the chosen infinite sequence; (2) is **not** a uniform `5/6` bound for every individual solution. Unit-base triples do not affect the argument: Mihăilescu leaves only finitely many distinct powered triples with a unit base.

For the [universal Frey curve](full-height-conductor.md), `h(j)=6log C+O(1)` and `N(E)≤K₂R`. A fixed upper bound on `N(E)` would fix the odd prime support and make the powered triples finite by the fixed-`S` unit theorem. Thus `N(E)→∞` along the chosen distinct sequence, and (1)–(2) imply

`h(j)≥(36/5−o(1))log N(E)`.                          (3)

This slope `36/5=7.2` improves the pointwise `252/41≈6.146` slope. It still supplies a **lower** height–conductor bound on hypothetical solutions, not the upper bound needed for a contradiction.

There is also a sharper conditional abc threshold. If an unconditional estimate `C≤K_ε R^(1+ε)` held for these triples with one fixed `ε<1/5`, then `(5/6+o(1))(1+ε)<1` eventually, so (2) would bound `C`, contradicting the assumed infinite family. No such estimate is proved here. Conversely, along a hypothetical infinite family the fixed-`ε` quotient `C/R^(1+ε)` diverges for **every** `ε<1/5`: choose `δ>0` with `(5/6+δ)(1+ε)<1`; then eventually `R<C^(5/6+δ)` and

`C/R^(1+ε)>C^[1−(5/6+δ)(1+ε)]→∞`.

This strengthens the earlier single-`ε` contradiction calculation, but it does not establish Fermat–Catalan. The missing input remains an unconditional upper radical or height–conductor estimate with enough uniform strength on the all-prime family. No Lean formalization was started.
