---
title: "Fenwick Tree (Binary Indexed Tree)"
sidebar_label: "Fenwick Tree (Binary Indexed Tree)"
tags: [data-structure, trees]
---

# Fenwick Tree (Binary Indexed Tree)

> Compact array structure giving prefix sums with O(log n) update and query.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Trees |
| **Time** | Update/Query O(log n) |
| **Space** | O(n) |

## Key Techniques

- Low-bit trick
- Range sum

## Notes & Interview Tips

Lighter than segment tree when only prefix sums needed.

## How It Works

A Fenwick tree (BIT) supports prefix sum queries and point updates in O(log n) with just a 1D array. It achieves the same as a segment tree for prefix sums but with simpler code, lower memory, and smaller constants.

The magic is bit manipulation: the lowest set bit (`i & -i`) determines which range of elements each position covers. To query prefix sum: accumulate and remove LSB. To update: add delta and add LSB. Use 1-based indexing.

For range sum [L, R], compute `prefix(R) - prefix(L-1)`. Fenwick trees are a competitive programming staple — under 15 lines of code.

## Implementation

```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)
```

## Key Insight

> The operation `i & (-i)` extracts the lowest set bit, which elegantly partitions responsibilities among array positions. Fenwick trees are the simplest way to solve 'range sum with updates'.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/fenwicktree)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | 🟡 Medium | - |
|  | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | 🔴 Hard | - |
|  | [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) | 🔴 Hard | - |
|  | [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | 🔴 Hard | - |
|  | [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) | 🔴 Hard | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Fenwick_tree)
- [cp-algorithms.com](https://cp-algorithms.com/data_structures/fenwick.html)
