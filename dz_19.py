import networkx as nx
import matplotlib.pyplot as plt


filename = "cities.csv"
with open(filename) as file:
    edgelist = [line.rstrip().split(";") for line in file]


g = nx.Graph()
for edge in edgelist:
    g.add_edge(edge[0], edge[1], weight = int(edge[2]))


pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("City Graph")
plt.show()