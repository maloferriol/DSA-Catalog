"""
Add the 27 Sean-Prashad problems missing from my catalog as 'bonus' problems
under the most appropriate existing entry. Then regenerate progress.json with
all 56 problems mapped.
"""
import json, os, time

HERE = os.path.dirname(os.path.abspath(__file__))
enriched = json.load(open(os.path.join(HERE, 'dsa_enriched.json')))
g75 = set(json.load(open(os.path.join(HERE, 'grind75_slugs.json'))))
b75 = set(json.load(open(os.path.join(HERE, 'blind75_slugs.json'))))
nc150 = set(json.load(open(os.path.join(HERE, 'neetcode150_slugs.json'))))
done_slugs = set(json.load(open(os.path.join(HERE, 'sean_prashad_done.json'))))

# Metadata for missing problems (from LeetCode GraphQL)
MISSING = {
    "graph-valid-tree":              {"id":"261","title":"Graph Valid Tree","d":"Medium","ac":50,"p":True},
    "interval-list-intersections":   {"id":"986","title":"Interval List Intersections","d":"Medium","ac":73,"p":False},
    "peak-index-in-a-mountain-array":{"id":"852","title":"Peak Index in a Mountain Array","d":"Medium","ac":67,"p":False},
    "binary-tree-paths":             {"id":"257","title":"Binary Tree Paths","d":"Easy","ac":69,"p":False},
    "find-smallest-letter-greater-than-target":{"id":"744","title":"Find Smallest Letter Greater Than Target","d":"Easy","ac":59,"p":False},
    "convert-1d-array-into-2d-array":{"id":"2022","title":"Convert 1D Array Into 2D Array","d":"Easy","ac":72,"p":False},
    "find-peak-element":             {"id":"162","title":"Find Peak Element","d":"Medium","ac":47,"p":False},
    "meeting-rooms":                 {"id":"252","title":"Meeting Rooms","d":"Easy","ac":59,"p":True},
    "is-subsequence":                {"id":"392","title":"Is Subsequence","d":"Easy","ac":49,"p":False},
    "missing-number":                {"id":"268","title":"Missing Number","d":"Easy","ac":72,"p":False},
    "permutation-in-string":         {"id":"567","title":"Permutation in String","d":"Medium","ac":49,"p":False},
    "move-zeroes":                   {"id":"283","title":"Move Zeroes","d":"Easy","ac":64,"p":False},
    "merge-two-binary-trees":        {"id":"617","title":"Merge Two Binary Trees","d":"Easy","ac":79,"p":False},
    "backspace-string-compare":      {"id":"844","title":"Backspace String Compare","d":"Easy","ac":50,"p":False},
    "search-a-2d-matrix":            {"id":"74","title":"Search a 2D Matrix","d":"Medium","ac":54,"p":False},
    "maximum-average-subarray-i":    {"id":"643","title":"Maximum Average Subarray I","d":"Easy","ac":48,"p":False},
    "remove-linked-list-elements":   {"id":"203","title":"Remove Linked List Elements","d":"Easy","ac":54,"p":False},
    "path-sum":                      {"id":"112","title":"Path Sum","d":"Easy","ac":55,"p":False},
    "minimum-depth-of-binary-tree":  {"id":"111","title":"Minimum Depth of Binary Tree","d":"Easy","ac":53,"p":False},
    "number-of-connected-components-in-an-undirected-graph":{"id":"323","title":"Number of Connected Components in an Undirected Graph","d":"Medium","ac":65,"p":True},
    "fruit-into-baskets":            {"id":"904","title":"Fruit Into Baskets","d":"Medium","ac":51,"p":False},
    "squares-of-a-sorted-array":     {"id":"977","title":"Squares of a Sorted Array","d":"Easy","ac":74,"p":False},
    "average-of-levels-in-binary-tree":{"id":"637","title":"Average of Levels in Binary Tree","d":"Easy","ac":75,"p":False},
    "insert-interval":               {"id":"57","title":"Insert Interval","d":"Medium","ac":45,"p":False},
    "find-all-duplicates-in-an-array":{"id":"442","title":"Find All Duplicates in an Array","d":"Medium","ac":77,"p":False},
    "remove-duplicates-from-sorted-list":{"id":"83","title":"Remove Duplicates from Sorted List","d":"Easy","ac":57,"p":False},
    "find-all-numbers-disappeared-in-an-array":{"id":"448","title":"Find All Numbers Disappeared in an Array","d":"Easy","ac":64,"p":False},
}

