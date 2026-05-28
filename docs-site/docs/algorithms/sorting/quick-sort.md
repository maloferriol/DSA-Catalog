---
title: "Quick Sort"
sidebar_label: "Quick Sort"
tags: [algorithm, sorting]
---

# Quick Sort

> Pick a pivot, partition into smaller/greater, recurse; average O(n log n).

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Sorting |
| **Time** | Avg O(n log n), worst O(n^2) |
| **Space** | O(log n) recursion |

## Key Techniques

- Pivot selection
- Partitioning

## Notes & Interview Tips

Backbone of std::sort in many libraries (often introsort).

## How It Works

Quick sort picks a pivot, partitions the array so all elements less than the pivot come before it and all greater come after, then recursively sorts the partitions. Average case is O(n log n), but worst case is O(n²) when the pivot is always the smallest or largest element.

The partition step is the key: Lomuto's scheme is simpler (single pointer), Hoare's scheme is faster (fewer swaps). Choosing a good pivot is critical — **median of three** (first, middle, last) or **random pivot** avoids the worst case on nearly-sorted input.

Quick sort is in-place (O(log n) stack space), has excellent cache performance (sequential access), and is faster than merge sort in practice despite the same O(n log n) average. Python's built-in sort uses timsort, but C's `qsort` and many other standard libraries use quicksort variants.

## Implementation

```python
import random

def quick_sort(arr, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo >= hi: return
    pivot_idx = partition(arr, lo, hi)
    quick_sort(arr, lo, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, hi)

def partition(arr, lo, hi):
    pivot_idx = random.randint(lo, hi)
    arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i
```

## Key Insight

> Random pivot selection gives O(n log n) expected time regardless of input. Quick sort's cache-friendliness (sequential memory access) makes it 2-3x faster than merge sort in practice.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/sorting)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Sort Colors](https://leetcode.com/problems/sort-colors/) | 🟡 Medium | G75 |
|  | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟡 Medium | NC150 |
|  | [Sort an Array](https://leetcode.com/problems/sort-an-array/) | 🟡 Medium | - |
|  | [3Sum](https://leetcode.com/problems/3sum/) | 🟡 Medium | G75, B75, NC150 |
|  | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Quicksort)
- [visualgo.net](https://visualgo.net/en/sorting)
