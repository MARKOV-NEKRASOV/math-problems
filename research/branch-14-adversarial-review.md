# Cycle 14 adversarial audit (30 October 2026)

I read AGENTS.md and the three mandatory protocol notes, reviewed cycle 13's G-13 and B13.2, and independently read the primary arXiv:2605.02632v1 PDF text cached at /tmp/fc2605.txt, especially Proposition 5.1/5.2/5.6 and Theorem 6.1. This is a theorem/hypothesis check, not an audit of the external article's entire proof.

## G-13 semistability correction: prior adversarial objection refuted

Proposition 5.1 (PDF p.10) states good reduction for J_{2,r} at rational q if q∤2rAB(Aa²+Bb^r). It imposes no condition q∤ab. Proposition 5.2 states bad multiplicative reduction when q∤2rAB and q|Aa²+Bb^r. For A=B=C=1, Aa²+Bb^r=c^p. Hence, for every residual prime p>2r, every place above p is good if p∤c or multiplicative if p|c. This covers p|a and p|b as well. The cycle 13 restriction p∤ab resulted from an incorrect source reading and should be removed. The underlying old G-13 claim is recovered: fixed odd r≥7, even b, c with ℓ|c, ℓ∤2r, and p sufficiently large imply irreducibility by Theorem 6.1. Proposition 5.6 says the *curve* C_{2,r} has potentially good reduction at a place above 2 when v₂(b^r)≥6; good reduction of the curve after extension implies good reduction of its Jacobian. Theorem 3.3 supplies GL2 type. The paper's Corollary 6.1 proof uses a multiplicative prime ℓ to assert descent of all endomorphisms; I have not independently re-proved that assertion. Theorem 6.1 prints irreducible, whereas the paper's corollary prints absolutely irreducible; retain only irreducible.

## B14-W Wieferich-type necessary condition: proved

For primitive positive a²+b^r=c^p, odd prime r≥3, prime p>r, the bases are pairwise coprime. If p|b, then b^r≡0 mod p² and a²≡c^p mod p². Euler gives a^{2(p−1)}≡1 mod p². Since a^{p−1}≡1 mod p and the only roots of X²=1 mod p² are ±1, necessarily a^{p−1}≡1 mod p². If p|a, then a²≡0 mod p² and b^r≡c^p mod p². Euler gives (b^{p−1})^r≡1 mod p². Write b^{p−1}=1+kp mod p²; because p>r, rk≡0 mod p, so k≡0 and b^{p−1}≡1 mod p². These are necessary local restrictions only; no contradiction or upper bound follows. The p>r requirement is used in the second implication. It also implies p odd, so the first root argument is valid.

## B13.2 check and proof gate

For coprime odd y<z with x^p=z⁴−y⁴, one of z−y,z+y has v₂=1 and the other t≥2; v₂(z²+y²)=1. Hence p v₂(x)=t+2. Thus t≡−2 mod p and z>2^{t−1}≥2^{p−3}. This lower bound is correct but no upper bound is supplied. It does not close a branch.

All seven F2/F1/F0 escape profiles remain open. A complete F2 (2,r,p) proof still needs treatment of b odd with r|c, elimination of every residual comparison form, and uniformity as r grows. No Lean formalization is warranted.
