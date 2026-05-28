---
title: "Bloom Filter"
sidebar_label: "Bloom Filter"
tags: [data-structure, hash-based]
---

# Bloom Filter

> Probabilistic set with no false negatives and tunable false positives, using k hash functions.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Hash-based |
| **Time** | Insert/Lookup O(k) |
| **Space** | O(m) bits |

## Key Techniques

- Multiple hash functions
- Bit array

## Notes & Interview Tips

System design favourite — caches, DB membership checks.

## How It Works

A Bloom filter is a space-efficient probabilistic data structure that tests whether an element is a member of a set. It can have **false positives** (says "maybe in set" when it's not) but **never false negatives** (if it says "definitely not in set," it's correct). This trade-off makes it ideal for pre-filtering expensive lookups.

It works using k hash functions and a bit array of m bits. To insert: hash the element k times, set those k bit positions to 1. To query: hash the element k times, check if all k positions are 1. If any is 0, the element is definitely not in the set. If all are 1, it's probably in the set (but other elements might have set those bits).

Real-world uses: databases (check if a key exists before disk lookup), web crawlers (avoid revisiting URLs), CDNs (cache membership), and spell checkers. The false positive rate depends on m/n (bits per element) and k (number of hash functions). With 10 bits per element and 7 hash functions, the false positive rate is about 1%.

## Implementation

```python
import hashlib

class BloomFilter:
    def __init__(self, size=1000, num_hashes=3):
        self.size = size
        self.num_hashes = num_hashes
        self.bits = [False] * size

    def _hashes(self, item):
        for i in range(self.num_hashes):
            h = hashlib.md5(f"{item}{i}".encode()).hexdigest()
            yield int(h, 16) % self.size

    def add(self, item):
        for pos in self._hashes(item):
            self.bits[pos] = True

    def might_contain(self, item):
        return all(self.bits[pos] for pos in self._hashes(item))
```

## Key Insight

> Bloom filters trade accuracy for extreme space efficiency. A hash set storing 1M URLs might use 50MB; a Bloom filter with 1% false positive rate uses only 1.2MB.

## Visualization

- [Interactive Visualization](https://www.jasondavies.com/bloomfilter/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [LRU Cache](https://leetcode.com/problems/lru-cache/) | 🟡 Medium | G75, NC150 |
|  | [Min Stack](https://leetcode.com/problems/min-stack/) | 🟡 Medium | G75, NC150 |
|  | [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | 🟡 Medium | - |
|  | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | 🟡 Medium | G75, B75, NC150 |
|  | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | 🟡 Medium | B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Bloom_filter)
- [systemdesign.io](https://systemdesign.io/bloom-filters/)
