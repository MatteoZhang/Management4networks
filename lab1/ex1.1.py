import networkx as nx

# Directed graph

DG = nx.DiGraph()
# Task 5
data = open("names.txt", "r")

for line in data:
    word = line.split()
    edge = (word[1], word[2])
    DG.add_edge(*edge)

n_strongly_connected = nx.number_strongly_connected_components(DG)
max_DG = max(nx.strongly_connected_components(DG), key=len)
print(DG.number_of_nodes())
print(DG.number_of_edges())
print(n_strongly_connected)
# print(max_DG)

Biggest = DG.subgraph(max_DG)
# print(Biggest.nodes())
diameter = nx.diameter(Biggest)
radius = nx.radius(Biggest)
centre = nx.center(Biggest)
print(diameter)
print(radius)
print(centre)

data.close()
