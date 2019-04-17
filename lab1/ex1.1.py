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
print(max_DG)

MDG = nx.DiGraph()
MDG.add_edges_from(max_DG)
diameter = nx.diameter(MDG)
radius = nx.radius(MDG)
center = nx.center(MDG)
print(diameter)
print(radius)
print(center)


data.close()
