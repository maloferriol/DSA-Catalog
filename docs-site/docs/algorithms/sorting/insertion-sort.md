---
title: "Insertion Sort"
sidebar_label: "Insertion Sort"
tags: [algorithm, sorting]
---

# Insertion Sort

> Build the sorted list one element at a time by inserting into the correct position.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Sorting |
| **Time** | O(n^2), O(n) on nearly-sorted |
| **Space** | O(1) |

## Key Techniques

- In-place
- Stable
- Online

## Notes & Interview Tips

Good for tiny or nearly-sorted arrays.

## How It Works

Insertion sort builds the sorted array one element at a time by inserting each element into its correct position among the already-sorted elements. It shifts larger elements right to make room.

Time: O(n²) worst/average, O(n) best (nearly sorted). Space: O(1). Stable: yes. Insertion sort excels on small arrays (n &lt; 20-50) and nearly-sorted data. This is why `timsort` (Python/Java's built-in sort) uses insertion sort for small runs.

It's also the sort to use when new elements arrive one at a time (online sorting) — each insertion takes O(n) in the worst case but O(1) if the element is already roughly in place.

## Implementation

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

## Key Insight

> Insertion sort is the fastest simple sort for nearly-sorted data and small arrays. Python's timsort uses insertion sort for runs shorter than 32-64 elements.

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

- [Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)
- [visualgo.net](https://visualgo.net/en/sorting)
