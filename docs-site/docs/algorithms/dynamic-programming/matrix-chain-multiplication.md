---
title: "Matrix Chain Multiplication"
sidebar_label: "Matrix Chain Multiplication"
tags: [algorithm, dynamic-programming]
---

# Matrix Chain Multiplication

> Find the cheapest way to parenthesize a chain of matrix multiplications.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Dynamic Programming |
| **Time** | O(n^3) |
| **Space** | O(n^2) |

## Key Techniques

- Interval DP

## Notes & Interview Tips

Classic interval DP teaching example.

## How It Works

Matrix chain multiplication finds the optimal parenthesization to minimize the total number of scalar multiplications when multiplying a chain of matrices. The key insight: the result is the same regardless of parenthesization, but the number of operations varies enormously.

DP approach: `dp[i][j]` = minimum cost to multiply matrices i through j. Try every possible split point k: `dp[i][j] = min(dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1])` for all i ≤ k &lt; j.

This is the prototype **interval DP** problem. The same pattern applies to optimal BST construction, burst balloons, minimum cost to merge stones, and palindrome partitioning.

## Implementation

```python
def matrix_chain(dims):
    n = len(dims) - 1  # number of matrices
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):  # chain length
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n-1]
```

## Key Insight

> Interval DP pattern: fill the table by increasing interval length. For each interval [i,j], try every split point k. This pattern recurs in burst balloons, palindrome partitioning, and optimal BST.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟡 Medium | G75, B75, NC150 |
|  | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 🔴 Hard | NC150 |
|  | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | 🟡 Medium | NC150 |
|  | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) | 🔴 Hard | - |
|  | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | 🔴 Hard | G75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Matrix_chain_multiplication)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/)
