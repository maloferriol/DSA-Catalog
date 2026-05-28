---
title: "AVL Tree"
sidebar_label: "AVL Tree"
tags: [data-structure, trees]
---

# AVL Tree

> Self-balancing BST where heights of children differ by at most 1; rebalances via rotations.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Trees |
| **Time** | All ops O(log n) |
| **Space** | O(n) |

## Key Techniques

- Rotations
- Height balancing

## Notes & Interview Tips

Conceptual — interview-relevant for 'how does std::map work?' style questions.

## How It Works

An AVL tree is a self-balancing BST where the heights of the left and right subtrees of every node differ by at most 1. After every insertion or deletion, the tree checks balance factors along the path to the root and performs rotations to restore balance. This guarantees O(log n) worst-case for all operations.

There are four rotation cases: **LL** (single right rotation), **RR** (single left rotation), **LR** (left then right rotation), and **RL** (right then left rotation). Identify the case by examining the balance factor of the unbalanced node and its child.

AVL trees are stricter than Red-Black trees (max height ~1.44 log n vs ~2 log n), making lookups slightly faster but insertions/deletions slightly slower due to more frequent rotations. They're preferred when reads dominate writes.

## Implementation

```python
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.height = 1

def height(node):
    return node.height if node else 0

def balance_factor(node):
    return height(node.left) - height(node.right) if node else 0

def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x

def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def insert(node, val):
    if not node: return AVLNode(val)
    if val < node.val:    node.left = insert(node.left, val)
    elif val > node.val:  node.right = insert(node.right, val)
    else: return node
    node.height = 1 + max(height(node.left), height(node.right))
    bf = balance_factor(node)
    if bf > 1 and val < node.left.val:   return rotate_right(node)       # LL
    if bf < -1 and val > node.right.val: return rotate_left(node)        # RR
    if bf > 1 and val > node.left.val:                                   # LR
        node.left = rotate_left(node.left)
        return rotate_right(node)
    if bf < -1 and val < node.right.val:                                 # RL
        node.right = rotate_right(node.right)
        return rotate_left(node)
    return node
```

## Key Insight

> After each insert/delete, update heights bottom-up and check balance factors. The rotation case is determined by the signs of the balance factors of the unbalanced node and its child.

## Visualization

- [Interactive Visualization](https://www.cs.usfca.edu/~galles/visualization/AVLtree.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) | 🟡 Medium | - |
|  | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | 🟡 Medium | - |
|  | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | 🟡 Medium | G75, B75, NC150 |
|  | [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) | 🟡 Medium | - |
|  | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/AVL_tree)
- [visualgo.net](https://visualgo.net/en/bst)
