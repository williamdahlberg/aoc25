grid = {
    x + y * 1j: n
    for y, r in enumerate(open("4.input"))
    for x, n in enumerate(r.strip())
}

def remove(removed = 0):
    t = 0
    for c, n in grid.items():
        if n == "@" and sum([grid.get(c + n, "") == "@" for n in (-1-1j, -1, -1+1j, -1j, 1j, 1-1j, 1, 1+1j)]) < 4:
                grid[c] = "."
                t += 1
    if t == 0:
        return removed
    return remove(removed + t)

print(remove())
