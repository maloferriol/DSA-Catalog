---
title: "Fast Exponentiation"
sidebar_label: "Fast Exponentiation"
tags: [algorithm, math]
---

# Fast Exponentiation

> Compute a^n in O(log n) via repeated squaring; works on integers and matrices.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Math |
| **Time** | O(log n) |
| **Space** | O(1) |

## Key Techniques

- Binary exponentiation

## Notes & Interview Tips

Matrix exponentiation accelerates linear recurrences.

## How It Works

Fast exponentiation (binary exponentiation) computes a^n in O(log n) multiplications by repeatedly squaring. The idea: a^n = (a^(n/2))² if n is even, a × a^(n-1) if n is odd.

This is essential for modular exponentiation: `pow(a, n, mod)` computes a^n mod m without overflow. Python's built-in `pow(a, n, mod)` uses this algorithm.

Applications: modular arithmetic in cryptography (RSA), matrix exponentiation for linear recurrences (Fibonacci in O(log n)), and computing large Fibonacci numbers.

## Implementation

```python
def fast_pow(base, exp, mod=None):
    result = 1
    base = base % mod if mod else base
    while exp > 0:
        if exp & 1:
            result = result * base % mod if mod else result * base
        exp >>= 1
        base = base * base % mod if mod else base * base
    return result

# Matrix exponentiation for Fibonacci
def fib(n):
    if n <= 1: return n
    def mat_mult(A, B):
        return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
                [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
    def mat_pow(M, p):
        result = [[1,0],[0,1]]
        while p:
            if p & 1: result = mat_mult(result, M)
            M = mat_mult(M, M)
            p >>= 1
        return result
    return mat_pow([[1,1],[1,0]], n)[0][1]
```

## Key Insight

> Squaring halves the exponent each step: a^16 = (a^8)² = ((a^4)²)² = ... Only O(log n) multiplications needed. Python's built-in pow(a, n, mod) already does this.

## Visualization

- [Interactive Visualization](https://cp-algorithms.com/algebra/binary-exp.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | 🟡 Medium | NC150 |
|  | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | 🟡 Medium | NC150 |
|  | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | 🟢 Easy | - |
|  | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | 🟡 Medium | - |
|  | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Exponentiation_by_squaring)
- [cp-algorithms.com](https://cp-algorithms.com/algebra/binary-exp.html)
