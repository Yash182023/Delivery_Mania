# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation

# # Create a graph with fake cities, places, and weights
# G = nx.Graph()
# G.add_nodes_from(['Delhi', 'CP', 'Lajpat Nagar', 'Kolkata', 'Mumbai', 'Chennai', 'Jaipur'])
# G.add_edges_from([('Delhi', 'CP', {'weight': 2}),
#                   ('Delhi', 'Lajpat Nagar', {'weight': 1}),
#                   ('CP', 'Kolkata', {'weight': 3}),
#                   ('Lajpat Nagar', 'Mumbai', {'weight': 4}),
#                   ('Kolkata', 'Chennai', {'weight': 5}),
#                   ('Mumbai', 'Chennai', {'weight': 2}),
#                   ('Chennai', 'Jaipur', {'weight': 3}),
#                   ('Jaipur', 'Delhi', {'weight': 4})])

# # Calculate all-pairs shortest paths using Floyd-Warshall
# all_shortest_paths = dict(nx.all_pairs_shortest_path_length(G, weight='weight'))

# # Matplotlib setup
# pos = nx.spring_layout(G)  # Layout for better visualization
# fig, ax = plt.subplots()

# # Draw the graph
# nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# # Animation function
# def update(frame):
#     # Highlight the edges in the shortest path
#     path_edges = []
#     for i in range(len(G.nodes)):
#         if i < len(G.nodes) - 1:
#             current_node = list(G.nodes)[i]
#             next_node = list(G.nodes)[i + 1]
#             if all_shortest_paths[current_node][next_node] < float('inf'):
#                 path_edges.append((current_node, next_node))

#     # Draw the graph with highlighted edges
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)
#     nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(G.nodes), interval=1000, repeat=False)

# # Show the animation
# # plt.show()
# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation

# # Create a graph with fake cities, places, and weights
# G = nx.Graph()
# G.add_nodes_from(['Delhi', 'CP', 'Lajpat Nagar', 'Kolkata', 'Mumbai', 'Chennai', 'Jaipur'])
# G.add_edges_from([('Delhi', 'CP', {'weight': 2}),
#                   ('Delhi', 'Lajpat Nagar', {'weight': 1}),
#                   ('CP', 'Kolkata', {'weight': 3}),
#                   ('Lajpat Nagar', 'Mumbai', {'weight': 4}),
#                   ('Kolkata', 'Chennai', {'weight': 5}),
#                   ('Mumbai', 'Chennai', {'weight': 2}),
#                   ('Chennai', 'Jaipur', {'weight': 3}),
#                   ('Jaipur', 'Delhi', {'weight': 4})])

# # Calculate all-pairs shortest paths using Dijkstra's algorithm
# all_shortest_paths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))

# # Matplotlib setup
# pos = nx.spring_layout(G)  # Layout for better visualization
# fig, ax = plt.subplots()

# # Draw the graph
# nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# # Animation function
# def update(frame):
#     # Highlight the edges in the shortest path
#     path_edges = []
#     for i in range(len(G.nodes)):
#         if i < len(G.nodes) - 1:
#             current_node = list(G.nodes)[i]
#             next_node = list(G.nodes)[i + 1]
#             if all_shortest_paths[current_node][next_node] < float('inf'):
#                 path_edges.append((current_node, next_node))

#     # Draw the graph with highlighted edges
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)
#     nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(G.nodes), interval=1000, repeat=False)

# # Show the animation
# # plt.show()
# import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation

# # Create a graph with fake cities, places, and weights
# G = nx.Graph()
# G.add_nodes_from(['Delhi', 'CP', 'Lajpat Nagar', 'Kolkata', 'Mumbai', 'Chennai', 'Jaipur'])
# G.add_edges_from([('Delhi', 'CP', {'weight': 2}),
#                   ('Delhi', 'Lajpat Nagar', {'weight': 1}),
#                   ('CP', 'Kolkata', {'weight': 3}),
#                   ('Lajpat Nagar', 'Mumbai', {'weight': 4}),
#                   ('Kolkata', 'Chennai', {'weight': 5}),
#                   ('Mumbai', 'Chennai', {'weight': 2}),
#                   ('Chennai', 'Jaipur', {'weight': 3}),
#                   ('Jaipur', 'Delhi', {'weight': 4})])

# # Get the number of nodes
# num_nodes = len(G.nodes)

# # Create a matrix to store shortest paths between all pairs of nodes
# inf = float('inf')
# shortest_paths_matrix = np.full((num_nodes, num_nodes), inf)

# # Fill the matrix with initial weights
# for i, j, data in G.edges(data=True):
#     weight = data.get('weight', 1)  # Default weight is 1 if not specified
#     node_i = list(G.nodes).index(i)
#     node_j = list(G.nodes).index(j)
#     shortest_paths_matrix[node_i, node_j] = weight
#     shortest_paths_matrix[node_j, node_i] = weight

