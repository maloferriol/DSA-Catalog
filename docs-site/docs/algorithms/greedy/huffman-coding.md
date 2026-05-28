---
title: "Huffman Coding"
sidebar_label: "Huffman Coding"
tags: [algorithm, greedy]
---

# Huffman Coding

> Build optimal prefix code by repeatedly merging two least-frequent symbols.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Greedy |
| **Time** | O(n log n) |
| **Space** | O(n) |

## Key Techniques

- Min-heap

## Notes & Interview Tips

Compression classic.

## How It Works

Huffman coding creates an optimal prefix-free binary code where frequent characters get shorter codes. It uses a greedy algorithm: repeatedly merge the two least-frequent nodes into a new node until one tree remains.

The algorithm: (1) create a leaf for each character with its frequency, (2) build a min-heap, (3) extract the two minimum nodes, create a new internal node with their sum as frequency, (4) insert the new node, (5) repeat until one node remains. Left edges = 0, right edges = 1.

Huffman coding is used in JPEG, MP3, gzip/deflate, and is the foundation of data compression. The prefix-free property (no code is a prefix of another) ensures unique decodability.

## Implementation

```python
import heapq

def huffman_coding(freq):
    heap = [(f, i, c) for c, f in freq.items() for i in [0]]
    heapq.heapify(heap)
    codes = {c: '' for c in freq}
    if len(heap) == 1:
        codes[heap[0][2]] = '0'
        return codes
    counter = len(freq)
    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        heapq.heappush(heap, (f1 + f2, counter, (left, right)))
        counter += 1
    def assign(node, code):
        if isinstance(node, str):
            codes[node] = code
            return
        left, right = node
        assign(left, code + '0')
        assign(right, code + '1')
    assign(heap[0][2], '')
    return codes
```

## Key Insight

> The greedy choice of always merging the two least-frequent nodes produces optimal prefix-free codes. More frequent characters naturally end up with shorter paths (codes) in the tree.

## Visualization

- [Interactive Visualization](https://www.cs.usfca.edu/~galles/visualization/Huffman.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) | 🟡 Medium | - |
|  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium | G75, B75, NC150 |
|  | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) | 🔴 Hard | - |
|  | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | 🟡 Medium | NC150 |
|  | [Jump Game](https://leetcode.com/problems/jump-game/) | 🟡 Medium | B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/)
