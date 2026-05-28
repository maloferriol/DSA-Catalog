---
title: "Kosaraju's SCC"
sidebar_label: "Kosaraju's SCC"
tags: [algorithm, graph]
---

# Kosaraju's SCC

> Find SCCs with two DFS passes: original graph then reversed graph.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Graph |
| **Time** | O(V+E) |
| **Space** | O(V) |

## Key Techniques

- DFS
- Reverse graph

## Notes & Interview Tips

Simpler than Tarjan to implement.

## How It Works

Kosaraju's algorithm finds SCCs using two DFS passes: (1) DFS on the original graph, recording finish order, (2) DFS on the reversed graph in reverse finish order. Each DFS tree in the second pass is an SCC.

The intuition: the first DFS orders vertices so that SCC roots come after their SCC members. Reversing the graph makes cross-SCC edges point backward. Processing in reverse finish order ensures the second DFS can't escape an SCC.

Kosaraju's is conceptually simpler than Tarjan's but requires two passes and storing the reversed graph. Both run in O(V + E).

## Implementation

```python
def kosaraju_scc(graph, n):
    # Pass 1: DFS on original graph, record finish order
    visited = [False] * n
    order = []
    def dfs1(v):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]: dfs1(u)
        order.append(v)
    for i in range(n):
        if not visited[i]: dfs1(i)

    # Build reversed graph
    rev = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            rev[v].append(u)

    # Pass 2: DFS on reversed graph in reverse finish order
    visited = [False] * n
    sccs = []
    def dfs2(v, component):
        visited[v] = True
        component.append(v)
        for u in rev[v]:
            if not visited[u]: dfs2(u, component)
    for v in reversed(order):
        if not visited[v]:
            comp = []
            dfs2(v, comp)
            sccs.append(comp)
    return sccs
```

## Key Insight

> Two DFS passes: forward to get finish order, backward (on reversed graph) to extract SCCs. The reversed graph ensures DFS in the second pass can't cross SCC boundaries.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/dfsbfs)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Clone Graph](https://leetcode.com/problems/clone-graph/) | 🟡 Medium | G75, B75, NC150 |
|  | [Course Schedule](https://leetcode.com/problems/course-schedule/) | 🟡 Medium | G75, B75, NC150 |
|  | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 🟡 Medium | NC150 |
|  | [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) | 🟡 Medium | G75 |
|  | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | 🔴 Hard | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm)
- [cp-algorithms.com](https://cp-algorithms.com/graph/strongly-connected-components.html)
