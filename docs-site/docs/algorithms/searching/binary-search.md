---
title: "Binary Search"
sidebar_label: "Binary Search"
tags: [algorithm, searching]
---

# Binary Search

> Repeatedly halve a sorted range to locate a target in O(log n).

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Searching |
| **Time** | O(log n) |
| **Space** | O(1) iterative |

## Key Techniques

- Two pointers (lo/hi)
- Binary search on answer
- Lower/upper bound

## Notes & Interview Tips

Sean Prashad: 'If input array is sorted → Binary search, Two pointers.' Also 'binary search on answer' pattern.

## How It Works

Binary search finds a target in a sorted array by repeatedly halving the search space. Compare the target with the middle element: if equal, found; if less, search the left half; if greater, search the right half. Time: O(log n).

The real power of binary search extends far beyond sorted arrays. It applies to any problem with a **monotonic predicate**: a function that is false for some prefix and true for some suffix (or vice versa). "Binary search on the answer" uses this to find the minimum/maximum value satisfying a condition.

Common bugs: integer overflow in `(lo + hi) / 2` (use `lo + (hi - lo) // 2`), infinite loops from wrong boundary updates, and off-by-one errors. Use the template: `lo, hi = inclusive bounds; while lo < hi; mid = lo + (hi - lo) // 2`.

## Implementation

```python
# Standard binary search
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:   return mid
        elif arr[mid] < target:  lo = mid + 1
        else:                    hi = mid - 1
    return -1

# Binary search on answer: minimum capacity to ship within D days
def ship_within_days(weights, days):
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        # Can we ship with capacity mid in ≤ days?
        d, curr = 1, 0
        for w in weights:
            if curr + w > mid:
                d += 1
                curr = 0
            curr += w
        if d <= days: hi = mid
        else:         lo = mid + 1
    return lo
```

## Key Insight

> Binary search works whenever there's a monotonic predicate. 'Binary search on the answer' is the pattern: guess a value, check if it's feasible, narrow the range. This solves many optimization problems.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/binarysearch)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Binary Search](https://leetcode.com/problems/binary-search/) | 🟢 Easy | G75, NC150 |
|  | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | 🟡 Medium | G75, B75, NC150 |
|  | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | 🟡 Medium | B75, NC150 |
|  | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard | NC150 |
|  | [First Bad Version](https://leetcode.com/problems/first-bad-version/) | 🟢 Easy | G75 |
|  | [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/) | 🟡 Medium | - |
|  | [Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) | 🟢 Easy | - |
|  | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | 🟡 Medium | - |
|  | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | 🟡 Medium | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/binary-search/)
- [leetcode.com](https://leetcode.com/explore/learn/card/binary-search/)
