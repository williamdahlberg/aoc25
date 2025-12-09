from itertools import combinations
def size(p1, p2): return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
print(max([size(*p) for p in combinations(list(map(eval, open("9.input"))), 2)]))