# Map each missing slug → catalog entry name
ASSIGN = {
    "graph-valid-tree":              "Disjoint Set Union (Union-Find)",
    "interval-list-intersections":   "Two Pointers",
    "peak-index-in-a-mountain-array":"Binary Search",
    "binary-tree-paths":             "Binary Tree",
    "find-smallest-letter-greater-than-target":"Binary Search",
    "convert-1d-array-into-2d-array":"Matrix (Grid)",
    "find-peak-element":             "Binary Search",
    "meeting-rooms":                 "Interval Scheduling",
    "is-subsequence":                "Two Pointers",
    "missing-number":                "Bit Manipulation",
    "permutation-in-string":         "Sliding Window",
    "move-zeroes":                   "Two Pointers",
    "merge-two-binary-trees":        "Binary Tree",
    "backspace-string-compare":      "Two Pointers",
    "search-a-2d-matrix":            "Binary Search",
    "maximum-average-subarray-i":    "Sliding Window",
    "remove-linked-list-elements":   "Linked List (Singly)",
    "path-sum":                      "Binary Tree",
    "minimum-depth-of-binary-tree":  "Binary Tree",
    "number-of-connected-components-in-an-undirected-graph":"Disjoint Set Union (Union-Find)",
    "fruit-into-baskets":            "Sliding Window",
    "squares-of-a-sorted-array":     "Two Pointers",
    "average-of-levels-in-binary-tree":"Breadth-First Search (BFS)",
    "insert-interval":               "Interval Scheduling",
    "find-all-duplicates-in-an-array":"Hash Set",
    "remove-duplicates-from-sorted-list":"Linked List (Singly)",
    "find-all-numbers-disappeared-in-an-array":"Hash Set",
}

# Build slug → problem-record lookup
entry_by_name = {e["name"]: e for e in enriched}

added = 0
for slug, entry_name in ASSIGN.items():
    if entry_name not in entry_by_name:
        print(f"  ! Skipping {slug}: entry '{entry_name}' not found")
        continue
    meta = MISSING[slug]
    new_p = {
        "id": meta["id"],
        "title": meta["title"],
        "slug": slug,
        "difficulty": meta["d"],
        "ac_rate": meta["ac"],
        "premium": meta["p"],
        "url": f"https://leetcode.com/problems/{slug}/",
        "grind75": slug in g75,
        "blind75": slug in b75,
        "neetcode150": slug in nc150,
    }
    entry_by_name[entry_name]["leetcode"].append(new_p)
    added += 1

print(f"Added {added} bonus problems to the catalog.")

# Save the enriched data (overwrite)
with open(os.path.join(HERE, 'dsa_enriched.json'), 'w') as f:
    json.dump(enriched, f, ensure_ascii=False)

# Recompute totals
total_problems = sum(len(e["leetcode"]) for e in enriched)
print(f"Total catalog problems now: {total_problems}")

# Now rebuild progress.json: every Sean-Prashad-done slug → its problem id
slug_to_pid = {p["slug"]: p["id"] for e in enriched for p in e["leetcode"]}
progress = {}
matched = 0
unmatched = []
ts = int(time.time() * 1000)
for slug in done_slugs:
    pid = slug_to_pid.get(slug)
    if pid:
        progress[pid] = {"done": True, "at": ts}
        matched += 1
    else:
        unmatched.append(slug)

out = '/sessions/ecstatic-tender-cray/mnt/Data Structure & Algorithm/progress.json'
with open(out, 'w') as f:
    json.dump(progress, f, indent=2)
print(f"\nWrote {out}")
print(f"  {matched} of {len(done_slugs)} Sean-Prashad-completed problems mapped")
if unmatched:
    print(f"  Still unmatched ({len(unmatched)}): {unmatched}")
