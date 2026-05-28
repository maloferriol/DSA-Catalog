---
title: "Breadth-First Search (BFS)"
sidebar_label: "Breadth-First Search (BFS)"
tags: [algorithm, graph-traversal]
---

# Breadth-First Search (BFS)

> Level-by-level graph traversal using a queue; finds shortest path in unweighted graphs.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Graph traversal |
| **Time** | O(V+E) |
| **Space** | O(V) |

## Key Techniques

- Queue
- Visited set
- Level tracking

## Notes & Interview Tips

Shortest path in unweighted graph; level-order on trees.

## How It Works

BFS explores a graph level by level using a queue. Starting from a source node, it visits all neighbors first, then all neighbors' neighbors, and so on. This guarantees the shortest path in unweighted graphs.

The template: initialize a queue with the start node, mark it visited, then repeatedly dequeue, process, and enqueue unvisited neighbors. For level-by-level processing, use the "queue size" trick: at the start of each iteration, note the queue size and process exactly that many nodes.

BFS applications: shortest path in unweighted graphs, level-order tree traversal, minimum steps/moves problems, connected components, and bi-directional search (BFS from both ends to meet in the middle).

## Implementation

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# Shortest path (unweighted)
def bfs_shortest(graph, start, end):
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        if node == end: return dist
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, dist + 1))
    return -1
```

## Key Insight

> BFS guarantees shortest path in unweighted graphs because it explores nodes in order of increasing distance. Always mark nodes as visited WHEN ENQUEUING (not when dequeuing) to avoid duplicates.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/dfsbfs)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | 🟡 Medium | G75, B75, NC150 |
|  | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟡 Medium | G75, B75, NC150 |
|  | [Word Ladder](https://leetcode.com/problems/word-ladder/) | 🔴 Hard | G75, NC150 |
|  | [Open the Lock](https://leetcode.com/problems/open-the-lock/) | 🟡 Medium | - |
|  | [Same Tree](https://leetcode.com/problems/same-tree/) | 🟢 Easy | B75, NC150 |
|  | [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
- [visualgo.net](https://visualgo.net/en/dfsbfs)
