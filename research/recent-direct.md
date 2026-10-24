# Recent direct Fermat–Catalan literature check (through October 2026)

**Scope and method.** I queried the official arXiv Atom API for the phrase `Fermat-Catalan` (sorted by submission date) and for recent titles containing `generalized Fermat`; I then checked targeted arXiv abstracts and the arXiv abstract-page metadata for the most relevant records. A later broad API request hit HTTP 429, so this is a targeted survey rather than a completeness claim. I found **no verified proof of the full Fermat–Catalan finiteness conjecture**. Statements below distinguish authors' claims from independently established results.

## Closest recent records

| Record | Exact scope and status | Implication |
| --- | --- | --- |
| Peter Chocian, [*The Primitive Generalized Fermat Equation x³+y⁵=z⁷: A computer-assisted proof*](https://arxiv.org/abs/2609.26996), arXiv:2609.26996v1, submitted 22 September 2026 | The abstract and Theorem 1.1 **claim** no nonzero primitive integer solutions for the single signature `(3,5,7)`. The arXiv page has no journal-reference or DOI metadata as checked here. I did not audit the proof or certificate archive. | Even if valid, one fixed signature cannot prove uniform finiteness over varying exponents. Preserve it as an unreviewed preprint claim. |
| Preda Mihăilescu, [*The strong Fermat-Catalan Equation*](https://arxiv.org/abs/2509.18275), arXiv:2509.18275v1, submitted 22 September 2025 | The abstract says it proves nonexistence for `(x^p+y^p)/(x+y)=p^e z^q` under coprimality and distinct odd-prime conditions. This is a specialized cyclotomic equation, **not** the full Fermat–Catalan conjecture. I checked the abstract, not the paper's complete proof. | Potential technique lead; do not catalogue as a solution to the full conjecture. |
| Adam S. Sikora, [*Fermat-Catalan and Tijdeman-Zagier conjectures for products*](https://arxiv.org/abs/2410.21552), arXiv:2410.21552v1, submitted 28 October 2024 | The abstract **proposes conjectural generalizations** replacing powers by products. It does not claim to prove the classical Fermat–Catalan conjecture. | Context, not proof progress on the classical statement. |

## Recent adjacent work with varying exponents

- Ariel Pacetti and Lucas Villagra Torcomian, [arXiv:2512.17845](https://arxiv.org/abs/2512.17845), submitted 19 December 2025, studies signature `(5,p,3)`. Its abstract states a no-nontrivial-solutions result only **assuming a standard large-image conjecture**, for sufficiently large prime `p` and `3∤c`. It is conditional and restricted to one family.
- Satyabrat Sahoo, [arXiv:2509.21083](https://arxiv.org/abs/2509.21083), submitted 25 September 2025, studies `(2p,2q,r)` with varying primes `p,q` and fixed `r`. Its abstract makes the exclusion depend on an `S`-unit condition and additional narrow-class-number criteria; the paper may provide a useful method for uniformity, but the abstract does not announce Fermat–Catalan in full.
- Pedro-José Cazorla García, Angelos Koutsianas and Lucas Villagra-Torcomian, [arXiv:2605.02632](https://arxiv.org/abs/2605.02632), submitted 4 May 2026, develops the modular method for `Ax²+By^r=Cz^p` and applies it to a related coefficient equation. The abstract does not claim the full conjecture.

**Recommended next check.** Read the exact statements and dependencies in Mihăilescu's 2025 paper and Sahoo's 2025 paper before adding extracted claims to the database; separately audit Chocian's 2026 certificate archive with an independent reviewer. No source above supplies an unconditional proof uniform across every hyperbolic exponent signature.
