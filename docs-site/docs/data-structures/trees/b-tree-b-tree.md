---
title: "B-Tree / B+ Tree"
sidebar_label: "B-Tree / B+ Tree"
tags: [data-structure, trees]
---

# B-Tree / B+ Tree

> Multi-way balanced search tree optimized for block-based storage (databases, filesystems).

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Trees |
| **Time** | All ops O(log n) |
| **Space** | O(n) |

## Key Techniques

- Node splitting
- Disk-friendly layout

## Notes & Interview Tips

System design / database internals topic.

## How It Works

A B-Tree of order m allows each node to have up to m children and m-1 keys. Unlike binary trees, B-Trees are wide and shallow, minimizing disk I/O by keeping the height very low (typically 3-4 levels for millions of keys). Each node is designed to fit within a single disk page.

A B+ Tree is the variant used by virtually every database index (MySQL, PostgreSQL, SQLite). The key difference: all data is stored only in leaf nodes, and leaves are linked together for efficient range scans. Internal nodes contain only routing keys.

For interviews, the important thing is understanding **why** databases use B+ Trees: (1) low height = few disk reads, (2) leaf links = fast range queries, (3) high fanout = better cache utilization.

## Implementation

```python
# B-Tree conceptual overview
# Not typically implemented in interviews, but understand the operations:

# INSERT:
# 1. Find the correct leaf node
# 2. Insert the key in sorted order
# 3. If the node overflows (> m-1 keys):
#    - Split into two nodes
#    - Push the median key up to the parent
#    - Recursively split the parent if needed
# Tree grows in height ONLY when the root splits

# WHY B+ Trees for databases:
# - Height of 3-4 for billions of rows (each node = 1 disk page = 4-16 KB)
# - Range query: find start leaf, then follow leaf pointers
# - All leaves at same depth = predictable performance
```

## Key Insight

> B+ Trees minimize disk I/O by maximizing fanout. A B+ Tree with 4KB pages and 100-byte keys has a fanout of ~40, meaning 3 levels can index 40³ = 64,000 keys with just 3 disk reads.

## Visualization

- [Interactive Visualization](https://www.cs.usfca.edu/~galles/visualization/BPlusTree.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [LRU Cache](https://leetcode.com/problems/lru-cache/) | 🟡 Medium | G75, NC150 |
|  | [Min Stack](https://leetcode.com/problems/min-stack/) | 🟡 Medium | G75, NC150 |
|  | [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | 🟡 Medium | - |
|  | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | 🟡 Medium | G75, B75, NC150 |
|  | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | 🟡 Medium | B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/B-tree)
- [en.wikipedia.org](https://en.wikipedia.org/wiki/B%2B_tree)
