# Continued attempt at the full Fermat–Catalan conjecture

**Status, 25 October 2026: no complete proof.** Four agents first attacked the remaining all-prime signatures and independently reviewed their deductions. A second four-agent pass tested primitive divisors, Frobenius traces, radical optimization, and a stronger local modular bound. The conjecture concerns finitely many **distinct powered-value triples** `A+B=C`, where `A=x^p`, `B=y^q`, `C=z^r`, `gcd(x,y,z)=1`, and `1/p+1/q+1/r<1`. Earlier source-checked work reduces its unresolved infinite part to all-prime exponent signatures; the fixed composite signatures and the variable `(2,4,ℓ)` family contribute only finitely many triples.

## Attempted global contradiction

For a hypothetical infinite all-prime family, pass to a subsequence in which each coordinate exponent is fixed or tends to infinity. At least one tends to infinity by fixed-signature finiteness. The [escape-profile argument](all-prime-escape-profiles.md) gives `rad(ABC)<C^(5/6+o(1))` when exactly one exponent diverges, `rad(ABC)<C^(1/2+o(1))` when two diverge, and `rad(ABC)=C^o(1)` when all three diverge. Its [independent review](review-all-prime-escape-profiles.md) checks the quantifiers and the signed Siegel lemma: if exactly one exponent diverges while the other two are fixed, the prime support of that variable coordinate's base must escape every fixed finite set. None of these restrictions bounds the moving support.

For distinct prime signatures, the [branch analysis](distinct-prime-escape.md) gives sharper limiting reciprocal sums of `5/6`, `7/10`, `8/15`, or `12/35`, according to the two smallest fixed exponents. Its [review](review-distinct-prime-escape.md) checks the radical and Frey calculations. A [real-variable optimization](radical-constant-attempt.md) improves the radical bound to `rad(ABC)≤θ(p,q)C^σ`, where `θ(p,q)=(q/(p+q))^(1/p)(p/(p+q))^(1/q)<1`. The improved constant leaves the missing positive-power radical bound untouched. No unconditional height–conductor or abc-strength inequality checked here contradicts these escape profiles.

## Repeated-prime branch

For positive `a^p+b^p=c^t` with odd prime `p`, factor as `U=a+b` and `V=(a^p+b^p)/(a+b)`. The [size and local analysis](prime-cube-size-local.md), checked in its [review](review-prime-cube-size-local.md), derives an exact archimedean gap when `U` and `V` are both `t`th powers. It also constructs 3-adic solutions in the `3|U` branch for every prime `t≥5`, showing why the 3-adic valuation alone gives no contradiction. A [primitive-divisor attempt](primitive-divisor-attempt.md) forces a prime `Q≡1 (mod 2p)` with `Q^t|V`, hence `a+b>(2p+1)^(t/(p−1))`. It also shows why an earlier Eisenstein cofactor-power construction does not automatically satisfy the simultaneous `U` condition. These conclusions cover the positive-left orientation as stated and do not bound the moving exponents.

## `(2,3,p)` and the recent modular paper

For positive primitive `a²+b³=c^p`, Freitas–Naskręcki–Stoll compares a small quadratic twist of the Frey curve's residual `p`-torsion with one of seven fixed curves for prime `p≥11`. The [first modular attempt](prime-237-nonsplit.md) checks that the Frey curve has nonintegral `j` and hence is non-CM, but its mod-`p` comparison does not give a rational isogeny or fixed conductor. The [independent review](review-prime-237-nonsplit.md) improves the local conclusion: every prime `q≥5` dividing `c` satisfies

`q ≥ (√p − 1)²`.

The [all-seven-branch derivation](all-seven-roughness.md) gives the precise argument: for `q≠p`, `p` divides one of the positive factors `q+1±a_q(E_i)`, each at most `(√q+1)²` by Hasse; for `q=p` the displayed inequality is automatic. The seven comparison curves have good reduction at all `q≥5`. In particular, `5∤c` for `p≥11`. This is a uniform roughness condition on `c`, not an upper bound on `p` or `c`. A separate [trace-window attempt](trace-window-attempt.md) obtains exact trace agreement with `27a1` at certain small good primes, but the unbounded Frey conductor prevents an isogeny conclusion.

Hashimoto–Lido–Lombardo–Mascot–Parent, [arXiv:2608.10919v1](https://arxiv.org/abs/2608.10919v1), is a recent method for non-split Cartan curves. Its abstract, introduction, and Theorem 1.1 were inspected. It identifies the seven CM rational points at **level 13** and explicitly poses the all-sufficiently-large-level CM-only assertion as a question. Its paper-library record marks the reading as partial. Using it as a theorem for every varying `p` would insert an unproved Serre-uniformity step.

The [recent-paper audit in the roughness note](all-seven-roughness.md) also identifies a literal unit counterexample to the printed equation in Theorem 1 of Mihăilescu's [arXiv:2509.18275v1](https://arxiv.org/abs/2509.18275v1). Its paper-library record is marked *questioned*. A missing intended nonunit condition may explain the issue, but the printed theorem cannot currently be used as an exclusion lemma.

## Remaining proof obligation

The research still lacks an unconditional argument that bounds **all** moving prime exponents and supports in the all-prime signatures. The `(2,3,p)` modular filters and repeated-prime cyclotomic restrictions address proper subfamilies; the radical bounds are necessary conditions. No full mathematical proof has been found, so Lean formalization remains deferred under the user's instruction.

## Constructed lemmas and subproblems

The [lemma ledger](lemma-subproblem-ledger.md) now gives exact next targets and records four concrete checks. The [simultaneous-factor lemma](simultaneous-factor-lemma.md) excludes `a+b=2^t` in the clean positive `(3,3,t)` branch for prime `t≥5`. The [output-prime sieve](output-prime-sieve.md) proves that a fixed prime `q≥5` can divide the output base in only finitely many positive `(2,3,p)` powered triples; it also verifies the small primes `5,7,11` by direct finite-field point counts. A [fixed-gap finiteness theorem](fixed-gap-finiteness.md) allows arbitrary moving output prime support when `x−y` is fixed in `x²+y³=z^r`. Finally, an [explicit Frey-shaped family](trace-rigidity-counterexample.md) matches `27a1` at an arbitrarily long initial run of primes without being isogenous to it, showing that finite trace agreement alone cannot finish the modular route. Each result has a narrower scope than the full conjecture.
