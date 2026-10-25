# Full Fermat–Catalan attempt: optimizing universal descent by the elliptic `j`-invariant

**Outcome: incomplete.** I tried to force a contradiction for an infinite sequence of distinct primitive powered-value triples by attaching one elliptic curve to every solution, bounding its real `j`-invariant or its set of bad primes, then invoking finiteness of elliptic curves with restricted reduction. The local calculation is uniform in all exponent signatures; the hoped-for finiteness step fails for a precise reason.

## Uniform curve and exact invariant

Write `A=x^p`, `B=y^q`, `C=z^r=A+B` for positive bases with `gcd(x,y,z)=1`, `p,q,r>1` and `1/p+1/q+1/r<1`. The equation makes `A,B,C` pairwise coprime. Attach

`E_(A,B): Y²=X(X−A)(X+B)`.

Its invariants are

`Δ=16 A²B²C²`, `c₄=16(A²+AB+B²)`,

`j=256(A²+AB+B²)³/(A²B²C²)`.

These follow by expanding the Weierstrass equation; they require no conjectural input. Moreover the polynomial identity

`4(A²+AB+B²)³−27A²B²(A+B)²=(A−B)²(2A+B)²(A+2B)²`

gives

`j−1728=64(A−B)²(2A+B)²(A+2B)²/(A²B²C²)≥0`.

Equality requires `A=B`; pairwise coprimality then makes `A=B=1`, `C=2`, which cannot equal `z^r` for `r>1`. Hence **every Fermat–Catalan solution in this universe gives `j>1728`**. This is a uniform real constraint, but it is not yet an arithmetic finiteness theorem.

There is also an exact arithmetic-height observation. Put `S=A²+AB+B²`. Pairwise coprimality gives `gcd(S,ABC)=1`: modulo a prime dividing `A`, `B`, or `C`, the value of `S` is respectively `B²`, `A²`, or `A²`, always a unit. Thus the denominator of the reduced rational number `j=256S³/(ABC)²` is `(ABC)²/gcd(256,(ABC)²)≥(ABC)²/256`. In particular, an infinite family with `C→∞` has **unbounded rational `j`-height**, even if its real `j`-values stay in a compact interval. Each fixed rational `j` can arise from only finitely many powered-value triples by this denominator bound.

At each odd prime `t≥3` dividing exactly one of `A,B,C`, the formula for `c₄` is a `t`-adic unit and `v_t(Δ)>0`, so this integral model has multiplicative reduction. At primes `t∤2ABC`, the discriminant is a unit and reduction is good. Thus the odd bad-prime support is exactly the odd part of `rad(ABC)`. This is the same local setting used by modular/Frey arguments; compare Poonen–Schaefer–Stoll §4 and Freitas–Naskręcki–Stoll §2 for special signatures.

## Contradiction attempted and why it fails

Assume infinitely many **distinct** powered-value triples. Unit-base triples are finite by Mihăilescu, and bounded `C` gives finitely many triples, so pass to solutions with `x,y,z≥2` and `C→∞`. Normalize `u=A/C∈(0,1)`. Then

`j=256(1−u+u²)³/[u²(1−u)²]`.

A subsequence has `u→u₀∈[0,1]`. If `u₀∈(0,1)`, the *real values* `j(E)` stay bounded. I tried to invoke Northcott-style finiteness here, but that is invalid: bounded real absolute value does **not** bound the height of rational `j`. The denominator `A²B²C²` can grow, so rational `j`-values of bounded magnitude may have unbounded height. If `u₀=0` or `1`, the real `j` tends to infinity, and this route has no boundedness at all.

A second attempted shortcut is Shafarevich finiteness: for each fixed finite set `S` of primes, only finitely many elliptic curves over `Q` have good reduction outside `S` (see [Shafarevich's theorem on elliptic curves](https://en.wikipedia.org/wiki/Shafarevich%27s_theorem_on_elliptic_curves)). Here `S={2}∪supp(ABC)` moves with the solution. An infinite solution family must have unbounded prime support already by the `S`-unit theorem applied to `A/C+B/C=1`; passing to a subsequence with one fixed `S` is unjustified. Shafarevich finiteness therefore gives no contradiction across the whole family.

A stronger conjectural height/conductor inequality of abc/Szpiro type might control these moving supports, but inserting it would be an unproved step. The exact missing input is a uniform arithmetic bound on rational `j`-height, conductor, exponent signatures, or powered values across all solutions. The real bound `j>1728` and the moving-support reduction do not supply one.

## Conclusion

The universal elliptic curve gives a signature-independent invariant and a clean description of its bad primes. It neither proves that `j` has bounded arithmetic height nor fixes its set of bad primes; therefore no full Fermat–Catalan proof follows. No Lean formalization was attempted, in keeping with the user's preference.

**Sources:** [Poonen–Schaefer–Stoll, arXiv:math/0508174](https://arxiv.org/abs/math/0508174), §4; [Freitas–Naskręcki–Stoll, arXiv:1703.05058](https://arxiv.org/abs/1703.05058), §2; [Evertse's `S`-unit result](https://doi.org/10.1007/BF01388644); [Shafarevich finiteness](https://en.wikipedia.org/wiki/Shafarevich%27s_theorem_on_elliptic_curves). The invariant and factorization above are direct algebraic calculations.
