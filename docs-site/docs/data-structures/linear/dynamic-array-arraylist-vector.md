---
title: "Dynamic Array (ArrayList / Vector)"
sidebar_label: "Dynamic Array (ArrayList / Vector)"
tags: [data-structure, linear]
---

# Dynamic Array (ArrayList / Vector)

> Resizable array that doubles capacity on overflow giving amortized O(1) append.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Linear |
| **Time** | Access O(1) · Append amortized O(1) · Insert/Delete O(n) |
| **Space** | O(n) |

## Key Techniques

- Amortized analysis
- Geometric resizing

## Notes & Interview Tips

Java ArrayList, C++ vector, Python list.

## How It Works

A dynamic array solves the fixed-size problem of regular arrays by automatically resizing when full. When the internal array runs out of space, a new array (typically 2× the size) is allocated, and all elements are copied over. This gives **amortized O(1)** append — most appends are O(1), but occasionally one triggers an O(n) copy.

The amortized analysis works because the expensive copies are exponentially rare. If you double the size each time, the total cost of n appends is O(n), giving O(1) per operation on average. This is the strategy used by Python's `list`, Java's `ArrayList`, C++'s `vector`, and Go's `slice`.

The key gotcha: if you know the final size in advance, pre-allocate to avoid unnecessary copies. In Python, use list comprehensions instead of repeated `.append()` when possible. Also be aware that deleting from the middle is still O(n) due to shifting.

## Implementation

```python
# Dynamic array from scratch (simplified)
class DynamicArray:
    def __init__(self):
        self._data = [None] * 2
        self._size = 0
        self._capacity = 2

    def append(self, val):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = val
        self._size += 1

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_cap

    def __getitem__(self, i):
        if i < 0 or i >= self._size:
            raise IndexError
        return self._data[i]
```

## Key Insight

> Doubling the capacity on resize gives amortized O(1) append. The total cost of n insertions is O(n) because the copy costs form a geometric series: 1 + 2 + 4 + ... + n = 2n - 1.

## Visualization

- [Interactive Visualization](https://www.cs.usfca.edu/~galles/visualization/ArrayList.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | G75, B75, NC150 |
|  | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard | NC150 |
|  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium | G75, B75, NC150 |
|  | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | 🟢 Easy | - |
|  | [3Sum](https://leetcode.com/problems/3sum/) | 🟡 Medium | G75, B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Dynamic_array)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/how-do-dynamic-arrays-work/)
