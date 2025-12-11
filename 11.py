import networkx as nx

devices = {this[:-1]: outputs for this, *outputs in [line.split() for line in open("11.input")]}
G = nx.DiGraph(devices)

# p1
print(len(list(nx.all_simple_paths(G, source="you", target="out"))))
