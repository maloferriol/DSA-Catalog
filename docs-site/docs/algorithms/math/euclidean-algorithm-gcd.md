---
title: "Euclidean Algorithm (GCD)"
sidebar_label: "Euclidean Algorithm (GCD)"
tags: [algorithm, math]
---

# Euclidean Algorithm (GCD)

> Compute greatest common divisor via gcd(a,b) = gcd(b, a mod b).

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Math |
| **Time** | O(log min(a,b)) |
| **Space** | O(1) |

## Key Techniques

- Recursion or iteration

## Notes & Interview Tips

Extended Euclidean also computes Bézout coefficients.

## How It Works

The Euclidean algorithm finds the Greatest Common Divisor (GCD) of two numbers in O(log(min(a,b))) time. The key insight: `gcd(a, b) = gcd(b, a % b)`, with base case `gcd(a, 0) = a`.

The extended Euclidean algorithm also finds integers x and y such that `ax + by = gcd(a, b)`. This is used in modular inverse computation, RSA cryptography, and solving linear Diophantine equations.

Python's `math.gcd` implements this. For LCM: `lcm(a, b) = a * b // gcd(a, b)`.

## Implementation

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# Extended Euclidean: finds x, y such that ax + by = gcd(a, b)
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y
```

## Key Insight

> gcd(a, b) = gcd(b, a % b) reduces the problem by at least half each step (the remainder is always less than b), giving O(log n) time. The Fibonacci numbers are the worst case.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/math)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | 🟡 Medium | NC150 |
|  | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | 🟡 Medium | NC150 |
|  | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | 🟢 Easy | - |
|  | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | 🟡 Medium | - |
|  | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm)
- [cp-algorithms.com](https://cp-algorithms.com/algebra/euclid-algorithm.html)
