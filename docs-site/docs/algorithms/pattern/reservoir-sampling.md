---
title: "Reservoir Sampling"
sidebar_label: "Reservoir Sampling"
tags: [algorithm, pattern]
---

# Reservoir Sampling

> Sample k items uniformly from a stream of unknown length.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Pattern |
| **Time** | O(n) |
| **Space** | O(k) |

## Key Techniques

- Random replacement

## Notes & Interview Tips

Sean Prashad: 'If given a stream of data → Heap, Design.'

## How It Works

Reservoir sampling selects k random items from a stream of unknown length n, giving each item an equal 1/n probability. The algorithm: keep the first k items, then for each subsequent item i, replace a random item in the reservoir with probability k/i.

This is essential when you can't store all items (streaming data) or don't know the total count in advance. Single-element version (k=1): keep item i with probability 1/i.

Applications: random sampling from databases, streaming analytics, and randomized algorithms.

## Implementation

```python
import random

def reservoir_sample(stream, k):
    reservoir = []
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item
    return reservoir
```

## Key Insight

> Each item has probability k/n of being in the final sample, even though n is unknown during processing. The proof uses induction on the stream length.

## Visualization

- [Interactive Visualization](https://en.wikipedia.org/wiki/Reservoir_sampling)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/) | 🟡 Medium | - |
|  | [Random Pick Index](https://leetcode.com/problems/random-pick-index/) | 🟡 Medium | - |
|  | [Random Point in Non-overlapping Rectangles](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/) | 🟡 Medium | - |
|  | [Random Flip Matrix](https://leetcode.com/problems/random-flip-matrix/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Reservoir_sampling)
- [en.wikipedia.org](https://en.wikipedia.org/wiki/Reservoir_sampling)
