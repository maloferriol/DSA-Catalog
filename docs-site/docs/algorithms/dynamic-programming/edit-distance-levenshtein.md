---
title: "Edit Distance (Levenshtein)"
sidebar_label: "Edit Distance (Levenshtein)"
tags: [algorithm, dynamic-programming]
---

# Edit Distance (Levenshtein)

> Minimum number of insert/delete/replace operations to transform one string into another.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Dynamic Programming |
| **Time** | O(n·m) |
| **Space** | O(n·m) |

## Key Techniques

- 2D DP

## Notes & Interview Tips

Foundational string DP.

## How It Works

Edit distance measures the minimum number of single-character operations (insert, delete, replace) to transform one string into another. It's fundamental in spell checking, DNA sequence alignment, and fuzzy matching.

DP approach: `dp[i][j]` = edit distance between first i chars of s1 and first j chars of s2. If characters match, `dp[i][j] = dp[i-1][j-1]` (no operation needed). Otherwise, take the minimum of insert (`dp[i][j-1]+1`), delete (`dp[i-1][j]+1`), or replace (`dp[i-1][j-1]+1`).

Time: O(m × n). Space: O(m × n), optimizable to O(n) since each row only depends on the previous row.

## Implementation

```python
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],      # delete
                                   dp[i][j-1],      # insert
                                   dp[i-1][j-1])    # replace
    return dp[m][n]
```

## Key Insight

> Edit distance generalizes LCS to three operations. The base cases encode the cost of converting empty strings. Each cell considers three choices: insert, delete, or replace.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Edit Distance](https://leetcode.com/problems/edit-distance/) | 🟡 Medium | NC150 |
|  | [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) | 🟡 Medium | - |
|  | [One Edit Distance](https://leetcode.com/problems/one-edit-distance/) | 🟡 Medium | - |
|  | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟡 Medium | G75, B75, NC150 |
|  | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 🔴 Hard | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [leetcode.com](https://leetcode.com/problems/edit-distance/)
