# A full-conjecture attempt through Gaussian descent on the (2,4,prime) family

**Subsequent source check:** This variable family is finite by the [Bennett–Skinner and Ellenberg reduction](reduction-to-prime-signatures.md). The calculation below is a valid earlier descent but is no longer the strongest known input for this family.

**Outcome: no full proof.** The latest exponent reduction leaves two infinite classes: all-prime hyperbolic signatures, and `(2,4,ℓ)` for primes `ℓ≥7`. I targeted the second class. A Gaussian factorization gives a uniform, exact necessary condition for every prime `ℓ`, but it does not bound `ℓ` or rule out solutions. Even an elimination of this entire class would leave the all-prime class, including `(2,3,ℓ)`, untouched.

## Exact descent for `x²+y⁴=z^ℓ`

Let `x,y,z` be positive and primitive, and `ℓ≥7` an odd prime. Primitivity plus the equation makes `x,y,z` pairwise coprime. Both `x` and `y` cannot be odd: then `x²+y⁴≡2 (mod 4)`, so `v₂(z^ℓ)=1`, impossible. Both cannot be even. Hence `x,y` have opposite parity and `z` is odd.

In the Gaussian integers,

`(x+i y²)(x−i y²)=z^ℓ`.

The two Gaussian factors are coprime. A common Gaussian prime divides both `2x` and `2i y²`; by `gcd(x,y)=1` it lies over 2, but `1+i` does not divide `x+i y²` because `x+y²` is odd. Unique factorization in `Z[i]` therefore gives `x+i y²=ε(a+bi)^ℓ` for a Gaussian unit `ε`. Since `ℓ` is odd, taking the `ℓ`th power permutes the four units, and `ε` can be absorbed into `a+bi`. Thus

`x+i y²=(a+bi)^ℓ`, `z=a²+b²`, `gcd(a,b)=1`, and `a,b` have opposite parity.

The imaginary part can be written

`y²=b U_ℓ(a,b)`, where

`U_ℓ(a,b)=Σ_{j odd, 1≤j≤ℓ} (-1)^((j−1)/2) * binom(ℓ,j) * a^(ℓ−j) * b^(j−1)`.

(The sign of `b` is unrestricted, while the right-hand product is positive.) Modulo `b`, `U_ℓ≡ℓ a^(ℓ−1)`. Since `gcd(a,b)=1`, any common prime divisor of `b` and `U_ℓ` is `ℓ`. If `ℓ|b`, the initial term has valuation exactly 1 at `ℓ`; all higher terms have valuation at least 2 because they contain `b²` and either another factor of `ℓ` in their binomial coefficient or the final high power of `b`. Hence `v_ℓ(U_ℓ)=1` and

`gcd(|b|,|U_ℓ|)=gcd(|b|,ℓ)`.

It follows that for integers `v,w≥1` and a common sign `δ∈{−1,+1}` one of two cases holds:

- If `ℓ∤b`, then `b=δ v²` and `U_ℓ=δ w²`.
- If `ℓ|b`, then `b=δ ℓ v²` and `U_ℓ=δ ℓ w²`. In this case `ℓ∤w`, as `v_ℓ(U_ℓ)=1`.

The Lucas form is `U_ℓ=((a+bi)^ℓ−(a−bi)^ℓ)/(2bi)`. Thus any solution would create a square or `ℓ` times a square at a variable prime index in a Lucas-type sequence whose parameters `a,b` also vary.

## Why this does not finish the proof

The factorization proves a necessary condition, not the nonexistence of its integer solutions. In particular, the inference that `U_ℓ` must have an odd-valuation prime factor is unsupported. A primitive-prime-divisor theorem, even if applied, supplies a new prime divisor of `U_ℓ`; it does not automatically say that its valuation is odd. It can divide a square with even valuation. Local congruences for an individual `ℓ` do not give a uniform exclusion over all prime `ℓ` either.

The integer `a` and the square parameter `v` remain free, while the degree of `U_ℓ` grows with `ℓ`. Fixed-`ℓ` Thue or curve methods cannot be summed over infinitely many prime indices without a uniform theorem. No such theorem was established in this attempt, and the all-prime signature class is separate. Therefore the full Fermat–Catalan conjecture remains unproved; no Lean formalization was attempted.

## Reproducible algebra check

The valuation and gcd claims above follow directly from the displayed binomial expansion. For example, at `ℓ=7`, `U_7=7a^6−35a^4b²+21a²b⁴−b⁶`, so if `7|b` but `7∤a` its 7-adic valuation is exactly 1. This is an illustration of the general proof, not numerical evidence for the conjecture.
