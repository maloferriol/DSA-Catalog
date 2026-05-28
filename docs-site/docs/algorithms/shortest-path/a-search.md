---
title: "A* Search"
sidebar_label: "A* Search"
tags: [algorithm, shortest-path]
---

# A* Search

> Best-first search using f(n) = g(n) + h(n); admissible heuristic yields optimal path.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Shortest path |
| **Time** | Depends on heuristic; O(E) at best |
| **Space** | O(V) |

## Key Techniques

- Heuristic search
- Priority queue

## Notes & Interview Tips

Pathfinding in games and AI.

## How It Works

A* is an informed search algorithm that finds the shortest path using a heuristic function h(n) that estimates the distance from node n to the goal. It explores nodes in order of f(n) = g(n) + h(n), where g(n) is the actual cost from start to n.

A* is optimal when h(n) is **admissible** (never overestimates) and **consistent** (h(n) ≤ cost(n,m) + h(m)). The most common heuristic for grids is Manhattan distance (4-directional) or Euclidean distance (any-direction). A* reduces to Dijkstra when h(n) = 0, and to greedy best-first search when g(n) = 0.

A* is used in game pathfinding, robotics, GPS navigation, and puzzle solving (15-puzzle, Rubik's cube). It's the standard algorithm for single-pair shortest path on grids.

## Implementation

```python
import heapq

def a_star(grid, start, goal):
    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])  # Manhattan distance

    heap = [(0 + heuristic(start, goal), 0, start)]
    g_cost = {start: 0}
    came_from = {}
    while heap:
        f, g, current = heapq.heappop(heap)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = current[0]+dr, current[1]+dc
            neighbor = (nr, nc)
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and not grid[nr][nc]:
                new_g = g + 1
                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    heapq.heappush(heap, (new_g + heuristic(neighbor, goal), new_g, neighbor))
                    came_from[neighbor] = current
    return []
```

## Key Insight

> A* = Dijkstra + heuristic guidance. The heuristic steers the search toward the goal, dramatically reducing explored nodes. Manhattan distance is the standard heuristic for grid pathfinding.

## Visualization

- [Interactive Visualization](https://www.redblobgames.com/pathfinding/a-star/introduction.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | 🟡 Medium | - |
|  | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | 🟡 Medium | NC150 |
|  | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | 🟡 Medium | NC150 |
|  | [Reachable Nodes In Subdivided Graph](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/) | 🔴 Hard | - |
|  | [Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [redblobgames.com](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
