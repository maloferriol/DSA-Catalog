---
title: "Permutations / Combinations / Subsets"
sidebar_label: "Permutations / Combinations / Subsets"
tags: [algorithm, backtracking]
---

# Permutations / Combinations / Subsets

> Enumerate all permutations, combinations, or subsets of a collection.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Backtracking |
| **Time** | O(n·n!), O(n·2^n) |
| **Space** | O(n) |

## Key Techniques

- Backtracking
- Bit enumeration

## Notes & Interview Tips

Pattern: choose / explore / unchoose.

## How It Works

These three problems form the backbone of backtracking. All follow the same template: make a choice, recurse, undo the choice (backtrack).

**Subsets**: for each element, choose to include or exclude it. 2^n subsets total. **Permutations**: for each position, try every unused element. n! permutations total. **Combinations**: like subsets but with a fixed size k. Use a start index to avoid duplicates.

For duplicates in the input, sort first and skip consecutive equal elements at the same decision level. This pruning is essential for problems like "combination sum" with repeated candidates.

## Implementation

```python
# Subsets
def subsets(nums):
    result = []
    def backtrack(start, curr):
        result.append(curr[:])
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
    backtrack(0, [])
    return result

# Permutations
def permutations(nums):
    result = []
    def backtrack(curr, remaining):
        if not remaining:
            result.append(curr[:])
            return
        for i in range(len(remaining)):
            curr.append(remaining[i])
            backtrack(curr, remaining[:i] + remaining[i+1:])
            curr.pop()
    backtrack([], nums)
    return result

# Combinations (n choose k)
def combinations(n, k):
    result = []
    def backtrack(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        for i in range(start, n + 1):
            curr.append(i)
            backtrack(i + 1, curr)
            curr.pop()
    backtrack(1, [])
    return result
```

## Key Insight

> The backtracking template: choose → explore → unchoose. Subsets: include/exclude each element. Permutations: try each unused element at each position. Combinations: subsets of fixed size k.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Permutations](https://leetcode.com/problems/permutations/) | 🟡 Medium | G75, NC150 |
|  | [Subsets](https://leetcode.com/problems/subsets/) | 🟡 Medium | G75, NC150 |
|  | [Combinations](https://leetcode.com/problems/combinations/) | 🟡 Medium | - |
|  | [Combination Sum](https://leetcode.com/problems/combination-sum/) | 🟡 Medium | G75, B75, NC150 |
|  | [Subsets II](https://leetcode.com/problems/subsets-ii/) | 🟡 Medium | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Permutation)
- [leetcode.com](https://leetcode.com/tag/backtracking/)
