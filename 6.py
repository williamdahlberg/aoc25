from operator import add, mul
from functools import reduce

# p1
lines = [l.split() for l in open("6.input")]
total = 0
for i in range(len(lines[0])):
    op = mul if lines[-1][i] == "*" else add
    total += reduce(op, [int(lines[x][i]) for x in range(len(lines) - 1)])
print(total)