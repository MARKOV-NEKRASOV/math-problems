# Independent review of the six composite `(2,3,n)` exceptions

**Verdict:** `research/six-exceptions.md` correctly distinguishes unconditional signed-integer classifications, a conditional `n=25` theorem, and implications for positive bases. It does not prove the full Fermat–Catalan conjecture.

## Primary-source checks

- [Brown, arXiv:0911.2932v3, Theorem 1.1](https://arxiv.org/abs/0911.2932) lists exactly 12 primitive integer triples for `x²+y³=z¹⁰`: `(±1,−1,0)`, `(±1,0,±1)`, `(0,1,±1)`, and `(±3,−2,±1)`. Every nontrivial one has negative `y`, so the conclusion “no positive-base solution for `n=10`” follows unconditionally.
- [Siksek–Stoll, arXiv:1309.4421v2, Theorem 1.1](https://arxiv.org/abs/1309.4421) lists only trivial triples and `(±3,−2,1)` for `x²+y³=z¹⁵`. Again, there is no positive-base solution. Its introduction also gives the divisibility reduction using `6,8,9,10,15,25` and prime exponents at least 7.
- [Freitas–Stoll, arXiv:2506.10667v1, Theorem 1.1](https://arxiv.org/abs/2506.10667) is explicitly **conditional** on the expected solutions to five degree-10 equations over sextic fields. The introduction says these five equations remain beyond current methods and resources even assuming GRH. Under the condition, only trivial and signed Catalan triples remain. The paper does not establish an unconditional no-positive-solution theorem for `n=25`; the ledger states this correctly.
- [Freitas–Naskręcki–Stoll, arXiv:1703.05058v3, Introduction](https://arxiv.org/abs/1703.05058) says `n=6` reduces to two rank-zero elliptic curves and lists the signed nontrivial solutions known for `n≥7`. Its signed `n=8` examples are `(30042907,−96222,43)` and `(1549034,−15613,−33)` when interpreted with the paper's signs. Neither has positive `x,y,z`. The ledger correctly avoids claiming it independently checked Bruin's complete classification. The positive `n=9` equality `13²+7³=2⁹` checks arithmetically.

## Reduction and quantifiers

The six composite exponents `8,9,10,12,15,25` are indeed the composite `n≥7` with no proper divisor `d≥7`: any other composite `n≥7` has a proper divisor at least 7 (equivalently, is divisible by one of the listed six or a prime at least 7). The `n=12` reduction to `n=6` preserves positive bases and primitivity through `z¹²=(z²)⁶`; the reduced signature is parabolic, so the ledger appropriately treats it separately from the hyperbolic-divisor reduction. Brown and Siksek–Stoll's signed classifications justify their positive conclusions; the `n=25` conditional theorem does not.

**Small wording refinement:** The row for `n=8` says the second identity “cannot be rearranged to a positive eighth-power RHS.” The exact signed `n=8` equation in Freitas–Naskręcki–Stoll has RHS `−33⁸`, which is negative; writing that explicitly would prevent confusion with `(-33)⁸=33⁸`. This is a clarity issue, not a mathematical error.

I did not inspect Bruin's original `n=8,9` papers or the original `n=6` classification. Those remain the ledger's stated source-review tasks.
