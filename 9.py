from itertools import combinations
points = list(map(eval, open("9.input")))

def size(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

sizes = sorted([size(*pair) for pair in combinations(points, r=2)])
print(sizes[-1])
