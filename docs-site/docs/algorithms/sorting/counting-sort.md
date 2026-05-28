---
title: "Counting Sort"
sidebar_label: "Counting Sort"
tags: [algorithm, sorting]
---

# Counting Sort

> Non-comparison sort using counts per value; O(n+k) for small integer range k.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Sorting |
| **Time** | O(n + k) |
| **Space** | O(k) |

## Key Techniques

- Bucketing by value

## Notes & Interview Tips

Beats O(n log n) when range is small.

## How It Works

Counting sort counts the occurrences of each value, then uses those counts to place elements directly into their sorted positions. It runs in O(n + k) time where k is the range of values. It's not a comparison sort — it doesn't compare elements against each other.

The algorithm: (1) count frequencies, (2) compute prefix sums (cumulative counts), (3) place each element at its computed position. This makes it stable when done correctly (iterate input in reverse when placing elements).

Counting sort is ideal when k is small relative to n (e.g., sorting grades 0-100, characters 'a'-'z', or ages 0-150). It's also used as the subroutine in radix sort.

## Implementation

```python
def counting_sort(arr, max_val=None):
    if not arr: return arr
    if max_val is None: max_val = max(arr)
    count = [0] * (max_val + 1)
    for x in arr:
        count[x] += 1
    result = []
    for val, cnt in enumerate(count):
        result.extend([val] * cnt)
    return result
```

## Key Insight

> Counting sort breaks the O(n log n) comparison-sort lower bound by not comparing elements. It trades space (O(k) for counts) for time. Only practical when k is small.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/sorting)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [H-Index](https://leetcode.com/problems/h-index/) | 🟡 Medium | - |
|  | [Array Partition](https://leetcode.com/problems/array-partition/) | 🟢 Easy | - |
|  | [Sort an Array](https://leetcode.com/problems/sort-an-array/) | 🟡 Medium | - |
|  | [Height Checker](https://leetcode.com/problems/height-checker/) | 🟢 Easy | - |
|  | [Relative Sort Array](https://leetcode.com/problems/relative-sort-array/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Counting_sort)
- [visualgo.net](https://visualgo.net/en/sorting)
