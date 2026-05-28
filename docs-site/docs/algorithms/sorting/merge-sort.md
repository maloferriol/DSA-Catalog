---
title: "Merge Sort"
sidebar_label: "Merge Sort"
tags: [algorithm, sorting]
---

# Merge Sort

> Divide-and-conquer sort: split, recursively sort halves, then merge.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Sorting |
| **Time** | O(n log n) |
| **Space** | O(n) |

## Key Techniques

- Divide & conquer
- Stable
- Used for merging sorted lists

## Notes & Interview Tips

Sean Prashad: 'If asked to merge sorted lists/intervals → Merge sort, Heap.'

## How It Works

Merge sort divides the array in half, recursively sorts each half, then merges the two sorted halves. It's a classic divide-and-conquer algorithm with guaranteed O(n log n) time regardless of input.

The merge step is the key operation: use two pointers to walk through both halves, always picking the smaller element. This produces a sorted result in O(n). The recursion depth is O(log n), and each level does O(n) work, giving O(n log n) total.

Merge sort is stable, predictable (no worst-case degradation), and naturally parallelizable. Its main disadvantage is O(n) extra space. It's the algorithm of choice for sorting linked lists (no random access needed) and external sorting (sorting data that doesn't fit in memory).

## Implementation

```python
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
```

## Key Insight

> Merge sort is the only comparison-based O(n log n) sort that is stable AND has guaranteed worst-case O(n log n). Use it for linked lists and when stability matters.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/sorting)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | 🟢 Easy | - |
|  | [Sort List](https://leetcode.com/problems/sort-list/) | 🟡 Medium | - |
|  | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | 🔴 Hard | G75, B75, NC150 |
|  | [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) | 🔴 Hard | - |
|  | [3Sum](https://leetcode.com/problems/3sum/) | 🟡 Medium | G75, B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)
- [visualgo.net](https://visualgo.net/en/sorting)
