# Independent review of the full-conjecture height attempt

**Verdict:** The arithmetic in (1)–(5) and the failure diagnosis check out. No full Fermat–Catalan proof follows.

1. Pairwise coprimality and `R<C^σ` are valid for positive non-unit bases. The maximal eligible reciprocal sum is `41/42`.
2. Assuming the displayed Stewart–Yu estimate `log C<K R^(1/3)(log R)^3`, the two-case inversion is correct: for `L=log C` sufficiently large, `R>c L³/(log L)^9` with one absolute `c>0`. The primary Stewart–Yu article was not inspected; the note accurately says the displayed formula was checked against a secondary overview. The subsequent steps are conditional on that source attribution being correct, not on the unproved abc conjecture.
3. Taking logarithms of this lower bound and comparing with `R<C^σ` yields `σ>[log c+3loglog C−9logloglog C]/log C`, exactly (4). Since `σ≤3/m` for `m=min(p,q,r)`, (5) follows once its denominator is positive. The threshold implicit in `o(1)` is uniform because `c` is absolute. This bound is asymptotically smaller than `log₂ C`, but still grows without bound.
4. The proposed estimate (6) would imply a uniform bound on `C`: inserting `R<C^(41/42)` leaves the exponent `1−(41/42)η<1`. Conversely, finiteness of the set of powered-value triples yields such a constant for any chosen `0<η<42/41`. Specify that range of `η` for a positive exponent. The estimate is therefore a reformulation of the hard part on this restricted universe, not an available lemma.
5. The abc implication is clearly labeled conditional. Neither fixed-signature finiteness nor the polylogarithmic radical lower bound can close the varying-signature gap.

**Remaining obligation:** prove a genuinely unconditional power-scale radical/height estimate uniform over all Fermat–Catalan triples, or use a different global method. The note does not supply one.
