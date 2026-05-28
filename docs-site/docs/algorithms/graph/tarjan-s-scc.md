---
title: "Tarjan's SCC"
sidebar_label: "Tarjan's SCC"
tags: [algorithm, graph]
---

# Tarjan's SCC

> Find strongly connected components in a directed graph in O(V+E) using DFS lowlinks.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Graph |
| **Time** | O(V+E) |
| **Space** | O(V) |

## Key Techniques

- DFS lowlink
- Stack

## Notes & Interview Tips

Advanced; useful for 2-SAT and dependency analysis.

## How It Works

Tarjan's algorithm finds all Strongly Connected Components (SCCs) in a directed graph using a single DFS pass. An SCC is a maximal set of vertices where every vertex is reachable from every other.

It tracks discovery time and the lowest reachable discovery time (lowlink) for each node. Nodes on the DFS stack form potential SCCs. When a node's lowlink equals its discovery time, it's the root of an SCC — pop all nodes from the stack up to this root.

Applications: simplifying directed graphs (contract SCCs into single nodes), 2-SAT solver, finding bridges and articulation points (modified version).

## Implementation

```python
def tarjan_scc(graph, n):
    idx = [0]
    stack, on_stack = [], [False] * n
    index = [-1] * n
    lowlink = [0] * n
    sccs = []

    def strongconnect(v):
        index[v] = lowlink[v] = idx[0]
        idx[0] += 1
        stack.append(v)
        on_stack[v] = True
        for w in graph[v]:
            if index[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], index[w])
        if lowlink[v] == index[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v: break
            sccs.append(scc)

    for v in range(n):
        if index[v] == -1:
            strongconnect(v)
    return sccs
```

## Key Insight

> When lowlink[v] == index[v], v is the 'root' of an SCC. Everything on the stack above v (including v) forms the SCC. The single-pass DFS makes this efficient.

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

- [Wikipedia](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm)
- [cp-algorithms.com](https://cp-algorithms.com/graph/strongly-connected-components.html)
