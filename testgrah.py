import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

edges = [(1, 3), (1, 7), (1, 11), (7, 2), (7, 8), (8, 9), (9, 10), (10, 5), (10, 6), (11, 4), (6, 12), (2, 8), (7, 11)]

for i in edges:
    G.add_edge(str(i[0]), str(i[1]), weight=1)


def pytb(start_v, end_v):
    global G
    a = nx.shortest_path(G, start_v, end_v, weight="weight")
    # nx.draw(G, with_labels=True, font_weight='bold')
    # plt.show()
    return a



# print(pytb("2", "1"))
#если передатғ None то выдаст список со всеми ключами и значениями

# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()
