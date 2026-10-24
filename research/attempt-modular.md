# Fermat–Catalan: unconditional reduction and attempted modular route

## Exact target

Let \(x,y,z\) be positive integers with \(\gcd(x,y,z)=1\), and let \(p,q,r\ge2\) be integers such that
\[
x^p+y^q=z^r,\qquad 1/p+1/q+1/r<1.
\]
The conjecture counts **distinct triples of powered values** \((x^p,y^q,z^r)\), not choices of bases and exponents. This distinction matters when a base is 1. Source: [Fermat–Catalan overview](https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture).

## Rigorous unconditional reductions

1. **The bases are pairwise coprime.** If a prime \(\ell\) divided both \(x\) and \(y\), the equation would give \(\ell\mid z^r\), hence \(\ell\mid z\), contradicting \(\gcd(x,y,z)=1\). The same argument applies to each pair.

2. **A unit base contributes only the powered-value triple \((1,8,9)\), up to swapping summands.** If \(x=1\), then \(z^r-y^q=1\), with \(q,r>1\). Mihăilescu's theorem on consecutive perfect powers forces \(y^q=2^3=8\) and \(z^r=3^2=9\). The hyperbolic condition then requires \(p>6\), but all those choices give the same powered-value triple. If \(y=1\), swap the first two entries. If \(z=1\), the equation is impossible. [Mihăilescu, *Primary cyclotomic units and a proof of Catalan's conjecture*](https://doi.org/10.1515/crll.2004.048) is the underlying theorem; the [Fermat–Catalan overview](https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture) notes this precise degeneracy.

3. **The three exponents cannot have a common divisor greater than 2.** Suppose an integer \(d\ge3\) divides \(p,q,r\). Put \(A=x^{p/d}\), \(B=y^{q/d}\), and \(C=z^{r/d}\). Then \(A^d+B^d=C^d\), contrary to Fermat's Last Theorem for positive integers. Thus \(\gcd(p,q,r)\in\{1,2\}\). Source for FLT: [Wiles, *Modular elliptic curves and Fermat's Last Theorem*](https://doi.org/10.2307/2118559), with the Taylor–Wiles companion paper.

4. **The common-divisor-2 case becomes a constrained primitive Pythagorean triple.** If \(\gcd(p,q,r)=2\), set \(A=x^{p/2}\), \(B=y^{q/2}\), \(C=z^{r/2}\). Then \(A^2+B^2=C^2\), and pairwise coprimality makes the triple primitive. Euclid's parametrization gives, up to swapping \(A,B\), \(A=m^2-n^2\), \(B=2mn\), \(C=m^2+n^2\) for coprime \(m>n>0\) of opposite parity. The remaining conditions demand that these three quantities equal powers with respective exponents \(p/2,q/2,r/2\). A quotient of 1 imposes no perfect-power restriction on that coordinate. This is a reduction, not a classification.

5. **A uniform exponent bound would be enough—and is the missing theorem.** After the unit-base case is removed, all bases are at least 2. If there existed an absolute \(B\) bounding \(p,q,r\) in every primitive solution, only finitely many exponent signatures would remain. Darmon–Granville gives finitely many primitive solutions for each fixed signature with reciprocal sum below 1, so the full conjecture would follow. Conversely, if there are only finitely many distinct powered-value triples with bases at least 2, each exponent is at most \(\log_2\) of its powered value, so a bound \(B\) exists. Thus, with the known fixed-signature theorem, **uniform exponent boundedness is equivalent to the non-unit-base Fermat–Catalan finiteness statement**. [Poonen–Schaefer–Stoll, §1.2](https://arxiv.org/pdf/math/0508174) explicitly cites the Darmon–Granville fixed-signature result.

## Route attempted and exact failure

I tried to partition signatures by their common exponent divisor and apply Fermat's Last Theorem or Euclid's parametrization. This eliminates every signature with a common divisor \(d\ge3\), and turns the \(d=2\) signatures into simultaneous perfect-power conditions on a Pythagorean parametrization. It does **not** control the \(d=1\) signatures. In particular, \((2,3,\ell)\) is eligible for every prime \(\ell\ge7\); these signatures have common divisor 1 and form an infinite family. The detailed modular and descent methods for \((2,3,7)\) in [Poonen–Schaefer–Stoll](https://arxiv.org/abs/math/0508174) solve that fixed case, not all \(\ell\).

An attempted shortcut asserting that one exponent must be 2 would assume the unproved Beal conjecture. The [Fermat–Catalan overview](https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture) states this equivalence. Even that shortcut would leave infinitely many \((2,3,\ell)\) signatures.

**Next obligation:** Find an unconditional argument that bounds exponents for non-unit primitive solutions, or a different uniform finiteness theorem across the infinite signature family. The current common-divisor and fixed-signature methods do not provide one. No proof of Fermat–Catalan has been obtained here. Formalization is deferred until a complete mathematical proof is found.
