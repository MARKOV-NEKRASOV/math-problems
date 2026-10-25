# A moving-support finiteness slice: fixed input-base gap

**Status: proved as a restricted consequence of Schinzel–Tijdeman and Siegel; not a proof of Fermat–Catalan.** The output base below may have arbitrary, moving prime factors. The restriction is instead a fixed difference between the two input bases.

## Polynomial perfect-power lemma

Let `F(T) in Z[T]` be squarefree of degree at least `3`. There are only finitely many pairs of integers `n` and positive integers `z>=2`, together with exponents `r>=2`, satisfying

`F(n)=z^r`.

**Proof.** Since `F` has at least two distinct complex zeros, the Schinzel–Tijdeman theorem for `Y^m=F(X)` bounds `r` in terms of `F` when `z>1`. For each remaining fixed `r`, the smooth projective model of `Y^r=F(X)` has genus

`g=((r-1)(d-1)-gcd(r,d)+1)/2`, `d=deg(F)`.

This is at least `1` for `d>=3`, `r>=2`: the minimum is the cubic hyperelliptic case `d=3,r=2`, of genus `1`. By Siegel's theorem, a genus-at-least-one affine curve has finitely many integral points. A finite union over the bounded `r` is finite. The lemma does not give a uniform count as `F` varies.

## Fermat–Catalan slice with arbitrary output support

Fix any nonzero integer `D`. Then the equation

`x^2+y^3=z^r`, `x,y,z positive`, `r>=2`, `x-y=D`             (1)

has only finitely many triples of powered values `(x^2,y^3,z^r)`. This holds without a primitivity assumption, and therefore also for the primitive hyperbolic `(2,3,r)` Fermat–Catalan subfamily, where `r>=7`. For primitive solutions the same finiteness also holds for `D=0`, vacuously.

For `D != 0`, set `T=x`, `y=T-D` and

`F_D(T)=T^2+(T-D)^3`.

It is a cubic with discriminant `disc(F_D)=-D^3(27D-4)`. For nonzero integer `D`, both factors are nonzero, so `F_D` is squarefree. The polynomial lemma proves finiteness of integer `(x,z,r)` and hence of (1). For `D=0`, `x=y`; if the bases are primitive, `x=y=1` and `2=z^r` has no solution with `r>=2`. **Without primitivity the unrestricted `D=0` statement is false:** for every integer `n>=2`, put `t=n^2-1`, `x=y=t`, `z=nt`, and `r=2`. Then `x^2+y^3=t^2(1+t)=(nt)^2`, giving infinitely many powered-value triples. This is outside the hyperbolic Fermat–Catalan range. Thus the unrestricted theorem requires `D != 0`, while the primitive version covers every integer `D`.

The positive bases of hypothetical `(2,3,r)` counterexamples therefore cannot retain any fixed gap `x-y=D` infinitely often. This allows the output prime support to move freely, unlike the project's fixed-output-support Siegel lemma. It still leaves infinitely many possible gaps `D` and supplies no uniform bound as `|D|` grows. In particular, it does not close even the full `(2,3,r)` branch.

## Source and scope

Schinzel–Tijdeman is the classical exponent-boundedness theorem for `Y^m=P(X)` when `P` has at least two distinct zeros and `Y>1`. The arXiv abstract of *The Erdős–Selfridge and the Schinzel–Tijdeman theorems hold in PA^-*, arXiv:1410.8441v2, restates those hypotheses; I checked that abstract, not its full proof. Siegel's integral-point theorem and the superelliptic genus formula are used in their standard forms. The discriminant was expanded algebraically and checked symbolically. No complete proof or Lean formalization resulted.
