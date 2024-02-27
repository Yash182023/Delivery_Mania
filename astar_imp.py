import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from pages.astar import astar  # Import the A* algorithm

# Create a graph with fake vertices, edges, and weights
G = nx.Graph()
G.add_nodes_from(['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Hyderabad', 'Jaipur', 'Ahmedabad', 'Pune', 'Lucknow'])
G.add_edges_from([('Delhi', 'Mumbai', {'weight': 2}),
                  ('Delhi', 'Kolkata', {'weight': 1}),
                  ('Mumbai', 'Chennai', {'weight': 3}),
                  ('Kolkata', 'Bangalore', {'weight': 4}),
                  ('Chennai', 'Bangalore', {'weight': 5}),
                  ('Hyderabad', 'Bangalore', {'weight': 2}),
                  ('Jaipur', 'Delhi', {'weight': 3}),
                  ('Ahmedabad', 'Mumbai', {'weight': 2}),
                  ('Pune', 'Mumbai', {'weight': 1}),
                  ('Lucknow', 'Delhi', {'weight': 2})])

# Matplotlib setup
pos = nx.spring_layout(G)  # Layout for better visualization
fig, ax = plt.subplots()

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# Animation function
def update(frame):
    # Highlight the edges in the shortest path
    path_edges = []
    for i in range(frame):
        path_edges.append((shortest_path[i], shortest_path[i + 1]))

    # Draw the graph with highlighted edges
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# Choose the starting and ending nodes
start_node = 'Hyderabad'
end_node = 'Jaipur'

# Define a heuristic function (example: straight-line distance)
def heuristic(node, goal):
    return np.linalg.norm(np.array(pos[node]) - np.array(pos[goal]))

# Calculate the shortest path using A* algorithm
shortest_path_length = astar(G, start_node, end_node, heuristic=heuristic)
shortest_path = nx.shortest_path(G, source=start_node, target=end_node)

# Create an animation
ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_path), interval=1000, repeat=False)

# Show the animation
plt.show()
