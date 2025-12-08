from math import dist
from itertools import combinations
from operator import itemgetter, mul
from functools import reduce

points = [tuple(map(int, coords.split(","))) for coords in open("8.input")]  # from input
distances = sorted([(pair, dist(*pair)) for pair in combinations(points, r=2)], key=itemgetter(1))
circuits = {frozenset((p,)) for p in points}
for i, ((a, b), _) in enumerate(distances):
    matches = set([c for c in circuits if a in c or b in c])
    circuits -= matches
    circuits.add(frozenset.union(*matches))
    if i == 999:  # p1
       print(reduce(mul, [len(c) for c in sorted(circuits, key=len, reverse=True)[:3]])) 
    if len(circuits) == 1:  # p2
        print(a[0] * b[0])
        break
