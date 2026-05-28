---
title: "Matrix (Grid)"
sidebar_label: "Matrix (Grid)"
tags: [data-structure, graph]
---

# Matrix (Grid)

> 2D array often treated as an implicit graph; cells = nodes, adjacency = neighbours.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Graph |
| **Time** | Traversal O(rows·cols) |
| **Space** | O(rows·cols) |

## Key Techniques

- BFS
- DFS
- DP on grid
- Flood fill

## Notes & Interview Tips

Sean Prashad: 'If given a matrix → BFS, DFS, Dynamic programming.'

## How It Works

A matrix or grid is a 2D array commonly used to represent maps, game boards, and images. Grid problems are essentially graph problems where each cell is a node connected to its 4 (or 8) neighbors.

The most common pattern is **BFS/DFS on a grid**: iterate through cells, when you find a starting condition (like '1' in Number of Islands), explore all connected cells using BFS or DFS. Use a visited set or modify the grid in-place to mark visited cells.

Direction arrays (`dx = [-1,0,1,0], dy = [0,1,0,-1]`) are the standard way to iterate over 4 neighbors. Always check bounds before accessing a neighbor.

## Implementation

```python
from collections import deque

# Number of Islands (BFS)
def num_islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                queue = deque([(r, c)])
                grid[r][c] = '0'  # mark visited
                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr, nc = cr+dr, cc+dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'
                            queue.append((nr, nc))
    return count

# Shortest path in binary matrix (BFS)
def shortest_path(grid):
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]: return -1
    queue = deque([(0, 0, 1)])
    grid[0][0] = 1
    for r, c, dist in queue:
        if r == n-1 and c == n-1: return dist
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and not grid[nr][nc]:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, dist + 1))
    return -1
```

## Key Insight

> Grid problems are graph problems in disguise. The standard template: iterate cells, BFS/DFS from each starting point, mark visited. Direction arrays `[(-1,0),(1,0),(0,-1),(0,1)]` iterate 4-connected neighbors.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/dfsbfs)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟡 Medium | G75, B75, NC150 |
|  | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | 🟡 Medium | G75, NC150 |
|  | [Word Search](https://leetcode.com/problems/word-search/) | 🟡 Medium | G75, B75, NC150 |
|  | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | 🟡 Medium | B75, NC150 |
|  | [Rotate Image](https://leetcode.com/problems/rotate-image/) | 🟡 Medium | B75, NC150 |
|  | [Convert 1D Array Into 2D Array](https://leetcode.com/problems/convert-1d-array-into-2d-array/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Matrix_(mathematics))
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/matrix/)
