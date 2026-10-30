# Cycle 14 geometry: correct the semistability audit for (2,r,p)

**Date:** 2026-10-30. **Status:** PROVED correction to the source-hypothesis check, subject to independent review. It restores the originally proposed G-13 even-b irreducibility implication *without* `p∤ab`; it does not prove an F2 branch, much less full Fermat–Catalan.

## G14-S, exact statement

Fix an odd prime r≥7. There is a constant C_r such that every positive primitive nonunit solution a²+b^r=c^p, with b even and p prime >C_r, whose output base c has a prime divisor ℓ outside {2,r}, gives an irreducible residual two-dimensional representation attached to J_{2,r}/K_r at every prime of K_r=Q(ζ_r)^+ above p. No condition p∤ab is required. By the repository's fixed-output-support Siegel lemma for fixed input exponents (2,r), the remaining solutions with supp(c)⊆{2,r} contribute finitely many *powered-value triples* as p varies. Thus the even-b slice has residual irreducibility for all sufficiently large p, though no elimination of newforms or bound on p follows.

## Primary-source proof audit

Cazorla García–Koutsianas–Villagra Torcomian, *The generalized Fermat equation Ax²+By^r=Cz^p and applications*, arXiv:2605.02632v1, PDF pp. 10–12 and 22, source text checked from cached /tmp/branch2605.pdf (SHA-256 5a0cdab4ab6d72143ea7cb3e527916999ba9696a110aa4431958853c534b4873). Fresh arXiv PDF/API download returned HTTP 403, so no claim that a newer version was ruled out by live query; cached PDF is explicitly v1.

- Proposition 5.1, p.10, says good reduction at rational q if q∤2rAB(Aa²+Bb^r). **It does not require q∤ab.** For A=B=C=1, q=p>2r and p∤c, we have p∤a²+b^r=c^p, so this proposition applies even when p|a or p|b.
- Proposition 5.2, p.10, says bad multiplicative reduction at q if q∤2rAB and q|Aa²+Bb^r. For q=p>2r and p|c, it applies. Indeed primitivity implies p∤ab in this latter case, but that is automatic and need not be assumed globally. Consequently J_{2,r} is semistable at *every* prime above residual p, with no p∤ab condition.
- Proposition 5.6, p.12, gives potentially good reduction at a place above 2 when v₂(Bb^r)≥6. With B=1, r≥7 and b even, this holds whether r|c or not.
- Theorem 3.3, p.8, gives GL2(K_r)-type for b≠0. A prime ℓ∤2r dividing c supplies multiplicative reduction via Proposition 5.2; the paper's Corollary 6.1 proof (p.22) uses this to satisfy the endomorphism-descent hypothesis. This last implication is inherited from the source's own proof, not reproved independently here.
- Theorem 6.1, p.22, permits **any** fixed prime ideal q of K_r, so a place above 2 is allowed. Its threshold C(K_r,g,q), g=(r−1)/2, depends on r and q but not on a,b,c,p. It states *irreducible*, while Corollary 6.1 states *absolutely irreducible*. Claim only irreducible pending audit of cited Billerey–Chen–Dieulefait–Freitas Corollary 1.

Thus all four hypotheses of Theorem 6.1 hold on the stated slice. The prior cycle-13 adversarial review asserted Proposition 5.1 additionally needed p∤b. That is a source misreading: the displayed condition is p∤2rAB(Aa²+Bb^r), and equation (3.2) shows no factor from a or b in the discriminant for A=B=1. The corrected G-13 added an unnecessary p∤ab hypothesis. Remove that restriction only after independent source review of this correction.

## Quantitative impact and exact gap

Previous G-13: b even, p∤ab, and ℓ|c outside {2,r} implies irreducibility for p>C_r. New G14-S: the same implication for **all** b even. This removes the p|ab exceptional slice. It does not provide an upper bound on p or C=c^p, so it remains far from the sufficient F2 slope κ<2r/(r+2). The field K_r has degree (r−1)/2, the Jacobian dimension is (r−1)/2, and C_r may grow with r. Nothing here survives uniformly when r→∞ for F1/F0 without a separate theorem. The b-odd, r|c case and comparison newforms remain open.

## Literature opening/closure and next falsifiable step

At opening, reread arXiv:2605.02632v1 source statements (primary PDF cached) and cycle-13 source ledger. At closure, checked the same PDF's discriminant (3.2), Theorem 3.3, Propositions 5.1/5.2/5.6, Theorem 6.1 and Corollary 6.1. Live arXiv PDF fetch was HTTP 403; no new-version statement inferred. Next: an independent reviewer should check the exact Proposition 5.1 condition and the endomorphism-descent inference, then compute actual residual comparison forms for the even-b slice. If any remains, irreducibility alone does not close F2.
