---
title: "Divide & Conquer"
sidebar_label: "Divide & Conquer"
tags: [paradigm, divide-conquer]
---

# Divide & Conquer

> Solve by splitting problem into subproblems, recursing, and combining results.

## Quick Facts

| | |
|---|---|
| **Kind** | Paradigm |
| **Category** | Divide & Conquer |
| **Time** | Master theorem dependent |
| **Space** | Recursion depth |

## Key Techniques

- Recursion
- Master theorem

## Notes & Interview Tips

Powers merge sort, quick sort, FFT, Karatsuba.

## How It Works

Divide and Conquer breaks a problem into smaller independent subproblems, solves them recursively, then combines the results. Unlike DP, the subproblems don't overlap.

The template: (1) **Divide** the problem into subproblems, (2) **Conquer** by solving subproblems recursively, (3) **Combine** the solutions. The time complexity is analyzed using the Master Theorem.

Classic examples: merge sort (divide array, sort halves, merge), quick sort (partition, sort partitions), binary search (halve search space), closest pair of points, and Strassen's matrix multiplication.

## Implementation

```python
# Maximum subarray using divide and conquer
def max_subarray_dc(nums, lo=0, hi=None):
    if hi is None: hi = len(nums) - 1
    if lo == hi: return nums[lo]
    mid = (lo + hi) // 2
    left_max = max_subarray_dc(nums, lo, mid)
    right_max = max_subarray_dc(nums, mid + 1, hi)
    # Max crossing subarray
    left_sum = float('-inf')
    s = 0
    for i in range(mid, lo - 1, -1):
        s += nums[i]
        left_sum = max(left_sum, s)
    right_sum = float('-inf')
    s = 0
    for i in range(mid + 1, hi + 1):
        s += nums[i]
        right_sum = max(right_sum, s)
    return max(left_max, right_max, left_sum + right_sum)
```

## Key Insight

> The Master Theorem gives the complexity: T(n) = aT(n/b) + O(n^d). Compare log_b(a) with d to determine if divide, combine, or both dominate.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Majority Element](https://leetcode.com/problems/majority-element/) | 🟢 Easy | G75 |
|  | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | 🟡 Medium | G75, B75, NC150 |
|  | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟡 Medium | NC150 |
|  | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | 🔴 Hard | G75, B75, NC150 |
|  | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm)
- [en.wikipedia.org](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))
