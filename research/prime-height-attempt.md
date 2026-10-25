# Full Fermat–Catalan attempt after reduction to all-prime signatures: asymptotic conductor and radical

**Outcome: no full proof.** The infinite-family hypothesis leads to a stronger abc-quality and elliptic height–conductor obstruction than the pointwise `41/42` estimate. The improvement comes from combining the reviewed reduction to all-prime signatures with Darmon–Granville finiteness for each *fixed* signature. None of the available unconditional upper bounds contradicts it.

Let `T=(A,B,C)=(x^p,y^q,z^r)` be a primitive positive powered triple, `A+B=C`, with all three exponents prime and `1/p+1/q+1/r<1`. Count distinct `T`, not representations. Discard unit-base triples, of which there are only finitely many powered triples by Mihăilescu. Let `R=rad(ABC)`, `L=log C`, and let `E_T:Y²=X(X−A)(X+B)` be the universal Frey curve. Pairwise coprimality makes exactly one of `A,B,C` even.

## A quantifier-safe escape lemma

For each integer `H`, only finitely many distinct `T` admit an all-prime eligible representation with `max(p,q,r)≤H`: there are finitely many ordered prime exponent signatures below `H`, and Darmon–Granville gives finitely many primitive solutions for each hyperbolic fixed signature. Define `M(T)` as the *minimum* of `max(p,q,r)` over eligible all-prime representations of `T`. This minimum exists for every such triple, even if representations are nonunique. Along any sequence of infinitely many distinct all-prime powered triples, `M(T)→∞` outside a finite initial set. Choose a representation attaining that minimum for each `T`.

Two exponents other than the largest `M` cannot both be `2`, because such a signature would not be hyperbolic. Their reciprocal sum is therefore at most `1/2+1/3=5/6`. Consequently

`σ=1/p+1/q+1/r ≤ 5/6+1/M(T)`, and `R≤xyz<C^σ≤C^(5/6+1/M(T))`.  (1)

This is valid even if the smaller exponents vary, repeat, or are chosen from different representations. It improves the universal `41/42` exponent *asymptotically along any hypothetical infinite family*. It does not say every individual Fermat–Catalan triple has reciprocal sum at most `5/6`.

By fixed-prime-set `S`-unit finiteness, `R→∞` along any infinite distinct sequence: bounded `R` fixes a finite set of primes and `A/C+B/C=1` then has finitely many primitive positive solutions. Hence `N_odd=R/2`, the product of the odd primes dividing `ABC`, also tends to infinity. At each such odd prime the Frey curve has multiplicative reduction with conductor exponent 1, so `N_odd` is exactly the odd conductor. The earlier exact calculation gives `h(j(E_T))=6L+O(1)` uniformly. Equation (1) therefore implies

`h(j(E_T)) ≥ [6/(5/6+1/M(T))] log N_odd−O(1) = (36/5−o(1))log N_odd`. (2)

A standard absolute bound on the 2-adic conductor exponent gives the same asymptotic statement with full conductor `N(E_T)` in place of `N_odd`; the odd-conductor formulation needs no sharp 2-adic constant.

## Optimizing the contradiction threshold

From (1), for any **fixed** `ε<1/5`,

`C/R^(1+ε) > C^[1−(1+ε)(5/6+1/M(T))] →∞`.                         (3)

Indeed `M(T)→∞`, so the exponent tends to `1−(1+ε)5/6>0`, and `C→∞`. For the concrete choice `ε=1/6`, once `M≥43` the exponent is at least `1/1548` (equality at `M=43`); hence an abc-type upper bound `C≤K R^(7/6)` uniform on these triples would bound `C`, and the finitely many signatures with `M<43` are already finite. At the boundary `ε=1/5`, this calculation yields no fixed positive exponent. Thus falsity of Fermat–Catalan would force an infinite family violating *every* fixed-ε abc inequality with `ε<1/5`, as well as elliptic height–conductor upper bounds with slope below `36/5`.

A finer signature split gives even larger conditional gaps. If `(2,3,M)` is excluded by an additional theorem, the two smaller primes in any remaining large-`M` signature have reciprocal sum at most `1/2+1/5=7/10`, giving asymptotic `h(j)/log N_odd≥60/7−o(1)`. If there are no exponents `2` or `3`, the pair sum is at most `2/5`, giving slope at least `15−o(1)`. These are conditional on excluding the indicated infinite families; no such exclusion has been proved here.

## Why this still fails as a full proof

The unconditional Stewart–Yu radical estimate used in the project is reported as `L<K R^(1/3)(log R)^3`; its exact form was corroborated only through a secondary source. It gives merely `R>c L³/(log L)^9`, compatible with (1) for unbounded `L`. Neither Faltings/Darmon–Granville nor fixed-`S` S-unit finiteness has constants uniform in the moving signatures or prime sets. No unconditional bound `C≤K R^(1+ε)` with `ε<1/5`, nor an unconditional upper elliptic height–conductor slope below `36/5` for this family, was established. Inserting either would assume the precise missing theorem.

The asymptotic threshold is a necessary property of a hypothetical infinite all-prime family, not a contradiction. The full Fermat–Catalan conjecture remains unproved, so no Lean formalization was attempted.
