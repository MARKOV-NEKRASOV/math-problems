# A valuation-profile lemma for repeated odd exponents

**Result: a proved infinite-family exclusion, not a proof of Fermat–Catalan.** An elementary cyclotomic factorization removes an entire residue class of primitive repeated-odd-prime signatures, including the orientation in which the equal-exponent terms straddle the equality. Combining it with the earlier simultaneous-factor gap gives a stronger size obstruction in the positive `(3,3,t)` branch.

## Exact valuation-profile lemma

Let `p` be an odd prime, `t>=2` an integer, and let `a,b` be nonzero coprime **signed** integers such that `a^p+b^p=c^t>0` for an integer `c>0`. Put `U=a+b` and `V=(a^p+b^p)/(a+b)`. Then `U,V>0`, `gcd(U,V)|p`, and there exists an integer `u>=1` such that

- if `p∤U`, then `U=u^t`;
- if `p|U`, then `U=p^(t-1)u^t`.

In the latter case `V=pv^t` for an integer `v>=1` with `p∤v`. In the former case `V=v^t`.

**Proof.** The map `x↦x^p` is strictly increasing on the reals, so `a^p+b^p=a^p−(−b)^p` and `a+b=a−(−b)` have the same sign. The numerator is positive, hence `U>0` and `V>0`. Modulo `U`, substitute `a≡−b`: `V≡p b^(p−1) (mod U)`. Since `gcd(U,b)=gcd(a,b)=1`, `gcd(U,V)|p`. If `p∤U`, the two positive factors `U,V` of `c^t` are coprime and hence each is a t-th power. If `p|U`, the odd-prime LTE formula applies because `p∤ab`, giving `v_p(a^p+b^p)=v_p(U)+1` and therefore `v_p(V)=1`. The total p-valuation is divisible by `t`, so `v_p(U)=tm−1` for some integer `m>=1`. Every prime `q≠p` dividing `U` has `v_q(U)` divisible by `t` because `q∤V`. Taking `u` with `v_p(u)=m−1` and `v_q(u)=v_q(U)/t` for each `q≠p` gives `U=p^(t−1)u^t`. At p, `V` has valuation one and, at all other primes, valuations divisible by t, so `V=pv^t` with `p∤v`. □

## Direct Fermat–Catalan exclusions

If `a,b` are odd, `U` is even and `p` is odd. The lemma forces **`2^t|a+b`** in both branches. Hence no primitive signed repeated-odd-prime solution with odd `a,b` can have `a≡b (mod 4)`, because then `v_2(a+b)=1`. This removes a complete parity residue family for every odd `p` and every eligible odd prime `t`, independent of their sizes. For positive `a,b` on the same side, this says their odd bases must have **opposite** residues modulo 4. When the equal-exponent powers straddle the equality, write the original positive bases as `a,B` with `a>B` and signed `b=−B`; then `4|a−B` requires `a≡B (mod 4)`. Thus the opposite-residue class is excluded in that orientation. The condition does not apply when the two bases have opposite parity.

For the **positive-left** primitive `(3,3,t)` case with `a,b` odd and prime `t>=5`, one can say more. If `3∤U`, write `U=u^t` with even `u`. The earlier [simultaneous-factor lemma](simultaneous-factor-lemma.md) proves `u=2` impossible, so `u>=4` and `a+b>=4^t`. If `3|U`, the profile gives `U=3^(t−1)u^t` with even `u>=2`; hence `U>=3^(t−1)2^t>=4^t` for `t>=3`. Thus every such hypothetical positive-left solution satisfies

`a+b >= 4^t`.

This bound excludes the entire range `a+b<4^t` for odd positive inputs at every eligible prime `t`, but permits arbitrarily large inputs. For signed inputs, only the `2^t|U` conclusion is asserted: the clean-branch archimedean gap that excludes `u=2` relies on both p-th-power inputs being positive.

**Unit bases.** The factorization and parity statement allow one of `|a|,|b|` to equal 1; no unproved nonunit condition is used. The positive-left `a=b=1` case gives 2 and is not a t-th power for `t>=2`. The separately established Catalan-theorem analysis in [attempt-modular.md](attempt-modular.md) handles the finitely many distinct Fermat–Catalan powered-value triples with a unit base.

As a diagnostic check, the gcd and 2-adic valuation identities were also verified by exact integer arithmetic for all signed coprime odd `a,b` in `[-19,19]` with `a+b>0`, and `p∈{3,5,7,11}`. This bounded check is not part of the proof.

The proof uses only cyclotomic factorization, the odd-prime LTE formula, and the earlier reviewed real-size lemma. It does not use the questioned arXiv:2509.18275v1 claim. It excludes a residue family and a size range, not all repeated-prime signatures or the full conjecture. No Lean formalization was attempted.
