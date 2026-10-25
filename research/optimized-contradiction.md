# Fermat–Catalan: contradiction attempt from an infinite family

**Outcome: no proof of the conjecture.** The contradiction route gives a precise structural consequence of failure, but no established theorem rules that consequence out.

Let `A=x^p`, `B=y^q`, `C=z^r=A+B`, with positive bases, `gcd(x,y,z)=1`, exponents greater than 1, and `σ=1/p+1/q+1/r<1`. Count distinct powered-value triples `(A,B,C)`. The unit-base cases contribute only `(1,8,9)` and its swapped form by Mihăilescu, so an infinite counterexample family can be taken with `x,y,z≥2`. Primitive bases and the equation make `A,B,C` pairwise coprime.

## Step 1: force simultaneous escape

Assume infinitely many distinct triples exist. Every bounded set of heights `C` contains only finitely many triples. The canonical exponent reduction in `whole-exponents.md` represents every eligible powered-value triple with each exponent in `D={2,3,4,5,6,8,9,10,12,15,25} ∪ {prime ℓ≥7}`, without changing that triple or losing hyperbolicity. For each bound `M`, only finitely many canonical signatures lie entirely in `[2,M]`. Darmon–Granville gives finitely many primitive solutions per fixed hyperbolic signature (as stated in Poonen–Schaefer–Stoll §1.2), so only finitely many powered-value triples admit a reduced representation with all exponents at most `M`.

Likewise, for each `M`, there are only finitely many such triples whose radical `R=rad(ABC)` has all prime factors at most `M`. Indeed `u=A/C` and `v=B/C` are rational `S`-units with `u+v=1` for the fixed finite set `S={primes≤M}`; the S-unit theorem gives finitely many `(u,v)`. Each pair determines a unique primitive positive integer triple `(A,B,C)` after clearing denominators. This uses the established S-unit theorem, not a uniform bound as `S` varies.

Consequently one can choose a sequence of distinct hypothetical solutions such that, simultaneously, `C_i→∞`, the largest prime `P_i|R_i` tends to infinity, and at least one prime canonical exponent tends to infinity. For each `i`, discard the finite union of solutions with `C≤i`, `P≤i`, or admitting a reduced representation with all exponents≤`i`, then choose another solution. This simultaneous escape is rigorous; it is **not** a contradiction.

## Step 2: turn the sequence into high-quality abc triples

The hyperbolic reciprocal sum has the uniform maximum `σ≤41/42`. Since `x^p<C`, `y^q<C`, and `z^r=C`, we have

`R=rad(xyz)≤xyz<C^σ≤C^(41/42)`.

Thus `C>R^(42/41)`. Fix `ε=1/42`, so `1+ε=43/42` and `42/41−43/42=1/1722`. Every triple in the hypothetical sequence satisfies

`C / R^(1+ε) > R^(1/1722) → ∞`.

Therefore falsity of Fermat–Catalan would give an infinite, unbounded family of counterexamples to the usual quantitative abc inequality at one fixed positive epsilon. This is the contrapositive of the known conditional implication abc ⇒ Fermat–Catalan, made explicit with the radical escape above. **The abc conjecture is unproved; this implication cannot finish the contradiction.**

## Exactly where shortcuts fail

- Finiteness for each signature does not make the infinite union finite. The canonical signatures retain `(2,3,ℓ)` for every prime `ℓ≥7`.
- Finiteness for each fixed prime set `S` does not bound an infinite union over moving supports. The simultaneous escape lemma explicitly permits `P_i→∞`.
- Passing to a subsequence with a fixed smallest exponent (e.g. `2`) does not fix the other exponents; nor must the smallest exponent be fixed. Diagonal subsequences may have one, two, or three exponents diverging.
- Stewart–Yu's known unconditional abc-type estimate only gives a polylogarithmic lower bound on `R` in terms of `C`, compatible with `R<C^(41/42)` for unbounded `C`.

**Missing theorem:** an unconditional abc-strength bound for these special perfect-power triples, or another mechanism that bounds their heights or canonical prime exponents uniformly. The two escape statements and high abc-quality are necessary properties of a hypothetical counterexample family, not a disproof of its existence.

Sources: Poonen–Schaefer–Stoll, arXiv:math/0508174, Introduction §1.2; Evertse, *On equations in S-units and the Thue–Mahler equation*, DOI 10.1007/BF01388644; `whole-exponents.md` and `whole-height.md` for the reviewed reductions cited here.
