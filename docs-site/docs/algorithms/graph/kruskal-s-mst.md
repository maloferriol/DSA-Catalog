---
title: "Kruskal's MST"
sidebar_label: "Kruskal's MST"
tags: [algorithm, graph]
---

# Kruskal's MST

> Build minimum spanning tree by sorting edges and adding via union-find.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Graph |
| **Time** | O(E log E) |
| **Space** | O(V) |

## Key Techniques

- Sort edges
- Union-Find

## Notes & Interview Tips

MST when edge list is given.

## How It Works

Kruskal's algorithm finds the Minimum Spanning Tree by sorting all edges by weight and greedily adding the lightest edge that doesn't create a cycle (using Union-Find to check connectivity).

Time: O(E log E) for sorting + O(E α(V)) for Union-Find operations ≈ O(E log E). Kruskal's is preferred for sparse graphs (small E) and when edges are given as a list.

The MST property: a minimum spanning tree connects all vertices with the minimum total edge weight, using exactly V-1 edges.

## Implementation

```python
def kruskal(n, edges):
    edges.sort(key=lambda e: e[2])  # sort by weight
    uf = UnionFind(n)  # see Union-Find implementation
    mst = []
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            if len(mst) == n - 1: break
    return mst
```

## Key Insight

> Kruskal's = sort edges + Union-Find. The greedy choice (always add cheapest non-cycle edge) is provably optimal for MST.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/mst)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) | 🔴 Hard | - |
|  | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | 🟡 Medium | NC150 |
|  | [Maximize Spanning Tree Stability with Upgrades](https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/) | 🔴 Hard | - |
|  | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | 🟡 Medium | B75, NC150 |
|  | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | 🟡 Medium | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
- [cp-algorithms.com](https://cp-algorithms.com/graph/mst_kruskal.html)
