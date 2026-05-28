---
title: "Depth-First Search (DFS)"
sidebar_label: "Depth-First Search (DFS)"
tags: [algorithm, graph-traversal]
---

# Depth-First Search (DFS)

> Explore as far as possible along each branch before backtracking; recursion or stack.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Graph traversal |
| **Time** | O(V+E) |
| **Space** | O(V) |

## Key Techniques

- Recursion
- Stack
- Visited set
- Backtracking

## Notes & Interview Tips

Foundation of cycle detection, connectivity, topological sort.

## How It Works

DFS explores as far as possible along each branch before backtracking. It uses a stack (explicit or implicit via recursion). DFS is simpler to implement recursively and naturally handles tree-shaped problems.

DFS applications: cycle detection, topological sort, connected components, path finding, generating permutations/combinations, and solving puzzles (maze, N-queens). DFS on trees is the foundation of most tree algorithms.

Key DFS variants: **preorder** (process before children), **postorder** (process after children), and **inorder** (process between children, BST-specific). For graphs, track node states: WHITE (unvisited), GRAY (in current path), BLACK (fully processed) — GRAY→GRAY edge = cycle in directed graph.

## Implementation

```python
# DFS iterative
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if node in visited: continue
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return order

# DFS recursive: detect cycle in directed graph
def has_cycle_directed(graph, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    def dfs(node):
        color[node] = GRAY
        for nei in graph[node]:
            if color[nei] == GRAY: return True   # back edge = cycle
            if color[nei] == WHITE and dfs(nei): return True
        color[node] = BLACK
        return False
    return any(dfs(i) for i in range(n) if color[i] == WHITE)
```

## Key Insight

> DFS uses three colors for cycle detection in directed graphs: WHITE (unvisited), GRAY (in current path), BLACK (done). A GRAY→GRAY edge means you've found a cycle back to the current path.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/dfsbfs)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟡 Medium | G75, B75, NC150 |
|  | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | 🟢 Easy | G75, B75, NC150 |
|  | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | 🟡 Medium | G75, B75, NC150 |
|  | [Clone Graph](https://leetcode.com/problems/clone-graph/) | 🟡 Medium | G75, B75, NC150 |
|  | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | 🟡 Medium | B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)
- [visualgo.net](https://visualgo.net/en/dfsbfs)
