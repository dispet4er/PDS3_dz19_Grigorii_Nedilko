import networkx as nx


def path(g, start, finish):
    path = nx.shortest_path(g, start, finish, weight = 'weight')
    length = nx.shortest_path_length(g, start, finish, weight = 'weight')
    return path, length


filename = "cities.csv"
with open(filename) as file:
    edgelist = [line.rstrip().split(";") for line in file]


g = nx.Graph()
for edge in edgelist:
    g.add_edge(edge[0], edge[1], weight = int(edge[2]))


print(path(g, 'Poltava', 'Lviv'))