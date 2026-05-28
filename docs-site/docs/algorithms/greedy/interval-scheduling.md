---
title: "Interval Scheduling"
sidebar_label: "Interval Scheduling"
tags: [algorithm, greedy]
---

# Interval Scheduling

> Select the maximum number of non-overlapping intervals; sort by end time and scan.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Greedy |
| **Time** | O(n log n) |
| **Space** | O(1) |

## Key Techniques

- Sort by end time

## Notes & Interview Tips

Sean Prashad: 'If asked for overlapping intervals → Sorting, Sweep line.'

## How It Works

Interval scheduling selects the maximum number of non-overlapping intervals (or finds the minimum intervals to cover a range). The greedy approach: sort intervals by end time, greedily select the earliest-ending interval that doesn't overlap with the last selected one.

For minimum meeting rooms (interval partitioning), sort by start time and use a min-heap tracking end times. For interval merging, sort by start time and merge overlapping intervals.

The greedy choice (earliest end time) is optimal because it leaves the most room for future intervals. This is one of the classic greedy proofs: exchange argument.

## Implementation

```python
# Maximum non-overlapping intervals
def max_non_overlapping(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by end time
    count = 0
    end = float('-inf')
    for s, e in intervals:
        if s >= end:
            count += 1
            end = e
    return count

# Merge overlapping intervals
def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return merged

# Minimum meeting rooms (min-heap)
import heapq
def min_rooms(intervals):
    intervals.sort()
    heap = []
    for s, e in intervals:
        if heap and heap[0] <= s:
            heapq.heapreplace(heap, e)
        else:
            heapq.heappush(heap, e)
    return len(heap)
```

## Key Insight

> Sort by END time for maximum non-overlapping. Sort by START time for merging and minimum rooms. The greedy choice of earliest end time provably maximizes the number of selected intervals.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | 🟡 Medium | B75, NC150 |
|  | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | 🟡 Medium | - |
|  | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | 🟡 Medium | G75, B75, NC150 |
|  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium | G75, B75, NC150 |
|  | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) | 🔴 Hard | - |
|  | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | 🟢 Easy | B75, NC150 |
|  | [Insert Interval](https://leetcode.com/problems/insert-interval/) | 🟡 Medium | G75, B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Interval_scheduling)
- [leetcode.com](https://leetcode.com/problems/non-overlapping-intervals/)
