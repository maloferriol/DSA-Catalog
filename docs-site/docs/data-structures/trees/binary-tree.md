---
title: "Binary Tree"
sidebar_label: "Binary Tree"
tags: [data-structure, trees]
---

# Binary Tree

> Tree where each node has at most two children (left, right).

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Trees |
| **Time** | Traversal O(n) |
| **Space** | O(n) |

## Key Techniques

- DFS (pre/in/post-order)
- BFS (level order)
- Recursion
- Morris traversal

## Notes & Interview Tips

Sean Prashad: 'If given a tree → DFS, BFS.'

## How It Works

A binary tree is a hierarchical data structure where each node has at most two children (left and right). It's the foundation for BSTs, heaps, segment trees, and more. Binary trees can be complete (every level filled except possibly the last, filled left to right), full (every node has 0 or 2 children), or perfect (all leaves at the same depth).

Traversal is the most critical operation. There are four main traversals: **inorder** (left-root-right), **preorder** (root-left-right), **postorder** (left-right-root), and **level-order** (BFS). Understanding these recursively and iteratively is essential. Interviewers frequently ask for iterative implementations using an explicit stack.

Most tree problems reduce to a single pattern: solve for left subtree, solve for right subtree, combine at root. This is bottom-up recursion. Master this pattern and you can solve maximum depth, diameter, path sum, subtree validation, and dozens of other problems.

## Implementation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Maximum depth (bottom-up recursion)
def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Inorder traversal (iterative)
def inorder(root):
    result, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result

# Diameter of binary tree
def diameter(root):
    best = 0
    def height(node):
        nonlocal best
        if not node: return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)
        return 1 + max(l, r)
    height(root)
    return best
```

## Key Insight

> The pattern for most tree problems: (1) base case: null node returns identity value, (2) recurse on left and right, (3) combine results at current node. This bottom-up approach naturally handles the tree structure.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/bst)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | 🟢 Easy | G75, B75, NC150 |
|  | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | 🟡 Medium | G75, B75, NC150 |
|  | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | 🟢 Easy | G75, B75, NC150 |
|  | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | 🟡 Medium | G75 |
|  | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | 🟢 Easy | G75, NC150 |
|  | [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | 🟢 Easy | - |
|  | [Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/) | 🟢 Easy | - |
|  | [Path Sum](https://leetcode.com/problems/path-sum/) | 🟢 Easy | - |
|  | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Binary_tree)
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/tree/)
- [visualgo.net](https://visualgo.net/en/bst)
