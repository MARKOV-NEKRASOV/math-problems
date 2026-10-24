# Peer review of `fc-modular-attempt.md`

**Verdict:** The stated reductions are mathematically sound, with one wording correction below. They do not prove Fermat–Catalan; the note identifies the missing uniform step correctly.

1. Pairwise coprimality, the unit-base case via Mihăilescu, and exclusion of a common exponent divisor at least 3 via Fermat's Last Theorem are correct. For a unit summand, `(1,8,9)` is one powered-value triple even though every exponent on 1 greater than 6 gives another representation.
2. The primitive Pythagorean reduction and Euclid parametrization are correct. Replace “these three quantities be perfect powers” with “these three quantities equal powers with respective exponents `p/2`, `q/2`, `r/2`.” A quotient may equal 1 (for example, `p=2`), in which case that coordinate has **no** perfect-power restriction. This distinction matters if the reduction is used for a descent or sieve.
3. The uniform-exponent-bound equivalence is correct for non-unit bases **using** Darmon–Granville fixed-signature finiteness. It supplies no bound itself. The converse uses `x,y,z >= 2`, so each exponent is bounded by the base-2 logarithm of its powered value.
4. The source attributions are appropriate: the cited Fermat–Catalan overview states both the unit-base degeneracy and the Beal equivalence; Poonen–Schaefer–Stoll §1.2 invokes Darmon–Granville for a fixed signature. Wiles plus Taylor–Wiles underpins the invoked FLT result. Euclid parametrization is classical and needs no specialized paper.

**Remaining obligation:** Produce an unconditional bound on exponents for non-unit primitive solutions, or another theorem that controls all varying signatures. The infinite eligible family `(2,3,l)` for primes `l >= 7` demonstrates why these reductions alone cannot finish the conjecture. Formalization is deferred until a complete proof is found.
