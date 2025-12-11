import networkx as nx

devices = {}
for line in open("11.input"):
    this, *outputs = line.split()
    this = this[:-1]
    devices[this] = outputs

G = nx.DiGraph(devices)

# p1
print(len(list(nx.all_simple_paths(G, source="you", target="out"))))
