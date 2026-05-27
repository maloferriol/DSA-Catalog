"""Add Grind 75 / Blind 75 / NeetCode 150 membership flags to each problem in dsa_enriched.json."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
enriched = json.load(open(os.path.join(HERE, 'dsa_enriched.json')))
g75 = set(json.load(open(os.path.join(HERE, 'grind75_slugs.json'))))
b75 = set(json.load(open(os.path.join(HERE, 'blind75_slugs.json'))))
nc150 = set(json.load(open(os.path.join(HERE, 'neetcode150_slugs.json'))))

print(f"Source lists — Grind 75: {len(g75)}, Blind 75: {len(b75)}, NeetCode 150: {len(nc150)}")

# Tag each problem
total_problems = 0
g75_hits = 0
b75_hits = 0
nc150_hits = 0
any_hit = 0
for e in enriched:
    for p in e["leetcode"]:
        total_problems += 1
        slug = p["slug"]
        p["grind75"] = slug in g75
        p["blind75"] = slug in b75
        p["neetcode150"] = slug in nc150
        if p["grind75"]: g75_hits += 1
        if p["blind75"]: b75_hits += 1
        if p["neetcode150"]: nc150_hits += 1
        if p["grind75"] or p["blind75"] or p["neetcode150"]:
            any_hit += 1

# Save
out = os.path.join(HERE, 'dsa_enriched.json')
with open(out, 'w') as f:
    json.dump(enriched, f, ensure_ascii=False)

print(f"\nCatalog: {total_problems} LeetCode problems across {len(enriched)} entries")
print(f"  in Grind 75:     {g75_hits} ({100*g75_hits/total_problems:.0f}%)")
print(f"  in Blind 75:     {b75_hits} ({100*b75_hits/total_problems:.0f}%)")
print(f"  in NeetCode 150: {nc150_hits} ({100*nc150_hits/total_problems:.0f}%)")
print(f"  in ANY of the 3: {any_hit} ({100*any_hit/total_problems:.0f}%)")

# How many SOURCE-list problems are NOT in my catalog
catalog_slugs = {p["slug"] for e in enriched for p in e["leetcode"]}
g75_missing = g75 - catalog_slugs
b75_missing = b75 - catalog_slugs
nc150_missing = nc150 - catalog_slugs

print(f"\nFrom each curated list, problems NOT in my catalog:")
print(f"  Grind 75 missing:     {len(g75_missing)} / {len(g75)}")
print(f"  Blind 75 missing:     {len(b75_missing)} / {len(b75)}")
print(f"  NeetCode 150 missing: {len(nc150_missing)} / {len(nc150)}")
if g75_missing: print(f"    G75: {sorted(g75_missing)[:8]} ...")
if b75_missing: print(f"    B75: {sorted(b75_missing)[:8]} ...")

# Per-entry summary: how many of each list's problems each entry already touches
print()
print("Top 10 entries by Grind 75 coverage:")
ranked = sorted(enriched, key=lambda e: sum(1 for p in e["leetcode"] if p["grind75"]), reverse=True)
for e in ranked[:10]:
    n_g = sum(1 for p in e["leetcode"] if p["grind75"])
    n_b = sum(1 for p in e["leetcode"] if p["blind75"])
    n_nc = sum(1 for p in e["leetcode"] if p["neetcode150"])
    print(f"  {e['name']:40s} G75:{n_g} B75:{n_b} NC150:{n_nc}  (of {len(e['leetcode'])})")
