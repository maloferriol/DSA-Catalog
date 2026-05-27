"""Map each catalog entry to LeetCode problems via the topic-tag JSON."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dsa_data import ENTRIES

LC = json.load(open(os.path.join(os.path.dirname(__file__), 'leetcode_tags2.json')))

# Add stubs for canonical IDs that aren't in the top 100 of any fetched tag
STUBS = {
    "1143": {"i": "1143", "t": "Longest Common Subsequence", "s": "longest-common-subsequence", "d": "M", "a": 60, "p": 0},
}
for tag in ("dynamic-programming", "string"):
    if tag in LC:
        ids_in_tag = {p["i"] for p in LC[tag]["problems"]}
        for sid, stub in STUBS.items():
            if sid not in ids_in_tag:
                LC[tag]["problems"].append(stub)

# Map entry name -> list of LeetCode topic-tag slugs (priority order)
# Where the canonical tag isn't a perfect fit, I steer to where the famous
# problems for this technique actually live on LeetCode.
ENTRY_TAGS = {
    # ---------- Linear DS ----------
    "Array": ["array", "two-pointers"],
    "Dynamic Array (ArrayList / Vector)": ["array", "design"],
    "String": ["string", "two-pointers", "sliding-window"],
    "Linked List (Singly)": ["linked-list", "two-pointers"],
    "Doubly Linked List": ["doubly-linked-list", "linked-list", "design"],
    "Stack": ["stack", "monotonic-stack"],
    "Queue": ["queue", "breadth-first-search"],
    "Deque (Double-ended queue)": ["monotonic-queue", "queue", "sliding-window"],
    "Hash Table / Hash Map": ["hash-table", "design"],
    "Hash Set": ["hash-table", "array"],
    "Bloom Filter": ["design", "hash-table"],
    # ---------- Trees ----------
    "Binary Tree": ["binary-tree", "tree", "depth-first-search"],
    "Binary Search Tree (BST)": ["binary-search-tree", "tree"],
    "AVL Tree": ["binary-search-tree", "tree"],
    "Red-Black Tree": ["binary-search-tree", "ordered-set"],
    "B-Tree / B+ Tree": ["design", "ordered-set"],
    "Trie (Prefix Tree)": ["trie", "design"],
    "Heap (Binary Heap)": ["heap-priority-queue"],
    "Priority Queue": ["heap-priority-queue", "design"],
    "Segment Tree": ["segment-tree"],
    "Fenwick Tree (Binary Indexed Tree)": ["binary-indexed-tree", "segment-tree"],
    "Disjoint Set Union (Union-Find)": ["union-find"],
    "Suffix Array / Suffix Tree": ["suffix-array", "string-matching"],
    # ---------- Graph ----------
    "Graph": ["graph", "depth-first-search", "breadth-first-search"],
    "Matrix (Grid)": ["matrix", "depth-first-search", "breadth-first-search"],
    # ---------- Specialized ----------
    "Monotonic Stack": ["monotonic-stack"],
    "Monotonic Queue / Deque": ["monotonic-queue", "sliding-window"],
    "LRU Cache": ["design", "doubly-linked-list", "hash-table"],
    "Skip List": ["design", "linked-list"],
    "Sparse Table": ["segment-tree", "binary-search"],
    # ---------- Searching ----------
    "Linear Search": ["array"],
    "Binary Search": ["binary-search"],
    "Ternary Search": ["binary-search", "math"],
    "Quickselect": ["quickselect", "heap-priority-queue"],
    # ---------- Sorting ----------
    "Bubble Sort": ["sorting"],
    "Insertion Sort": ["sorting"],
    "Selection Sort": ["sorting"],
    "Merge Sort": ["sorting", "divide-and-conquer"],
    "Quick Sort": ["sorting", "divide-and-conquer"],
    "Heap Sort": ["sorting", "heap-priority-queue"],
    "Counting Sort": ["counting-sort", "sorting"],
    "Radix Sort": ["radix-sort", "sorting"],
    "Bucket Sort": ["bucket-sort", "sorting"],
    "Topological Sort": ["topological-sort", "graph"],
    # ---------- Graph traversal & shortest path ----------
    "Breadth-First Search (BFS)": ["breadth-first-search", "graph"],
    "Depth-First Search (DFS)": ["depth-first-search", "graph"],
    "Dijkstra's Algorithm": ["shortest-path", "graph", "heap-priority-queue"],
    "Bellman-Ford": ["shortest-path", "graph"],
    "Floyd-Warshall": ["shortest-path", "graph", "dynamic-programming"],
    "A* Search": ["shortest-path", "graph"],
    "Kruskal's MST": ["minimum-spanning-tree", "union-find"],
    "Prim's MST": ["minimum-spanning-tree", "graph"],
    "Tarjan's SCC": ["graph", "depth-first-search"],
    "Kosaraju's SCC": ["graph", "depth-first-search"],
    "Floyd's Cycle Detection (Tortoise & Hare)": ["two-pointers", "linked-list"],
    # ---------- DP ----------
    "Dynamic Programming": ["dynamic-programming"],
    "Knapsack (0/1)": ["dynamic-programming"],
    "Unbounded Knapsack": ["dynamic-programming"],
    "Longest Common Subsequence (LCS)": ["dynamic-programming", "string"],
    "Longest Increasing Subsequence (LIS)": ["dynamic-programming", "binary-search"],
    "Edit Distance (Levenshtein)": ["dynamic-programming", "string"],
    "Matrix Chain Multiplication": ["dynamic-programming"],
    "Bitmask DP": ["bit-manipulation", "dynamic-programming"],
    # ---------- Greedy ----------
    "Greedy Algorithm": ["greedy"],
    "Interval Scheduling": ["greedy", "array"],
    "Huffman Coding": ["greedy", "heap-priority-queue"],
    # ---------- Divide & Conquer ----------
    "Divide & Conquer": ["divide-and-conquer"],
    # ---------- Backtracking ----------
    "Backtracking": ["backtracking"],
    "N-Queens": ["backtracking"],
    "Permutations / Combinations / Subsets": ["backtracking", "combinatorics"],
    # ---------- String ----------
    "KMP (Knuth-Morris-Pratt)": ["string-matching", "string"],
    "Rabin-Karp": ["string-matching", "rolling-hash", "string"],
    "Z Algorithm": ["string-matching", "string"],
    "Manacher's Algorithm": ["string", "dynamic-programming"],
    "Aho-Corasick": ["string-matching", "trie"],
    # ---------- Math ----------
    "Euclidean Algorithm (GCD)": ["math", "number-theory"],
    "Sieve of Eratosthenes": ["math", "number-theory"],
    "Fast Exponentiation": ["math", "divide-and-conquer"],
    "Bit Manipulation": ["bit-manipulation"],
    # ---------- Patterns ----------
    "Two Pointers": ["two-pointers"],
    "Sliding Window": ["sliding-window"],
    "Fast & Slow Pointers": ["two-pointers", "linked-list"],
    "Prefix Sum": ["prefix-sum"],
    "Difference Array": ["prefix-sum", "array"],
    "Sweep Line": ["array", "sorting", "ordered-set"],
    "Recursion": ["recursion"],
    "Memoization": ["memoization", "dynamic-programming"],
    "Flood Fill": ["depth-first-search", "matrix", "breadth-first-search"],
    "Reservoir Sampling": ["reservoir-sampling"],
    "Fisher-Yates Shuffle": ["array", "math"],
    "Boyer-Moore Majority Vote": ["array", "hash-table"],
    "Kadane's Algorithm": ["array", "dynamic-programming"],
}

# Hand-picked canonical problem IDs that BEST exercise the technique.
# These take precedence so the most famous problems show up first.
CANONICAL = {
    "Array": ["1", "121", "53", "238", "11"],
    "String": ["3", "5", "76", "242", "49"],
    "Linked List (Singly)": ["206", "21", "141", "19", "234"],
    "Doubly Linked List": ["146", "432", "460"],
    "Stack": ["20", "155", "739", "150", "232"],
    "Queue": ["232", "933", "622", "225"],
    "Deque (Double-ended queue)": ["239", "862", "1438"],
    "Hash Table / Hash Map": ["1", "242", "49", "560", "146"],
    "Hash Set": ["217", "202", "128"],
    "Binary Tree": ["104", "102", "226", "236", "543"],
    "Binary Search Tree (BST)": ["98", "230", "235", "538", "108"],
    "Trie (Prefix Tree)": ["208", "211", "212", "648"],
    "Heap (Binary Heap)": ["215", "347", "23", "295", "703"],
    "Priority Queue": ["215", "23", "253", "295", "973"],
    "Segment Tree": ["307", "315", "327"],
    "Fenwick Tree (Binary Indexed Tree)": ["307", "315", "493"],
    "Disjoint Set Union (Union-Find)": ["200", "684", "547", "721", "990"],
    "Graph": ["207", "210", "133", "743", "1584"],
    "Matrix (Grid)": ["200", "994", "79", "73", "48"],
    "Monotonic Stack": ["739", "496", "84", "42", "503"],
    "Monotonic Queue / Deque": ["239", "862", "1438"],
    "LRU Cache": ["146", "460"],
    "Binary Search": ["704", "33", "153", "4", "278"],
    "Quickselect": ["215", "973", "347"],
    "Merge Sort": ["88", "148", "23", "493"],
    "Quick Sort": ["75", "215", "912"],
    "Heap Sort": ["912", "215"],
    "Bucket Sort": ["347", "451", "164"],
    "Topological Sort": ["207", "210", "269", "329"],
    "Breadth-First Search (BFS)": ["102", "200", "994", "127", "752"],
    "Depth-First Search (DFS)": ["200", "104", "98", "133", "417"],
    "Dijkstra's Algorithm": ["743", "787", "1631", "1514"],
    "Bellman-Ford": ["787"],
    "Floyd-Warshall": ["1334"],
    "Floyd's Cycle Detection (Tortoise & Hare)": ["141", "142", "287"],
    "Dynamic Programming": ["70", "300", "322", "53", "198"],
    "Knapsack (0/1)": ["416", "474", "494"],
    "Unbounded Knapsack": ["322", "518", "279"],
    "Longest Common Subsequence (LCS)": ["1143", "583", "72"],
    "Longest Increasing Subsequence (LIS)": ["300", "354", "673"],
    "Edit Distance (Levenshtein)": ["72", "583", "161"],
    "Bitmask DP": ["78", "473", "847"],
    "Greedy Algorithm": ["55", "45", "763", "881", "134"],
    "Interval Scheduling": ["435", "452", "56"],
    "Huffman Coding": ["1167"],
    "Divide & Conquer": ["169", "53", "215", "23"],
    "Backtracking": ["46", "78", "39", "51", "131"],
    "N-Queens": ["51", "52"],
    "Permutations / Combinations / Subsets": ["46", "78", "77", "39", "90"],
    "Rabin-Karp": ["28", "187"],
    "KMP (Knuth-Morris-Pratt)": ["28", "459"],
    "Manacher's Algorithm": ["5", "647"],
    "Bit Manipulation": ["136", "191", "338", "190", "260"],
    "Two Pointers": ["167", "15", "11", "125", "75"],
    "Sliding Window": ["3", "76", "239", "424", "209"],
    "Fast & Slow Pointers": ["141", "142", "287", "876"],
    "Prefix Sum": ["303", "560", "974", "238", "304"],
    "Sweep Line": ["56", "253", "218"],
    "Recursion": ["50", "21", "104", "206"],
    "Memoization": ["70", "509", "139"],
    "Flood Fill": ["733", "200", "130", "417"],
    "Reservoir Sampling": ["382", "398"],
    "Fisher-Yates Shuffle": ["384"],
    "Boyer-Moore Majority Vote": ["169", "229"],
    "Kadane's Algorithm": ["53", "152", "918"],
}

def pick_problems(entry, target=5):
    """Pick up to `target` LeetCode problems for an entry."""
    name = entry["name"]
    canonical_ids = set(CANONICAL.get(name, []))
    tags = ENTRY_TAGS.get(name, [])
    # Build a pool of problems from related tags in priority order
    pool = []
    seen = set()
    # Pass 1: canonical IDs in order
    canonical_order = CANONICAL.get(name, [])
    canonical_map = {}
    for tag in tags:
        for p in LC.get(tag, {}).get("problems", []):
            if p["i"] in canonical_ids and p["i"] not in canonical_map:
                canonical_map[p["i"]] = p
    # Add canonical in the order I specified
    for pid in canonical_order:
        if pid in canonical_map:
            pool.append(canonical_map[pid])
            seen.add(pid)
    # Pass 2: fill from related tags
    for tag in tags:
        for p in LC.get(tag, {}).get("problems", []):
            if p["i"] not in seen:
                pool.append(p)
                seen.add(p["i"])
                if len(pool) >= target * 3: break
        if len(pool) >= target * 3: break

    # Take up to `target`, prefer mix of difficulties
    out = []
    # First, take all canonical that exist
    for p in pool:
        if p["i"] in canonical_ids:
            out.append(p)
        if len(out) >= target: break
    # Then fill with others (non-paid first)
    if len(out) < target:
        for p in pool:
            if p["i"] in canonical_ids: continue
            if p.get("p"): continue  # skip paid in fill
            out.append(p)
            if len(out) >= target: break
    # If still short, allow paid
    if len(out) < target:
        for p in pool:
            if p in out: continue
            out.append(p)
            if len(out) >= target: break
    return out

# Apply mapping
enriched = []
unmapped = []
for e in ENTRIES:
    problems = pick_problems(e, target=5)
    if not problems:
        unmapped.append(e["name"])
    enriched.append({
        "name": e["name"],
        "kind": e["kind"],
        "category": e["category"],
        "definition": e["definition"],
        "time": e["time"],
        "space": e["space"],
        "techniques": e["techniques"],
        "wikipedia": e["wikipedia"],
        "resources": e["resources"],
        "sean_prashad": e["sean_prashad"],
        "grind75": e["grind75"],
        "notes": e["notes"],
        "leetcode": [
            {
                "id": p["i"],
                "title": p["t"],
                "slug": p["s"],
                "difficulty": {"E":"Easy","M":"Medium","H":"Hard"}.get(p["d"], p["d"]),
                "ac_rate": p["a"],
                "premium": bool(p.get("p")),
                "url": f"https://leetcode.com/problems/{p['s']}/",
            }
            for p in problems
        ],
    })

# Save the enriched dataset
out_path = os.path.join(os.path.dirname(__file__), 'dsa_enriched.json')
with open(out_path, 'w') as f:
    json.dump(enriched, f, ensure_ascii=False)

# Print summary
print(f"Mapped {len(enriched)} entries.")
total_problems = sum(len(e["leetcode"]) for e in enriched)
print(f"Total problem references: {total_problems}")
print(f"Entries with no problems mapped: {len(unmapped)}")
if unmapped:
    print("Unmapped:", unmapped)

# Distribution of difficulties
from collections import Counter
diff_counter = Counter()
for e in enriched:
    for p in e["leetcode"]:
        diff_counter[p["difficulty"]] += 1
print("Difficulty mix:", dict(diff_counter))

# Sample
sample = next(e for e in enriched if e["name"] == "Binary Search")
print("\nSample — Binary Search:")
for p in sample["leetcode"]:
    print(f"  #{p['id']} {p['title']} ({p['difficulty']}) ac={p['ac_rate']}%")
