# Independent review: simultaneous exponent reduction for full Fermat–Catalan

**Verdict:** I found no counterexample to the reduction in `research/whole-exponents.md`. The divisor lemma, preservation of primitivity and powered values, and hyperbolicity case split are sound. The result is a useful reparameterization, not a proof of finiteness.

1. **Divisor list.** Every `n≥7` either has a prime divisor `ℓ≥7`, or is of the form `2^a3^b5^c`. Exponents `a≥3`, `b≥2`, or `c≥2` give respective divisors `8,9,25`. When `a≤2,b≤1,c≤1`, a number at least 7 must contain `2·5=10`, `3·5=15`, or `2²·3=12`; otherwise it is at most 6. Thus `F={8,9,10,12,15,25}` is complete for the stated purpose. Boundary examples `14→7`, `49→7`, `20→10`, `36→9`, and `60→12` or `15` behave as claimed.

2. **Representations.** For each original exponent `n` and chosen `d|n`, replacing a base `u` by `u^(n/d)` preserves its powered value `u^n` exactly. Raising bases to positive integer powers preserves `gcd(x,y,z)=1`, including when a base is 1. Consequently the map covers the *same set of distinct powered-value triples*, even though it changes exponent tuples.

3. **Hyperbolicity.** For any original `n≥7`, the chosen divisor is at least 7; for `2≤n≤6`, the chosen divisor is unchanged. In particular, a reduced exponent 2 can occur only if the original exponent was 2. If two reduced exponents were 2, the original reciprocal sum would exceed 1, so that case is impossible. With exactly two small reduced exponents, the largest allowable reciprocal pair is `(2,3)`, and the third contributes at most `1/7`, totaling `41/42`. The other cases in the note are straightforward. This is the subtle point that prevents the otherwise invalid operation of reducing arbitrary exponents without preserving the hyperbolic inequality.

4. **Limits.** Darmon–Granville finiteness for each fixed signature does not finish the proof because `(2,3,ℓ)` remains eligible for infinitely many primes `ℓ≥7`. No theorem in the note bounds the number or height of solutions uniformly over these canonical signatures. The reduction can be stated as equality between the full set of eligible powered-value triples and the subset represented with exponents in `D`, but `D` is infinite.

**Small wording suggestion:** Explicitly mention in the proof that “reduced exponent 2 implies original exponent 2.” This makes the key hyperbolicity step immediately auditable. No Lean work was done.
