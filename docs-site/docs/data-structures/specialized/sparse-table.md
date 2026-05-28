---
title: "Sparse Table"
sidebar_label: "Sparse Table"
tags: [data-structure, specialized]
---

# Sparse Table

> Precomputed table that answers immutable range min/max/gcd queries in O(1) after O(n log n) prep.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Specialized |
| **Time** | Build O(n log n) · Query O(1) |
| **Space** | O(n log n) |

## Key Techniques

- Doubling
- Idempotent operations only

## Notes & Interview Tips

Range min/max query specialty.

## How It Works

A sparse table answers static range minimum (or maximum, GCD) queries in O(1) after O(n log n) preprocessing. It precomputes answers for all ranges of power-of-2 lengths. Any range [L, R] can be covered by at most two overlapping power-of-2 ranges.

The table `st[i][j]` stores the minimum of the range starting at index j with length 2^i. Building: `st[0][j] = arr[j]`, then `st[i][j] = min(st[i-1][j], st[i-1][j + 2^(i-1)])`. Querying: find k = floor(log2(R-L+1)), return min(st[k][L], st[k][R-2^k+1]).

Sparse tables work for idempotent operations (min, max, GCD, OR) where overlapping ranges don't cause problems. For sum, use a prefix sum array or Fenwick tree instead.

## Implementation

```python
import math

class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        k = int(math.log2(n)) + 1
        self.st = [[0] * n for _ in range(k)]
        self.st[0] = arr[:]
        for i in range(1, k):
            for j in range(n - (1 << i) + 1):
                self.st[i][j] = min(self.st[i-1][j],
                                    self.st[i-1][j + (1 << (i-1))])

    def query(self, l, r):
        k = int(math.log2(r - l + 1))
        return min(self.st[k][l], self.st[k][r - (1 << k) + 1])
```

## Key Insight

> Any range [L,R] can be covered by two overlapping power-of-2 ranges. For idempotent operations like min/max/GCD, overlapping doesn't matter, giving O(1) queries.

## Visualization

- [Interactive Visualization](https://cp-algorithms.com/data_structures/sparse-table.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | 🔴 Hard | - |
|  | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | 🟡 Medium | - |
|  | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | 🔴 Hard | - |
|  | [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) | 🔴 Hard | - |
|  | [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Range_minimum_query)
- [cp-algorithms.com](https://cp-algorithms.com/data_structures/sparse-table.html)
