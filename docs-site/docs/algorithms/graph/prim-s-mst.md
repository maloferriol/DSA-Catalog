---
title: "Prim's MST"
sidebar_label: "Prim's MST"
tags: [algorithm, graph]
---

# Prim's MST

> Grow MST by repeatedly adding the cheapest edge to the growing component.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Graph |
| **Time** | O((V+E) log V) |
| **Space** | O(V) |

## Key Techniques

- Priority queue
- Visited set

## Notes & Interview Tips

MST when adjacency-list is given.

## How It Works

Prim's algorithm grows the MST from a starting vertex by repeatedly adding the cheapest edge connecting the tree to a non-tree vertex. It uses a min-heap to efficiently find the minimum-weight crossing edge.

Time: O((V + E) log V) with a binary heap. Prim's is preferred for dense graphs (large E) and when the graph is given as an adjacency list. It's conceptually similar to Dijkstra.

Both Kruskal's and Prim's find the same MST (or one of multiple MSTs if edge weights aren't unique). Choose Kruskal's for sparse graphs, Prim's for dense graphs.

## Implementation

```python
import heapq
from collections import defaultdict

def prim(graph, n):
    visited = [False] * n
    heap = [(0, 0)]  # (weight, node)
    total_weight = 0
    edges_added = 0
    while heap and edges_added < n:
        w, u = heapq.heappop(heap)
        if visited[u]: continue
        visited[u] = True
        total_weight += w
        edges_added += 1
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(heap, (weight, v))
    return total_weight
```

## Key Insight

> Prim's grows the MST one vertex at a time (like Dijkstra grows shortest path tree). The min-heap always contains the cheapest edge to each non-tree vertex.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/mst)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) | 🔴 Hard | - |
|  | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | 🟡 Medium | NC150 |
|  | [Maximize Spanning Tree Stability with Upgrades](https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/) | 🔴 Hard | - |
|  | [Clone Graph](https://leetcode.com/problems/clone-graph/) | 🟡 Medium | G75, B75, NC150 |
|  | [Course Schedule](https://leetcode.com/problems/course-schedule/) | 🟡 Medium | G75, B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Prim%27s_algorithm)
- [cp-algorithms.com](https://cp-algorithms.com/graph/mst_prim.html)
