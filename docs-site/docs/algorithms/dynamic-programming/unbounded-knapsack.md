---
title: "Unbounded Knapsack"
sidebar_label: "Unbounded Knapsack"
tags: [algorithm, dynamic-programming]
---

# Unbounded Knapsack

> Knapsack variant allowing unlimited copies of each item.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Dynamic Programming |
| **Time** | O(n·W) |
| **Space** | O(W) |

## Key Techniques

- 1D DP, forward iteration

## Notes & Interview Tips

Coin change is a special case.

## How It Works

The unbounded knapsack allows each item to be used unlimited times. The only change from 0/1 knapsack: iterate capacity FORWARDS in the 1D DP, allowing items to be counted multiple times.

The classic example is the **coin change** problem: find the minimum number of coins to make a target amount, where each coin denomination can be used unlimited times.

The DP relation: `dp[w] = max(dp[w], dp[w - weight[i]] + value[i])` for each item. By iterating w forwards, `dp[w - weight[i]]` may already include item i, enabling reuse.

## Implementation

```python
# Coin Change: minimum coins to make amount
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for a in range(coin, amount + 1):  # forwards = unlimited use
            dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Coin Change II: count ways to make amount
def coin_change_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]
    return dp[amount]
```

## Key Insight

> 0/1 knapsack iterates capacity backwards (each item used once). Unbounded knapsack iterates forwards (items reused). This single change in loop direction switches between the two variants.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Coin Change](https://leetcode.com/problems/coin-change/) | 🟡 Medium | G75, B75, NC150 |
|  | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | 🟡 Medium | NC150 |
|  | [Perfect Squares](https://leetcode.com/problems/perfect-squares/) | 🟡 Medium | - |
|  | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟡 Medium | G75, B75, NC150 |
|  | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 🔴 Hard | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem#Unbounded_knapsack_problem)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/)
