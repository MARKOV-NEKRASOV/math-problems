# Fermat–Catalan research notebook

## Mandatory F2 → F0 agent protocol

All agents must follow [the unified mathematical specification](AGENT_F2_TO_F0_SPEC.md), conduct [continuous literature searches](LITERATURE_WATCH_F2_F0.md), and inspect [the proved three-point-cover complexity barrier](F2_TO_F0_GEOMETRIC_BARRIER.md). The project's goal remains unconditional finiteness across ALL seven variable-exponent branches. Sources and partial improvements must be audited for actual uniformity; no full solution has been obtained.


The conjecture asks whether there are finitely many **distinct triples of powered values** satisfying (x^p+y^q=z^r), where the positive bases are coprime and (1/p+1/q+1/r<1). Varying an exponent on a base of 1 can repeat the same triple, so counting exponent tuples gives the wrong statement. See the [problem overview](https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture).

The latest [F2 → F0 cycle report](f2-to-f0-cycle-1.md) follows the updated [agent protocol](AGENT_F2_TO_F0_SPEC.md). It audits which fixed-exponent techniques survive when more exponents grow, records a new sufficient error-budget lemma and a field-dependence barrier for a rank-two construction, and keeps all seven infinite escape profiles explicit. The earlier [bounds and priorities](bounds-and-priorities.md) remain useful tactical restrictions, but **do not prove the conjecture**.

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

## Further full-proof attempt

Four agents pursued the two remaining infinite signature classes and independent global contradictions. The [full argument and reviews](full-proof-attempt-v3.md) record a cyclotomic cofactor condition for repeated prime exponents, an exact Gaussian/Lucas condition for `(2,4,ℓ)`, and the uniform estimate `h(j)=6log C+O(1)` for the universal Frey curve. These results impose constraints on a hypothetical infinite solution family, but none supplies an unconditional finiteness theorem. The conjecture remains unproved; Lean formalization remains deferred.

## Integrated reduction to prime signatures

The [new reduction](reduction-to-prime-signatures.md) and [independent review](review-reduction-to-prime-signatures.md) check every orientation of `(2,4,ℓ)`. Bennett–Skinner excludes the signed square and fourth-power output orientations for prime `ℓ≥7`. Ellenberg excludes the prime-power output orientation for `ℓ≥211`; Darmon–Granville makes the finitely many smaller fixed signatures finite. Together with the 19 fixed composite signatures, this leaves only all-prime hyperbolic signatures as a uniform obligation. The [integrated attempt](integrated-full-proof-attempt.md) applies the prior cyclotomic, radical, and elliptic findings to that class and identifies the remaining gap. The paper library now has 31 records, including source-checked Bennett–Skinner and Ellenberg theorem statements. No full proof or Lean formalization followed.

## Prime-signature proof attempt

Four agents pursued the remaining all-prime signatures. The [synthesis and reviews](prime-signature-full-attempt.md) prove that an infinite family would satisfy `rad(ABC)<C^(5/6+o(1))` and `h(j)≥(36/5−o(1))log N`; neither contradicts a known unconditional upper bound. A new [fixed-output-support theorem](fixed-output-support.md) gives finiteness when two input exponents and the output prime set are fixed, even with a varying output exponent. Published exclusions narrow `(3,3,t)` to large prime residue classes, while a 2026 preprint on `(r,r,p)` requires coefficient `C>2`. The paper library now holds 33 records, with the two source statements and reading limits recorded. Full Fermat–Catalan finiteness remains unproved; Lean formalization remains deferred.

## Continued all-prime proof attempt

The [25 October synthesis](continued-prime-proof-attempt.md) links the four branch attempts, their independent reviews, and four additional routes. An infinite counterexample family would have one, two, or three diverging coordinate exponents, with increasingly severe radical deficits. A signed Siegel argument forces the variable base's prime support to escape whenever the other two exponents are fixed. In the positive `(2,3,p)` family, a reviewed seven-curve local argument forces each output prime `q≥5` to satisfy `q≥(√p−1)²`. Primitive divisors and optimized radical constants add necessary conditions in other branches. None gives a uniform finiteness theorem. The 2026 non-split Cartan preprint checked here treats level 13 and leaves uniform large-level rational points as a question. No full proof or Lean formalization followed.

The [focused lemma ledger](lemma-subproblem-ledger.md) records smaller targets and four constructed results: a simultaneous-factor exclusion for a fixed smallest sum, a finite output-prime sieve, a fixed input-gap finiteness theorem with moving output support, and an explicit counterexample to height-free finite-trace rigidity. These sharpen the questions the next agents should attack without treating a subfamily result as a full proof.

## Case-eliminating generalizations

The [new synthesis](purposeful-generalizations.md) records three proved constructions with direct consequences. A signed fixed-gap theorem covers every placement of the variable exponent when the other two exponents and their base gap are fixed. A finite compatibility graph built from seven comparison curves rules out 12 input-prime divisibility families in positive `(2,3,p)` for prime `p≥59`, including the simpler `5|b` with `7|a` exclusion valid for `p≥11`. A repeated-prime valuation profile rules out odd signed bases congruent modulo 4. Independent reviews checked the modular and parity deductions. These eliminate proper infinite families; none supplies the uniform all-prime finiteness required for the conjecture.

## Bound-guided subproblems

The [quantitative board](bounds-and-priorities.md) and [proof-obligation audit](bound-proof-obligations.md) distinguish lower bounds from the upper bounds that would create a contradiction. The [effective signed fixed-gap bound](effective-fixed-gap-bounds.md), using Bérczes–Evertse–Győry Theorem 2.3, gives an explicit exponent cutoff depending on fixed `P,Q,D`; it cannot hold uniformly when `D` moves. The [modular selector metrics](modular-selector-bounds.md) extend the finite compatibility graph to 42 excluded divisibility pairs for prime exponent `p≥103`; their 6.7062% density is for ordinary coprime base pairs, not for conjecture solutions. The [congruence-corrected repeated-cube bounds](congruence-corrected-size-gaps.md) force roots at least 46,520 or 6,890 in the two positive branches after the published `t>10⁹` restriction. All three quantify progress while leaving the full moving-parameter problem open.

## F2 → F0 protocol cycle

The [cycle report](f2-to-f0-cycle-1.md) records four roles: geometry, inequalities, permanent literature discovery, and adversarial review. It audits the seven F2/F1/F0 escape profiles, the proposed sufficient upper bounds, and the growth of the chosen hypergeometric motive's field. A [prior-bound audit](audit-prior-bounds.md) corrected the effective fixed-gap theorem's scope for signed squares and a transcription of an external source constant; the Fermat–Catalan restricted bounds survive. New [nonzero-trace](nonzero-trace-sieve.md), [gap-valuation](valuation-gap-bound.md), and [cube-congruence](mod-eight-cube-gaps.md) lemmas eliminate further case families, but remain tactical F2 restrictions. No uniform F1/F0 upper inequality was proved, and Lean formalization remains deferred.

## Collaborative next steps

1. Check each ledger row against the original paper and add exact results, methods, and source URLs to the paper database.
2. Have another agent review sign and permutation conventions and challenge any inferred gap.
3. Independently reproduce a known result before exploring an unclassified fixed signature. Record failed approaches and counterexamples in the shared research database.
4. Keep fixed-signature progress separate from the full finiteness conjecture, which requires control across varying exponents.
