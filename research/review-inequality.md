# Peer review of `/tmp/fc-inequality-attempt.md`

**Verdict:** The stated mathematical deductions are correct. The note clearly labels its finiteness argument as conditional on abc; it does not claim a proof of Fermat–Catalan.

- The maximal hyperbolic reciprocal sum is indeed `41/42`, attained by the sorted signature `(2,3,7)`. All cases in Lemma 1 cover the possible sorted integer exponents.
- Primitivity makes the three bases, hence `A,B,C`, pairwise coprime. The radical identity and the strict inequality `rad(ABC)<C^(41/42)` follow as written.
- The abc calculation is correct: `(41/42)(1+1/42)=1763/1764`, so a single uniform abc constant bounds `C`. With bounded positive `C`, only finitely many powered-value triples occur.
- The FLT reduction for `gcd(p,q,r)≥3` is sound. If either summand base is 1, the equation gives consecutive perfect powers; Mihăilescu leaves `8` and `9`, so `(1,8,9)` and its swapped form are the only powered-value triples in this case. A unit base on the right is impossible.
- Darmon–Granville supplies finiteness per fixed hyperbolic signature, not a bound uniform across signatures. The distinction is correctly maintained.

**Minor clarifications:** The phrase “a restricted abc estimate with exponent strictly below `42/41` ... would suffice” should explicitly require a *single constant uniform over all solutions/signatures*. Also, attribute the count of distinct powered-value triples primarily to the Fermat–Catalan overview; Poonen–Schaefer–Stoll §1.2 chiefly treats the fixed-signature generalized Fermat equation. These are precision edits, not flaws in the proof attempt.

**Unresolved obligation:** Nothing here supplies the uniform upper bound on `C` or the exponent signatures. The unconditional argument stops at the lower bound `C>rad(ABC)^(42/41)`.
