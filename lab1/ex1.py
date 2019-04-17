import networkx as nx
import matplotlib.pyplot as plt
from statistics import mean

data = open("names.txt", "r")
G = nx.Graph()
i = 0
influencer = []
for line in data:
    word = line.split()
    edge = (word[1], word[2])
    G.add_edge(*edge)

influencer = list(G.nodes)
plt.plot()
# nx.draw(G, with_labels=True)

# Task 1
n_edges = G.number_of_edges()
n_nodes = G.number_of_nodes()
print("tot edges: ", n_edges)
print("tot nodes: ", n_nodes)

# Task 2.1
# CCDF
# degree_sequence = sorted([d for n, d in G.degree()])
# plt.loglog(degree_sequence, marker='o')
# plt.title("CCDF")
# plt.xlabel("degree")
# plt.ylabel("profiles")

# Task 2.2
# number of degree of each node / by number of node
deg_list = [G.degree(i) for i in influencer]
average = mean(deg_list)
print("avg deg nodes: ", average)

# Task 3
# clustering coefficient default trials = 1000
# avg_cluster = nx.average_clustering(G)
# print("avg clustering coefficient (%) : ", avg_cluster*100)

# Task 4
giant = max(nx.connected_components(G))
print("size of giant component", len(giant))

plt.show()
data.close()
# put ccdf vs random graph table



