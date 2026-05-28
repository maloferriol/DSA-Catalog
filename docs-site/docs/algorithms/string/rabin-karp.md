---
title: "Rabin-Karp"
sidebar_label: "Rabin-Karp"
tags: [algorithm, string]
---

# Rabin-Karp

> Substring search using rolling hash; great for multiple patterns.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | String |
| **Time** | Avg O(n+m), worst O(n·m) |
| **Space** | O(1) |

## Key Techniques

- Rolling hash
- Modular arithmetic

## Notes & Interview Tips

Use double hashing to avoid collisions.

## How It Works

Rabin-Karp uses rolling hash to find pattern matches in O(n + m) expected time. It computes a hash of the pattern and slides a window over the text, updating the hash in O(1) using the rolling hash formula.

The rolling hash: `hash = (hash - text[i] * base^(m-1)) * base + text[i+m]`. When hashes match, verify with actual string comparison to handle collisions. Using a large prime modulus reduces collision probability.

Rabin-Karp's advantage over KMP: it easily extends to multi-pattern matching (compute hashes for all patterns, check against text hash) and 2D pattern matching. Its disadvantage: O(n × m) worst case due to hash collisions.

## Implementation

```python
def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n: return []
    BASE, MOD = 256, 10**9 + 7
    p_hash = t_hash = 0
    h = pow(BASE, m - 1, MOD)
    for i in range(m):
        p_hash = (p_hash * BASE + ord(pattern[i])) % MOD
        t_hash = (t_hash * BASE + ord(text[i])) % MOD
    matches = []
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i+m] == pattern:
            matches.append(i)
        if i < n - m:
            t_hash = ((t_hash - ord(text[i]) * h) * BASE + ord(text[i+m])) % MOD
    return matches
```

## Key Insight

> Rolling hash updates the window hash in O(1) by removing the leftmost character's contribution and adding the new character. This makes substring comparison O(1) on average.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | 🟢 Easy | - |
|  | [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) | 🟡 Medium | - |
|  | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | 🔴 Hard | - |
|  | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | 🟢 Easy | - |
|  | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | 🟢 Easy | B75, NC150 |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm)
- [cp-algorithms.com](https://cp-algorithms.com/string/rabin-karp.html)
