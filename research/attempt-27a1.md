# Fermat–Catalan: the surviving 27a1 branch

**Scope and status.** Let `p≥17` be prime with `p≡2 (mod 3)`, and let positive pairwise coprime integers `a,b,c` satisfy `a²+b³=c^p`. Assume the solution's Frey curve belongs to the `27a1` branch of Freitas–Naskręcki–Stoll's level-lowering list. The argument below gives a new-to-this-ledger necessary condition on primes dividing `c`, but does not exclude the branch or prove Fermat–Catalan.

## Source boundary

[Freitas–Naskręcki–Stoll, Lemma 6.1](https://arxiv.org/pdf/1703.05058) eliminates the `27a1` branch for `p≡1 (mod 3)`, using a theorem on normalizers of **split** Cartan subgroups. For `p≡2 (mod 3)`, the CM curve `27a1` instead yields a non-split Cartan normalizer, and the authors explicitly state they lack the analogous result. Their Table 4 retains the `27a1` branch in all four eligible residue classes `5,11,17,23 (mod 24)`; its table applies to `p≥11`. Their §7.1 handles `p=11` by a separate computation, not by a uniform Cartan theorem. A positive solution has Frey `j=1728 b³/c^p∈(0,1728)`, but this real inequality alone does not classify rational points on the twisted modular curves.

## A prime-divisor filter within this branch

**Lemma.** Suppose a prime `q≥5`, `q≠p`, divides `c`. Let `a_q` be the Frobenius trace of the fixed elliptic curve `27a1: y²+y=x³−7` over `F_q`. Then

`p | ((q+1)²−a_q²)`.

If additionally `q≡2 (mod 3)`, then `a_q=0`, so `p | q+1`. Since `q` is odd, `q≡2 (mod 3)`, and `p≥17` is coprime to 6, this sharpens to `6p | q+1`. In particular, no such prime `q<6p−1` can divide `c` on this branch.

**Argument.** At `q≥5` dividing `c`, primitivity gives `q∤ab`. The Frey curve `E: v²=u³+3bu−2a` has `q`-adic unit `c₄=−144b` and minimal discriminant valuation `p v_q(c)`, so it has multiplicative reduction. The quadratic twist used in [Lemma 2.3](https://arxiv.org/pdf/1703.05058) has parameter in `{±1,±2,±3,±6}`; at `q≥5` this is an unramified twist, which may switch split and nonsplit multiplicative reduction, and does not change the divisibility of the discriminant valuation by `p`. For `q≠p`, the standard Tate-curve local representation then has unramified mod-`p` semisimplification with Frobenius trace congruent to either `q+1` or `−(q+1)`. Lemma 2.3 identifies its mod-`p` representation with `27a1[p]`; this fixed curve has good reduction at `q≥5`, so its trace satisfies `a_q≡±(q+1) (mod p)`, proving the first claim.

For `q≡2 (mod 3)`, cubing is a bijection on `F_q`. As `x` runs through `F_q`, `x³−7` runs through all residues once. Thus the number of affine pairs `(x,y)` satisfying `y²+y=x³−7` is exactly `q`: each of the `q` values of `y` determines one `x`. With the point at infinity, `#27a1(F_q)=q+1` and `a_q=0`. The divisibility simplifies to `p|(q+1)²`, hence `p|q+1` and, combining parity and `q≡2 (mod 3)`, `6p|q+1`.

This filter uses a standard local Tate-curve trace fact in addition to the paper's Lemma 2.3; it should be checked against that local theorem before promotion beyond a research note. It is consistent with the source's uniform level-lowering route. The case `q=p` and primes `2,3` require separate local analysis.

## Why the route stops

The condition `p|q+1` allows arbitrarily large primes `q≡−1 (mod p)` in principle. Nothing here bounds `p`, `c`, or the number of supporting primes. The absence of a uniform non-split-Cartan rational-point theorem remains the global obstacle. A sharper next task is to combine this prime-divisor filter with the `2`- and `3`-adic conditions of Freitas–Naskręcki–Stoll for the `27a1` branch and test whether any congruence class of positive integral reconstructions is excluded uniformly. Until such a theorem is proved, this is partial work.
