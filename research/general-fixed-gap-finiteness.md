# Fixed-gap theorem across all input exponent pairs

**Outcome: a proved infinite-family restriction, not a full Fermat–Catalan proof.** The earlier fixed-gap theorem covered only `(2,3,r)`. The argument below extends it to every fixed input exponent pair `P,Q≥2` except `(2,2)`, while allowing the output exponent and every prime dividing the output base to move. It eliminates any hypothetical infinite all-prime Fermat–Catalan family that retains a fixed pair of input exponents and a bounded difference of input bases.

## General polynomial construction

Let `f,g∈Z[T]`, fix integers `P,Q≥2`, and put `F(T)=f(T)^P+g(T)^Q`. If `F` is squarefree and has degree at least three, then the powered-value triples from `f(n)^P+g(n)^Q=z^r`, with integer `n`, positive `z≥2`, and `r≥2`, form a finite set.

Indeed, `F` has at least two distinct complex roots, so Schinzel–Tijdeman bounds `r` by a constant depending on `F`. For each remaining `r`, the smooth projective model of `Y^r=F(T)` has genus `((r−1)(d−1)−gcd(r,d)+1)/2≥1`, where `d=deg F≥3`. Siegel then gives finitely many integral pairs `(n,z)`. Both inputs and the output prime support may vary. The theorem is tied to a **fixed polynomial relation**; it supplies no bound uniform in the coefficients of `f,g`.

Squarefreeness matters: for `F(T)=T^6`, every positive `n` gives `F(n)=n^6`, and the curve does not have the stated genus. This is a structural counterexample to dropping the root hypothesis, not a Fermat–Catalan counterexample.

## New all-pair fixed-gap theorem

**Theorem.** Fix integers `P,Q≥2` with `(P,Q)≠(2,2)` and fix a nonzero integer `D`. There are only finitely many positive integer solutions, and hence finitely many distinct powered-value triples, of

`x^P+y^Q=z^r`, `x−y=D`, `z≥2`, `r≥2`.                 (1)

No coprimality or fixed output-prime-support condition is needed. In particular, this applies to every primitive hyperbolic Fermat–Catalan solution with those fixed input exponents and base gap. The theorem remains true for a *fixed finite set* of allowed `(P,Q,D)` by taking a finite union. For a primitive family with `D=0`, `x=y=1` is forced and `2=z^r` has no solution with `r≥2`.

**Squarefreeness proof.** Set `F_D(T)=T^P+(T−D)^Q`. Its degree is `max(P,Q)≥3`; if `P=Q`, its leading coefficient is 2. Suppose `α` is a multiple complex root and put `β=α−D`. Since `D≠0`, neither `α` nor `β` can be zero: `F_D(α)=0` would otherwise force both zero. The equations

`α^P+β^Q=0`, `Pα^(P−1)+Qβ^(Q−1)=0`

give `α/P=β/Q`, hence `Qα=Pβ`. If `P=Q`, this gives `α=β`, contrary to `D≠0`. Otherwise write `M=max(P,Q)`, `m=min(P,Q)`. Solving for `α,β` and taking absolute values in the first equation yields

`|D|^(M−m)=m^m (M−m)^(M−m)/M^M`.                 (2)

The right side is `(m/M)^m ((M−m)/M)^(M−m)`, strictly between 0 and 1. The left side is a positive integer. Contradiction. Therefore `F_D` is squarefree, and the polynomial construction proves the theorem. This algebra is valid for either sign of `D` and either order of `P,Q`.

I independently checked `gcd(F_D,F_D')=1` symbolically for `2≤P,Q≤9`, `(P,Q)≠(2,2)`, and every integer `D` with `1≤|D|≤12` (1,512 cases); the calculation supports but is not used in the proof.

## Direct implication and exact remaining gap

For a hypothetical infinite Fermat–Catalan sequence with fixed input exponents `P,Q`, the differences `x−y` must escape every fixed bounded set of integers. This is stronger than the old `(2,3,r)` statement and is independent of output-prime support; it eliminates a proper infinite-dimensional slice of *every* fixed-input-pair branch. Combined with the project's fixed-output-support lemma, any such sequence must have both an escaping input-base gap and escaping output prime support. The two necessary escape conditions may occur together and do not contradict each other. The theorem does not handle a family where `P,Q` or `D` vary without bound, so it does not prove full Fermat–Catalan.

**Source status.** The Schinzel–Tijdeman exponent-bound theorem is used in its standard form for `Y^m=F(X)` with `Y>1` and at least two distinct zeros of `F`; Pambuccian, arXiv:1410.8441v2, abstract, restates these hypotheses, but the original classical proof was not audited here. Siegel's integral-point theorem and the superelliptic genus formula are standard inputs. The squarefreeness argument above is self-contained. No Lean formalization was attempted.
