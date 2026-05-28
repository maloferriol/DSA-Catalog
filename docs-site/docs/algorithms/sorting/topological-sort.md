---
title: "Topological Sort"
sidebar_label: "Topological Sort"
tags: [algorithm, sorting]
---

# Topological Sort

> Linear ordering of a DAG's vertices such that for every edge u→v, u precedes v.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Sorting |
| **Time** | O(V+E) |
| **Space** | O(V) |

## Key Techniques

- Kahn's (BFS, in-degree)
- DFS post-order

## Notes & Interview Tips

Sean Prashad: 'If asked for ordering/scheduling → Topological sort.'

## How It Works

Topological sort orders vertices of a directed acyclic graph (DAG) such that for every edge u → v, u comes before v. It's used for dependency resolution: build systems (make), task scheduling, course prerequisites, and package managers.

Two approaches: (1) **Kahn's algorithm** (BFS): start with nodes having no incoming edges (indegree 0), process them, reduce indegree of neighbors, add new zero-indegree nodes to the queue. (2) **DFS-based**: run DFS, add nodes to result in reverse post-order (when all descendants are visited, add the node).

If the graph has a cycle, topological sort is impossible. Kahn's algorithm detects cycles naturally: if the result has fewer nodes than the graph, there's a cycle. This makes it useful for cycle detection in directed graphs.

## Implementation

```python
from collections import deque, defaultdict

# Kahn's algorithm (BFS-based)
def topological_sort(num_nodes, edges):
    graph = defaultdict(list)
    indegree = [0] * num_nodes
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    queue = deque(i for i in range(num_nodes) if indegree[i] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == num_nodes else []  # empty = cycle
```

## Key Insight

> Kahn's algorithm processes nodes in dependency order: start with nodes that have no prerequisites (indegree 0). If the result is shorter than the number of nodes, there's a cycle.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/dfsbfs)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Course Schedule](https://leetcode.com/problems/course-schedule/) | 🟡 Medium | G75, B75, NC150 |
|  | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 🟡 Medium | NC150 |
|  | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | 🔴 Hard | B75, NC150 |
|  | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | 🔴 Hard | NC150 |
|  | [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) | 🟡 Medium | G75 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting)
- [cp-algorithms.com](https://cp-algorithms.com/graph/topological-sort.html)
