
from collections import defaultdict


curr_beams =  defaultdict(int)
splitters = set()
for y, line in enumerate(open("7.input")):
    for x, char in enumerate(line):
        if char == "S": curr_beams[(x + y*1j)] = 1
        if char == "^": splitters.add((x + y*1j))

def check(beams):
    new_beams = defaultdict(int)
    splits = 0
    for coord, count in beams.items():
        under = coord + 1j
        if under in splitters:
            splits += count
            new_beams[under + 1] += count
            new_beams[under - 1] += count
        else:
            new_beams[under] += count
    return splits, new_beams

# p2 only
bottom = int(max([y.imag for y in splitters])) + 1
timelines = 1
for y in range(bottom):
    splits, curr_beams = check(curr_beams)
    timelines += splits

print(timelines)