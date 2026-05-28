---
title: "Two Pointers"
sidebar_label: "Two Pointers"
tags: [technique, pattern]
---

# Two Pointers

> Use two indices moving through an array/string in coordinated fashion; opposite ends or same direction.

## Quick Facts

| | |
|---|---|
| **Kind** | Technique |
| **Category** | Pattern |
| **Time** | O(n) |
| **Space** | O(1) |

## Key Techniques

- Opposite-ends
- Same-direction
- Fast & slow

## Notes & Interview Tips

Sean Prashad: 'If input sorted / given a linked list → Two pointers.'

## How It Works

The two-pointer technique uses two indices that move through the data, typically from opposite ends toward the center (converging) or from the same end at different speeds (sliding window). It reduces O(n²) brute force to O(n).

Common patterns: (1) **Converging pointers** on sorted arrays (Two Sum, Container With Most Water), (2) **Same-direction pointers** for in-place operations (remove duplicates, partition), (3) **Left-right partitioning** (Dutch National Flag / 3-way partition).

Two pointers work when the problem has a monotonic relationship: moving one pointer in a direction always increases or decreases the objective, allowing you to eliminate possibilities.

## Implementation

```python
# Container With Most Water
def max_area(height):
    lo, hi = 0, len(height) - 1
    best = 0
    while lo < hi:
        best = max(best, min(height[lo], height[hi]) * (hi - lo))
        if height[lo] < height[hi]: lo += 1
        else: hi -= 1
    return best

# Remove duplicates in-place from sorted array
def remove_duplicates(nums):
    if not nums: return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write
```

## Key Insight

> Two pointers exploit ordering or partitioning to skip unnecessary comparisons. The key question: 'when I move this pointer, what can I guarantee about the elements I'm skipping?'

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | 🟡 Medium | NC150 |
|  | [3Sum](https://leetcode.com/problems/3sum/) | 🟡 Medium | G75, B75, NC150 |
|  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium | G75, B75, NC150 |
|  | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | 🟢 Easy | G75, B75, NC150 |
|  | [Sort Colors](https://leetcode.com/problems/sort-colors/) | 🟡 Medium | G75 |
|  | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | 🟡 Medium | - |
|  | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | 🟢 Easy | - |
|  | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | 🟢 Easy | - |
|  | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | 🟢 Easy | - |
|  | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Two_pointers_technique)
- [leetcode.com](https://leetcode.com/articles/two-pointer-technique/)
