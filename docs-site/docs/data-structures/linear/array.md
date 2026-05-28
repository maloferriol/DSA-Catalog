---
title: "Array"
sidebar_label: "Array"
tags: [data-structure, linear]
---

# Array

> Contiguous block of memory storing fixed-size elements, accessed by integer index in O(1).

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Linear |
| **Time** | Access O(1) · Search O(n) · Insert/Delete O(n) |
| **Space** | O(n) |

## Key Techniques

- Two pointers
- Sliding window
- Prefix sum
- Difference array
- In-place swap
- Sorting

## Notes & Interview Tips

Most common interview structure. Master sliding window and two pointers first.

## How It Works

An array is the most fundamental data structure: a contiguous block of memory where elements are stored at fixed-size intervals. Because the memory is contiguous and elements are uniformly sized, accessing any element by index is O(1) — the address is simply `base + index × element_size`. This makes arrays the fastest structure for random access.

The trade-off is rigidity. Inserting or deleting in the middle requires shifting all subsequent elements, costing O(n). Arrays also have a fixed size at allocation time (in languages like C/Java). Despite these limitations, arrays underpin nearly every other data structure — hash tables, heaps, and even graphs are often implemented with arrays.

For interviews, arrays are the most common structure you'll encounter. Master the core patterns: **two pointers** (converging from both ends), **sliding window** (fixed or variable-size subarray), and **prefix sum** (precompute cumulative sums for O(1) range queries).

## Implementation

```python
# Two Pointers: check if sorted array has pair summing to target
def two_sum_sorted(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        s = nums[lo] + nums[hi]
        if s == target:
            return [lo, hi]
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return []

# Prefix Sum: O(1) range sum queries after O(n) preprocessing
def build_prefix(nums):
    prefix = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x
    return prefix  # range_sum(l, r) = prefix[r+1] - prefix[l]
```

## Key Insight

> Arrays give O(1) random access because memory addresses are computed arithmetically. This is why array-based structures (heaps, hash tables) are so fast — they reduce to index arithmetic.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/array)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | G75, B75, NC150 |
|  | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | 🟢 Easy | G75, B75, NC150 |
|  | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | 🟡 Medium | G75, B75, NC150 |
|  | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | 🟡 Medium | G75, B75, NC150 |
|  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium | G75, B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Array_(data_structure))
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/array/)
- [visualgo.net](https://visualgo.net/en/list)
