from itertools import combinations

machines = []
for line in open("10.input"):
    lights, *buttons, joltage = line.split()
    bs = []
    [bs.append(tuple(map(int, b[1:-1].split(",")))) for b in buttons]
    ls = [c == "#" for c in lights[1:-1]]
    j = tuple(map(int, joltage[1:-1].split(",")))
    machines.append((ls, bs, j))

def match(ls, c):
    result = [0] * len(ls)
    for press in c:
        for change in press:
            result[change] += 1
    return [x % 2 == 1 for x in result] == ls

tot = 0
for ls, bs, j in machines:
    found = 0
    for i in range(1, 50):
        if found: break
        cs = combinations(bs, i)
        for c in cs:
            if match(ls, c):
                found = i
                break
    tot += found

print(tot)
