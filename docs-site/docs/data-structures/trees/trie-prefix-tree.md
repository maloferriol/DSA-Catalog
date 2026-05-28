---
title: "Trie (Prefix Tree)"
sidebar_label: "Trie (Prefix Tree)"
tags: [data-structure, trees]
---

# Trie (Prefix Tree)

> Tree where each path from root encodes a string; O(L) insert/lookup for length-L key.

## Quick Facts

| | |
|---|---|
| **Kind** | Data Structure |
| **Category** | Trees |
| **Time** | Insert/Search O(L) |
| **Space** | O(N·L·alphabet) |

## Key Techniques

- Prefix matching
- Autocomplete
- Word search backtracking

## Notes & Interview Tips

Sean Prashad: 'If asked for common strings → Map, Trie.'

## How It Works

A trie stores strings character by character, with each node representing a single character and paths from root representing stored strings. Lookup, insertion, and deletion are all O(L) where L is the string length, independent of how many strings are stored.

Tries excel at **prefix-based operations**: autocomplete, spell checking, IP routing (longest prefix match), and word games. The TrieNode typically contains a children map/array and an `is_end` flag marking complete words.

For interviews, the most important problems are: **Word Search II** (build trie from word list, DFS on board with trie pruning), **Design Autocomplete** (trie + DFS from prefix node), and **Implement Trie** (insert, search, startsWith).

## Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._find(prefix) is not None

    def _find(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
```

## Key Insight

> A trie trades space for time: it uses more memory than a hash set of strings but enables prefix queries that hash-based structures cannot do efficiently.

## Visualization

- [Interactive Visualization](https://www.cs.usfca.edu/~galles/visualization/Trie.html)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | 🟡 Medium | G75, B75, NC150 |
|  | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | 🟡 Medium | B75, NC150 |
|  | [Word Search II](https://leetcode.com/problems/word-search-ii/) | 🔴 Hard | B75, NC150 |
|  | [Replace Words](https://leetcode.com/problems/replace-words/) | 🟡 Medium | - |
|  | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | 🟢 Easy | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Trie)
- [techinterviewhandbook.org](https://www.techinterviewhandbook.org/algorithms/trie/)
