ranges, ingredients = [l.split("\n") for l in open("5.input").read().split("\n\n")]
ranges = sorted([tuple(map(int, r.split("-"))) for r in ranges])

# p1
print(sum([any([a <= int(ingredient) <= b for a, b in ranges]) for ingredient in ingredients]))

# p2
total = low = 0
for a, b in sorted(ranges):
    low = max(a, low + 1)
    total += max(b - low + 1, 0)
    low = b

print(total)
