# Fermat–Catalan: elementary and congruence route

**Scope.** Let positive integers `a,b,c` and exponents `p,q,r > 1` satisfy
`a^p + b^q = c^r`, `gcd(a,b,c)=1`, and `1/p+1/q+1/r<1`. The conjecture concerns
finitely many **distinct triples of powered values** `(a^p,b^q,c^r)`, not finitely
many exponent tuples. No claim below proves the conjecture.

## Rigorous lemmas

1. **Primitive implies pairwise coprime.** If a prime divides both `a` and `b`,
   it divides `c^r`, hence `c`, contradicting primitivity. If it divides `a`
   and `c`, then it divides `b^q`, hence `b`; similarly for `b,c`. Thus
   `gcd(a,b)=gcd(a,c)=gcd(b,c)=1`. This justifies factoring arguments that use
   coprimality of two bases, not merely of all three at once.

2. **A mod-4 exclusion.** If `p` and `q` are even and `a,b` are odd, then
   `a^p+b^q ≡ 1+1 = 2 (mod 4)`. If `c` is odd, `c^r` is odd; if `c` is even,
   `c^r ≡ 0 (mod 4)` since `r≥2`. Both contradict the equation. Hence an
   even-even input signature requires exactly one of `a,b` to be even.

3. **A mod-8 refinement when the output is even.** If `a,b` are odd and `c`
   is even with `r≥3`, then `a^p+b^q≡0 (mod 8)`. For an odd base, an even
   exponent gives residue 1 mod 8, while an odd exponent gives the base's
   residue. Therefore: if both input exponents are odd, `a+b≡0 (mod 8)`;
   if `p` is even and `q` is odd, `b≡7 (mod 8)`; if `p` is odd and `q` is even, `a≡7 (mod 8)`; and if both are even the
   mod-4 exclusion already applies. These are necessary, never sufficient.

4. **Difference-of-squares reduction for one infinite signature family.**
   Suppose `a²+b^q=c^(2s)` with `q≥2`, `s≥1`, `b` odd, and the solution
   primitive. Let `U=c^s−a` and `V=c^s+a`. They are positive odd integers
   because `b^q` is odd, so `c^s` and `a` have opposite parity. Also
   `gcd(U,V)` divides `2c^s` and `2a`; by pairwise coprimality and oddness,
   `gcd(U,V)=1`. Since `UV=b^q`, unique factorization gives `U=u^q` and
   `V=v^q` for positive coprime `u,v`, with `b=uv`. Consequently
   `v^q−u^q=2a` and `v^q+u^q=2c^s`. This reduction works for arbitrary
   `q,s`, so it is useful across varying exponents, but the resulting
   perfect-power equations remain difficult. The `b`-odd hypothesis is
   essential because when `b` is even the two factors may share powers of 2.

## Counterexamples to shortcuts

- `1^m+2³=3²` holds for every `m>6`, with reciprocal sum below 1. These
  infinitely many exponent tuples all represent the same powered-value
  triple `(1,8,9)`. Counting exponent tuples would make the conjecture false
  by definition.
- `2⁵+7²=3⁴` is a genuine primitive solution (`32+49=81`) with reciprocal
  sum `19/20`. Reducing output exponent 4 to 2 by writing `(3²)²` gives
  exponent triple `(5,2,2)` with reciprocal sum `6/5>1`. Exponent reduction
  can leave the hyperbolic region and cannot be used without tracking it.
- The same solution written `7²+2⁵=3⁴` has an even second base, so the
  odd-`b` factorization lemma does not apply. It is a counterexample to
  ignoring the 2-adic case in a factorization strategy.
- A bounded search with `z≤120` for primitive positive `x²+y³=z⁷` finds
  `(2213459,1414,65)` and `(15312283,9262,113)`. The complete integer
  classification includes both (Poonen–Schaefer–Stoll, Theorem 1.1).
  A search only to `z≤100` misses the second; no finite search controls
  larger `z` without a proven bound. Script: [`fermat_catalan_237.py`](fermat_catalan_237.py).

## Research use and limitation

For each candidate exponent family, a shared agent ledger can record
pairwise-coprimality, parity, local residue exclusions, known complete
classifications, and unresolved cases. The mod-4/mod-8 rules above are cheap
filters. For families with two even exponents, the factorization lemma can
turn the problem into coprime perfect-power factors. Agents should retain
the discarded even-base cases as explicit subtasks. This may establish
partial results for signatures or families, but no local test or fixed
signature classification gives the uniform control over varying exponents
required by Fermat–Catalan. Darmon–Granville already gives finiteness for
each fixed hyperbolic signature; that is weaker than the conjecture.

## Sources

- Poonen, Schaefer, and Stoll, *Twists of X(7) and primitive solutions to
  x²+y³=z⁷*, Theorem 1.1 and Sections 1.2–1.3:
  https://arxiv.org/abs/math/0508174
- Darmon and Granville, *On the equations z^m=F(x,y) and Ax^p+By^q=Cz^r*:
  https://doi.org/10.1112/blms/27.6.513
- Fermat–Catalan conjecture overview (includes powered-value distinction,
  known solutions, and partial results):
  https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture
