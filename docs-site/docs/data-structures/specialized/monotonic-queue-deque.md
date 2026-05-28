---
title: "Monotonic Queue / Deque"
sidebar_label: "Monotonic Queue / Deque"
tags: [data-structure, specialized]
---

# Monotonic Queue / Deque

> Deque maintained in monotonic order so the front is always the max/min of the current window.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Specialized |
| **Time** | Amortized O(1) per element |
| **Space** | O(window) |

## Key Techniques

- Sliding window max/min

## Notes & Interview Tips

LeetCode 239 is the canonical use-case.

## How It Works

A monotonic queue (implemented as a deque) maintains elements in non-increasing or non-decreasing order, enabling O(1) access to the min or max of a sliding window. Elements are removed from both ends: from the back when a new element makes them obsolete, and from the front when they leave the window.

This solves the sliding window maximum/minimum problem in O(n) total. The classic approach: maintain a deque of indices in decreasing order of values. For each new element, pop from the back all elements smaller than it (they'll never be the max), then append. Pop from the front if it's outside the window.

Also used in DP optimization (convex hull trick, sliding window DP) and 0-1 BFS.

## Implementation

```python
from collections import deque

# Sliding window maximum
def max_sliding_window(nums, k):
    dq = deque()  # indices, decreasing values
    result = []
    for i, num in enumerate(nums):
        while dq and dq[0] < i - k + 1: dq.popleft()
        while dq and nums[dq[-1]] <= num: dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

## Key Insight

> The monotonic deque gives O(1) sliding window min/max by maintaining a deque where the front is always the current answer. Each element enters and leaves the deque at most once → O(n) total.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | 🔴 Hard | NC150 |
|  | [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | 🔴 Hard | - |
|  | [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | 🟡 Medium | - |
|  | [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) | 🟡 Medium | - |
|  | [Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/) | 🔴 Hard | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Double-ended_queue)
- [leetcode.com](https://leetcode.com/problems/sliding-window-maximum/)
