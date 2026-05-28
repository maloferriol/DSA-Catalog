---
title: "Queue"
sidebar_label: "Queue"
tags: [data-structure, linear]
---

# Queue

> FIFO container; enqueue at the rear, dequeue at the front in O(1).

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Linear |
| **Time** | Enqueue/Dequeue O(1) |
| **Space** | O(n) |

## Key Techniques

- BFS scheduling
- Producer-consumer
- Level-order traversal

## Notes & Interview Tips

Used everywhere in BFS.

## How It Works

A queue is a First-In-First-Out (FIFO) collection with `enqueue` (add to back) and `dequeue` (remove from front), both O(1). Think of a line at a store — first come, first served.

Queues are the backbone of **BFS** (breadth-first search), which explores nodes level by level. They're also used in scheduling (task queues, message queues), buffering (I/O buffers, print spooling), and rate limiting. In Python, use `collections.deque` for an efficient queue — `list` has O(n) `pop(0)`.

A common interview pattern is **BFS with level tracking**: use the queue size at the start of each iteration to process exactly one level. This is used for level-order traversal, shortest path in unweighted graphs, and rotting oranges-style problems.

## Implementation

```python
from collections import deque

# BFS level-order traversal of a binary tree
def level_order(root):
    if not root: return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):  # process one level
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result

# BFS shortest path in unweighted graph
def shortest_path(graph, start, end):
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        if node == end: return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1
```

## Key Insight

> BFS = queue. DFS = stack (or recursion). When a problem asks for the shortest path in an unweighted graph or minimum steps, BFS with a queue is almost always the answer.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/list)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | 🟢 Easy | G75 |
|  | [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) | 🟢 Easy | - |
|  | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | 🟡 Medium | - |
|  | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | 🟢 Easy | - |
|  | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | 🔴 Hard | NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/queue/)
