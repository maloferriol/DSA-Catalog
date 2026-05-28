---
title: "Binary Search Tree (BST)"
sidebar_label: "Binary Search Tree (BST)"
tags: [data-structure, trees]
---

# Binary Search Tree (BST)

> Binary tree where left subtree &lt; node &lt; right subtree, giving O(log n) search if balanced.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Trees |
| **Time** | Search/Insert/Delete avg O(log n), worst O(n) |
| **Space** | O(n) |

## Key Techniques

- In-order traversal yields sorted sequence
- Validation via bounds

## Notes & Interview Tips

Watch for degenerate skewed BST → use self-balancing in practice.

## How It Works

A BST is a binary tree where for every node, all values in the left subtree are strictly less, and all values in the right subtree are strictly greater. This invariant enables O(log n) search, insertion, and deletion on average — but O(n) worst-case when the tree degenerates into a linked list.

The key insight is that an **inorder traversal of a BST produces elements in sorted order**. This property is exploited constantly: validating a BST, finding the kth smallest element, or finding the closest value. Deletion is the trickiest operation — when removing a node with two children, replace it with either its inorder successor (smallest in right subtree) or predecessor (largest in left subtree).

To validate a BST, pass min/max bounds recursively: `isValid(node, min, max)`. Do NOT simply check `left < root < right` at each node — that only checks immediate children and misses violations deeper in the subtree.

## Implementation

```python
# Validate BST with range bounds
def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    if not root: return True
    if root.val <= lo or root.val >= hi:
        return False
    return (is_valid_bst(root.left, lo, root.val) and
            is_valid_bst(root.right, root.val, hi))

# Kth smallest element (inorder traversal)
def kth_smallest(root, k):
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0: return curr.val
        curr = curr.right

# LCA in BST (exploit BST property)
def lca_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
```

## Key Insight

> Inorder traversal of a BST = sorted order. For LCA in a BST, exploit the ordering: if both values are less than root, go left; both greater, go right; otherwise root is the LCA.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/bst)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | 🟡 Medium | G75, B75, NC150 |
|  | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | 🟡 Medium | G75, B75, NC150 |
|  | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | 🟡 Medium | G75, B75, NC150 |
|  | [Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/) | 🟡 Medium | - |
|  | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_tree)
- [visualgo.net](https://visualgo.net/en/bst)
