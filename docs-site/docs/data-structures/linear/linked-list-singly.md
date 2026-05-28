---
title: "Linked List (Singly)"
sidebar_label: "Linked List (Singly)"
tags: [data-structure, linear]
---

# Linked List (Singly)

> Chain of nodes, each holding a value and a pointer to the next node.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Linear |
| **Time** | Access O(n) · Insert/Delete at head O(1) |
| **Space** | O(n) |

## Key Techniques

- Two pointers
- Fast & slow (Floyd's cycle)
- Dummy head
- Iterative reverse

## Notes & Interview Tips

Sean Prashad: 'If given a linked list → Two pointers.'

## How It Works

A singly linked list is a chain of nodes where each node contains a value and a pointer to the next node. Unlike arrays, linked lists don't require contiguous memory, so insertion and deletion at a known position are O(1) — you just redirect pointers. The trade-off: there's no random access. To reach the nth element, you must traverse from the head, taking O(n).

The most important technique is using a **dummy head** (sentinel node). This eliminates edge cases for operations at the head of the list. Without a dummy head, inserting/deleting the first element requires special handling; with it, all positions are treated uniformly.

For interviews, linked list problems are fundamentally about pointer manipulation. The critical patterns are: **fast & slow pointers** (cycle detection, finding the middle), **reversing** (iterative with three pointers: prev, curr, next), and **merge** (combining two sorted lists). Always draw the pointers on paper before coding.

## Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reverse a linked list (iterative)
def reverse_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Detect cycle (Floyd's algorithm)
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

## Key Insight

> Always use a dummy head node to avoid special-casing operations on the first element. Return `dummy.next` as the result.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/list)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | 🟢 Easy | G75, B75, NC150 |
|  | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | 🟢 Easy | G75, B75, NC150 |
|  | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | 🟢 Easy | G75, B75, NC150 |
|  | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | 🟡 Medium | B75, NC150 |
|  | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | 🟢 Easy | - |
|  | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) | 🟢 Easy | - |
|  | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Linked_list)
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/linked-list/)
- [visualgo.net](https://visualgo.net/en/list)
