*gifts, trees = open("12.input").read().split("\n\n")
gift_sizes = [g.count("#") for g in gifts]

fits = 0
for tree in trees.split("\n"):
    size, *items = tree.split()
    a, b = list(map(int, size[:-1].split("x")))
    required_size = sum([int(item) * gift_sizes[i] for i, item in enumerate(items)])
    if required_size <= a * b:
        fits += 1
print(fits)
