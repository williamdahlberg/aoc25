ranges, ingredients = [l.split("\n") for l in open("5.input").read().split("\n\n")]
ranges = sorted([tuple(map(int, r.split("-"))) for r in ranges])

# p1
i = 0
for ingredient in ingredients:
    for a, b in ranges:
        if a <= int(ingredient) <= b:
            i += 1
            break

print(i)

# p2
merged = set()
new_ranges = []
for i, (a, b) in enumerate(ranges):
    if i in merged:
        continue
    merged.add(i)

    for j, (x, y) in enumerate(ranges[i:]):
        if x <= b:
            merged.add(i + j)
            b = max(b, y)

    new_ranges.append((a, b))
print(sum([b-a+1 for a, b in new_ranges]))

