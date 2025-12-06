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
lines = open("6.input").readlines()
tot = curr = 0
for i in range(len(lines[0]) - 1):
    if lines[-1][i] in "+*":
        tot += curr
        op = {"*": mul, "+": add}[lines[-1][i]]
        curr = {"*": 1, "+": 0}[lines[-1][i]]

    num = ""
    for j in range(len(lines) - 1):
        num += lines[j][i]
    if num.strip():
        curr = op(curr, int(num))

tot += curr

print(tot)
