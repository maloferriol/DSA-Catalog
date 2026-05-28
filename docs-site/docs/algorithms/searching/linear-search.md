---
title: "Linear Search"
sidebar_label: "Linear Search"
tags: [algorithm, searching]
---

# Linear Search

> Scan the collection element-by-element until target is found.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Searching |
| **Time** | O(n) |
| **Space** | O(1) |

## Key Techniques

- Brute force baseline

## Notes & Interview Tips

Baseline to beat.

## How It Works

Linear search checks each element sequentially until finding the target or reaching the end. Time: O(n) worst/average, O(1) best. It works on unsorted data and requires no preprocessing.

While simple, linear search is the optimal choice for unsorted data, small arrays, or one-time searches. For repeated searches on the same data, sort first + binary search or use a hash set.

Linear search is also the only option when data arrives as a stream and you can't store everything. The sentinel optimization places the target at the end to avoid checking bounds in the loop.

## Implementation

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

## Key Insight

> Linear search is optimal for unsorted data. If you're searching the same data repeatedly, consider sorting it (O(n log n) once) for O(log n) binary searches.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/sorting)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | G75, B75, NC150 |
|  | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard | NC150 |
|  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium | G75, B75, NC150 |
|  | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | 🟢 Easy | - |
|  | [3Sum](https://leetcode.com/problems/3sum/) | 🟡 Medium | G75, B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Linear_search)
- [en.wikipedia.org](https://en.wikipedia.org/wiki/Linear_search)
