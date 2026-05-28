---
title: "Prefix Sum"
sidebar_label: "Prefix Sum"
tags: [technique, pattern]
---

# Prefix Sum

> Precompute cumulative sums so any range sum is answered in O(1).

## Quick Facts

| | |
|---|---|
| **Kind** | Technique |
| **Category** | Pattern |
| **Time** | Build O(n) · Query O(1) |
| **Space** | O(n) |

## Key Techniques

- 1D and 2D prefix
- Hash-map prefix for subarray sums

## Notes & Interview Tips

Sean Prashad: 'If need range sum/frequency queries → Prefix sum, BIT, Segment tree.'

## How It Works

Prefix sum precomputes cumulative sums so that any range sum query [L, R] can be answered in O(1). The prefix array: `prefix[i] = arr[0] + arr[1] + ... + arr[i-1]`. Then `sum(L, R) = prefix[R+1] - prefix[L]`.

This extends to 2D: `prefix[i][j]` = sum of rectangle from (0,0) to (i-1,j-1). A 2D range sum uses inclusion-exclusion on four corners.

Prefix sums are used in subarray sum problems (subarray sum equals K: count pairs where prefix[j] - prefix[i] = K using a hash map), difference arrays, and integral images.

## Implementation

```python
# Subarray sum equals K
from collections import defaultdict
def subarray_sum(nums, k):
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    curr_sum = 0
    count = 0
    for num in nums:
        curr_sum += num
        count += prefix_count[curr_sum - k]
        prefix_count[curr_sum] += 1
    return count

# 2D prefix sum
def build_2d_prefix(matrix):
    m, n = len(matrix), len(matrix[0])
    p = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            p[i+1][j+1] = matrix[i][j] + p[i][j+1] + p[i+1][j] - p[i][j]
    return p  # sum(r1,c1,r2,c2) = p[r2+1][c2+1]-p[r1][c2+1]-p[r2+1][c1]+p[r1][c1]
```

## Key Insight

> Prefix sum converts range sum queries from O(n) to O(1). Combined with a hash map (prefix_count), it solves 'subarray sum equals K' in O(n) by looking up complement prefix sums.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | 🟢 Easy | - |
|  | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | 🟡 Medium | - |
|  | [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | 🟡 Medium | - |
|  | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | 🟡 Medium | G75, B75, NC150 |
|  | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Prefix_sum)
- [leetcode.com](https://leetcode.com/tag/prefix-sum/)
