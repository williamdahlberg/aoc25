
# combination
p1 = p2 = 0
for rs, re in [map(int, r.split("-")) for r in open("2.input").read().split(",")]:
    for i in range(rs, re+1):
        s = str(i)
        for chunk_size in reversed(range(1, len(s)//2 + 1)):
            ss = [s[n:n+chunk_size] for n in range(0, len(s), chunk_size)]
            if all(t == ss[0] for t in ss):
                p2 += i
                if len(ss) == 2: p1 += i
                break
print(p1, p2)
