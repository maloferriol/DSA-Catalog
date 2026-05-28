---
title: "Selection Sort"
sidebar_label: "Selection Sort"
tags: [algorithm, sorting]
---

# Selection Sort

> Repeatedly select the minimum from the unsorted suffix and place it.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Sorting |
| **Time** | O(n^2) |
| **Space** | O(1) |

## Key Techniques

- In-place

## Notes & Interview Tips

Educational only.

## How It Works

Selection sort finds the minimum element in the unsorted portion and swaps it with the first unsorted element. It makes exactly n-1 swaps, which is optimal when swaps are expensive (e.g., large records with small keys).

Time: O(n²) always (no best-case optimization). Space: O(1). Stable: no (the swap can change relative order of equal elements). Selection sort is rarely used in practice except when minimizing writes is critical.

The key property: after k iterations, the first k elements are the k smallest in sorted order. This makes selection sort useful as a mental model for understanding partial sorting.

## Implementation

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

## Key Insight

> Selection sort makes the minimum number of swaps (n-1). Use it when writing to memory is expensive but comparisons are cheap.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/sorting)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [3Sum](https://leetcode.com/problems/3sum/) | 🟡 Medium | G75, B75, NC150 |
|  | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | 🟡 Medium | - |
|  | [4Sum](https://leetcode.com/problems/4sum/) | 🟡 Medium | - |
|  | [Permutations II](https://leetcode.com/problems/permutations-ii/) | 🟡 Medium | - |
|  | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | 🟡 Medium | B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Selection_sort)
- [visualgo.net](https://visualgo.net/en/sorting)
