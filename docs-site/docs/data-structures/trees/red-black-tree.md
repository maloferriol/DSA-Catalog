---
title: "Red-Black Tree"
sidebar_label: "Red-Black Tree"
tags: [data-structure, trees]
---

# Red-Black Tree

> Self-balancing BST using node colours and 5 invariants to guarantee O(log n).

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Trees |
| **Time** | All ops O(log n) |
| **Space** | O(n) |

## Key Techniques

- Recolouring
- Rotations

## Notes & Interview Tips

Backs Java TreeMap, C++ std::map.

## How It Works

A Red-Black tree is a self-balancing BST that uses node coloring (red or black) and five invariants to maintain approximate balance. The rules guarantee the longest path is at most twice the shortest, yielding O(log n) operations.

The five properties: (1) every node is red or black, (2) root is black, (3) null leaves are black, (4) red nodes can't have red children, (5) every path from a node to its leaves has the same number of black nodes (black-height).

Red-Black trees perform fewer rotations than AVL trees on insert/delete, making them better for write-heavy workloads. This is why they're used in Java's `TreeMap`, C++ `std::map`, and Linux's CFS scheduler. Understanding the concept is more important than memorizing every case for interviews.

## Implementation

```python
# Red-Black tree conceptual overview (not full implementation)
# The mental model: a 2-3-4 tree mapped to a binary tree
# - A black node alone = 2-node
# - A black node with one red child = 3-node
# - A black node with two red children = 4-node

# Key operations:
# Insert: always add as RED, then fix violations
# Fix-up cases:
#   Case 1: Uncle is RED -> recolor parent, uncle to black, grandparent to red
#   Case 2: Uncle is BLACK, node is "inside" child -> rotate to make it Case 3
#   Case 3: Uncle is BLACK, node is "outside" child -> rotate grandparent, recolor

# In practice, use your language's built-in:
# Python: sortedcontainers.SortedDict (not RB but same interface)
# Java: TreeMap, TreeSet
# C++: std::map, std::set
```

## Key Insight

> Red-Black trees are 2-3-4 trees in disguise. A red node is 'glued' to its black parent to form a multi-node. This mental model makes the rotations and recoloring intuitive.

## Visualization

- [Interactive Visualization](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) | 🟡 Medium | - |
|  | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | 🟡 Medium | - |
|  | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | 🟡 Medium | G75, B75, NC150 |
|  | [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) | 🟡 Medium | - |
|  | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/introduction-to-red-black-tree/)
