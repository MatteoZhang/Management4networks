import networkx as nx

# Directed graph

DG = nx.DiGraph()
# Task 5
data = open("names.txt", "r")

i = 0
for line in data:
    #if i < 2000:
    word = line.split()
    edge = (word[1], word[2])
    DG.add_edge(*edge)
    #i += 1

n_strongly_connected = nx.number_strongly_connected_components(DG)
max_DG = max(nx.strongly_connected_components(DG), key=len)
print("tot nodes: ", DG.number_of_nodes())
print("tot edges: ", DG.number_of_edges())
print("tot strongly connected components: ", n_strongly_connected)
# print(max_DG)

max_W_DG = max(nx.weakly_connected_components(DG), key=len)

Biggest = DG.subgraph(max_DG)
Biggest_W = DG.subgraph(max_W_DG)
Biggest_W = Biggest_W.to_undirected()

# print(Biggest.nodes())
diameter = nx.diameter(Biggest)
radius = nx.radius(Biggest)
centre = nx.center(Biggest)
print("diameter strongly connected: ", diameter)
print("radius: ", radius)
print("center nodes: ", centre)

diameter_W = nx.diameter(Biggest_W)
centre_W = nx.center(Biggest_W)
radius_W = nx.radius(Biggest_W)
print("diameter weakly connected: ", diameter_W)
print("radius: ", radius_W)
print("center: ", centre_W)

data.close()
