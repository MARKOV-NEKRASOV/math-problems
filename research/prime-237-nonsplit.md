# Full-proof attempt on the surviving `(2,3,p)` family and the non-split Cartan branch

**Outcome: incomplete.** The Fermat–Catalan conjecture is reduced in the repository to all-prime hyperbolic signatures. I tried to finish the indispensable `a²+b³=c^p` subfamily (positive primitive bases, prime `p≥7`) using Freitas–Naskręcki–Stoll's seven fixed comparison curves, the positivity condition on `j`, and the project's fixed-output-support lemma. The missing step is a uniform non-split-Cartan rational-point or fixed-curve isogeny theorem; neither is established in the checked sources. Even a proof for this subfamily would leave other all-prime signatures.

## Frey curve and exact arithmetic obstruction

Let `a²+b³=c^p`, `a,b,c>0`, `gcd(a,b,c)=1`, and `p≥11` prime (the fixed `p=7` case is classified by Poonen–Schaefer–Stoll). The Frey curve `E:y²=x³+3bx−2a` has

`Δ(E)=−2⁶3³c^p`, `c₄(E)=−2⁴3²b`, `j(E)=1728b³/c^p`.

Hence `0<j(E)<1728`. Also `gcd(b,c)=1`, so the reduced denominator of `j(E)` is exactly `c^p/gcd(c^p,1728)`. Since `1728=2⁶3³`, that denominator is >1 for every `c≥2` and `p≥7`: if `c` has a prime ≥5 it remains in the denominator; if `c` is 2,3-smooth, any prime divisor occurs to exponent at least `p`, exceeding its exponent in 1728. Therefore `j(E)` is a noninteger rational number. A CM elliptic curve's `j`-invariant is an algebraic integer, so `E` has no CM.

FNS (arXiv:1703.05058v3, Lemma 2.3 and Proposition 2.4) supplies an isomorphism of mod-`p` Galois representations between one of eight small quadratic twists of `E` and one of seven fixed rational curves. This follows for nontrivial primitive solutions at `p≥11` after irreducibility, but it is only a residual congruence. It does not give a rational isogeny, equal `j`, or equal conductor. At a prime `q≥5` dividing `c`, `E` has multiplicative reduction with minimal-discriminant valuation `p v_q(c)`. That divisibility is exactly why the prime can disappear under mod-`p` level lowering while remaining a bad prime of `E`.

## The `27a1` branch and an attempted local closure

For the comparison curve `27a1`, prior reviewed work in `research/attempt-27a1.md` proves the following. If `q≥5`, `q≠p`, divides `c` and the twist of `E[p]` matches `27a1[p]`, then

`p | (q+1)²−a_q(27a1)²`.

Hasse's bound `|a_q|≤2√q` makes the positive integer on the right at most `(q+1)²`; thus `q≥√p−1`. When `q≡2 (mod 3)`, cubing permutes `F_q`, so `a_q(27a1)=0` and the stronger `p|q+1` holds, hence `q≥p−1` (indeed `6p|q+1` for p≥17). The prime `q=p` already satisfies `q≥√p−1`. Consequently every prime `q≥5` dividing `c` in this branch is at least `√p−1` for large `p`. This is a genuine uniform *small-prime exclusion*, not a bound on `c` or `p`: arbitrarily large primes can satisfy the divisibility conditions, and the number of supporting primes can vary.

FNS Lemma 6.1 excludes the `27a1` branch for prime `p≥17` with `p≡1 (mod 3)` by a split-Cartan argument. It explicitly leaves the `p≡2 (mod 3)` non-split-Cartan situation open. A tempting replacement is the assertion that all rational points on the non-split Cartan curve `X_ns^+(p)` are CM for all sufficiently large `p`; our `E` has nonintegral `j` and is non-CM, so such a theorem would rule out this branch. **This uniform assertion is still an open form of Serre's uniformity question, not a theorem in the sources checked.** A 2020 theorem (arXiv:2002.02714v2) says that for `p>1.4×10⁷`, a non-CM elliptic curve whose mod-`p` image is contained in a non-split Cartan normalizer has image equal to the *full* normalizer; full normalizer is still a proper subgroup of `GL₂(F_p)`, so that result does not exclude the branch.

The newer Hashimoto–Lido–Lombardo–Mascot–Parent preprint, arXiv:2608.10919v1 (11 August 2026), describes an equationless quadratic Chabauty method for `X_ns^+(N)` of prime level `N≥13`. Its Theorem 1.1 rederives the seven known CM points on `X_ns^+(13)`. Its introduction explicitly asks whether there is a bound beyond which *all* rational points on `X_ns^+(N)` are CM; it does **not** prove that uniform assertion. I inspected its arXiv v1 abstract, introduction, and Theorem 1.1, not its full computation. Thus this recent primary paper supplies a method for individual levels, not a closure over unbounded `p`.

## Fixed-output-support route and precise failure

The project's reviewed Siegel lemma (`research/fixed-output-support.md`) proves: with the two input exponents fixed at `(2,3)` and `supp(c)` inside any fixed finite prime set `S`, only finitely many powered triples arise as `p` varies. Hence, if infinitely many positive `(2,3,p)` solutions existed, the largest prime factor of `c` would have to escape every fixed bound. The local `q≥√p−1` condition is compatible with that escape; it does not force a *fixed* `S`. Nor does the residual match to seven curves fix `S`, since mod-`p` congruence does not preserve conductors. A Frey–Mazur isogeny principle would fix `S` but is conjectural.

**Unclosed proof obligation:** show unconditionally that no non-CM Frey curve with `0<j<1728` arises on every surviving mod-`p` twist for unbounded `p`, in particular the non-split `27a1` branch; and independently handle the other all-prime signatures. The source-checked local and fixed-support restrictions do not establish this. No complete proof and no Lean formalization resulted.

Sources inspected: Freitas–Naskręcki–Stoll, arXiv:1703.05058v3, Lemma 2.3, Proposition 2.4, Lemma 6.1, Table 4; Poonen–Schaefer–Stoll, arXiv:math/0508174, Theorem 1.1; Hashimoto et al., arXiv:2608.10919v1, abstract/introduction/Theorem 1.1; Lemos, arXiv:2002.02714v2, abstract. The last paper's detailed proof was not checked.
