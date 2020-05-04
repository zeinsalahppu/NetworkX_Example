"""
NetworkX Examples
Course: Algorithms and Progeamming for Intelligent sysytems
Semester: SS 2020
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_node("A")
G.add_nodes_from(["B" ,"C", "D", "E", "F"])

G.add_edge("A", "B", weight=4)
G.add_weighted_edges_from([("A", "C", 2), ("B", "C", 5), ("B", "D", 10),
                           ("C", "E", 3), ("D", "F", 11), ("E", "D", 4),])


# print some graph info
print("Nodes of graph: ", end="")
print(G.nodes())
print("Edges of graph: ", end="")
print(G.edges())

print((G.degree("D")))
print((G.in_degree("D")))
print((G.out_degree("D")))


# Traversal algorithms
print(list(nx.dfs_preorder_nodes(G, "A")))

bft_list = dict(nx.bfs_successors(G, "A"))
print(bft_list)


# shortest path algorithms
print(nx.shortest_path(G, "A", "E"))

path = nx.dijkstra_path(G, "A", "F")
print(path)

paths = nx.single_source_dijkstra_path(G, "A")
print(paths)

path_lengths = nx.single_source_dijkstra_path_length(G, "A")
print(path_lengths)


# draw graph using matplotlib
pos = nx.spectral_layout(G, 2)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()