from math import dist
from itertools import combinations
from operator import itemgetter, mul
from functools import reduce

points = [tuple(map(int, coords.split(","))) for coords in open("8.input")]  # from input
distances = sorted([(pair, dist(*pair)) for pair in combinations(points, r=2)], key=itemgetter(1))
circuits = [{p} for p in points]
for i, ((a, b), _) in enumerate(distances):
    if i == 1000:
        break
    to_merge = []
    connected = False
    for c in circuits:
        if a in c and b in c:
            connected = True
        if a in c:
            to_merge.append(c)
        if b in c:
            to_merge.append(c)
    if not connected:
        circuits.remove(to_merge[0])
        circuits.remove(to_merge[1])
        circuits.append(to_merge[0].union(to_merge[1]))

print(reduce(mul, [len(c) for c in sorted(circuits, key=len, reverse=True)[:3]]))
