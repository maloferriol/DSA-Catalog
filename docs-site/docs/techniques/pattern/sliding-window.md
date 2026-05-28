---
title: "Sliding Window"
sidebar_label: "Sliding Window"
tags: [technique, pattern]
---

# Sliding Window

> Maintain a window over a contiguous range that grows/shrinks while tracking aggregate state.

## Quick Facts

| | |
|---|---|
| **Kind** | Technique |
| **Category** | Pattern |
| **Time** | O(n) |
| **Space** | O(1) to O(window) |

## Key Techniques

- Fixed window
- Variable window
- Hash map state

## Notes & Interview Tips

Sean Prashad: 'If asked for max/min subarray/subset → DP, Sliding window.'

## How It Works

The sliding window technique maintains a window (subarray/substring) that expands or contracts as it moves through the data. It solves problems involving contiguous sequences in O(n) time.

**Fixed-size window**: advance both ends together, maintaining a window of size k. **Variable-size window**: expand the right end to include more, shrink the left end when a constraint is violated. The template: expand right → update state → shrink left while invalid → record answer.

Classic problems: maximum sum subarray of size k, longest substring without repeating characters, minimum window substring, and longest subarray with sum ≤ k.

## Implementation

```python
# Minimum window substring
from collections import Counter

def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    left = 0
    best = (0, float('inf'))
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:  # window contains all chars of t
            if right - left < best[1] - best[0]:
                best = (left, right)
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return s[best[0]:best[1]+1] if best[1] != float('inf') else ""
```

## Key Insight

> The variable-size sliding window template: expand right to satisfy the condition, then shrink left to find the minimum/optimal window. Each element is added and removed at most once → O(n).

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟡 Medium | G75, B75, NC150 |
|  | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | 🔴 Hard | G75, B75, NC150 |
|  | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | 🔴 Hard | NC150 |
|  | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | 🟡 Medium | B75, NC150 |
|  | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | 🟡 Medium | - |
|  | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | 🟡 Medium | NC150 |
|  | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | 🟢 Easy | - |
|  | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Sliding_window_protocol)
- [leetcode.com](https://leetcode.com/tag/sliding-window/)
