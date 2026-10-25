#!/usr/bin/env python3
"""Finite exact FNS trace-selector coverage, no extrapolation beyond cutoff."""
from fractions import Fraction
from itertools import product
from math import isqrt

CURVES = {
    '27a1': (0,0,1,0,-7), '54a1': (1,-1,0,12,8),
    '96a1': (0,1,0,-2,0), '288a1': (0,0,0,3,0),
    '864a1': (0,0,0,-3,6), '864b1': (0,0,0,-24,48),
    '864c1': (0,0,0,24,-16),
}

def primes_upto(n):
    out=[]
    for q in range(2,n+1):
        if all(q%d for d in range(2,isqrt(q)+1)):out.append(q)
    return out

def order(model,q):
    a1,a2,a3,a4,a6=model
    return 1+sum((y*y+a1*x*y+a3*y-x*x*x-a2*x*x-a4*x-a6)%q==0
                 for x in range(q) for y in range(q))

def traces(q):
    return {name:q+1-order(model,q) for name,model in CURVES.items()}

def Z(q):
    return frozenset(name for name,t in traces(q).items() if t==0)

def eligible(q,P):
    # For every prime p>=P: q != p and p>2 sqrt(q).
    return q<P and P*P>4*q

def metrics(Q,P):
    qs=[q for q in primes_upto(Q) if q>=5 and eligible(q,P)]
    bs=[q for q in qs if q%3==2]
    aa=[q for q in qs if q%4==3]
    zz={q:Z(q) for q in qs}
    bad=[(b,a) for b,a in product(bs,aa) if b!=a and not zz[b].intersection(zz[a])]
    def union_density(S):
        v=Fraction(1)
        for q in S:v*=Fraction(q,q+1)
        return 1-v
    # Find a maximum complete bipartite subgraph of the *excluded* pair graph.
    # Enumerating 2^|B| subsets is tiny for the stated q<=101 audit.
    best_area=-1
    best_density=Fraction(-1)
    best_b=[]
    best_a=[]
    for mask in range(1 << len(bs)):
        chosen_b=[q for i,q in enumerate(bs) if mask & (1 << i)]
        chosen_a=[q for q in aa if all((b,q) in bad for b in chosen_b)]
        area=len(chosen_b)*len(chosen_a)
        density=union_density(chosen_b)*union_density(chosen_a)
        if (area,density)>(best_area,best_density):
            best_area,best_density=area,density
            best_b,best_a=chosen_b,chosen_a
    assert all((b,a) in bad for b,a in product(best_b,best_a))
    return bs,aa,bad,best_b,best_a,best_density

if __name__=='__main__':
    for q in primes_upto(101):
        if q>=5 and (q%3==2 or q%4==3):
            print(f'q={q:3} roles={"B" if q%3==2 else ""}{"A" if q%4==3 else ""} Z={sorted(Z(q))}')
    print('METRICS')
    for Q,P in [(7,11),(19,23),(29,31),(53,59),(101,59),(101,103)]:
        b,a,bad,sb,sa,d=metrics(Q,P)
        print(f'Q={Q} P={P} |B|={len(b)} |A|={len(a)} excluded_pairs={len(bad)} full_biclique_B={sb} full_biclique_A={sa} base_pair_density={d} ~= {float(d):.7f}')
