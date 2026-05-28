---
title: "Monotonic Stack"
sidebar_label: "Monotonic Stack"
tags: [data-structure, specialized]
---

# Monotonic Stack

> Stack whose elements are kept in monotonic order; used for next-greater/smaller-element problems.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Specialized |
| **Time** | Each element pushed/popped once → O(n) |
| **Space** | O(n) |

## Key Techniques

- Next greater / smaller element
- Histogram largest rectangle

## Notes & Interview Tips

Sean Prashad: 'If asked for next greater/smaller element → Monotonic stack.'

## How It Works

A monotonic stack maintains elements in strictly increasing (or decreasing) order. When pushing a new element, pop all elements that violate the monotonic property. This efficiently finds the "next greater element," "next smaller element," or "previous greater/smaller element" for every position in O(n) total.

The key insight: each element is pushed and popped at most once, so the total work across all iterations is O(n), not O(n²). The stack stores indices (not values) so you can compute distances.

Applications: next greater element, largest rectangle in histogram, trapping rain water, stock span, and daily temperatures.

## Implementation

```python
# Daily temperatures: days until a warmer day
def daily_temperatures(temps):
    n = len(temps)
    result = [0] * n
    stack = []  # indices, decreasing temps
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result

# Largest rectangle in histogram
def largest_rectangle(heights):
    stack = []  # indices, increasing heights
    max_area = 0
    heights.append(0)  # sentinel
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()
    return max_area
```

## Key Insight

> Each element is pushed and popped at most once → O(n) total. When you pop an element, you've found its 'answer' (next greater/smaller). The stack stores candidates still waiting for their answer.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | 🟡 Medium | NC150 |
|  | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | 🟢 Easy | - |
|  | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | 🔴 Hard | G75, NC150 |
|  | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | 🔴 Hard | G75, NC150 |
|  | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Monotonic_function)
- [liuzhenglaichn.gitbook.io](https://liuzhenglaichn.gitbook.io/algorithm/monotonic-stack)
