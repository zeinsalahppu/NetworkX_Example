"""
NetworkX Examples
Course: Algorithms and Progeamming for Intelligent sysytems
Semester: SS 2020
"""

import networkx as nx

G = nx.DiGraph()
G.add_node("A")
G.add_nodes_from(["B" ,"C", "D", "E", "F"])

G.add_edge("A", "B", weight=4)
G.add_weighted_edges_from([("A", "C", 2), ("B", "C", 5), ("B", "D", 10),
                           ("C", "E", 3), ("D", "F", 11), ("E", "D", 4),])

