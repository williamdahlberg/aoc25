from operator import add, mul
from functools import reduce

# p1
lines = [l.split() for l in open("6.input")]
total = 0
for i in range(len(lines[0])):
    op = mul if lines[-1][i] == "*" else add
    total += reduce(op, [int(lines[x][i]) for x in range(len(lines) - 1)])
print(total)

# p2
lines = ["".join(s) for s in (zip(*open("6.input").readlines()))]
tot = curr = 0
for line in lines:
    if "+" in line or "*" in line:
        tot += curr
        op = add if "+" in line else mul
        curr = int(line[:-1])
        continue
    if line.strip():
        curr = op(curr, int(line))

tot += curr
print(tot)