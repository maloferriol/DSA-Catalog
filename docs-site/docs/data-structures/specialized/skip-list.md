---
title: "Skip List"
sidebar_label: "Skip List"
tags: [data-structure, specialized]
---

# Skip List

> Probabilistic data structure of sorted linked lists with multiple levels giving O(log n) ops.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Specialized |
| **Time** | Search/Insert/Delete avg O(log n) |
| **Space** | O(n) |

## Key Techniques

- Randomized levels

## Notes & Interview Tips

Redis sorted sets are built on skip lists.

## How It Works

A skip list is a probabilistic data structure that provides O(log n) average-case search, insertion, and deletion — similar to a balanced BST but simpler to implement. It consists of multiple levels of sorted linked lists, where each higher level is a "fast lane" that skips over multiple elements.

Each element is promoted to higher levels with probability 1/2. Searching starts at the top level and moves right until the next element is too large, then drops down a level. On average, the height is O(log n) and each level has half the elements of the level below.

Skip lists are used in Redis (sorted sets), LevelDB, and MemSQL. They're an alternative to balanced BSTs with the advantage of simpler concurrent implementations (lock-free skip lists are easier than lock-free RB trees).

## Implementation

```python
import random

class SkipNode:
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level=16):
        self.max_level = max_level
        self.head = SkipNode(float('-inf'), max_level)
        self.level = 0

    def _random_level(self):
        lvl = 0
        while random.random() < 0.5 and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, target):
        curr = self.head
        for i in range(self.level, -1, -1):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        curr = curr.next[0]
        return curr and curr.val == target
```

## Key Insight

> Skip lists achieve O(log n) by creating 'express lanes' — higher levels skip over more elements. Probabilistic promotion (coin flip) provides balance without rotations.

## Visualization

- [Interactive Visualization](https://www.cs.usfca.edu/~galles/visualization/SkipList.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [LRU Cache](https://leetcode.com/problems/lru-cache/) | 🟡 Medium | G75, NC150 |
|  | [Min Stack](https://leetcode.com/problems/min-stack/) | 🟡 Medium | G75, NC150 |
|  | [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | 🟡 Medium | - |
|  | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | 🟡 Medium | G75, B75, NC150 |
|  | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | 🟡 Medium | B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Skip_list)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/skip-list/)
