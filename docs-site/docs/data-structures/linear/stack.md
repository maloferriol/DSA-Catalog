---
title: "Stack"
sidebar_label: "Stack"
tags: [data-structure, linear]
---

# Stack

> LIFO container supporting push and pop at the top in O(1).

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Linear |
| **Time** | Push/Pop/Peek O(1) |
| **Space** | O(n) |

## Key Techniques

- Recursion simulation
- Monotonic stack
- Parentheses matching
- Function call tracking

## Notes & Interview Tips

Sean Prashad: 'If recursion is banned → Stack.'

## How It Works

A stack is a Last-In-First-Out (LIFO) collection with two primary operations: `push` (add to top) and `pop` (remove from top), both O(1). Think of a stack of plates — you can only add or remove from the top.

Stacks are used implicitly every time you call a function (the call stack), and explicitly for problems involving **nesting** (matching parentheses), **backtracking** (DFS, undo operations), and **monotonic patterns** (next greater element). The stack is also used to convert recursive algorithms to iterative ones.

The **monotonic stack** is a powerful interview pattern: maintain a stack where elements are always in increasing (or decreasing) order. When pushing a new element, pop all elements that violate the order. This efficiently solves "next greater element," "largest rectangle in histogram," and similar problems in O(n).

## Implementation

```python
# Valid parentheses
def is_valid(s):
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in match:
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack

# Next greater element using monotonic stack
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # indices of elements waiting for their next greater
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            result[stack.pop()] = num
        stack.append(i)
    return result
```

## Key Insight

> Whenever you see nesting, matching, or 'nearest greater/smaller' in a problem, think stack. The monotonic stack pattern solves many O(n²) brute-force problems in O(n).

## Visualization

- [Interactive Visualization](https://visualgo.net/en/list)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | 🟢 Easy | G75, B75, NC150 |
|  | [Min Stack](https://leetcode.com/problems/min-stack/) | 🟡 Medium | G75, NC150 |
|  | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | 🟡 Medium | NC150 |
|  | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | 🟡 Medium | G75, NC150 |
|  | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | 🟢 Easy | G75 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/stack/)
