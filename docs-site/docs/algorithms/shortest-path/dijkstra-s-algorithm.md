---
title: "Dijkstra's Algorithm"
sidebar_label: "Dijkstra's Algorithm"
tags: [algorithm, shortest-path]
---

# Dijkstra's Algorithm

> Single-source shortest paths in weighted graph with non-negative edges using a priority queue.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Shortest path |
| **Time** | O((V+E) log V) |
| **Space** | O(V) |

## Key Techniques

- Priority queue
- Greedy relaxation

## Notes & Interview Tips

Standard for weighted shortest paths when no negative edges.

## How It Works

Dijkstra's algorithm finds the shortest path from a source to all other vertices in a weighted graph with non-negative edge weights. It uses a priority queue (min-heap) to always process the vertex with the smallest known distance.

The algorithm: (1) set all distances to infinity except source (0), (2) push source into the min-heap, (3) extract the minimum, (4) for each neighbor, if the path through the current node is shorter, update the distance and push to the heap. Continue until the heap is empty.

Time: O((V + E) log V) with a binary heap. Cannot handle negative edge weights — use Bellman-Ford for that. For interviews, always use the lazy deletion approach (allow duplicates in the heap, skip outdated entries).

## Implementation

```python
import heapq
from collections import defaultdict

def dijkstra(graph, start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue  # skip outdated entry
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dict(dist)
```

## Key Insight

> The lazy deletion trick: allow duplicate entries in the heap and skip them when popped (`if d > dist[u]: continue`). This is simpler than decrease-key and works well in practice.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/sssp)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | 🟡 Medium | NC150 |
|  | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | 🟡 Medium | NC150 |
|  | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | 🟡 Medium | - |
|  | [Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | 🟡 Medium | - |
|  | [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [visualgo.net](https://visualgo.net/en/sssp)
