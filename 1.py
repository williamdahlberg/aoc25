
dial, p1, p2 = 50, 0, 0
for line in open('1.input'):
    for _ in range(int(line[1:])): 
        dial = dial + 1 if line[0] == "R" else dial - 1
        if dial % 100 == 0:
            p2 += 1
    if dial % 100 == 0:
        p1 += 1

print(p1, p2)
