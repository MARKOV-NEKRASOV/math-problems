# Fermat–Catalan: a sharper reduction of all exponent signatures

**Result: a reduction, not a proof.** Every eligible powered-value triple has a representation whose unordered exponent signature is either (i) all prime, (ii) `(2,4,ℓ)` with prime `ℓ≥7`, or (iii) one of 19 fixed signatures below. These three classes still contain infinitely many all-prime signatures, so the full conjecture is not resolved.

## Target and allowable operation

Suppose positive integers `x,y,z` satisfy `x^p+y^q=z^r`, `gcd(x,y,z)=1`, `p,q,r≥2`, and `1/p+1/q+1/r<1`. Count the powered values `(x^p,y^q,z^r)`, not exponent tuples. If `d≥2` divides an exponent `n`, replace its base `u` by `u^(n/d)` and its exponent by `d`. This preserves its powered value, the equation, and primitivity. It is allowable only when the new reciprocal sum remains strictly below 1.

Keep applying allowable proper-divisor replacements. The sum of the three integer exponents strictly decreases, so the process terminates at an **irreducible signature**: no single exponent can be replaced by a proper divisor `d≥2` while preserving hyperbolicity. Every original powered-value triple has at least one such representation.

## Classifying irreducible signatures

1. For a hyperbolic signature, the other two exponents cannot both be 2. Their reciprocal sum is therefore at most `1/2+1/3=5/6`. Consequently, replacing any one exponent by **any divisor at least 7** keeps the reciprocal sum at most `5/6+1/7=41/42<1`. Thus an irreducible composite exponent `n≥7` has no proper divisor at least 7. The elementary divisor classification from [the previous full-scope attempt](whole-exponents.md) gives exactly `F={8,9,10,12,15,25}` for such composite `n`.
2. If an exponent `n∈F` has another exponent at least 7, replace `n` by its largest proper divisor, respectively `4,3,5,6,5,5`. The remaining exponent is at least 2, so the new reciprocal sum is at most `1/3+1/7+1/2=41/42<1`. Therefore **every other exponent beside a surviving member of `F` is at most 6**.
3. If an irreducible signature contains exponent 6 and another exponent at least 7, replacing 6 by 3 gives at most `1/3+1/7+1/2=41/42<1`. So 6 cannot coexist with a high exponent in an irreducible signature.
4. If an irreducible signature contains exponent 4 and another exponent at least 7, replacing 4 by 2 is allowed whenever the third exponent is at least 3, since `1/2+1/3+1/7=41/42<1`. Hence the third exponent must be 2. The high exponent is then either prime (giving `(2,4,ℓ)` with `ℓ≥7`) or belongs to `F`, which is included in the finite check below.

If no exponent is at least 7, all are in `{2,3,4,5,6}`. If a member of `F` occurs, the other two are in `{2,3,4,5,6}`. Thus every irreducible signature with a composite exponent, apart from the `(2,4,ℓ)` prime family, occurs in the finite set `T³` where `T={2,3,4,5,6,8,9,10,12,15,25}`. Checking each sorted hyperbolic triple in this finite set against proper divisors leaves **19** signatures:

| First two exponents | Third exponents |
| --- | --- |
| `(2,3)` | `8,9,10,12,15,25` |
| `(2,4)` | `5,6,8,9` |
| `(2,5)` | `6,9` |
| `(2,6)` | `6` |
| `(3,3)` | `4,6,9` |
| `(3,4)` | `4,5` |
| `(4,4)` | `4` |

The four all-prime minimal triples in `T³` are `(2,5,5)`, `(3,3,5)`, `(3,5,5)`, and `(5,5,5)`, giving **23** finite-set minimal signatures in all. Fermat's Last Theorem rules out `(3,3,6)`, `(3,3,9)`, `(4,4,4)`, and `(5,5,5)`, whose three exponents have a common divisor at least 3. Separately, **19** of the 23 are not eliminated by FLT; **16** of those 19 have a composite exponent. The 19 signatures in the table are counted by composite content, not by FLT exclusion. These counts do not assert solutions exist for any listed signature.

The finite check uses only exact rational arithmetic. This self-contained snippet reproduces the table and the 23/19 counts:

```python
from fractions import Fraction
from itertools import combinations_with_replacement
T = (2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 25)
def divisors(n):
    return [d for d in range(2, n) if n % d == 0]
def reciprocal_sum(xs):
    return sum((Fraction(1, x) for x in xs), Fraction(0))
minimal = []
for xs in combinations_with_replacement(T, 3):
    if reciprocal_sum(xs) >= 1:
        continue
    if all(reciprocal_sum(xs[:i] + (d,) + xs[i+1:]) >= 1
           for i, x in enumerate(xs) for d in divisors(x)):
        minimal.append(xs)
from math import gcd
from functools import reduce
assert len(minimal) == 23
assert len([xs for xs in minimal if reduce(gcd, xs) < 3]) == 19
exceptions = [xs for xs in minimal if any(divisors(x) for x in xs)]
assert len(exceptions) == 19
print(exceptions)
```

## What this does and does not prove

Darmon–Granville's fixed-signature theorem (as cited in [Poonen–Schaefer–Stoll §1.2](https://arxiv.org/abs/math/0508174)) gives finitely many primitive solutions for each of the 19 fixed composite-signature cases (three of which FLT already excludes). Therefore the full Fermat–Catalan conjecture is **equivalent** to finiteness of the union of powered-value triples represented by all-prime hyperbolic signatures together with the `(2,4,ℓ)` family for prime `ℓ≥7`. This is a sharper reduction than merely allowing each exponent separately to lie in an infinite canonical set.

It remains far from a proof: `(2,3,ℓ)` is an all-prime hyperbolic signature for every prime `ℓ≥7`, and no cited theorem bounds their union. The family `(2,4,ℓ)` is also infinite. Counting a finite number of fixed signatures, or arguing that each prime signature has finitely many solutions, cannot show their infinite union is finite. No Lean formalization was attempted under the user's preference.
