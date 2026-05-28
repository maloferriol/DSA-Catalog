---
title: "Flood Fill"
sidebar_label: "Flood Fill"
tags: [algorithm, pattern]
---

# Flood Fill

> Fill connected region in a grid by recursively visiting neighbours of same value.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Pattern |
| **Time** | O(rows·cols) |
| **Space** | O(rows·cols) |

## Key Techniques

- BFS or DFS on grid

## Notes & Interview Tips

Number of islands, surrounded regions.

## How It Works

Flood fill colors all connected cells of the same value starting from a given cell. It's a BFS/DFS on a grid, commonly used in paint programs (bucket fill), image processing, and game maps (region detection).

The algorithm: from the starting cell, recursively (or iteratively) visit all 4-connected neighbors that have the same original color and change them to the new color. Mark cells as visited by changing their color.

## Implementation

```python
def flood_fill(image, sr, sc, new_color):
    original = image[sr][sc]
    if original == new_color: return image
    rows, cols = len(image), len(image[0])
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols: return
        if image[r][c] != original: return
        image[r][c] = new_color
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            dfs(r+dr, c+dc)
    dfs(sr, sc)
    return image
```

## Key Insight

> Flood fill is just DFS/BFS on a grid with color-matching as the visited condition. Change the color in-place to mark cells as visited (no extra visited set needed).

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Flood Fill](https://leetcode.com/problems/flood-fill/) | 🟢 Easy | G75 |
|  | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟡 Medium | G75, B75, NC150 |
|  | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | 🟡 Medium | NC150 |
|  | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | 🟡 Medium | B75, NC150 |
|  | [Word Search](https://leetcode.com/problems/word-search/) | 🟡 Medium | G75, B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Flood_fill)
- [leetcode.com](https://leetcode.com/problems/flood-fill/)
