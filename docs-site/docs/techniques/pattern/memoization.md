---
title: "Memoization"
sidebar_label: "Memoization"
tags: [technique, pattern]
---

# Memoization

> Cache results of subproblem calls to avoid recomputation; top-down DP.

## Quick Facts

| | |
|---|---|
| **Kind** | Technique |
| **Category** | Pattern |
| **Time** | Problem-specific |
| **Space** | O(states) |

## Key Techniques

- Hash map cache
- Recursion + cache

## Notes & Interview Tips

Python's functools.lru_cache; manual map otherwise.

## How It Works

Memoization caches the results of expensive function calls and returns the cached result when the same inputs occur again. It's the top-down approach to DP: write the recursive solution, then add caching.

In Python, use `@functools.lru_cache` or `@functools.cache` for automatic memoization. For custom caching, use a dictionary keyed by the function arguments.

Memoization is equivalent to bottom-up DP in terms of what it computes, but it only computes states that are actually needed (lazy evaluation). Bottom-up DP computes all states. Memoization is often easier to write but may have higher overhead due to recursion and hash table lookups.

## Implementation

```python
from functools import lru_cache

# Minimum cost climbing stairs with memoization
@lru_cache(maxsize=None)
def min_cost(costs, i=0):
    if i >= len(costs): return 0
    return costs[i] + min(min_cost(costs, i+1), min_cost(costs, i+2))

# Grid paths with memoization
@lru_cache(maxsize=None)
def unique_paths(m, n):
    if m == 1 or n == 1: return 1
    return unique_paths(m-1, n) + unique_paths(m, n-1)
```

## Key Insight

> Memoization = recursion + cache. Write the brute-force recursive solution, then add @lru_cache. If you can write the recursion, you've solved the DP problem. Optimization to bottom-up can come later.

## Visualization

- [Interactive Visualization](https://pythontutor.com/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | 🟢 Easy | G75, B75 |
|  | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | 🟢 Easy | - |
|  | [Word Break](https://leetcode.com/problems/word-break/) | 🟡 Medium | G75, B75, NC150 |
|  | [Word Break II](https://leetcode.com/problems/word-break-ii/) | 🔴 Hard | - |
|  | [Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Memoization)
- [en.wikipedia.org](https://en.wikipedia.org/wiki/Memoization)
