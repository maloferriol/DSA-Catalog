---
title: "Dynamic Programming"
sidebar_label: "Dynamic Programming"
tags: [paradigm, dynamic-programming]
---

# Dynamic Programming

> Solve problems by combining solutions to overlapping subproblems; top-down (memo) or bottom-up (table).

## Quick Facts

| | |
|---|---|
| **Kind** | Paradigm |
| **Category** | Dynamic Programming |
| **Time** | Problem-specific |
| **Space** | Problem-specific |

## Key Techniques

- Memoization
- Tabulation
- State design
- Optimal substructure

## Notes & Interview Tips

Sean Prashad: 'If asked for max/min subarray/subset → DP, Sliding window.'

## How It Works

Dynamic Programming (DP) solves problems by breaking them into overlapping subproblems and storing results to avoid recomputation. The two approaches: **top-down** (recursion + memoization) and **bottom-up** (iterative, filling a table).

The key to recognizing DP: (1) **optimal substructure** — the optimal solution contains optimal solutions to subproblems, (2) **overlapping subproblems** — the same subproblems are solved repeatedly. If only (1) holds, use divide-and-conquer; if both hold, use DP.

Common DP patterns: linear (1D array), grid (2D), interval, knapsack, string (LCS/edit distance), tree, bitmask, and digit DP. Start with brute-force recursion, add memoization, then optimize to bottom-up if needed.

## Implementation

```python
# Top-down (memoization) - Fibonacci
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# Bottom-up (tabulation) - Fibonacci
def fib_bottom_up(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

## Key Insight

> The DP process: (1) define the state (what changes between subproblems), (2) write the recurrence (how states relate), (3) identify base cases, (4) determine computation order (bottom-up) or use memoization (top-down).

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | 🟢 Easy | G75, B75 |
|  | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | 🟡 Medium | B75, NC150 |
|  | [Coin Change](https://leetcode.com/problems/coin-change/) | 🟡 Medium | G75, B75, NC150 |
|  | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | 🟡 Medium | G75, B75, NC150 |
|  | [House Robber](https://leetcode.com/problems/house-robber/) | 🟡 Medium | B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming)
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/dynamic-programming/)
