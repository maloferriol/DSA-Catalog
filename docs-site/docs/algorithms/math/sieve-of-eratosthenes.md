---
title: "Sieve of Eratosthenes"
sidebar_label: "Sieve of Eratosthenes"
tags: [algorithm, math]
---

# Sieve of Eratosthenes

> Find all primes up to N by iteratively marking multiples.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Math |
| **Time** | O(N log log N) |
| **Space** | O(N) |

## Key Techniques

- Boolean sieve

## Notes & Interview Tips

Linear sieve variant runs in O(N).

## How It Works

The Sieve of Eratosthenes finds all prime numbers up to n in O(n log log n) time. It starts by assuming all numbers are prime, then iterates from 2 upward, marking all multiples of each prime as composite.

Optimization: start marking from p² (all smaller multiples are already marked by smaller primes). Only iterate up to √n. This is the fastest general-purpose primality sieve for n up to ~10^8.

For larger ranges or single-number primality testing, use Miller-Rabin. For finding primes in a range [L, R], use a segmented sieve.

## Implementation

```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
```

## Key Insight

> Start marking composites from p² because all smaller multiples of p have a smaller prime factor and are already marked. This optimization cuts the work significantly.

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

- [Wikipedia](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- [cp-algorithms.com](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html)
