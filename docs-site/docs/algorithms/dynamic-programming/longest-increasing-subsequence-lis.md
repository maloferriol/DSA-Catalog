---
title: "Longest Increasing Subsequence (LIS)"
sidebar_label: "Longest Increasing Subsequence (LIS)"
tags: [algorithm, dynamic-programming]
---

# Longest Increasing Subsequence (LIS)

> Find the longest strictly increasing subsequence; O(n log n) with patience sorting.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Dynamic Programming |
| **Time** | O(n log n) |
| **Space** | O(n) |

## Key Techniques

- DP + binary search (patience sort)

## Notes & Interview Tips

Russian doll envelopes is a 2D variant.

## How It Works

LIS finds the longest subsequence where each element is strictly greater than the previous. The classic O(n²) DP: `dp[i]` = length of LIS ending at index i. For each i, check all j &lt; i where `nums[j] < nums[i]`.

The O(n log n) approach uses patience sorting: maintain a list `tails` where `tails[i]` is the smallest tail of all increasing subsequences of length i+1. For each new element, binary search for the position to insert/replace. The length of `tails` is the LIS length.

LIS appears in many forms: longest chain of pairs, Russian doll envelopes, maximum number of non-overlapping intervals in order.

## Implementation

```python
import bisect

# O(n log n) using patience sorting
def lis(nums):
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)

# O(n^2) DP (simpler, allows reconstruction)
def lis_dp(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

## Key Insight

> The O(n log n) solution maintains the smallest possible tail for each LIS length. Binary search finds where each new element fits. The tails array isn't the actual LIS, but its length is correct.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | 🟡 Medium | B75, NC150 |
|  | [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) | 🔴 Hard | - |
|  | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟡 Medium | G75, B75, NC150 |
|  | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 🔴 Hard | NC150 |
|  | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | 🟡 Medium | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Longest_increasing_subsequence)
- [leetcode.com](https://leetcode.com/problems/longest-increasing-subsequence/)