# # Apply Floyd-Warshall algorithm to compute all-pairs shortest paths
# for k in range(num_nodes):
#     for i in range(num_nodes):
#         for j in range(num_nodes):
#             if shortest_paths_matrix[i, k] + shortest_paths_matrix[k, j] < shortest_paths_matrix[i, j]:
#                 shortest_paths_matrix[i, j] = shortest_paths_matrix[i, k] + shortest_paths_matrix[k, j]

# # Matplotlib setup
# pos = nx.spring_layout(G)  # Layout for better visualization
# fig, ax = plt.subplots()

# # Draw the graph
# nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# # Animation function
# def update(frame):
#     # Highlight the edges in the shortest path
#     path_edges = []
#     for i in range(num_nodes):
#         for j in range(num_nodes):
#             if i < j and shortest_paths_matrix[i, j] < inf:
#                 path_edges.append((list(G.nodes)[i], list(G.nodes)[j]))

#     # Draw the graph with highlighted edges
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)
#     nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=1, interval=1000, repeat=False)

# # Show the animation
# plt.show()
# main_script.py
# import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation
# from pages.floydwarshall import floyd_warshall

# # Create a graph with fake cities, places, and weights
# G = nx.Graph()
# G.add_nodes_from(['Delhi', 'CP', 'Lajpat Nagar', 'Kolkata', 'Mumbai', 'Chennai', 'Jaipur'])
# G.add_edges_from([('Delhi', 'CP', {'weight': 2}),
#                   ('Delhi', 'Lajpat Nagar', {'weight': 1}),
#                   ('CP', 'Kolkata', {'weight': 3}),
#                   ('Lajpat Nagar', 'Mumbai', {'weight': 4}),
#                   ('Kolkata', 'Chennai', {'weight': 5}),
#                   ('Mumbai', 'Chennai', {'weight': 2}),
#                   ('Chennai', 'Jaipur', {'weight': 3}),
#                   ('Jaipur', 'Delhi', {'weight': 4})])

# # Apply Floyd-Warshall algorithm
# shortest_paths_matrix = floyd_warshall(G)

# # Matplotlib setup
# pos = nx.spring_layout(G)  # Layout for better visualization
# fig, ax = plt.subplots()

# # Draw the graph
# nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# # Animation function
# def update(frame):
#     # Highlight the edges in the shortest path
#     path_edges = []
#     for i in range(len(G.nodes)):
#         for j in range(len(G.nodes)):
#             if i < j and shortest_paths_matrix[i, j] < float('inf'):
#                 path_edges.append((list(G.nodes)[i], list(G.nodes)[j]))

#     # Draw the graph with highlighted edges
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)
#     nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=1, interval=1000, repeat=False)

# # Show the animation
# plt.show()
# main_script.py
# import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation
# from pages.floydwarshall import floyd_warshall

# # Create a graph with fake cities, places, and weights
# G = nx.Graph()
# G.add_nodes_from(['Delhi', 'CP', 'Lajpat Nagar', 'Kolkata', 'Mumbai', 'Chennai', 'Jaipur'])
# G.add_edges_from([('Delhi', 'CP', {'weight': 2}),
#                   ('Delhi', 'Lajpat Nagar', {'weight': 1}),
#                   ('CP', 'Kolkata', {'weight': 3}),
#                   ('Lajpat Nagar', 'Mumbai', {'weight': 4}),
#                   ('Kolkata', 'Chennai', {'weight': 5}),
#                   ('Mumbai', 'Chennai', {'weight': 2}),
#                   ('Chennai', 'Jaipur', {'weight': 3}),
#                   ('Jaipur', 'Delhi', {'weight': 4})])

# # Apply Floyd-Warshall algorithm
# shortest_paths_matrix = floyd_warshall(G)

# # Matplotlib setup
# pos = nx.spring_layout(G)  # Layout for better visualization
# fig, ax = plt.subplots()

# # Draw the graph
# nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# # Animation function
# def update(frame):
#     # Highlight the edges in the shortest path from 'Delhi' to 'Jaipur'
#     path_edges = []
#     delhi_index = list(G.nodes).index('Delhi')
#     jaipur_index = list(G.nodes).index('Jaipur')
#     if shortest_paths_matrix[delhi_index, jaipur_index] < float('inf'):
#         path_edges.append(('Delhi', 'Jaipur'))

#     # Draw the graph with highlighted edges
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)
#     nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=1, interval=1000, repeat=False)

# # Show the animation
# plt.show()
# main_script.py
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from pages.floydwarshall import floyd_warshall

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

# Apply Floyd-Warshall algorithm
shortest_paths_matrix = floyd_warshall(G)

# Matplotlib setup
pos = nx.spring_layout(G)  # Layout for better visualization
fig, ax = plt.subplots()

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# Animation function
def update(frame):
    # Highlight the edges in the shortest path from 'Hyderabad' to 'Jaipur'
    path_edges = []
    mumbai_index = list(G.nodes).index('Hyderbad')
    jaipur_index = list(G.nodes).index('CP')
    if shortest_paths_matrix[mumbai_index, jaipur_index] < float('inf'):
        path_edges.append(('Hyderabad', 'CP'))

    # Draw the graph with highlighted edges
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# Create an animation
ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_paths_matrix), interval=1000, repeat=False)

# Show the animation
plt.show()
