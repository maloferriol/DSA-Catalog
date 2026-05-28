---
title: "Heap Sort"
sidebar_label: "Heap Sort"
tags: [algorithm, sorting]
---

# Heap Sort

> Build a max-heap, then repeatedly extract the max.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Sorting |
| **Time** | O(n log n) |
| **Space** | O(1) |

## Key Techniques

- Heapify

## Notes & Interview Tips

In-place O(n log n) but not stable.

## How It Works

Heap sort builds a max-heap from the array, then repeatedly extracts the maximum to build the sorted array from right to left. It combines the guaranteed O(n log n) of merge sort with the O(1) extra space of insertion sort.

The process: (1) build a max-heap in O(n) using bottom-up heapify, (2) swap the root (maximum) with the last element, reduce heap size by 1, and sift down the new root. Repeat n-1 times.

Heap sort is not stable and has poor cache performance (jumping around the array during sift-down). In practice, it's slower than quicksort but useful as a guaranteed O(n log n) fallback. Introsort (used by C++ `std::sort`) starts with quicksort and switches to heapsort if recursion depth exceeds 2 log n.

## Implementation

```python
def heap_sort(arr):
    n = len(arr)
    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, n, i)
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(arr, i, 0)
    return arr

def sift_down(arr, size, i):
    largest = i
    left, right = 2*i + 1, 2*i + 2
    if left < size and arr[left] > arr[largest]:   largest = left
    if right < size and arr[right] > arr[largest]:  largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        sift_down(arr, size, largest)
```

## Key Insight

> Heap sort gives O(n log n) worst-case with O(1) extra space — the only comparison sort that achieves both. The build-heap step is O(n), not O(n log n).

## Visualization

- [Interactive Visualization](https://visualgo.net/en/sorting)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Sort an Array](https://leetcode.com/problems/sort-an-array/) | 🟡 Medium | - |
|  | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟡 Medium | NC150 |
|  | [3Sum](https://leetcode.com/problems/3sum/) | 🟡 Medium | G75, B75, NC150 |
|  | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | 🟡 Medium | - |
|  | [4Sum](https://leetcode.com/problems/4sum/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Heapsort)
- [visualgo.net](https://visualgo.net/en/sorting)
