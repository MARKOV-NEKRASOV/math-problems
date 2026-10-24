# Fermat–Catalan height/radical route, second pass (October 2026)

**Status: no proof of the conjecture.** This pass tests an established unconditional abc estimate and obtains a limited unconditional finiteness lemma. None controls the varying exponent signatures.

## Setup

Write `A=x^p`, `B=y^q`, `C=z^r`, where `A+B=C`, `gcd(x,y,z)=1`, `x,y,z>=2`, `p,q,r>=2`, and `σ=1/p+1/q+1/r<1`. The powered values are pairwise coprime. The elementary hyperbolic gap gives `σ<=41/42`, so for `R=rad(ABC)=rad(xyz)` we have

`R <= xyz < C^σ <= C^(41/42)`.                                               (1)

The largest possible `σ` is attained by the signature `(2,3,7)`. The non-unit restriction removes the repeated representation `(1,8,9)` caused by variable exponents on 1. See the [Fermat–Catalan overview](https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture) and [Poonen–Schaefer–Stoll, introduction](https://arxiv.org/pdf/math/0508174).

## Test of an unconditional abc estimate

Stewart–Yu, *On the abc conjecture, II*, Duke Math. J. 108 (2001), [DOI 10.1215/S0012-7094-01-10815-6](https://doi.org/10.1215/S0012-7094-01-10815-6), is reported by the linked abc overview to give an absolute constant `K` for which coprime positive `A+B=C` satisfy

`log C < K R^(1/3) (log R)^3`                                                (2)

for `C>2`; the formula is also reproduced in the [abc overview, partial results](https://en.wikipedia.org/wiki/Abc_conjecture#Partial_results). Combining (1) and (2) yields only

`log C < K C^(41/126) ((41/42) log C)^3`.                                    (3)

For every fixed `K>0`, (3) holds automatically once `C` is large. Thus the substitution gives **no upper bound on `C`**. Inversion of (2) gives a much weaker, legitimate consequence: for every `δ>0`, all sufficiently large such triples have `R>(log C)^(3-δ)`. For `0<δ<3`, if `R<=(log C)^(3-δ)`, then the right side of (2) is at most `O((log C)^(1-δ/3)(log log C)^3)=o(log C)`, a contradiction; larger `δ` follow immediately. This polylogarithmic lower bound on `R` is far below the power of `C` needed to counter (1).

## A fixed-prime-support subproblem is finite

Fix a finite set of primes `S`. Among primitive positive triples `A+B=C` whose prime factors all lie in `S`, there are only finitely many powered-value triples, hence only finitely many Fermat–Catalan triples with that support. To see this, `u=A/C` and `v=B/C` are rational `S`-units with `u+v=1`. The `S`-unit theorem gives finitely many such pairs. Each pair determines at most one primitive positive integer triple `A,B,C`: clearing denominators produces the unique coprime triple. This uses the established `S`-unit result; see J.-H. Evertse, *On equations in S-units and the Thue–Mahler equation*, Invent. Math. 75 (1984), [DOI 10.1007/BF01388644](https://doi.org/10.1007/BF01388644).

Consequently a fixed bound on `R` would imply Fermat–Catalan finiteness, since only finitely many prime sets have product at most that bound. But (2) points in the opposite direction: large `C` forces `R` to grow; it does not bound `R`. An infinite hypothetical solution family could keep introducing new prime factors, so the fixed-`S` theorem does not cover it.

## Exact remaining height obligation

For some fixed `0<η<42/41` and a single `K` uniform across all exponent signatures, a bound `C<=K R^(42/41-η)` on these **special** triples would combine with (1) to bound `C`, since `(41/42)(42/41-η)<1`. Conversely, if Fermat–Catalan finiteness holds, such a bound exists trivially after choosing `K` over the finite solution set. This restricted power-saving estimate is therefore itself equivalent to the non-unit conjecture; it cannot be inserted as an unproved lemma. The unconditional estimate (2) is exponentially weaker than this needed power estimate.

**Next research obligation:** Find a genuinely unconditional estimate uniform in `(p,q,r)` and in the prime support of `xyz`, or another argument controlling all varying signatures. Fixed-signature finiteness (Darmon–Granville, cited by Poonen–Schaefer–Stoll) and fixed-support finiteness leave the same union-over-infinitely-many-cases gap.
