
lines = [l.strip() for l in open("7.input")]
answer = [[1 if char == "S" else 0 for char in lines[0]]]
for _ in range(len(lines[0])): answer.append([0] * len(lines[0]))

splits = 0
for y, line in enumerate(lines[1:], 1):
    for x, char in enumerate(line):
        if char == "^":
            if answer[y-1][x] > 0: splits += 1
            answer[y][x + 1] += answer[y-1][x]
            answer[y][x - 1] += answer[y-1][x]
        else:
            answer[y][x] += answer[y-1][x]

print(splits, sum(answer[-1]))
