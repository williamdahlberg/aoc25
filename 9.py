# p1
from itertools import combinations
def size(a, b): return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
print(max([size(*p) for p in combinations(list(map(eval, open("9.input"))), 2)]))

# p2
from shapely import Polygon
reds = list(map(eval, open("9.input")))
poly = Polygon(reds)
squares = list(combinations(reds, 2))
def square_poly(a, b): return Polygon((a, (a[0], b[1]), b, (b[0], a[1])))
print(max([size(*square) for square in squares if poly.covers(square_poly(*square))]))
