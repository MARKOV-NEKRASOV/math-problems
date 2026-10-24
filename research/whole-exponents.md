# Full Fermat–Catalan proof attempt: uniform exponent reduction

**Result:** An unconditional reduction covers every eligible signature by prime exponents at least 7 and a finite list of small exponents. This does **not** prove finiteness: the reduced signatures still include infinite families such as `(2,3,ℓ)` for all primes `ℓ≥7`.

## Exact target

For positive `x,y,z`, primitive `gcd(x,y,z)=1`, and integers `p,q,r>1` with `x^p+y^q=z^r` and `1/p+1/q+1/r<1`, show that only finitely many **distinct powered-value triples** `(x^p,y^q,z^r)` occur. Counting exponent tuples would be false because `1^m+2^3=3^2` for every `m>6` gives the same powered-value triple. See [Poonen–Schaefer–Stoll, Introduction §1.2](https://arxiv.org/abs/math/0508174) for the generalized Fermat setting and [the Fermat–Catalan overview](https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture) for the distinct-triple convention.

## Lemma: a prime-or-small divisor for every exponent

Let `F={8,9,10,12,15,25}`. For every integer `n≥7`, there is a divisor `d|n` with `d≥7` such that either `d` is prime or `d∈F`.

**Proof.** If `n` has a prime divisor at least 7, choose it. Otherwise `n=2^a3^b5^c`. If `a≥3`, choose 8; if `b≥2`, choose 9; if `c≥2`, choose 25. In the remaining range `a≤2,b≤1,c≤1`, choose 10 when `a,c≥1`, 15 when `b,c≥1`, or 12 when `a=2,b=1`. If none applies, `n` is at most 6, contrary to `n≥7`. Every chosen number divides `n`.

For `2≤n≤6`, set `d=n`. Thus every exponent can be reduced to a divisor in

`D={2,3,4,5,6,8,9,10,12,15,25} ∪ {primes ℓ≥7}`,

with `d≥7` whenever `n≥7`.

## Lemma: simultaneous reduction preserves the conjecture's hypotheses

Choose such divisors `p'|p`, `q'|q`, `r'|r`, and set `X=x^(p/p')`, `Y=y^(q/q')`, `Z=z^(r/r')`. Then `X^p'+Y^q'=Z^r'`, the powered-value triple is **identical**, and `gcd(X,Y,Z)=1`. Also `1/p'+1/q'+1/r'<1`:

- If all three reduced exponents are at least 7, their reciprocal sum is at most `3/7<1`.
- If exactly one is in `{2,3,4,5,6}`, the sum is at most `1/2+2/7<1`.
- If exactly two are in `{2,3,4,5,6}`, they cannot both equal 2, because a reduced exponent 2 can only come from an original exponent 2: the original exponent triple would then contain two 2s and could not be hyperbolic. The largest remaining reciprocal pair is `(2,3)`, giving at most `1/2+1/3+1/7=41/42<1`.
- If all three are at most 6, reduction changes none of them, so the original strict inequality applies.

Thus every Fermat–Catalan powered-value solution has an equivalent representation with exponents in `D`. This proof includes unit bases, since exponent changes on 1 do not alter powered values.

## Attempted closing step and failure

One might hope that `D` is finite and invoke the Darmon–Granville theorem, which gives finitely many primitive solutions **per fixed hyperbolic signature** (as explained in Poonen–Schaefer–Stoll §1.2). But `D` contains every prime `ℓ≥7`. In particular, `(2,3,ℓ)` lies in `D^3` and is hyperbolic for each such prime. The reduction supplies no bound on `ℓ`, nor a theorem controlling the union of its fixed-signature solution sets. A countable union of finite sets can be infinite. Replacing this missing step by “large primes have no solutions” would assert precisely the new uniform result that must be proved.

A second tempting shortcut is to say some exponent must be 2. That is at least as difficult as the unresolved Beal conjecture for primitive non-unit solutions with all exponents above 2; it cannot be used as a lemma. Likewise, Fermat's Last Theorem excludes a common divisor at least 3 of **all three** exponents, not solutions with three unrelated prime exponents.

**Exact remaining obligation:** Prove unconditional uniform finiteness for the canonical signatures in `D^3`, especially the infinite prime families such as `(2,3,ℓ)`, or find a different argument that bounds the powered values or prime exponents. This exponent-reduction attempt does not prove Fermat–Catalan and has not been formalized in Lean, per the user's preference.
