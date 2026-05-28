---
title: "Segment Tree"
sidebar_label: "Segment Tree"
tags: [data-structure, trees]
---

# Segment Tree

> Tree over array intervals supporting range queries and point/range updates.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Trees |
| **Time** | Build O(n) · Query/Update O(log n) |
| **Space** | O(n) |

## Key Techniques

- Lazy propagation
- Range sum/min/max

## Notes & Interview Tips

Sean Prashad: 'If need range sum/frequency queries → Prefix sum, Binary indexed tree, Segment tree.'

## How It Works

A segment tree answers range queries (sum, min, max, GCD) over an array while supporting point or range updates, both in O(log n). Each leaf represents a single element, and each internal node stores the aggregate of its children's ranges.

Building takes O(n). For a range query [L, R], traverse the tree and at each node whose range is completely inside [L, R], take its value directly instead of recursing further. This decomposes the query into O(log n) nodes.

**Lazy propagation** extends segment trees to handle range updates in O(log n). Instead of updating every leaf, store a pending update at internal nodes and push it down only when needed.

## Implementation

```python
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self._build(nums, 1, 0, self.n - 1)

    def _build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
            return
        mid = (start + end) // 2
        self._build(nums, 2 * node, start, mid)
        self._build(nums, 2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update(self, idx, val, node=1, start=0, end=None):
        if end is None: end = self.n - 1
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid: self.update(idx, val, 2*node, start, mid)
        else:          self.update(idx, val, 2*node+1, mid+1, end)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

    def query(self, l, r, node=1, start=0, end=None):
        if end is None: end = self.n - 1
        if r < start or end < l: return 0
        if l <= start and end <= r: return self.tree[node]
        mid = (start + end) // 2
        return (self.query(l, r, 2*node, start, mid) +
                self.query(l, r, 2*node+1, mid+1, end))
```

## Key Insight

> Segment trees decompose any range [L,R] into O(log n) pre-computed segments. Lazy propagation defers range updates by storing pending operations at internal nodes.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/segmenttree)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | 🟡 Medium | - |
|  | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | 🔴 Hard | - |
|  | [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) | 🔴 Hard | - |
|  | [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | 🔴 Hard | - |
|  | [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Segment_tree)
- [cp-algorithms.com](https://cp-algorithms.com/data_structures/segment_tree.html)
