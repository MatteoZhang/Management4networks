import networkx as nx
import matplotlib.pyplot as plt
from statistics import mean

data = open("names.txt", "r")
G = nx.Graph()
i = 0
influencer = []
for line in data:
    i += 1
    word = line.split()
    edge = (word[1], word[2])
    G.add_edge(*edge)

print("total number of entries: ", i)
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
# CCDF:
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
user_degree = {}
for i in degree_sequence:
    if i not in user_degree.keys():
        user_degree[i] = 1
    else:
        user_degree[i] += 1
a = sorted(user_degree.items())
x, y = zip(*a)
plt.loglog(x, y, '.')
plt.grid(which='minor')
plt.grid(which='major')
plt.title("Degree Distribution")
plt.ylabel("Number of profiles")
plt.xlabel("Degree")

plt.show()
# End CCDF

# Task 2.2
# number of degree of each node / by number of node
deg_list = [G.degree(i) for i in influencer]
average = mean(deg_list)
print("avg deg nodes: ", average)

# Task 3
# clustering coefficient default trials = 1000
avg_cluster = nx.average_clustering(G)
print("avg clustering coefficient : ", avg_cluster)

# Task 4
giant = max(nx.connected_components(G))
print("size of giant component: ", len(giant))

plt.show()
data.close()
# put CCDF vs random graph table



