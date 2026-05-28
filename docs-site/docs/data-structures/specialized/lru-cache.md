---
title: "LRU Cache"
sidebar_label: "LRU Cache"
tags: [data-structure, specialized]
---

# LRU Cache

> Cache that evicts the least-recently-used entry; canonical implementation is hash map + doubly linked list.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Specialized |
| **Time** | Get/Put O(1) |
| **Space** | O(capacity) |

## Key Techniques

- Hash map + Doubly linked list

## Notes & Interview Tips

Sean Prashad: 'If given a stream of data → Heap, Design.' Classic design question.

## How It Works

An LRU (Least Recently Used) cache combines a hash map with a doubly linked list to provide O(1) `get` and `put`. The hash map gives O(1) key lookup; the doubly linked list maintains access order with O(1) move-to-front and remove-from-tail.

On `get`: if key exists, move its node to the front (most recently used) and return the value. On `put`: if key exists, update and move to front. If new, add to front. If over capacity, evict the tail (least recently used).

This is one of the most common system design interview questions and also appears as LeetCode 146. The implementation uses sentinel head/tail nodes to avoid edge cases.

## Implementation

```python
# See Doubly Linked List section for full implementation
# Key insight: HashMap<key, DLLNode> + Doubly Linked List
# - get(key): O(1) lookup + O(1) move to front
# - put(key, val): O(1) insert at front + O(1) evict from tail if full
```

## Key Insight

> LRU Cache = HashMap + Doubly Linked List. The hash map gives O(1) access to any node; the linked list maintains the access order with O(1) restructuring.

## Visualization

- [Interactive Visualization](https://www.cs.usfca.edu/~galles/visualization/LRUCache.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [LRU Cache](https://leetcode.com/problems/lru-cache/) | 🟡 Medium | G75, NC150 |
|  | [LFU Cache](https://leetcode.com/problems/lfu-cache/) | 🔴 Hard | - |
|  | [Min Stack](https://leetcode.com/problems/min-stack/) | 🟡 Medium | G75, NC150 |
|  | [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | 🟡 Medium | - |
|  | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | 🟡 Medium | G75, B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU))
- [leetcode.com](https://leetcode.com/problems/lru-cache/)
