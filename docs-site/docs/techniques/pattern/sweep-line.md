---
title: "Sweep Line"
sidebar_label: "Sweep Line"
tags: [technique, pattern]
---

# Sweep Line

> Sort events by coordinate then sweep, maintaining active set; common for interval problems.

## Quick Facts

| | |
|---|---|
| **Kind** | Technique |
| **Category** | Pattern |
| **Time** | O(n log n) |
| **Space** | O(n) |

## Key Techniques

- Event sorting
- Active set

## Notes & Interview Tips

Sean Prashad: 'If asked for overlapping intervals → Sorting, Sweep line.'

## How It Works

Sweep line processes events sorted by position (usually x-coordinate or time), maintaining active state as the line sweeps from left to right. It converts 2D geometric problems into 1D problems.

The pattern: (1) create events (interval starts and ends), (2) sort events, (3) process events left to right, maintaining a data structure (set, heap, or counter) of active intervals.

Applications: interval intersection, rectangle overlap area, closest pair of points, and calendar booking conflicts.

## Implementation

```python
# Count maximum overlapping intervals
def max_overlap(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))   # interval starts
        events.append((end, -1))    # interval ends
    events.sort()
    max_count = count = 0
    for _, delta in events:
        count += delta
        max_count = max(max_count, count)
    return max_count
```

## Key Insight

> Convert intervals to +1/-1 events at start/end points. Sort by position, sweep through, track the running count. The maximum count is the answer for overlap problems.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | 🟡 Medium | G75, B75, NC150 |
|  | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | 🟡 Medium | B75, NC150 |
|  | [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | 🔴 Hard | - |
|  | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | G75, B75, NC150 |
|  | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Sweep_line_algorithm)
- [en.wikipedia.org](https://en.wikipedia.org/wiki/Sweep_line_algorithm)
