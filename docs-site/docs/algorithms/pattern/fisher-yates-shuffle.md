---
title: "Fisher-Yates Shuffle"
sidebar_label: "Fisher-Yates Shuffle"
tags: [algorithm, pattern]
---

# Fisher-Yates Shuffle

> Uniformly random in-place shuffle in O(n).

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | Pattern |
| **Time** | O(n) |
| **Space** | O(1) |

## Key Techniques

- Swap with random index

## Notes & Interview Tips

Used in randomized quicksort and 'shuffle an array' problem.

## How It Works

Fisher-Yates (Knuth shuffle) produces a uniformly random permutation of an array in O(n) time. For each position i from n-1 down to 1, swap arr[i] with a randomly chosen element from arr[0..i].

This is the correct way to shuffle an array. A common mistake is the naive shuffle (for each position, swap with any random position), which produces a biased distribution — some permutations are more likely than others.

Used in card games, randomized algorithms, A/B testing, and any application requiring unbiased random ordering.

## Implementation

```python
import random

def shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
```

## Key Insight

> Swap with a random element from the REMAINING (unshuffled) portion, not the entire array. This produces exactly n! equally likely permutations. The naive 'swap with any position' produces n^n outcomes, which doesn't divide evenly into n! permutations.

## Visualization

- [Interactive Visualization](https://bost.ocks.org/mike/shuffle/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/) | 🟡 Medium | - |
|  | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | G75, B75, NC150 |
|  | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard | NC150 |
|  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium | G75, B75, NC150 |
|  | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)
- [en.wikipedia.org](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)
