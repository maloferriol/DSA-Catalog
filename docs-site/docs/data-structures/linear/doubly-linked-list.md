---
title: "Doubly Linked List"
sidebar_label: "Doubly Linked List"
tags: [data-structure, linear]
---

# Doubly Linked List

> Linked list where each node has prev and next pointers, enabling O(1) deletion given a node.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Linear |
| **Time** | Access O(n) · Insert/Delete given node O(1) |
| **Space** | O(n) |

## Key Techniques

- Sentinel nodes
- LRU cache construction

## Notes & Interview Tips

Backbone of LRU cache (combined with hash map).

## How It Works

A doubly linked list extends the singly linked list by adding a `prev` pointer to each node, allowing traversal in both directions. This makes deletion O(1) when you have a reference to the node (no need to find the predecessor), and enables backward traversal.

The main practical use is in implementing **LRU caches** and **deques**. An LRU cache combines a hash map (for O(1) lookup) with a doubly linked list (for O(1) insertion/removal at both ends). When a key is accessed, its node is moved to the front; when the cache is full, the tail node is evicted.

The trade-off vs singly linked lists is memory: each node needs an extra pointer. In practice, doubly linked lists are used more often than singly linked lists because the bidirectional traversal eliminates many edge cases and simplifies algorithms.

## Implementation

```python
class DLLNode:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = DLLNode(), DLLNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_front(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache: return -1
        node = self.cache[key]
        self._remove(node)
        self._add_front(node)
        return node.val

    def put(self, key, val):
        if key in self.cache:
            self._remove(self.cache[key])
        node = DLLNode(key, val)
        self.cache[key] = node
        self._add_front(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```

## Key Insight

> Doubly linked lists with sentinel head/tail nodes make LRU Cache operations (move-to-front, remove-from-tail) clean O(1) with no edge cases.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/list)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [LRU Cache](https://leetcode.com/problems/lru-cache/) | 🟡 Medium | G75, NC150 |
|  | [All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) | 🔴 Hard | - |
|  | [LFU Cache](https://leetcode.com/problems/lfu-cache/) | 🔴 Hard | - |
|  | [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) | 🟡 Medium | - |
|  | [Design Browser History](https://leetcode.com/problems/design-browser-history/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Doubly_linked_list)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/doubly-linked-list/)
