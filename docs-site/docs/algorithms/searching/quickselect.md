---
title: "Quickselect"
sidebar_label: "Quickselect"
tags: [algorithm, searching]
---

# Quickselect

> Partition-based selection of the k-th smallest element in average O(n).

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Searching |
| **Time** | Avg O(n), worst O(n^2) |
| **Space** | O(1) |

## Key Techniques

- Lomuto/Hoare partition
- Randomized pivot

## Notes & Interview Tips

Often beats a heap for one-shot top-K.

## How It Works

Quickselect finds the kth smallest element in an unsorted array in O(n) average time using the partition step from quicksort. After partitioning, the pivot is in its final position. If the pivot is at index k, we're done. If k is less, recurse on the left; if greater, recurse on the right.

Unlike quicksort, quickselect only recurses on ONE side, giving O(n + n/2 + n/4 + ...) = O(n) average time. Worst case is O(n²) with bad pivots, but random pivot selection makes this extremely unlikely.

The median-of-medians algorithm guarantees O(n) worst case but has a large constant factor and is rarely used in practice. Python's `statistics.median` and numpy's `partition` use quickselect variants.

## Implementation

```python
import random

def quickselect(arr, k):
    """Find the kth smallest element (0-indexed)."""
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        pivot_idx = random.randint(lo, hi)
        arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]
        pivot = arr[hi]
        i = lo
        for j in range(lo, hi):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[hi] = arr[hi], arr[i]
        if i == k:   return arr[i]
        elif i < k:  lo = i + 1
        else:        hi = i - 1
    return arr[lo]
```

## Key Insight

> Quickselect is quicksort but only recursing on one side. This halves the work each time: n + n/2 + n/4 + ... = 2n = O(n). Use it for 'kth largest/smallest' without fully sorting.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/sorting)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟡 Medium | NC150 |
|  | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | 🟡 Medium | G75, NC150 |
|  | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | 🟡 Medium | B75, NC150 |
|  | [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) | 🟡 Medium | - |
|  | [Find Kth Largest XOR Coordinate Value](https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Quickselect)
- [en.wikipedia.org](https://en.wikipedia.org/wiki/Quickselect)
