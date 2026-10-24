# Darmon–Merel family claim: source audit

**Conclusion:** Poonen–Schaefer–Stoll (PSS) Table 1 lists the hyperbolic families `{2,n,n}` and `{3,n,n}` as **determined**, citing Darmon–Merel (1997) **and other work for small n**. I could not access the original Darmon–Merel article through the publisher's PDF endpoint (HTTP 403), so its exact internal theorem range and full solution list remain **unverified from the original**. Do not attribute every n or every exceptional solution solely to Darmon–Merel based on the table.

## What is independently confirmed

1. The publication metadata is corroborated by Crossref DOI [10.1515/crll.1997.490.81](https://doi.org/10.1515/crll.1997.490.81): Henri Darmon and Loïc Merel, *Winding quotients and some variants of Fermat's Last Theorem*, Journal für die reine und angewandte Mathematik **490** (1997), 81–100. The title, journal, volume and pages are also in the reference list of [Chen–Koutsianas, *Darmon's Program: A survey*, arXiv:2507.15149v1](https://arxiv.org/abs/2507.15149).
2. [PSS, *Twists of X(7)*, arXiv:math/0508174v1, Table 1 and caption](https://arxiv.org/pdf/math/0508174v1) explicitly lists `{2,n,n}` and `{3,n,n}` among exponent triples for which primitive **integer** solutions have been determined. Both rows say `[Darmon-Merel1997]; others for small n`. The caption says braces include **every permutation**, with solutions considered up to signs and permutations, and it omits the repeated unit-base form `1^n+2³=3²`.
3. The table applies only in the hyperbolic region `1/p+1/q+1/r<1`. Thus `{2,n,n}` requires `n≥5`, and `{3,n,n}` requires `n≥4`. It does **not** assert those ranges are precisely what Darmon–Merel alone proved.
4. [Chen–Koutsianas §2](https://arxiv.org/pdf/2507.15149v1) credits Darmon–Merel with a weaker large-image theorem for elliptic curves with extra level 2 or 3 structure, sufficient for applications to signatures `(p,p,2)` and `(p,p,3)`. It does not state a full primitive-solution list or exact lower bound on p there.

## What remains unverified

- The exact theorem numbers and exponent cutoffs in Darmon–Merel (1997), including whether their statement assumes prime n or treats composite n by reduction.
- The signed-integer exceptional triples and which small exponents are supplied by other authors. The PSS caption has a convention, but it is not the original theorem's complete statement.
- Whether later literature changes the classification; a 2005 table is a historical reference.

The original PDF link exposed by Crossref is `https://www.degruyter.com/document/doi/10.1515/crll.1997.490.81/pdf`. Direct access was denied with HTTP 403 in this environment even after a network permission request. This is a **source-access limit**, not evidence against the theorem. The safe reusable claim is the PSS table's historical classification, with precise table conventions. A primary-source audit should remain open before inserting a more specific Darmon–Merel theorem into the paper-claims database.
