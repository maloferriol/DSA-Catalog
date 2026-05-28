---
title: "Disjoint Set Union (Union-Find)"
sidebar_label: "Disjoint Set Union (Union-Find)"
tags: [data-structure, trees]
---

# Disjoint Set Union (Union-Find)

> Partition of elements into disjoint sets supporting near-O(1) union and find.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Trees |
| **Time** | Union/Find amortized ~O(α(n)) |
| **Space** | O(n) |

## Key Techniques

- Path compression
- Union by rank/size

## Notes & Interview Tips

Sean Prashad: 'If asked for connectivity/grouping → Union-Find, DFS.'

## How It Works

Union-Find tracks disjoint sets with two operations: `find(x)` returns which set x belongs to, and `union(x, y)` merges two sets. With path compression and union by rank, both operations are nearly O(1) amortized.

Path compression flattens the tree during `find`: `parent[x] = find(parent[x])`. Union by rank attaches the shorter tree under the taller one. Together, these give inverse Ackermann time — effectively constant.

Union-Find is the go-to for dynamic connectivity: detecting cycles in undirected graphs, Kruskal's MST, connected components, and problems like "number of islands" or "accounts merge".

## Implementation

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        self.components -= 1
        return True
```

## Key Insight

> Path compression (`parent[x] = find(parent[x])`) is the single most important line — it flattens the tree on every find, keeping future operations near O(1).

## Visualization

- [Interactive Visualization](https://visualgo.net/en/ufds)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟡 Medium | G75, B75, NC150 |
|  | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | 🟡 Medium | NC150 |
|  | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | 🟡 Medium | - |
|  | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | 🟡 Medium | G75 |
|  | [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | 🟡 Medium | - |
|  | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | 🟡 Medium | B75, NC150 |
|  | [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | 🟡 Medium | B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)
- [cp-algorithms.com](https://cp-algorithms.com/data_structures/disjoint_set_union.html)
