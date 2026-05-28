---
title: "Aho-Corasick"
sidebar_label: "Aho-Corasick"
tags: [algorithm, string]
---

# Aho-Corasick

> Multi-pattern matching using a trie augmented with failure links.

## Quick Facts

| | |
|---|---|
| **Kind** | Algorithm |
| **Category** | String |
| **Time** | O(n + m + z) |
| **Space** | O(m) |

## Key Techniques

- Trie + BFS failure links

## Notes & Interview Tips

Antivirus signature scanning; multi-pattern matching.

## How It Works

Aho-Corasick is a multi-pattern string matching algorithm that finds all occurrences of multiple patterns in a text simultaneously in O(n + m + z) time, where n is text length, m is total pattern length, and z is the number of matches.

It builds a trie from all patterns, then adds failure links (similar to KMP's failure function) that connect nodes to the longest proper suffix that is also a prefix of some pattern. This creates an automaton that processes the text character by character.

Aho-Corasick is used in intrusion detection systems (scanning network traffic for malware signatures), text editors (multi-find), and bioinformatics. It's essentially KMP generalized to multiple patterns.

## Implementation

```python
from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        self.goto = [{}]
        self.fail = [0]
        self.output = [[]]

    def add_pattern(self, pattern, idx):
        state = 0
        for ch in pattern:
            if ch not in self.goto[state]:
                self.goto[state][ch] = len(self.goto)
                self.goto.append({})
                self.fail.append(0)
                self.output.append([])
            state = self.goto[state][ch]
        self.output[state].append(idx)

    def build(self):
        queue = deque()
        for ch, s in self.goto[0].items():
            queue.append(s)
        while queue:
            r = queue.popleft()
            for ch, s in self.goto[r].items():
                queue.append(s)
                state = self.fail[r]
                while state and ch not in self.goto[state]:
                    state = self.fail[state]
                self.fail[s] = self.goto[state].get(ch, 0)
                if self.fail[s] == s: self.fail[s] = 0
                self.output[s] = self.output[s] + self.output[self.fail[s]]

    def search(self, text):
        state = 0
        results = []
        for i, ch in enumerate(text):
            while state and ch not in self.goto[state]:
                state = self.fail[state]
            state = self.goto[state].get(ch, 0)
            for pattern_idx in self.output[state]:
                results.append((i, pattern_idx))
        return results
```

## Key Insight

> Aho-Corasick = Trie + KMP failure links. It processes the text once and matches all patterns simultaneously, making it much faster than running KMP for each pattern separately.

## Visualization

- [Interactive Visualization](https://algorithm-visualizer.org/)

## LeetCode Problems

| # | Problem | Difficulty | Curated Lists |
|---|---------|-----------|---------------|
|  | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | 🟢 Easy | - |
|  | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | 🔴 Hard | - |
|  | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | 🟢 Easy | - |
|  | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | 🟢 Easy | B75, NC150 |
|  | [Repeated String Match](https://leetcode.com/problems/repeated-string-match/) | 🟡 Medium | - |

## Resources

- [Wikipedia](https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm)
- [cp-algorithms.com](https://cp-algorithms.com/string/aho_corasick.html)
