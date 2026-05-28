---
title: "Floyd-Warshall"
sidebar_label: "Floyd-Warshall"
tags: [algorithm, shortest-path]
---

# Floyd-Warshall

> All-pairs shortest paths via DP over intermediate vertices.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Shortest path |
| **Time** | O(V^3) |
| **Space** | O(V^2) |

## Key Techniques

- DP triple loop

## Notes & Interview Tips

Good when V is small (≤500) and you need all pairs.

## How It Works

Floyd-Warshall finds shortest paths between ALL pairs of vertices in O(V³) time and O(V²) space. It uses dynamic programming: for each intermediate vertex k, check if the path i→k→j is shorter than the current path i→j.

The triple nested loop processes intermediate vertices in the outer loop. The DP relation: `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`. This handles negative weights but not negative cycles.

Use Floyd-Warshall when you need all-pairs shortest paths and V is small (up to ~500). For single-source shortest paths, Dijkstra or Bellman-Ford is faster.

## Implementation

```python
def floyd_warshall(n, edges):
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n): dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
```

## Key Insight

> The order of the triple loop matters: k (intermediate vertex) MUST be the outer loop. Think of it as 'adding vertex k as a possible waypoint for all pairs'.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/sssp)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | 🟡 Medium | - |
|  | [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | 🟡 Medium | - |
|  | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | 🟡 Medium | NC150 |
|  | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | 🟡 Medium | NC150 |
|  | [Reachable Nodes In Subdivided Graph](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/) | 🔴 Hard | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
- [cp-algorithms.com](https://cp-algorithms.com/graph/all-pair-shortest-path-floyd-warshall.html)
