# Independent review: finiteness of the variable `(2,4,p)` family

**Verdict:** The orientation argument in `reduction-to-prime-signatures.md` is sound. Using Ellenberg Theorem 4.1 and Bennett–Skinner Theorems 1.1–1.2, the unordered `(2,4,p)` class with prime `p≥7` contributes only finitely many positive primitive powered-value triples. This does **not** prove Fermat–Catalan; all-prime signatures remain an infinite uncontrolled class.

## Primary-source checks

I inspected the PDFs of Ellenberg [arXiv:math/0311497v1, Theorem 4.1](https://arxiv.org/pdf/math/0311497v1) and Bennett–Skinner [DOI 10.4153/cjm-2004-002-2, Theorems 1.1–1.2](https://doi.org/10.4153/cjm-2004-002-2). Ellenberg proves that coprime integer `A⁴+B²=C^p` with `p≥211` has `AB=0`. Bennett–Skinner Theorem 1.1 says that `X^n+Y^n=2Z²` has no nonzero pairwise-coprime integer solution for `n≥7`; its listed `C=2` exceptions have exponents 4 or 5. Their Theorem 1.2 says that for prime `n≥7`, `X^n+2^αY^n=Z²` with `α≥2` has no nonzero pairwise-coprime integer solution when `XY≠±1`; its possible `n≤C` caveat is vacuous for `C=1`.

The Poonen–Schaefer–Stoll [Table 1 and caption](https://arxiv.org/pdf/math/0508174v1) independently label signed-integer `(2,n,4)` solutions as determined via Bennett–Skinner. I did not rely on the table alone: the factorization below supplies a direct implication from the two primary Bennett–Skinner statements.

## Signed `(2,p,4)` factorization audit

Let nonzero, pairwise-coprime integers `a,b,c` satisfy `a²+b^p=c⁴`, with odd prime `p≥7`. Set `U=c²+a`, `V=c²−a`; then `UV=b^p` and `U+V=2c²`. Pairwise coprimality of `a,c` gives `gcd(U,V)|2`. Since `b≠0`, both factors are nonzero.

If `a,c` have opposite parity, `U,V` are odd and coprime. Because their product is a signed odd-prime power, each is a signed `p`th power: `U=u^p`, `V=v^p`. Thus `u^p+v^p=2c²`. Any common prime of `u,v` would divide both `U,V`, and any prime dividing `u,c` would divide `v` via the displayed sum; hence `u,v,c` are pairwise coprime. Bennett–Skinner Theorem 1.1 rules out this solution for `p≥7`. The theorem phrases solutions with `X>Y`; exchanging `u,v` supplies that ordering unless `u=v`, in which case `a=(U−V)/2=0`, forbidden.

If `a,c` are both odd, `U,V` are both even and have gcd exactly 2. Write `U=2u`, `V=2v`. Then `gcd(u,v)=1`, `u+v=c²` is odd, so one of `u,v` is even. Also `uv=b^p/4`, with even `b`. For the odd factor, all prime valuations are divisible by `p`, so it is a signed `p`th power, say `v_0^p`. For the even factor, its 2-adic valuation is `p v₂(b)−2 ≡ p−2 (mod p)` and all odd-prime valuations are divisible by `p`, so it is `2^{p−2}u_0^p`. Consequently `v_0^p+2^{p−2}u_0^p=c²`. Since `u,v` are coprime and sum to `c²`, their roots `u_0,v_0,c` are pairwise coprime. Bennett–Skinner Theorem 1.2 applies with `n=p`, `C=1`, `α=p−2≥5`, unless `u_0v_0=±1`.

In that exceptional unit case, `u_0,v_0∈{±1}` and `c²=±1±2^{p−2}`. Terms `1−2^k` and `−1−2^k` are negative; `2^k−1≡3 (mod 4)` for `k=p−2≥5`, so it is not a square. For `1+2^k`, `(c−1)(c+1)=2^k` forces two powers of 2 differing by 2. The only positive odd-square solution is `c²=9=1+2³`; thus none occurs for `k≥5`. If `a,c` are both even, primitivity fails. This exhausts signed `(2,p,4)` with nonzero bases.

## Orientations and finiteness

The output-prime positive orientation `a⁴+b²=c^p` is ruled out for `p≥211` by Ellenberg; the finite set of primes `7≤p<211` gives finitely many powered triples by Darmon–Granville fixed-signature finiteness. The output-fourth positive orientation `a²+b^p=c⁴` is ruled out for every prime `p≥7` by the signed argument. The output-square positive orientation `a⁴+b^p=c²` rearranges to `c²+(-b)^p=a⁴`, a signed `(2,p,4)` equation, and is also ruled out. Swapping the left summands creates no new orientation. Hence the `(2,4,p)` family is finite overall.

**Remaining full-conjecture gap:** All-prime hyperbolic signatures, such as `(2,3,p)` for every prime `p≥7`, are untouched by this theorem. The 19 fixed composite signatures are finite, but neither this review nor the four attempted global methods bounds the all-prime union.
