from math import dist
from itertools import combinations
from operator import itemgetter, mul
from functools import reduce

points = [tuple(map(int, coords.split(","))) for coords in open("8.input")]  # from input
distances = sorted([(pair, dist(*pair)) for pair in combinations(points, r=2)], key=itemgetter(1))
circuits = [{p} for p in points]
for (a, b), _ in distances[:1000]:
    new_set = set()
    for c in circuits.copy():
        if {a, b} - c and (a in c or b in c):
            new_set |= c
            circuits.remove(c)
    if new_set:
        circuits.append(new_set)

print(reduce(mul, [len(c) for c in sorted(circuits, key=len, reverse=True)[:3]]))
