import networkx as nx
import matplotlib.pyplot as plt
from statistics import mean
import random
import copy



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

list_of_active = []
dictionary_of_active = {}

INITIAL_SANE = 9999000  # choose from 0 to 100
NEIGHBOURS = 0.9  # choose from 0 to 1 if % of neighours are infected then also the node
RESISTANCE = 10

for i in list(G.nodes):
    x = random.randint(0, 10000000)
    if x < INITIAL_SANE:
        y = 0
    else:
        y = 1
    dictionary_of_active[i] = {'active': y}

nx.set_node_attributes(G, dictionary_of_active)

not_inf = 0
for i in list(G.nodes):
    #print(G.nodes[i]['active'], ": ", i)
    if G.nodes[i]['active'] == 0:
        not_inf += 1

surv = not_inf/n_nodes

r = random.randint(0, 100)
surv_list = []
surv_list.append(surv)
G_old = copy.deepcopy(G)
for i in range(20):
    for j in list(G.nodes):
        if G.nodes[j]['active'] == 0:
            infection_rate = 0
            for k in list(G_old.adj[j]):
                if G_old.nodes[k]['active'] == 1:
                    infection_rate += 1
            infetion_rate = infection_rate/len(list(G_old.adj[j]))
            if infection_rate > NEIGHBOURS and RESISTANCE < r:
                G.nodes[j]['active'] = 1
    G_old = copy.deepcopy(G)
    not_inf = 0
    for z in list(G.nodes):
        # print(G.nodes[i]['active'], ": ", i)
        if G.nodes[z]['active'] == 0:
            not_inf += 1
    new_surv = not_inf / n_nodes
    surv_list.append(new_surv)


print("old :", surv, " new: ", new_surv)
plt.plot(surv_list)
plt.show()
