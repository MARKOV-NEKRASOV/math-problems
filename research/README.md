# Fermat–Catalan research notebook

The conjecture asks whether there are finitely many **distinct triples of powered values** satisfying (x^p+y^q=z^r), where the positive bases are coprime and (1/p+1/q+1/r<1). Varying an exponent on a base of 1 can repeat the same triple, so counting exponent tuples gives the wrong statement. See the [problem overview](https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture).

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
| [Varying (2,3,ℓ) modular route](attempt-modular-uniform.md) | Frey-curve calculations and the cited seven-curve reduction are uniform in prime ℓ; determining relevant rational points on modular twists remains open across all ℓ. The literature claims were checked against the cited arXiv papers; a separate peer review is still pending. |
| [Literature survey](literature-survey.md) | A 2025 survey gives results for varying-signature families under explicit congruence conditions. Its Theorems 11.1, 11.2, and 11.5 were checked against the survey PDF; the original papers and a new 2026 preprint still need independent review. |
| [Congruence/factorization](attempt-congruence.md), [peer review](review-congruence.md) | Parity filters and a coprime factorization lemma apply across families but do not yield a uniform finiteness result. The review caught a missing symmetric mod-8 case, now added. |

## Collaborative next steps

1. Check each ledger row against the original paper and add exact results, methods, and source URLs to the paper database.
2. Have another agent review sign and permutation conventions and challenge any inferred gap.
3. Independently reproduce a known result before exploring an unclassified fixed signature. Record failed approaches and counterexamples in the shared research database.
4. Keep fixed-signature progress separate from the full finiteness conjecture, which requires control across varying exponents.
