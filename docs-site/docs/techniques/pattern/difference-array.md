---
title: "Difference Array"
sidebar_label: "Difference Array"
tags: [technique, pattern]
---

# Difference Array

> Apply range updates in O(1) and reconstruct array in O(n) via prefix-sum.

## Quick Facts

| | |
|---|---|
| **Kind** | Technique |
| **Category** | Pattern |
| **Time** | Update O(1) · Build O(n) |
| **Space** | O(n) |

## Key Techniques

- Range increment trick

## Notes & Interview Tips

Inverse of prefix sum for range updates.

## How It Works

A difference array supports O(1) range updates on an array: adding a value v to all elements in [L, R]. Instead of updating each element, increment `diff[L] += v` and `diff[R+1] -= v`. The original array is recovered by taking the prefix sum of the difference array.

This is the inverse of prefix sums: prefix sum converts point values to range sums, while difference arrays convert range updates to point updates. After all updates, one prefix sum pass gives the final array.

Applications: flight booking (add passengers to a range of stops), meeting room schedules, and any problem with multiple range increment operations.

## Implementation

```python
# Apply multiple range updates efficiently
def range_updates(n, updates):
    diff = [0] * (n + 1)
    for l, r, val in updates:
        diff[l] += val
        if r + 1 <= n:
            diff[r + 1] -= val
    # Recover actual values via prefix sum
    result = [0] * n
    result[0] = diff[0]
    for i in range(1, n):
        result[i] = result[i-1] + diff[i]
    return result
```

## Key Insight

> Difference array is the inverse of prefix sum. Mark +v at the start and -v after the end of a range. One final prefix sum pass reconstructs the array with all updates applied.

## Visualization

- [Interactive Visualization](https://cp-algorithms.com/data_structures/difference_array.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | 🟡 Medium | - |
|  | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | 🟡 Medium | G75, B75, NC150 |
|  | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | 🟢 Easy | - |
|  | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | 🟡 Medium | - |
|  | [Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/) | 🔴 Hard | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Prefix_sum)
- [leetcode.com](https://leetcode.com/problems/range-addition/)
