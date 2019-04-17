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
max_DG = max(nx.strongly_connected_components_subgraph(DG), key=len)
print(DG.number_of_nodes())
print(DG.number_of_edges())
print(n_strongly_connected)
print(max_DG)

print(type(max_DG))

H = nx.Graph(max_DG)
diameter = nx.diameter(H)
radius = nx.radius(H)
center = nx.center(H)
print(diameter)
print(radius)
print(center)


data.close()