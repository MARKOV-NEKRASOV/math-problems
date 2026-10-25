# Fixed-input-exponents and fixed-output-support finiteness lemma

**Unconditional restricted result.** Fix integers `P,Q≥2` with `(P,Q)≠(2,2)` and a finite set of rational primes `S`. Then there are only finitely many primitive positive powered-value triples `(a^P,b^Q,c^r)` satisfying `a^P+b^Q=c^r`, `r≥2`, and `supp(c)⊆S`. The result includes every fixed all-prime pair `(P,Q)` occurring on the input side of a hyperbolic signature. The output exponent `r` may equal `P` or `Q`; no distinctness is assumed. Unit input bases `a=1` or `b=1` are allowed. Positivity gives `C=a^P+b^Q≥2`, so `c≥2` automatically. It does not bound solutions as `P,Q` or `S` vary.

Put `L=lcm(P,Q)` and `C=c^r`. Since `C` is supported on `S`, write uniquely `C=Dw^L`, where `w` is a positive integer supported on `S` and `D=∏_{q∈S}q^{e_q}` with `0≤e_q<L`. There are finitely many `D`. Define rational `S`-integers

`u=a/w^{L/P}`, `v=b/w^{L/Q}`.

Then `u^P+v^Q=D`. For each fixed `D>0`, this affine plane curve is nonsingular: its partial derivatives vanish simultaneously only at `(0,0)`, which is not on the curve. Its smooth projective model has genus

`g=((P−1)(Q−1)−(gcd(P,Q)−1))/2≥1`

for all `P,Q≥2` except `(2,2)` (where `g=0`). Hence Siegel's theorem yields finitely many `S`-integral pairs `(u,v)` for each `D`.

Fix such a pair and a prime `q∈S`. If `t=v_q(w)>0`, then `q|C` and `q|c`. With `α=v_q(u)` and `β=v_q(v)`, the exponents of `q` in `a,b` are the nonnegative integers

`v_q(a)=α+(L/P)t`, `v_q(b)=β+(L/Q)t`.

Primitivity `gcd(a,b,c)=1` forces at least one to be zero. Since `α,β` are fixed, this leaves finitely many possible values of `t`. There are finitely many `q∈S`, so only finitely many `w`, then finitely many `(a,b,C)`. These are the powered-value triples being counted; no separate uniform bound on the possible representations `C=c^r` is needed.

The genus formula follows from Riemann–Hurwitz for the degree-`P` map to the `v`-line: the `Q` simple roots of `D−v^Q` are totally ramified, and the point at infinity has `gcd(P,Q)` points each of ramification index `P/gcd(P,Q)`; it gives genus 1 for `(2,3)` and `(3,3)`, and higher genus for many other pairs. The argument uses established Siegel finiteness for each fixed curve, not a uniform theorem over varying `P,Q,D,S`.

**Attempted full-proof application and failure.** If one could show that every hypothetical infinite Fermat–Catalan family has an infinite subsequence with fixed two input exponents `P,Q` and a fixed finite support set `S` for the output base `c`, this lemma would contradict that subsequence. The known reduction to all-prime signatures does not supply either fixedness: primes `(P,Q)` and output support can escape simultaneously. Modular level lowering to a fixed residual comparison curve does not imply equal conductor or fixed `S` without an additional unproved uniform isogeny assertion. Thus this lemma is useful restricted progress, not a proof of the whole conjecture.
