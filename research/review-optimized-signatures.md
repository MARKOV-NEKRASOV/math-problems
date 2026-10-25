# Independent review of the three-category signature reduction

**Verdict:** I found the reduction in `optimized-signatures.md` mathematically sound. It is a reduction of the full Fermat–Catalan problem, not a proof of finiteness. The 19 fixed signatures are exactly the composite-containing irreducible signatures in the stated finite set.

## Analytic checks

1. A proper-divisor replacement `n→d` with new base `u^(n/d)` preserves the powered value and the equation exactly. It preserves primitivity because raising bases to powers does not change their prime supports. If the new reciprocal sum is below 1, the new representation is eligible. The sum of the exponents decreases, so repeated replacements terminate.
2. For any two exponents in a hyperbolic signature, they cannot both be 2. Their reciprocal sum is at most `1/2+1/3=5/6`; replacing the third exponent by any divisor `d≥7` gives at most `41/42`. Thus an irreducible composite exponent `n≥7` has no proper divisor at least 7. The complete list of such integers is `{8,9,10,12,15,25}`: it follows by considering the smallest prime factor and largest proper divisor `n/s<7`, or by the divisor argument in the previous full-scope note.
3. For each `n` in that six-element list, its largest proper divisor is respectively `4,3,5,6,5,5`. If another exponent is at least 7, replacing `n` by this divisor keeps the reciprocal sum below 1; hence the other two exponents must be at most 6 in an irreducible signature. An exponent 6 also cannot coexist with an exponent at least 7, since `6→3` is allowed. For exponent 4 plus a high exponent, `4→2` is allowed unless the third exponent is 2. The only remaining infinite composite-containing class is consequently `(2,4,ℓ)` with prime `ℓ≥7`.
4. If all exponents are prime, they belong to the all-prime class. If a composite remains and there is no prime exponent at least 7 in the exceptional `(2,4,ℓ)` form, the signature lies in the finite `T³` check. These cases exhaust all terminal signatures. This is an unordered-signature classification; each fixed unordered signature has at most six ordered versions, so Darmon–Granville fixed-signature finiteness still gives a finite union for the 19 exceptions.

## Independent finite check

I reproduced the note's exact `Fraction` enumeration for `T={2,3,4,5,6,8,9,10,12,15,25}`. It returned precisely the 19 triples printed in its table, without numerical tolerance. As an additional counterexample search, I enumerated all 166,545 unordered hyperbolic triples with exponents between 2 and 100 and repeatedly applied allowable divisor reductions. Every terminal triple landed in one of the three claimed classes. The finite table computation and the analytic case split, not this bounded search, support the general reduction.

**Counting clarification:** A broader coordinatewise-minimal list has 23 triples, including four *all-prime* triples `(2,5,5)`, `(3,3,5)`, `(3,5,5)`, `(5,5,5)`. Subtracting these yields the 19 composite-containing exceptions. It would be incorrect to justify 19 by removing FLT-excluded signatures; three of the 19 listed exceptions have gcd at least 3 and are empty by FLT, but keeping them in a finite class is harmless.

**Remaining gap:** All-prime hyperbolic signatures include `(2,3,ℓ)` for every prime `ℓ≥7`, and `(2,4,ℓ)` is also infinite. Fixed-signature finiteness cannot bound either union. No full proof follows from this reduction.
