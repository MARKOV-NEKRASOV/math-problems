# A uniform output-prime trace sieve for the (2,3,p) family

**24 October 2026 — Status: unconditional necessary condition under the published modular-reduction theorem; NOT a proof of Fermat–Catalan.** This continues [prime-signature-full-attempt.md](prime-signature-full-attempt.md), especially [prime-237-attempt.md](prime-237-attempt.md). A complete proof is still missing.

## Statement

Let (p\ge11) be prime and suppose positive integers (a,b,c) satisfy

[
a^2+b^3=c^p,\qquad \gcd(a,b,c)=1.
]

For **every** prime (q\ge5) dividing (c),

[
\boxed{p\le (\sqrt q+1)^2,\quad\text{or equivalently}\quad q\ge(\sqrt p-1)^2.}\tag{1}
]

More precisely, if (q\ne p), there exists a curve (F) in the **fixed seven-element set**

[
\{27\mathrm{a}1,54\mathrm{a}1,96\mathrm{a}1,288\mathrm{a}1,864\mathrm{a}1,864\mathrm{b}1,864\mathrm{c}1\}
]

such that its good-reduction Frobenius trace (a_q(F)) satisfies

[
\boxed{p\mid q+1-a_q(F)\quad\text{or}\quad p\mid q+1+a_q(F).}\tag{2}
]

In fact the **same** curve (F) works for all primes (q\ge5), (q\ne p), dividing (c) for a given solution, since it arises from one fixed residual representation. For a given prime (q\ge5), the finite list of prime divisors of the fourteen positive integers (q+1\pm a_q(F)) gives a necessary and effectively computable list of possible exponents (p\ne q) in solutions with (q\mid c). It is a necessary condition, **not** a sufficient condition.

## Proof

The Frey curve associated to this generalized Fermat equation is

[
E_{a,b}:Y^2=X^3+3bX-2a.
]

Its invariants are

[
\Delta(E_{a,b})=-2^6 3^3 c^p,\qquad c_4(E_{a,b})=-2^4 3^2 b.
]

For any (q\ge5) dividing (c), primitivity and the equation imply (q\nmid b); hence (v_q(c_4)=0). Thus (E_{a,b}) has multiplicative reduction, the Weierstrass equation is (q)-minimal, and (v_q(\Delta_{\min})=p,v_q(c)).

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Lemma 2.3 and Proposition 2.4 ([arXiv:1703.05058](https://arxiv.org/abs/1703.05058)), prove that for prime (p\ge11), a quadratic twist (E_{a,b}^{(d)}), with (d\in\{\pm1,\pm2,\pm3,\pm6\}), has mod-(p) Galois representation isomorphic to (F[p]) for one of those seven elliptic curves (F/\mathbb Q). In particular, all seven have good reduction at (q\ge5), and the quadratic twist is unramified there.

If (q\ne p), the Tate-curve description of the mod-(p) torsion of a curve with multiplicative reduction, whose minimal-discriminant valuation is divisible by (p), shows that the residual representation is unramified and has Frobenius eigenvalues (1,q), up to a common quadratic sign. Hence its trace is (\pm(q+1)\pmod p). Comparing with (F[p]) yields (2). Twisting may change the sign; that is why both signs are allowed.

Hasse's theorem gives (|a_q(F)|\le2\sqrt q). Therefore both integers (q+1\pm a_q(F)) are strictly positive, and each is at most (q+1+2\sqrt q=(\sqrt q+1)^2). Since (p) divides at least one, (p\le(\sqrt q+1)^2). If (q=p), this numerical inequality holds trivially. Rearranging gives (1), **including** (q=p). □

## Example: the 27a1 branch

For (F=27\mathrm{a}1), an integral model is (y^2+y=x^3-7). At every prime (q\ge5), (q\equiv2\pmod3), the cube map permutes (\mathbb F_q), so (\#F(\mathbb F_q)=q+1) and (a_q(F)=0). Consequently, on **this branch only**, if (q\mid c), (q\ne p), then (p\mid q+1), and (q+1) is divisible by 2 and 3. Since (p\ge11), it follows that (6p\mid q+1). This was already established in [attempt-27a1.md](attempt-27a1.md); it is repeated only as a cross-check. It cannot be applied to the other six branches.

The companion script `prime_output_trace_sieve.py` computes the trace by an exact Legendre-symbol sum and cross-checks it against direct point counting for small primes. It tests only this **one** named curve and proves nothing beyond the displayed identities.

## Consequence and attempted contradiction

Along any hypothetical sequence of primitive positive solutions (a_i^2+b_i^3=c_i^{p_i}) with prime (p_i\to\infty), every (q_i\ge5) dividing (c_i) must tend to infinity, because (1) gives (q_i\ge(\sqrt{p_i}-1)^2). In particular every fixed prime (q\ge5) is eventually forbidden from dividing (c_i). The already reviewed [fixed-output-support theorem](fixed-output-support.md) guarantees that solutions supported entirely on the fixed set ({2,3}) cannot produce infinitely many distinct powered-value triples. Thus, in a hypothetical infinite family with (p_i\to\infty), eventually (c_i) must contain a prime (q_i\ge5), and the new lower bound applies to such prime divisors.

This **does not** imply finiteness: the divisors (q_i) may grow with (p_i), and the modular method does not provide a uniform upper bound on them. Even the stronger congruence in the 27a1 branch permits arbitrarily large candidate primes. It also does not address other all-prime signatures ((3,3,t)), ((2,s,t)), or ((r,s,t)).

**Explicit unproved closing obligation:** show, without assuming abc or Frey–Mazur, that no infinite sequence of primitive positive solutions with simultaneously unbounded prime exponents and output prime support exists. (1) is a necessary restriction on such a sequence, not a contradiction.

## Source and validity boundary

- Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Mathematica **156** (2020), 77–113; [arXiv:1703.05058](https://arxiv.org/abs/1703.05058), Lemma 2.3, Proposition 2.4.
- Hasse's bound for elliptic curves over finite fields and the standard Tate-curve local (p)-torsion representation at multiplicative primes.
- This note is a **single-author mathematical argument pending independent review**, not a reviewed discovery, not a proof of the full conjecture, and not a Lean formalization.
