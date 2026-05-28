---
title: "Fast & Slow Pointers"
sidebar_label: "Fast & Slow Pointers"
tags: [technique, pattern]
---

# Fast & Slow Pointers

> Two pointers advancing at different speeds — detects cycles, finds middle, etc.

## Quick Facts

| | |
|---|---|
| **Kind** | Technique |
| **Category** | Pattern |
| **Time** | O(n) |
| **Space** | O(1) |

## Key Techniques

- Floyd's cycle detection
- Find middle of LL

## Notes & Interview Tips

Linked list cycle problems.

## How It Works

Fast and slow pointers (Floyd's tortoise and hare) use two pointers moving at different speeds to detect cycles, find middle elements, or identify patterns in linked lists and sequences.

**Cycle detection**: slow moves 1 step, fast moves 2 steps. If they meet, there's a cycle. To find the cycle start, reset slow to head and advance both at speed 1. **Finding the middle**: when fast reaches the end, slow is at the middle.

This technique uses O(1) space compared to O(n) for a hash set approach. It works because the fast pointer closes the gap by 1 each step in a cycle.

## Implementation

```python
# Find middle of linked list
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Linked list cycle detection + cycle start (see Floyd's Cycle Detection)
# Happy number (detect cycle in digit-square sequence)
def is_happy(n):
    def next_num(x):
        return sum(int(d)**2 for d in str(x))
    slow = fast = n
    while True:
        slow = next_num(slow)
        fast = next_num(next_num(fast))
        if fast == 1: return True
        if slow == fast: return False
```

## Key Insight

> In a cycle of length C, the fast pointer gains 1 step per iteration on the slow pointer. They meet after at most C iterations. This makes cycle detection O(n) time, O(1) space.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/list)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | 🟢 Easy | G75, B75, NC150 |
|  | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | 🟡 Medium | - |
|  | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | 🟡 Medium | NC150 |
|  | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | 🟢 Easy | G75 |
|  | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟡 Medium | G75, B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare)
- [leetcode.com](https://leetcode.com/problems/linked-list-cycle/)
