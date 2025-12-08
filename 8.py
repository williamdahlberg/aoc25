from math import dist, prod
from itertools import combinations
from operator import itemgetter

points = [eval(coords) for coords in open("8.input")]
distances = sorted([pair for pair in combinations(points, r=2)], key=lambda p: dist(*p))
circuits = {frozenset((p,)) for p in points}
for i, (a, b) in enumerate(distances):
    matches = set([c for c in circuits if a in c or b in c])
    circuits -= matches
    circuits.add(frozenset.union(*matches))
    if i == 999:  # p1
       print(prod([len(c) for c in sorted(circuits, key=len, reverse=True)[:3]]))
    if len(circuits) == 1:  # p2
        print(a[0] * b[0])
        break
