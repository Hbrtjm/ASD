import networkx as nx
import matplotlib.pyplot as plt

# Adjacency list
adj_list = [
    [(9, 4), (1, 5), (2, 8), (6, 6)],
    [(0, 5), (2, 8), (7, 5), (8, 10)],
    [(1, 8), (3, 10), (0, 8)],
    [(2, 10), (4, 8), (5, 2), (7, 2)],
    [(3, 8), (5, 8), (6, 1)],
    [(4, 8), (6, 7), (3, 2), (8, 2)],
    [(5, 7), (4, 1), (0, 6)],
    [(8, 1), (9, 2), (3, 2), (1, 5)],
    [(7, 1), (9, 10), (5, 2), (1, 10)],
    [(8, 10), (0, 4), (7, 2)]
]

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
for i, neighbors in enumerate(adj_list):
    for neighbor, weight in neighbors:
        G.add_edge(i, neighbor, weight=weight)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes

plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=15, font_weight='bold', edge_color='gray')

# Draw edge labels
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.title("Graph Representation of the Given Adjacency List")
plt.show()