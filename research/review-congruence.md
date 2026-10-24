# Peer review of `fc-congruence-second.md`

**Verdict:** The mod-4 exclusion, factorization lemma, and cited counterexamples are correct. The mod-8 list needs one symmetric case to be complete. None of the results proves Fermat–Catalan.

## Correction

In Lemma 3, add: **if `p` is odd and `q` is even, then `a ≡ 7 (mod 8)`**. Since an odd square is 1 modulo 8, `a^p+b^q ≡ a+1`; with `r>=3` and even `c`, this must be 0 modulo 8. The existing even-`p`, odd-`q` case correctly gives `b ≡ 7 (mod 8)`. The both-odd case correctly gives `a+b ≡ 0 (mod 8)`.

## Checks

- Pairwise coprimality follows from `gcd(a,b,c)=1` and the equation. If `p,q` are even and both input bases odd, the left side is 2 modulo 4, while the right side is odd or 0 modulo 4. Pairwise coprimality then leaves exactly one even input base.
- In Lemma 4, `U=c^s-a` and `V=c^s+a` are positive odd integers. Every common divisor divides `2c^s` and `2a`; since it is odd and `gcd(c,a)=1`, `gcd(U,V)=1`. Unique factorization of `UV=b^q` therefore gives `U=u^q`, `V=v^q` and `b=uv`. The `b`-odd condition is essential. The statement includes algebraic cases outside the conjecture's hyperbolic region (`s=1`, for example); this is harmless, but applications should impose `1/2+1/q+1/(2s)<1`.
- `2^5+7^2=3^4` is primitive; its reciprocal sum is `19/20`. Replacing output exponent 4 with 2 changes that sum to `6/5`. In its swapped form `7^2+2^5=3^4`, the factors are `3^2-7=2` and `3^2+7=16`, with gcd 2, showing concretely why the odd-`b` splitting cannot be used.
- Both reported positive solutions to `x^2+y^3=z^7`, namely `(2213459,1414,65)` and `(15312283,9262,113)`, satisfy the equation and are primitive. They match the positive entries in Poonen–Schaefer–Stoll Theorem 1.1. The search bound `z<=120` is illustrative only; the theorem, not the search, establishes completeness.

**Source check:** Poonen–Schaefer–Stoll Theorem 1.1 and §1.2 support the fixed-signature claims and the two large solutions. The cited Darmon–Granville DOI matches the Bulletin of the London Mathematical Society paper listed in their bibliography.
