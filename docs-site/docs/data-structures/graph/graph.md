---
title: "Graph"
sidebar_label: "Graph"
tags: [data-structure, graph]
---

# Graph

> Set of vertices (nodes) and edges; can be directed/undirected, weighted/unweighted, cyclic/acyclic.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Graph |
| **Time** | Varies by algorithm |
| **Space** | Adj list O(V+E) · Adj matrix O(V^2) |

## Key Techniques

- BFS
- DFS
- Union-Find
- Topological sort
- Dijkstra
- Bellman-Ford

## Notes & Interview Tips

Sean Prashad: 'If given a graph → DFS, BFS, Union-Find.'

## How It Works

A graph consists of vertices (nodes) and edges connecting them. Graphs can be directed or undirected, weighted or unweighted, cyclic or acyclic. The two main representations are **adjacency list** (list of neighbors per vertex, space-efficient for sparse graphs) and **adjacency matrix** (2D array, fast edge lookup for dense graphs).

Most graph problems reduce to traversal (BFS/DFS), shortest path (Dijkstra/Bellman-Ford), or connectivity (Union-Find/DFS). The choice of representation matters: adjacency lists use O(V + E) space and are preferred for most problems; adjacency matrices use O(V²) but allow O(1) edge existence checks.

For interviews, always clarify: directed or undirected? weighted? can there be cycles? self-loops? disconnected components? These details determine the algorithm.

## Implementation

```python
from collections import defaultdict, deque

# Adjacency list representation
graph = defaultdict(list)
edges = [(0,1), (0,2), (1,3), (2,3)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # undirected

# DFS: detect cycle in undirected graph
def has_cycle(graph, n):
    visited = [False] * n
    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node): return True
            elif neighbor != parent:
                return True
        return False
    return any(dfs(i, -1) for i in range(n) if not visited[i])

# Count connected components
def count_components(graph, n):
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            queue = deque([i])
            visited[i] = True
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    return count
```

## Key Insight

> For sparse graphs (E &lt;&lt; V²), use adjacency lists. For dense graphs or when you need O(1) edge lookup, use an adjacency matrix. Most interview problems use adjacency lists.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/graphds)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Course Schedule](https://leetcode.com/problems/course-schedule/) | 🟡 Medium | G75, B75, NC150 |
|  | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 🟡 Medium | NC150 |
|  | [Clone Graph](https://leetcode.com/problems/clone-graph/) | 🟡 Medium | G75, B75, NC150 |
|  | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | 🟡 Medium | NC150 |
|  | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | 🟡 Medium | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Graph_(abstract_data_type))
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/graph/)
- [visualgo.net](https://visualgo.net/en/graphds)
