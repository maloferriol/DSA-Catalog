---
title: "Bellman-Ford"
sidebar_label: "Bellman-Ford"
tags: [algorithm, shortest-path]
---

# Bellman-Ford

> Single-source shortest paths allowing negative weights; detects negative cycles.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Shortest path |
| **Time** | O(V·E) |
| **Space** | O(V) |

## Key Techniques

- Edge relaxation V-1 times

## Notes & Interview Tips

Use when negative weights are possible.

## How It Works

Bellman-Ford finds shortest paths from a single source, even with negative edge weights. It relaxes all edges V-1 times. If any distance can still be reduced after V-1 iterations, there's a negative cycle.

Time: O(V × E). Slower than Dijkstra but handles negative weights. The SPFA (Shortest Path Faster Algorithm) optimization uses a queue to only re-process vertices whose distances changed, but worst case is still O(V × E).

Use Bellman-Ford when: (1) edges can have negative weights, (2) you need to detect negative cycles, (3) the graph is given as an edge list (not adjacency list).

## Implementation

```python
def bellman_ford(n, edges, src):
    dist = [float('inf')] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None  # negative cycle
    return dist
```

## Key Insight

> After V-1 relaxations, all shortest paths are found (shortest path has at most V-1 edges). A Vth relaxation that still reduces a distance proves a negative cycle exists.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/sssp)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | 🟡 Medium | NC150 |
|  | [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | 🟡 Medium | - |
|  | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | 🟡 Medium | NC150 |
|  | [Reachable Nodes In Subdivided Graph](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/) | 🔴 Hard | - |
|  | [Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
- [cp-algorithms.com](https://cp-algorithms.com/graph/bellman_ford.html)
