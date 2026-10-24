"""Bounded check of primitive positive x^2 + y^3 = z^7 for 1 <= z <= 120.

For the complete classification of *integer* solutions, see Theorem 1.1 of
Poonen, Schaefer, and Stoll: https://arxiv.org/abs/math/0508174
This finite computation is an illustration, not a proof of that theorem.
"""

from math import gcd, isqrt


def icbrt(n: int) -> int:
    """Floor cube root of a nonnegative integer, without floating point."""
    low, high = 0, 1 << ((n.bit_length() + 2) // 3)
    while low + 1 < high:
        mid = (low + high) // 2
        if mid**3 <= n:
            low = mid
        else:
            high = mid
    return low


def search(max_z: int = 120):
    matches = []
    candidates = 0
    for z in range(1, max_z + 1):
        target = z**7
        for y in range(1, icbrt(target - 1) + 1):
            candidates += 1
            square = target - y**3
            x = isqrt(square)
            if x > 0 and x*x == square and gcd(gcd(x, y), z) == 1:
                matches.append((x, y, z))
    return candidates, matches


if __name__ == "__main__":
    candidates, matches = search()
    print(f"Checked {candidates:,} (y,z) pairs for 1 <= z <= 120")
    for x, y, z in matches:
        assert x*x + y**3 == z**7
        print(f"(x,y,z) = ({x},{y},{z})")
    print(f"Primitive positive matches: {len(matches)}")
