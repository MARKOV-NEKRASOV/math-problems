# A full-scope Fermat–Catalan proof attempt: descent and height–conductor

**Subsequent source check:** The [integrated reduction](reduction-to-prime-signatures.md) and its [independent review](review-reduction-to-prime-signatures.md) show that the variable `(2,4,ℓ)` family is finite using Bennett–Skinner and Ellenberg. The Gaussian/Lucas obstruction below records the earlier attempt; it is no longer an unresolved infinite family. The [latest integrated attempt](integrated-full-proof-attempt.md) incorporates this result.

**Result: no complete proof.** Four agents attacked the remaining infinite exponent classes and sought a contradiction for an infinite family. Each new algebraic deduction was independently reviewed. The work below identifies exact equations a counterexample family would have to satisfy, but supplies no unconditional theorem excluding all of them.

The target is finiteness of **distinct powered-value triples** `(A,B,C)=(x^p,y^q,z^r)` with `A+B=C`, positive bases, `gcd(x,y,z)=1`, exponents at least 2, and `σ=1/p+1/q+1/r<1`. The [earlier irreducible-signature reduction](optimized-signatures.md) shows it is enough to control all-prime hyperbolic signatures and `(2,4,ℓ)` with prime `ℓ≥7`; 19 other signatures are fixed and thus finite by Darmon–Granville.

## Attempted proof by contradiction

Assume infinitely many distinct triples. Bounded `C` gives only finitely many triples, so `C→∞` along a sequence. The powered values are pairwise coprime and `R=rad(ABC)=rad(xyz)`. The elementary estimate is

`R≤xyz<C^σ≤C^(41/42)`.                                          (1)

One might try to contradict (1) with an unconditional radical estimate. The reported Stewart–Yu estimate yields only `R>c(log C)^3/(loglog C)^9` for large `C`, with its exact displayed form checked here through a secondary source. That lower bound and (1) are compatible for arbitrarily large `C`. An **additional**, currently unproved, bound `C≤K R^(1+ε)` for one fixed `ε<1/41` would bound `C` and finish the proof; the strict threshold follows from `(41/42)(1+ε)<1`. [Detailed contradiction attempt](full-radical-contradiction.md); [independent review](review-full-radical-contradiction.md).

## Descent on both remaining infinite classes

For a repeated odd prime exponent, write `a^p+b^p=c^t`, where `t` is another prime. Cyclotomic factorization gives `a^p+b^p=(a+b)V`, with `gcd(a+b,V)` equal to 1 or `p`. In the first case `V` is a `t`th power; in the second, `V=pv^t` and `v_p(a+b)≡−1 (mod t)`. The same argument applies when the repeated exponent crosses the equality. These are necessary cofactor equations for varying `p,t`; they do not bound either prime. Pairwise-distinct-prime signatures, including `(2,3,ℓ)`, do not even share this factorization. [Detailed prime descent](full-prime-descent.md); [independent review](review-full-prime-descent.md).

For the other infinite class, primitive `x²+y⁴=z^ℓ` with prime `ℓ≥7` has opposite parity `x,y`, so the Gaussian factors `x±iy²` are coprime. Unique factorization in `Z[i]` gives `x+iy²=(a+bi)^ℓ`, `z=a²+b²`. Taking imaginary parts yields `y²=bU_ℓ(a,b)` with `gcd(|b|,|U_ℓ|)=gcd(|b|,ℓ)`. Consequently `b,U_ℓ` are same-sign squares, or both same-sign `ℓ` times squares. This reduces the class to a variable-index Lucas-type square equation; no established result used here excludes it uniformly. [Detailed Gaussian descent](full-gaussian-descent.md); [independent review](review-full-gaussian-descent.md).

## A uniform elliptic-curve obstruction

The curve `E:Y²=X(X−A)(X+B)` gives another way to seek the missing bound. Let `S=A²+AB+B²=C²−AB`. Its rational `j`-invariant is `256S³/(ABC)²`. Since `gcd(S,ABC)=1` and `(3/4)C²≤S<C²`, its logarithmic height satisfies the **uniform exact estimate**

`6log C+log(27/64)≤h(j)<6log C+log 256`.                 (2)

Odd primes of bad reduction are precisely the odd primes of `ABC`; the conductor exponent at 2 is universally bounded. Hence `N(E)≤K₂ R` for an absolute constant `K₂`. Combining (1) and (2) gives

`h(j)>(252/41)log N(E)−O(1)`, where `252/41=6+6/41`.      (3)

An unconditional upper bound `h(j)≤(6+ε)log N+O_ε(1)` for this family with any fixed `ε<6/41` would contradict (3) for an infinite sequence. No such theorem was established or verified in this attempt. The real bound `j>1728` and fixed-bad-prime finiteness do not imply it, because rational height and prime support can grow. [Detailed height–conductor attempt](full-height-conductor.md); [independent review](review-full-height-conductor.md).

## Exact stopping point

The proof stalls at the passage from the necessary equations (1)–(3) and the two descent formulas to a **uniform bound on all powered-value triples**. Finiteness for each fixed exponent signature, each fixed prime support, or each fixed Gaussian/Lucas index cannot control their infinite union. Replacing the missing step with an abc-strength radical or height–conductor estimate would assume an unproved result of the required strength. No complete mathematical proof emerged, so no Lean formalization was started.
