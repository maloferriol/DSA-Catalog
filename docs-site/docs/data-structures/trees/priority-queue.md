---
title: "Priority Queue"
sidebar_label: "Priority Queue"
tags: [data-structure, trees]
---

# Priority Queue

> Abstract queue ordered by priority; typically a binary heap underneath.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Trees |
| **Time** | Insert/Pop O(log n) |
| **Space** | O(n) |

## Key Techniques

- Dijkstra
- Median of stream
- Merge K sorted

## Notes & Interview Tips

Java PriorityQueue, Python heapq.

## How It Works

A priority queue is an abstract data type supporting `insert` and `extract-min/max`. The most common implementation is a binary heap, but the interface is what matters: elements come out in priority order, not insertion order.

In Python, `heapq` is a min-heap. For max-heap, negate values. For custom objects, use tuples: `(priority, tie_breaker, item)` where the tie_breaker (e.g., insertion counter) prevents comparison errors when priorities are equal.

Priority queues appear in Dijkstra's algorithm, task scheduling, event-driven simulation, and the "K closest/largest" family of problems. The **two-heap** pattern (max-heap for lower half + min-heap for upper half) elegantly solves the median-finding problem.

## Implementation

```python
import heapq

# Task scheduler with cooldown
def least_interval(tasks, n):
    freq = [0] * 26
    for t in tasks:
        freq[ord(t) - ord('A')] += 1
    max_freq = max(freq)
    max_count = freq.count(max_freq)
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)

# K closest points to origin
def k_closest(points, k):
    return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)
```

## Key Insight

> In Python, always use heapq with tuples for custom priority: (priority, counter, object). The counter breaks ties and avoids comparing incomparable objects.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/heap)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟡 Medium | NC150 |
|  | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | 🔴 Hard | G75, B75, NC150 |
|  | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | 🟡 Medium | B75, NC150 |
|  | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | 🔴 Hard | G75, B75, NC150 |
|  | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | 🟡 Medium | G75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Priority_queue)
- [docs.python.org](https://docs.python.org/3/library/heapq.html)
