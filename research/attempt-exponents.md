# Fermat–Catalan: reduction of the `(2,3,n)` exponent family

**Status:** rigorous partial reduction, no proof of Fermat–Catalan. This note investigates whether varying output exponents can be reduced to a smaller set without leaving the hyperbolic condition.

## A uniform reduction to prime exponents and six fixed exceptions

Consider a primitive positive solution `a²+b³=cⁿ` with `n≥7`. If a divisor `d|n` has `d≥7`, write `C=c^(n/d)`. Then `a²+b³=C^d`, `gcd(a,b,C)=1`, and `1/2+1/3+1/d<1`. The powered-value triple `(a²,b³,cⁿ)` is unchanged. The reduction is valid even when a base is 1, since we count powered-value triples rather than exponent tuples.

If `n` is composite and its largest proper divisor `n/s`, where `s` is its smallest prime factor, is less than 7, then `n` is one of **8, 9, 10, 12, 15, 25**. Proof: if `s=2`, then `n<14`, giving composite `n≥7` equal to 8, 10, or 12. If `s=3`, then `n<21` and `n` is odd, giving 9 or 15. If `s=5`, then `n<35` and `n` has no factors 2 or 3, giving 25. If `s≥7`, compositeness gives `n≥s²`, hence `n/s≥7`, a contradiction. Repeatedly divide by a suitable factor until reaching either a prime `ℓ≥7` or one of those six exceptions.

Darmon–Granville finiteness for each fixed hyperbolic signature, as cited by Poonen–Schaefer–Stoll §1.2, makes the union of the six exceptional `(2,3,n)` signatures finite. Therefore **finiteness of distinct powered-value triples for the full `(2,3,n≥7)` family is equivalent to finiteness for its prime-exponent subfamily `(2,3,ℓ)` with prime `ℓ≥7`**, using that established fixed-signature theorem. This focuses one infinite family; it says nothing about all other exponent patterns and gives no uniform bound for the remaining primes.

## Why common factors of only two exponents do not give FLT

The primitive positive identity `13²+7³=2⁹` has `1/2+1/3+1/9=17/18<1`. The exponents 3 and 9 share a factor 3, yet this is a valid Fermat–Catalan triple. Fermat's Last Theorem excludes a common divisor at least 3 of **all three** exponents, not merely two.

For any solution with `3|q` and `3|r`, write `U=z^(r/3)` and `V=y^(q/3)`. Then `x^p=U³−V³=(U−V)(U²+UV+V²)`, with `U−V>0` because `x^p>0`; since `gcd(U,V)=1`, the two factors have gcd dividing 3. If `3∤x`, they are coprime and each is a `p`th power. In the concrete solution above, `U=8`, `V=7`, the factors are 1 and 169, so this factorization alone does not rule out solutions. The remaining cases where 3 divides `x` require a separate 3-adic analysis. This is a useful family reduction, not a uniform finiteness result.

## Sources and next obligation

- B. Poonen, E. F. Schaefer, M. Stoll, *Twists of X(7) and primitive solutions to x²+y³=z⁷*, Introduction §1.2, [arXiv:math/0508174](https://arxiv.org/abs/math/0508174): cites Darmon–Granville finiteness for each fixed hyperbolic signature.
- H. Darmon, A. Granville, *On the equations z^m = F(x,y) and Ax^p+By^q=Cz^r*, [DOI 10.1112/blms/27.6.513](https://doi.org/10.1112/blms/27.6.513): fixed-signature theorem (invoked through Poonen–Schaefer–Stoll; original theorem hypotheses should be checked before wider reuse).
- N. Freitas, B. Naskręcki, M. Stoll, *The generalized Fermat equation with exponents 2, 3, n*, [arXiv:1703.05058](https://arxiv.org/abs/1703.05058): studies exactly the surviving prime-exponent family through Frey curves and modular twists; it does not establish uniform finiteness over all primes.

**Open obligation:** bound or classify the powered-value triples for prime exponents `ℓ≥7` uniformly. Solving any finite list of fixed signatures, including the six exceptions, does not close that obligation.
