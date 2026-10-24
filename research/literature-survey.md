# Fermat–Catalan: varying-exponent literature survey (October 2026)

## Scope and exact question

The conjecture concerns primitive positive solutions of (a^p+b^q=c^r) with (p,q,r>1) and (1/p+1/q+1/r<1), counted as **distinct triples of powered values** ((a^p,b^q,c^r)). This qualification matters: (1^m+2^3=3^2) is the same powered-value triple for arbitrarily many (m>6). [Wikipedia's Fermat–Catalan entry](https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture) states the conjecture this way and lists ten known powered-value solutions as of 2024.

Poonen–Schaefer–Stoll, [*Twists of X(7) and primitive solutions to x²+y³=z⁷*](https://arxiv.org/abs/math/0508174), pp. 1–3, explain the divide: Darmon–Granville (1995) used descent and Faltings to prove finitely many primitive solutions for **each fixed** hyperbolic exponent signature. Varying all three exponents is stronger, and fixed-signature finiteness alone gives no uniform bound on the union.

## Unconditional results with varying exponents

Chen–Koutsianas, [*Darmon's Program: A survey*](https://arxiv.org/abs/2507.15149), §11, records several results that control *families* of signatures. The hypotheses are essential:

1. **(n,n,5), all (n\ge3), two congruence classes.** Survey Theorem 11.2 excludes nontrivial primitive integer solutions to (x^n+y^n=z^5) when either (2\nmid ab,5\mid ab), or (2\mid ab,5\nmid ab), where (a,b,c) denotes the proposed solution. Two classes remain outside the theorem: (2\mid ab,5\mid ab), where irreducibility is an obstacle, and (2\nmid ab,5\nmid ab), where elimination of a CM form is unresolved. This is a varying-exponent theorem but not a complete solution for the family.
2. **(r,r,n), fixed (r\in\{5,7,11,13\}), all (n\ge2), conditional on a divisibility *condition on the solution*.** Survey Theorem 11.5 excludes nontrivial primitive solutions to (x^r+y^r=z^n) when (2\mid(a+b)) **or** (r\mid(a+b)). The survey discusses Frey elliptic curves and higher-dimensional Frey abelian varieties; this does not settle signatures without that condition.
3. **(p,p,r), fixed regular prime (r), asymptotic and conditional on solution congruences.** Survey Theorem 11.1 excludes nontrivial primitive solutions to (x^p+y^p=z^r) for prime (p) sufficiently large relative to (r), provided (r\mid ab) and (2\nmid ab).

The same survey's Corollaries 11.4 and 11.8 obtain stronger *asymptotic* family exclusions only **assuming** a conjecture from Darmon's program. They should not be presented as unconditional results.

A newer arXiv **preprint**, Peter Chocian, [*The Primitive Generalized Fermat Equation x³+y⁵=z⁷: A computer-assisted proof*](https://arxiv.org/abs/2609.26996), v1 dated 22 September 2026, **claims** no nonzero primitive integer solutions for signature (3,5,7), using prior descent and modularity results plus computer-assisted exclusions. This is a claim by an unreviewed preprint, not an independently checked established theorem in this survey. Treat it as a high-priority verification item before marking that signature resolved in the database.

## A distinct conditional proof route through abc

The [abc conjecture](https://en.wikipedia.org/wiki/Abc_conjecture), if granted in its usual quantitative form, would imply Fermat–Catalan. Here is the uniformity argument, useful as a research map but **not an unconditional proof**.

Let (X=c^r=a^p+b^q) for a primitive positive solution. Then (a\le X^{1/p}), (b\le X^{1/q}), and (c=X^{1/r}), so

\[
\operatorname{rad}(abc)\le abc\le X^{\sigma},\qquad \sigma=1/p+1/q+1/r.
\]

For integer exponents greater than one with (\sigma<1), the maximum possible (\sigma) is (41/42), attained at ((2,3,7)) up to permutation. Quantitative abc gives (X\le K_\varepsilon\operatorname{rad}(abc)^{1+\varepsilon}\). Taking, for example, (\varepsilon=1/100) yields (X\le K_\varepsilon X^{4141/4200}\), hence (X^{59/4200}\le K_\varepsilon\). Thus (X) is uniformly bounded over all eligible signatures, and only finitely many powered-value triples can occur. The key gap is that abc itself is not a generally accepted theorem.

## Still open and a practical next review task

The surveyed unconditional theorems do not remove the solution congruence restrictions or cover all exponent families, so they do not prove the full Fermat–Catalan conjecture. Fixed-signature finiteness and bounded computational searches cannot substitute for uniform control over signatures.

**Independent review task:** read the original paper behind Survey Theorem 11.5 (follow its citation [17]/[19]), record for each (r=5,7,11,13) the exact statement and proof method, and construct a small ledger showing which congruence classes of ((a+b)\bmod 2r) are excluded and which remain. A second reviewer can reproduce this ledger from the paper before the database marks these families as resolved. In parallel, independently audit the certificates of the September 2026 (3,5,7) preprint rather than importing its claim as fact.
