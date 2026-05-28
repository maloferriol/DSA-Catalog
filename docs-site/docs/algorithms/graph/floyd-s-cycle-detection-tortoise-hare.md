---
title: "Floyd's Cycle Detection (Tortoise & Hare)"
sidebar_label: "Floyd's Cycle Detection (Tortoise & Hare)"
tags: [algorithm, graph]
---

# Floyd's Cycle Detection (Tortoise & Hare)

> Detect a cycle in a linked list / functional graph using two pointers at different speeds.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Graph |
| **Time** | O(n) |
| **Space** | O(1) |

## Key Techniques

- Fast & slow pointers

## Notes & Interview Tips

Canonical 'fast & slow pointers' pattern.

## How It Works

Floyd's algorithm detects cycles in a sequence using two pointers: a slow pointer (tortoise, moves 1 step) and a fast pointer (hare, moves 2 steps). If there's a cycle, they'll eventually meet inside the cycle. If the fast pointer reaches null, there's no cycle.

To find the cycle START: after the pointers meet, move one pointer back to the head and advance both at the same speed. They'll meet at the cycle entrance. This works because the distance from the head to the cycle start equals the distance from the meeting point to the cycle start (going around the cycle).

Applications: linked list cycle detection, finding duplicate numbers (LeetCode 287), detecting infinite loops in state machines, and any problem involving repeated function application.

## Implementation

```python
# Detect cycle and find cycle start
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            # Find cycle start
            slow = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow  # cycle start
    return None  # no cycle

# Find duplicate number (LeetCode 287)
def find_duplicate(nums):
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: break
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
```

## Key Insight

> After the tortoise and hare meet, resetting one to the start and advancing both at speed 1 finds the cycle entrance. This is because the distance from start to cycle entry equals the distance from meeting point to cycle entry.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/list)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | 🟢 Easy | G75, B75, NC150 |
|  | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | 🟡 Medium | - |
|  | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | 🟡 Medium | NC150 |
|  | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟡 Medium | G75, B75, NC150 |
|  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium | G75, B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Cycle_detection)
- [leetcode.com](https://leetcode.com/problems/linked-list-cycle-ii/)
