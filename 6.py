from itertools import takewhile
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
lines = (["".join(s) for s in (zip(*open("6.input").readlines()))])
t = 0
for i, line in enumerate(lines):
    if "+" in line or "*" in line:
        numbers = list(takewhile(lambda x: x.strip(), lines[i+1:]))
        t += reduce(mul if "*" in line else add, map(int, numbers + [line[:-1]]))
print(t)

# p2 oneliner
print(sum([reduce(mul if "*" in line else add, map(int, list(takewhile(lambda x: x.strip(), lines[i+1:])) + [line[:-1]])) for i, line in enumerate(lines) if "+" in line or "*" in line]))
