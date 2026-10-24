# Fermat–Catalan: geometric and function-field proof attempt

**Target.** For primitive positive integers `x,y,z` and `p,q,r>1` with `x^p+y^q=z^r` and `σ=1/p+1/q+1/r<1`, prove that only finitely many distinct powered-value triples `(x^p,y^q,z^r)` occur. **Outcome: no proof of the integer conjecture.** The route gives a uniform theorem for polynomial solutions and then stops at a precise arithmetic gap.

## Uniform function-field analogue (proved)

Let `k` be an algebraically closed field of characteristic zero. Suppose nonzero polynomials `x,y,z∈k[t]` satisfy `gcd(x,y,z)=1`, `x^p+y^q=z^r`, `p,q,r>1`, and `σ<1`. Then **all three polynomials are constant**.

To prove this, set `A=x^p`, `B=y^q`, `C=z^r`. A common irreducible factor of any two of `x,y,z` divides the third by `A+B=C`, so the three bases and hence `A,B,C` are pairwise coprime. If at least one base is nonconstant, then `D=max(deg A,deg B,deg C)>0`. The Mason–Stothers polynomial abc theorem for pairwise coprime `A+B=C` gives

`D ≤ deg rad(ABC) − 1 ≤ deg x + deg y + deg z − 1`.

Since `deg x≤D/p`, `deg y≤D/q`, `deg z≤D/r`, the right-hand side is at most `Dσ−1<D`, a contradiction. Thus no nonconstant primitive polynomial family exists for **any** hyperbolic signature. The proof is uniform in `(p,q,r)`; it does not need a separate genus calculation for each signature. The Mason–Stothers input and the use of `rad` are standard; see [Mason–Stothers theorem](https://en.wikipedia.org/wiki/Mason%E2%80%93Stothers_theorem).

## Attempted transfer to the integer conjecture

The same calculation over integers would need a height form of abc: for every `ε>0`, `C≤K_ε rad(ABC)^(1+ε)` for coprime positive `A+B=C`. Elementary bounds give `rad(ABC)≤xyz<C^σ≤C^(41/42)`. Choosing `ε<1/41` would then bound `C`, uniformly in all signatures. This recovers the known **conditional** implication from abc to Fermat–Catalan. The integer inequality is not supplied by Mason–Stothers: its derivative argument depends on polynomial degrees and does not apply to a single triple of integer constants.

One might hope that infinitely many integer solutions would interpolate to a nonconstant polynomial family, contradicting the proved function-field analogue. That inference is invalid. An infinite set of isolated integer points need not lie on a polynomial or rational-parameter curve. Faltings' theorem and Darmon–Granville indeed show finiteness for each fixed hyperbolic signature, but the union over infinitely many signatures need not be finite. [Poonen–Schaefer–Stoll, Introduction §1.2](https://arxiv.org/abs/math/0508174) states the fixed-signature result and its dependence on descent and Faltings.

A second hoped-for shortcut is to use the genus of the auxiliary curves: hyperbolicity makes the relevant curves high-genus, and genera tend to grow with exponents. Genus greater than one gives finiteness **on each curve**, not vanishing for all sufficiently high genera or a bound on the heights of points across this varying family. As a simple counterexample to “large genus means no rational points,” the curve `v²=u^(2g+1)+1` has rational point `(0,1)` for every positive genus `g`. The Fermat–Catalan family itself has the repeated unit-base identity `1^m+2³=3²` for every `m>6`, although these are one powered-value triple. So an exponent cutoff must explicitly remove unit bases and be proved for the remaining solutions.

## Exact missing obligation

To turn this geometry/function-field approach into a proof, one needs an unconditional number-field result that controls **the union** of rational/integral points across all hyperbolic signatures: for example, a uniform upper bound on the height `C`, or a uniform exponent bound after unit bases are removed, or an abc-strength bound for these special triples. A statement merely bounding the number of points for each fixed curve (even by a universal finite constant) would not suffice: infinitely many curves could each contribute a distinct point. No cited theorem supplies the required cross-signature bound. The polynomial theorem above is genuine but does not prove Fermat–Catalan over integers.
