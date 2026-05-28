---
title: "Hash Table / Hash Map"
sidebar_label: "Hash Table / Hash Map"
tags: [data-structure, hash-based]
---

# Hash Table / Hash Map

> Key→value store using a hash function to map keys to buckets for ~O(1) lookup.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Hash-based |
| **Time** | Insert/Lookup/Delete avg O(1), worst O(n) |
| **Space** | O(n) |

## Key Techniques

- Separate chaining
- Open addressing
- Rolling hash
- Counting
- Memoization

## Notes & Interview Tips

Sean Prashad: 'If need O(1) lookup → Hash table, Hash set.' Most common DS in interviews.

## How It Works

A hash table maps keys to values using a hash function that converts keys into array indices. On average, insertion, deletion, and lookup are all O(1). The hash function computes an index, and if two keys hash to the same index (a collision), the table resolves it — typically via **chaining** (linked list at each bucket) or **open addressing** (probing for the next empty slot).

The load factor (n/capacity) determines performance. When it exceeds a threshold (typically 0.75), the table resizes (usually doubling) and rehashes all entries. This keeps the average chain length short. Python's `dict` uses open addressing with a sophisticated probing scheme; Java's `HashMap` uses chaining with tree-ification for long chains.

For interviews, hash maps are your Swiss Army knife. They convert O(n) lookups into O(1) lookups. The classic pattern: "have I seen this before?" — store elements as you iterate, check existence in O(1). This underlies Two Sum, group anagrams, subarray sum equals K, and dozens more.

## Implementation

```python
# Two Sum: O(n) using hash map
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Group Anagrams: sort each word as the key
from collections import defaultdict
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return list(groups.values())
```

## Key Insight

> When a problem requires checking existence or counting frequencies, a hash map almost always gives you the O(n) solution. The pattern: iterate once, store in map, check in map.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/hashtable)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | G75, B75, NC150 |
|  | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | 🟢 Easy | G75, B75, NC150 |
|  | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | 🟡 Medium | B75, NC150 |
|  | [LRU Cache](https://leetcode.com/problems/lru-cache/) | 🟡 Medium | G75, NC150 |
|  | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟡 Medium | G75, B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/hash-table/)
