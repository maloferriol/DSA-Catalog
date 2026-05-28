---
title: "Ternary Search"
sidebar_label: "Ternary Search"
tags: [algorithm, searching]
---

# Ternary Search

> Search a unimodal function by splitting into thirds.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Searching |
| **Time** | O(log n) |
| **Space** | O(1) |

## Key Techniques

- Unimodal optimization

## Notes & Interview Tips

Useful for finding extrema of unimodal functions.

## How It Works

Ternary search finds the maximum or minimum of a unimodal function (a function that increases then decreases, or vice versa) by dividing the search space into thirds. At each step, evaluate the function at two points (m1 and m2 at 1/3 and 2/3 of the range) and eliminate one-third of the search space.

Time: O(log₃ n) comparisons, but each step requires 2 function evaluations vs binary search's 1, making it slightly slower per comparison. However, it solves a different class of problems: finding extrema of unimodal functions.

Ternary search is used in competitive programming for optimization on continuous functions (e.g., minimizing distance, maximizing area). For discrete problems, binary search on the derivative (difference) is often simpler.

## Implementation

```python
# Ternary search for minimum of unimodal function on [lo, hi]
def ternary_search(f, lo, hi, eps=1e-9):
    while hi - lo > eps:
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if f(m1) < f(m2):
            hi = m2
        else:
            lo = m1
    return (lo + hi) / 2
```

## Key Insight

> Ternary search finds extrema of unimodal functions where binary search can't. But for many discrete problems, you can convert to binary search by searching on the 'derivative' (adjacent differences).

## Visualization

- [Interactive Visualization](https://cp-algorithms.com/num_methods/ternary_search.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard | NC150 |
|  | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | 🟡 Medium | G75, B75, NC150 |
|  | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | 🟡 Medium | - |
|  | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | 🟢 Easy | - |
|  | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Ternary_search)
- [cp-algorithms.com](https://cp-algorithms.com/num_methods/ternary_search.html)
