---
title: "Recursion"
sidebar_label: "Recursion"
tags: [paradigm, pattern]
---

# Recursion

> Solve a problem by reducing it to smaller instances of itself.

## Quick Facts

| | |
|---|---|
| **Kind** | Paradigm |
| **Category** | Pattern |
| **Time** | Problem-specific |
| **Space** | O(depth) call stack |

## Key Techniques

- Base case
- Recursive case
- Tail recursion

## Notes & Interview Tips

Foundation of DP, backtracking, tree/graph traversal.

## How It Works

Recursion solves a problem by having a function call itself on a smaller instance. Every recursive solution has: (1) a **base case** (stops the recursion), (2) a **recursive case** (breaks the problem down and calls itself).

The mental model: trust that the recursive call solves the smaller problem correctly, and focus on how to combine it with the current step. This "leap of faith" is how to think about recursion — don't try to trace every call.

Common pitfalls: missing base case (infinite recursion), stack overflow (Python default limit: 1000), and doing too much work per call. Tail recursion (where the recursive call is the last operation) can be optimized by some compilers but not Python.

## Implementation

```python
# Power set using recursion
def power_set(nums, idx=0):
    if idx == len(nums):
        return [[]]
    rest = power_set(nums, idx + 1)
    return rest + [[nums[idx]] + s for s in rest]

# Tower of Hanoi
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)
```

## Key Insight

> Think of recursion as delegation: 'I'll handle this one step, and trust the recursive call to handle the rest.' Don't trace all the calls — define the contract and trust it.

## Visualization

- [Interactive Visualization](https://pythontutor.com/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | 🟡 Medium | NC150 |
|  | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | 🟢 Easy | G75, B75, NC150 |
|  | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | 🟢 Easy | G75, B75, NC150 |
|  | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | 🟡 Medium | NC150 |
|  | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 🔴 Hard | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Recursion_(computer_science))
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/recursion/)
