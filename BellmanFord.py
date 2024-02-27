# Import necessary libraries and modules
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from pages.bellmanford import bellman_ford

# Create a graph with fake cities, places, and weights
G = nx.Graph()
G.add_nodes_from(['Delhi', 'CP', 'Lajpat Nagar', 'Kolkata', 'Mumbai', 'Chennai', 'Jaipur', 'Hyderabad'])
G.add_edges_from([('Delhi', 'CP', {'weight': 2}),
                  ('Delhi', 'Lajpat Nagar', {'weight': 1}),
                  ('CP', 'Kolkata', {'weight': 3}),
                  ('Lajpat Nagar', 'Mumbai', {'weight': 4}),
                  ('Kolkata', 'Chennai', {'weight': 5}),
                  ('Mumbai', 'Chennai', {'weight': 2}),
                  ('Chennai', 'Jaipur', {'weight': 3}),
                  ('Jaipur', 'Delhi', {'weight': 4}),
                  ('Hyderabad', 'Jaipur', {'weight': 6})])

# Apply Bellman-Ford algorithm
start_node = 'Delhi'
end_node = 'Jaipur'
bellman_ford_paths = bellman_ford(G, start_node)

# Matplotlib setup
pos = nx.spring_layout(G)  # Layout for better visualization
fig, ax = plt.subplots()

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# Animation function
def update(frame):
    # Highlight the edges in the Bellman-Ford shortest path from 'Delhi' to 'Jaipur'
    path_edges = []
    for i in range(len(bellman_ford_paths[frame]) - 1):
        path_edges.append((bellman_ford_paths[frame][i], bellman_ford_paths[frame][i + 1]))

    # Draw the graph with highlighted edges
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# Create an animation
ani = animation.FuncAnimation(fig=fig, func=update, frames=len(bellman_ford_paths), interval=1000, repeat=False)

# Show the animation
plt.show()
