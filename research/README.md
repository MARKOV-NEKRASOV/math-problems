# Fermat–Catalan research notebook

The conjecture asks whether there are finitely many **distinct triples of powered values** satisfying (x^p+y^q=z^r), where the positive bases are coprime and (1/p+1/q+1/r<1). Varying an exponent on a base of 1 can repeat the same triple, so counting exponent tuples gives the wrong statement. See the [problem overview](https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture).

The latest [optimized attempt at the full conjecture](optimized-full-attempt.md) combines four reviewed routes. It narrows the remaining uniform problem to all-prime hyperbolic signatures and `(2,4,ℓ)` for prime `ℓ≥7`, but **does not prove the conjecture**. The [earlier full-scope attempt](full-conjecture-attempt.md) remains available.

[Darmon–Granville](https://doi.org/10.1112/blms/27.6.513) established finiteness for each fixed eligible exponent triple. The full conjecture lets the exponents vary. This is the central gap between a solved fixed signature and a solution to the full problem.

## Starting ledger

These signatures are listed as determined in [Poonen–Schaefer–Stoll, Table 1](https://arxiv.org/pdf/math/0508174). The table dates from 2005, so agents should check newer literature before treating any unlisted signature as open.

| Signature | Reference named in Table 1 |
| --- | --- |
| (2, 3, 7) | Poonen–Schaefer–Stoll, Theorem 1.1 |
| {2, 3, 8} | Bruin (1999, 2003) |
| {2, 3, 9} | Bruin (2004) |
| {2, 4, 5} | Bruin (2003) |
| {n, n, n}, n > 3 | Wiles and Taylor–Wiles (1995) |

Braces denote exponent permutations. Signs and the definition of a primitive solution matter; consult the cited papers before comparing counts.

## Bounded check for (2, 3, 7)

`fermat_catalan_237.py` uses exact integer arithmetic to test every positive (y) with (y^3<z^7) for (1\le z\le120), then checks whether (z^7-y^3) is a square and whether (x,y,z) are coprime.

```sh
python3 research/fermat_catalan_237.py
```

It checks 2,592,531 pairs and finds two primitive positive triples: `(2213459, 1414, 65)` and `(15312283, 9262, 113)`. Both appear in Theorem 1.1 of the [complete classification](https://arxiv.org/abs/math/0508174). This finite search proves nothing about values above the bound and is not a new proof of the theorem.

## First proof attempt

Two agents pursued independent routes and then reviewed one another's work:

| Route | Established reduction | Blocker |
| --- | --- | --- |
| [Inequality and height](attempt-inequality.md), [peer review](review-inequality.md) | Every eligible reciprocal sum is at most 41/42; each primitive solution gives a high-quality abc triple. The abc conjecture would imply finiteness. | No unconditional uniform upper bound on the height or radical. |
| [Common-exponent and modular](attempt-modular.md), [peer review](review-modular.md) | Common exponent divisors at least 3 are excluded by Fermat's Last Theorem; divisor 2 reduces to constrained Pythagorean triples. | Infinitely many coprime exponent signatures remain, including (2,3,ℓ) for primes ℓ≥7. |

The peer reviews found no proof of Fermat–Catalan. The conjecture remains open. The complete proof obligation is a uniform bound or another finiteness argument across varying exponents. Formalization is deferred until a complete mathematical proof is found.

Four agents completed a second research pass on height and radical bounds, modular methods across signatures, a current literature survey, and elementary or congruence arguments. Their separate work items and peer reviews are recorded in the databases. No route produced a proof.

| Second-pass record | Contribution and limit |
| --- | --- |
| [Height/radical](attempt-height.md), [peer review](review-height.md) | An unconditional Stewart–Yu estimate and fixed-prime-support finiteness are too weak to control all solutions. The cited Stewart–Yu formula was corroborated through a secondary source because the article text was inaccessible. |
| [Varying (2,3,ℓ) modular route](attempt-modular-uniform.md), [independent review](review-modular-uniform.md) | Frey-curve calculations and the cited seven-curve reduction are uniform in prime ℓ; determining relevant rational points on modular twists remains open across all ℓ. The review clarified that the cited Table 4 applies for prime ℓ≥11 and identified a concrete unresolved `27a1` branch. |
| [Literature survey](literature-survey.md) | A 2025 survey gives results for varying-signature families under explicit congruence conditions. Its Theorems 11.1, 11.2, and 11.5 were checked against the survey PDF; the original papers and a new 2026 preprint still need independent review. |
| [Congruence/factorization](attempt-congruence.md), [peer review](review-congruence.md) | Parity filters and a coprime factorization lemma apply across families but do not yield a uniform finiteness result. The review caught a missing symmetric mod-8 case, now added. |

## Third research pass

Four agents continued with primary-source audits and two new partial reductions:

| Record | Checked result and limit |
| --- | --- |
| [Modular-route review](review-modular-uniform.md) | Confirms the seven-curve reduction under its hypotheses, corrects the range of Table 4 to prime exponent at least 11, and isolates a surviving `27a1` branch. |
| [Survey review](review-literature.md) | Confirms the cited theorem statements and identifies **two** untreated divisibility classes in the `(n,n,5)` result. The recent `(3,5,7)` preprint remains an unverified claim. |
| [Prime-support bound](attempt-support.md), [review](review-support.md) | Quantifies a weak necessary growth rate for the radical and largest supporting prime using a reported Stewart–Yu estimate. It gives no height bound. The exact estimate was corroborated through a secondary source. |
| [Exponent reduction](attempt-exponents.md), [review](review-exponents.md) | Within `(2,3,n≥7)`, composite exponents reduce to prime exponents or six fixed exceptions `{8,9,10,12,15,25}`. Darmon–Granville then makes finiteness of this family equivalent to finiteness of its prime-exponent subfamily. This remains one infinite family of the full conjecture. |

The next mathematical obligations are uniform control of the surviving prime-exponent family, the positive-solution rational points in the modular branches, and the untreated congruence classes in existing family theorems. None of the third-pass work proves the full conjecture.

A [Darmon–Merel source audit](source-darmon-merel.md) confirms that Poonen–Schaefer–Stoll's 2005 table lists the hyperbolic families `{2,n,n}` and `{3,n,n}` as historically determined, with other work contributing for small `n`. The original 1997 article was inaccessible here, so its precise theorem and exception list remain unverified. Its paper record is a bibliographic lead, not an extracted theorem accepted as fact.

## Fourth research pass

| Route | Result and boundary |
| --- | --- |
| [`27a1` modular branch](attempt-27a1.md), [independent review](review-27a1.md), [local check](review-27a1-local.md) | For prime exponent `p≥17`, if a positive solution belongs to this branch and a prime `q≥5`, `q≠p`, divides `c` with `q≡2 (mod 3)`, then `q≡−1 (mod 6p)`. The branch assumption is essential; the condition leaves infinitely many possible primes. |
| [Coprime-to-10 class of `(n,n,5)`](attempt-cm-class.md), [review](review-cm-class.md) | For positive odd bases, `n` must be odd and `v₂(a+b)=5v₂(c)`, so `32|a+b`. Chen–Koutsianas already proves a relevant irreducibility result; its surviving CM comparison forms remain the central obstruction. |
| [Six fixed `(2,3,n)` exceptions](six-exceptions.md), [review](review-six-exceptions.md) | The cases `n=10,15` have signed classifications excluding positive non-unit solutions. The `n=25` source gives a conditional classification with five equations still unresolved. Sign and orientation conventions matter for `n=8`; the original Bruin paper and the `n=6` list behind `n=12` remain to audit. |
| [Smooth-support bound](attempt-smooth.md) | A reported Stewart–Yu estimate implies that an unbounded solution sequence must have largest supporting prime `P≥(3−o(1)) log log C`. This is a weak necessary condition, and the exact source formula has only been checked through a secondary reference here. |

These are partial results for selected families. The full Fermat–Catalan finiteness statement remains unproved.

## Recent-paper check

Four agents checked recent papers and preprints through 23 October 2026 (Argentina time). Their [direct-title survey](recent-direct.md), [(2,3,n) check](recent-23n.md), [varying-family survey](recent-families.md), and [independent provenance audit](recent-audit.md) distinguish theorems from conditional results and unreviewed claims. This was a targeted search, so absence from these lists does not establish that no other paper exists.

- A September 2026 [preprint on `(3,5,7)`](recent-audit.md) claims a complete signed-integer exclusion. Its arXiv record remains v1, and a companion archive is public, but neither the archive nor the mathematical proof was independently checked here. Keep the result marked **unverified preprint claim**. Even if correct, it concerns one fixed signature.
- The 2025 [solved-cases survey](recent-23n.md) still lists `(2,3,25)` as open; the later Freitas–Stoll paper remains conditional on five unresolved equations. A May 2026 `(2,r,p)` methods paper assumes `r≥5` and does not directly cover `(2,3,p)`.
- A 2025 [coefficient-one `(13,13,n)` paper](recent-families.md) gives an unconditional exclusion under `13|z` for all `n≥2`, while its `n=7` classification assumes GRH. Other recent family results require coefficients, divisibility conditions, or a large-image conjecture.

The paper library now has 29 records. Source-checked metadata, reading status, and proposed extracted claims are kept separate. No source in this targeted check establishes the full Fermat–Catalan conjecture.

## Optimized full-conjecture pass

Four agents tested new global strategies and reviewed the deductions. The [synthesis](optimized-full-attempt.md) links the detailed arguments and reviews. The strongest new reduction classifies all irreducible exponent signatures: 19 fixed composite-containing cases can be set aside by fixed-signature finiteness, leaving the infinite all-prime cases and `(2,4,ℓ)` for prime `ℓ≥7`. A contradiction argument shows an infinite solution family would give unbounded violations of the conjectural abc inequality for `ε=1/42`; unconditional height estimates and a universal elliptic curve do not rule it out. The full conjecture remains open, and Lean formalization remains deferred.

## Collaborative next steps

1. Check each ledger row against the original paper and add exact results, methods, and source URLs to the paper database.
2. Have another agent review sign and permutation conventions and challenge any inferred gap.
3. Independently reproduce a known result before exploring an unclassified fixed signature. Record failed approaches and counterexamples in the shared research database.
4. Keep fixed-signature progress separate from the full finiteness conjecture, which requires control across varying exponents.
