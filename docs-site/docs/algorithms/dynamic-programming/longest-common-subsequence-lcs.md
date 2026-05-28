---
title: "Longest Common Subsequence (LCS)"
sidebar_label: "Longest Common Subsequence (LCS)"
tags: [algorithm, dynamic-programming]
---

# Longest Common Subsequence (LCS)

> Find longest sequence appearing in both strings in the same order (not necessarily contiguous).

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Dynamic Programming |
| **Time** | O(n·m) |
| **Space** | O(n·m) or O(min(n,m)) |

## Key Techniques

- 2D DP table

## Notes & Interview Tips

Edit distance variant.

## How It Works

LCS finds the longest subsequence present in both strings. A subsequence maintains relative order but doesn't need to be contiguous. It's the foundation for diff tools, version control, and bioinformatics sequence alignment.

DP approach: `dp[i][j]` = length of LCS of first i chars of s1 and first j chars of s2. If `s1[i-1] == s2[j-1]`, extend the LCS: `dp[i][j] = dp[i-1][j-1] + 1`. Otherwise, skip one char from either string: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

Time: O(m × n). To reconstruct the actual LCS, trace back through the DP table from `dp[m][n]`.

## Implementation

```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# Space-optimized to O(n)
def lcs_optimized(s1, s2):
    m, n = len(s1), len(s2)
    prev = [0] * (n + 1)
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev = curr
    return prev[n]
```

## Key Insight

> LCS is the prototype 2D DP problem. The key insight: if characters match, extend the diagonal. If not, take the better of skipping from either string. The edit distance problem follows the same structure.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | 🟡 Medium | B75, NC150 |
|  | [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) | 🟡 Medium | - |
|  | [Edit Distance](https://leetcode.com/problems/edit-distance/) | 🟡 Medium | NC150 |
|  | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟡 Medium | G75, B75, NC150 |
|  | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 🔴 Hard | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/)
