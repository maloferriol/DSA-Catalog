---
title: "Z Algorithm"
sidebar_label: "Z Algorithm"
tags: [algorithm, string]
---

# Z Algorithm

> Compute Z-array (length of longest substring starting at i matching a prefix) in O(n).

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | String |
| **Time** | O(n+m) |
| **Space** | O(n) |

## Key Techniques

- Z-box

## Notes & Interview Tips

Alternative to KMP.

## How It Works

The Z algorithm computes the Z-array: `Z[i]` = length of the longest substring starting at position i that matches a prefix of the string. It runs in O(n) time and is an alternative to KMP for string matching.

For pattern matching, concatenate `pattern + '$' + text` and compute the Z-array. Any position i where `Z[i] == len(pattern)` is a match. The '$' separator prevents the Z-array from crossing the boundary.

The Z algorithm is often simpler to implement than KMP and has the same complexity. It's popular in competitive programming.

## Implementation

```python
def z_function(s):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z

def z_search(text, pattern):
    combined = pattern + '$' + text
    z = z_function(combined)
    m = len(pattern)
    return [i - m - 1 for i in range(m + 1, len(combined)) if z[i] == m]
```

## Key Insight

> Z[i] tells you how much of the string starting at i matches the prefix. For pattern matching, use pattern$text and find positions where Z[i] equals the pattern length.

## Visualization

- [Interactive Visualization](https://personal.utdallas.edu/~besp/demo/John2010/z-algorithm.htm)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | 🟢 Easy | - |
|  | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | 🔴 Hard | - |
|  | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | 🟢 Easy | - |
|  | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | 🟢 Easy | B75, NC150 |
|  | [Repeated String Match](https://leetcode.com/problems/repeated-string-match/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Z-function)
- [cp-algorithms.com](https://cp-algorithms.com/string/z-function.html)
