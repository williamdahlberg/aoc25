
curr_beams =  set()
splitters = set()
for y, line in enumerate(open("7.input")):
    for x, char in enumerate(line):
        if char == "S": curr_beams.add((x + y*1j))
        if char == "^": splitters.add((x + y*1j))

def check(beams):
    new_beams = set()
    splits = 0
    for beam in beams:
        under = beam + 1j
        if under in splitters:
            splits += 1
            new_beams.add(under + 1)
            new_beams.add(under - 1)
        else:
            new_beams.add(under)
    return splits, new_beams


bottom = int(max([y.imag for y in splitters])) + 1
splits = 0
for y in range(bottom):
    s, curr_beams = check(curr_beams)
    splits += s

print(splits)