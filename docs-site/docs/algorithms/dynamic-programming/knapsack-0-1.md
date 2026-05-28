---
title: "Knapsack (0/1)"
sidebar_label: "Knapsack (0/1)"
tags: [algorithm, dynamic-programming]
---

# Knapsack (0/1)

> Choose items with weights and values to maximize value under a weight cap; each item once.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Dynamic Programming |
| **Time** | O(n·W) |
| **Space** | O(n·W) or O(W) |

## Key Techniques

- 2D DP
- Space-optimised 1D backward

## Notes & Interview Tips

Subset sum, partition equal subset sum are reductions.

## How It Works

The 0/1 knapsack problem: given items with weights and values, find the maximum value that fits in a knapsack of capacity W. Each item can be taken at most once (0/1 choice).

The DP approach: `dp[i][w]` = max value using items 1..i with capacity w. Transition: either skip item i (`dp[i-1][w]`) or take it (`dp[i-1][w-weight[i]] + value[i]`). Time: O(n × W), Space: O(n × W), optimizable to O(W) using a 1D array (iterate W backwards).

This is the foundational DP problem. Many problems reduce to knapsack variants: subset sum, partition equal subset sum, target sum, and coin change.

## Implementation

```python
# 0/1 Knapsack (space-optimized to O(W))
def knapsack(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for w in range(W, weights[i] - 1, -1):  # iterate backwards!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]

# Subset Sum: can we pick elements summing to target?
def subset_sum(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for t in range(target, num - 1, -1):
            dp[t] = dp[t] or dp[t - num]
    return dp[target]
```

## Key Insight

> The 1D optimization iterates capacity BACKWARDS to ensure each item is used at most once. Iterating forwards would allow reusing items (which is the unbounded knapsack variant).

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | 🟡 Medium | G75, NC150 |
|  | [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) | 🟡 Medium | - |
|  | [Target Sum](https://leetcode.com/problems/target-sum/) | 🟡 Medium | NC150 |
|  | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟡 Medium | G75, B75, NC150 |
|  | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 🔴 Hard | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)
