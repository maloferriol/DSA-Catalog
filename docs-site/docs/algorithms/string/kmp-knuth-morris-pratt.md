---
title: "KMP (Knuth-Morris-Pratt)"
sidebar_label: "KMP (Knuth-Morris-Pratt)"
tags: [algorithm, string]
---

# KMP (Knuth-Morris-Pratt)

> Linear-time substring search using a failure function (LPS array).

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | String |
| **Time** | O(n+m) |
| **Space** | O(m) |

## Key Techniques

- LPS prefix function

## Notes & Interview Tips

Substring search and longest proper prefix/suffix problems.

## How It Works

KMP finds all occurrences of a pattern in a text in O(n + m) time by preprocessing the pattern into a failure function (partial match table). The failure function `lps[i]` stores the length of the longest proper prefix of pattern[0..i] that is also a suffix.

When a mismatch occurs at position j in the pattern, instead of restarting from the beginning, KMP jumps to `lps[j-1]` — the next position where a match could continue. This avoids re-examining characters in the text.

KMP is the standard string matching algorithm with guaranteed linear time. For practical use, Python's `str.find()` or `in` operator are simpler. KMP matters for interviews and when you need the failure function for other problems.

## Implementation

```python
def kmp_search(text, pattern):
    def build_lps(p):
        lps = [0] * len(p)
        length = 0
        i = 1
        while i < len(p):
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                i += 1
        return lps

    lps = build_lps(pattern)
    matches = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1; j += 1
            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1]
        elif j:
            j = lps[j - 1]
        else:
            i += 1
    return matches
```

## Key Insight

> The LPS (Longest Prefix Suffix) array lets KMP skip ahead on mismatch instead of restarting. Building the LPS array uses the same logic as the search itself.

## Visualization

- [Interactive Visualization](https://www.cs.usfca.edu/~galles/visualization/KMP.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | 🟢 Easy | - |
|  | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | 🟢 Easy | - |
|  | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | 🔴 Hard | - |
|  | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | 🟢 Easy | B75, NC150 |
|  | [Repeated String Match](https://leetcode.com/problems/repeated-string-match/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)
- [cp-algorithms.com](https://cp-algorithms.com/string/prefix-function.html)
