#!/usr/bin/env python3
"""Independent exact character-sum check of local Frey trace obstructions.

FNS seven comparison models are copied from arXiv:1703.05058v3, after Lemma 2.3.
The trace is computed by a character sum, not direct point enumeration.
"""
from fractions import Fraction

CURVES = {
    '27a1': (0, 0, 1, 0, -7),
    '54a1': (1, -1, 0, 12, 8),
    '96a1': (0, 1, 0, -2, 0),
    '288a1': (0, 0, 0, 3, 0),
    '864a1': (0, 0, 0, -3, 6),
    '864b1': (0, 0, 0, -24, 48),
    '864c1': (0, 0, 0, 24, -16),
}

def chi(n, q):
    n %= q
    if n == 0:
        return 0
    return 1 if pow(n, (q-1)//2, q) == 1 else -1

def trace(model, q):
    a1, a2, a3, a4, a6 = model
    return -sum(chi((a1*x+a3)**2 + 4*(x**3+a2*x*x+a4*x+a6), q)
                for x in range(q))

TARGETS = [(7, 'b', 2), (13, 'b', 4), (19, 'b', 12),
           (29, 'a', 14), (31, 'b', 20)]
remaining = Fraction(1)
for q, role, expected_count in TARGETS:
    fixed = {abs(trace(model, q)) for model in CURVES.values()}
    forbidden = []
    for residue in range(1, q):
        a, b = (residue, 0) if role == 'b' else (0, residue)
        frey = (0, 0, 0, 3*b, -2*a)
        if abs(trace(frey, q)) not in fixed:
            forbidden.append(residue)
    assert len(forbidden) == expected_count, (q, forbidden)
    share = Fraction(len(forbidden), q*q - 1)
    remaining *= 1-share
    print(f'q={q} role=q|{role} forbidden residues={forbidden} fraction among coprime base pairs={share}')
print('union density among coprime base pairs:', 1-remaining, float(1-remaining))
