---
title: "Bubble Sort"
sidebar_label: "Bubble Sort"
tags: [algorithm, sorting]
---

# Bubble Sort

> Repeatedly swap adjacent out-of-order pairs until sorted.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Sorting |
| **Time** | O(n^2) |
| **Space** | O(1) |

## Key Techniques

- Adjacent swaps

## Notes & Interview Tips

Educational only.

## How It Works

Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order. The largest unsorted element "bubbles" to its correct position each pass. After n-1 passes, the array is sorted.

Time: O(n²) average and worst case, O(n) best case (already sorted, with early termination). Space: O(1). Stable: yes. It's the simplest sorting algorithm to understand but one of the slowest in practice.

Useful only for educational purposes and tiny arrays. The only practical advantage: it can detect if the array is already sorted in O(n) by checking if any swap occurred during a pass.

## Implementation

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # already sorted
    return arr
```

## Key Insight

> The early termination optimization (if no swaps in a pass, the array is sorted) makes bubble sort O(n) on already-sorted input. Without it, it always runs O(n²).

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

- [Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)
- [visualgo.net](https://visualgo.net/en/sorting)
