---
title: "Deque (Double-ended queue)"
sidebar_label: "Deque (Double-ended queue)"
tags: [data-structure, linear]
---

# Deque (Double-ended queue)

> Container with O(1) insert/remove at both ends; basis of monotonic queue.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Linear |
| **Time** | Push/Pop both ends O(1) |
| **Space** | O(n) |

## Key Techniques

- Monotonic deque
- Sliding window max/min

## Notes & Interview Tips

Sean Prashad: 'If asked for sliding window max/min → Monotonic queue.'

## How It Works

A deque (double-ended queue) supports O(1) insertion and removal at both ends. It combines the capabilities of both stacks and queues. In Python, `collections.deque` is implemented as a doubly-linked list of fixed-size blocks, giving O(1) operations at both ends.

The most important interview application is the **sliding window maximum/minimum** problem. A monotonic deque maintains indices of elements in decreasing order of value. As the window slides, you remove elements from the back that are smaller than the new element (they can never be the max), and remove elements from the front that have fallen outside the window. This gives O(n) for the entire array.

Deques are also used to implement BFS variants like **0-1 BFS** (edges with weight 0 or 1), where 0-weight neighbors go to the front of the deque and 1-weight neighbors go to the back.

## Implementation

```python
from collections import deque

# Sliding window maximum (monotonic deque)
def max_sliding_window(nums, k):
    dq = deque()  # indices, front = index of current max
    result = []
    for i, num in enumerate(nums):
        # Remove elements outside the window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove smaller elements from the back
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

## Key Insight

> The monotonic deque pattern solves sliding window min/max in O(n). Each element is pushed and popped at most once, so the total work across all iterations is linear.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/list)

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
- [docs.python.org](https://docs.python.org/3/library/collections.html#collections.deque)
