---
title: "Suffix Array / Suffix Tree"
sidebar_label: "Suffix Array / Suffix Tree"
tags: [data-structure, trees]
---

# Suffix Array / Suffix Tree

> Sorted array (or compressed tree) of all suffixes of a string; powers fast substring queries.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Trees |
| **Time** | Build O(n log n) · Query O(m + log n) |
| **Space** | O(n) |

## Key Techniques

- DC3 algorithm
- LCP array

## Notes & Interview Tips

Advanced; rare in standard interviews but common in competitive programming.

## How It Works

A suffix array is a sorted array of all suffixes of a string, represented by their starting indices. Combined with an LCP (Longest Common Prefix) array, it can solve virtually any substring problem efficiently.

A suffix tree is the compressed trie of all suffixes, built in O(n) with Ukkonen's algorithm. Suffix arrays use less memory (4-8 bytes vs 20+ bytes per character) and have largely replaced suffix trees in practice.

These are advanced structures used in bioinformatics, text compression (BWT), and competitive programming. For interviews, knowing when to use them matters more than implementation details.

## Implementation

```python
# Simple suffix array construction (O(n log^2 n))
def build_suffix_array(s):
    n = len(s)
    suffixes = sorted(range(n), key=lambda i: s[i:])
    return suffixes

# Longest repeated substring using suffix array + LCP
def longest_repeated_substring(s):
    sa = build_suffix_array(s)
    best = ""
    for i in range(1, len(sa)):
        # Compare adjacent suffixes in sorted order
        a, b = s[sa[i-1]:], s[sa[i]:]
        lcp = 0
        while lcp < len(a) and lcp < len(b) and a[lcp] == b[lcp]:
            lcp += 1
        if lcp > len(best):
            best = s[sa[i]:sa[i]+lcp]
    return best
```

## Key Insight

> The suffix array + LCP array together solve most substring problems. The longest repeated substring is just the maximum value in the LCP array.

## Visualization

- [Interactive Visualization](https://visualgo.net/en/suffixarray)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) | 🔴 Hard | - |
|  | [Longest Common Subpath](https://leetcode.com/problems/longest-common-subpath/) | 🔴 Hard | - |
|  | [Number of Ways to Separate Numbers](https://leetcode.com/problems/number-of-ways-to-separate-numbers/) | 🔴 Hard | - |
|  | [Sum of Scores of Built Strings](https://leetcode.com/problems/sum-of-scores-of-built-strings/) | 🔴 Hard | - |
|  | [Construct String with Minimum Cost](https://leetcode.com/problems/construct-string-with-minimum-cost/) | 🔴 Hard | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Suffix_array)
- [cp-algorithms.com](https://cp-algorithms.com/string/suffix-array.html)
