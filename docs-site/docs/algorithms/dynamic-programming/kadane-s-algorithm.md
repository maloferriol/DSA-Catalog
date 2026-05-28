---
title: "Kadane's Algorithm"
sidebar_label: "Kadane's Algorithm"
tags: [algorithm, dynamic-programming]
---

# Kadane's Algorithm

> Find maximum sum contiguous subarray in O(n) by tracking best ending here / best so far.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Dynamic Programming |
| **Time** | O(n) |
| **Space** | O(1) |

## Key Techniques

- Rolling DP

## Notes & Interview Tips

Foundational subarray DP.

## How It Works

Kadane's algorithm finds the maximum sum contiguous subarray in O(n) time. The idea: at each position, decide whether to extend the current subarray or start a new one. If the current sum is negative, starting fresh is always better.

DP interpretation: `dp[i]` = maximum sum ending at index i. Transition: `dp[i] = max(nums[i], dp[i-1] + nums[i])`. The answer is `max(dp)`. This can be done in O(1) space by tracking only the current and global maximums.

Variants: maximum product subarray (track both max and min due to negative numbers), maximum circular subarray (max of normal Kadane and total sum minus minimum subarray), and maximum sum with at most k elements.

## Implementation

```python
def max_subarray(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Maximum product subarray
def max_product(nums):
    max_so_far = min_so_far = result = nums[0]
    for num in nums[1:]:
        candidates = (num, max_so_far * num, min_so_far * num)
        max_so_far, min_so_far = max(candidates), min(candidates)
        result = max(result, max_so_far)
    return result
```

## Key Insight

> At each position: extend or restart. If the running sum is negative, any future subarray is better off starting fresh. This greedy choice gives optimal results in one pass.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | 🟡 Medium | G75, B75, NC150 |
|  | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | 🟡 Medium | B75, NC150 |
|  | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | G75, B75, NC150 |
|  | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard | NC150 |
|  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium | G75, B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
- [leetcode.com](https://leetcode.com/problems/maximum-subarray/)
