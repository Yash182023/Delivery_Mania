# import streamlit as st
# import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation
# from floydwarshall import floyd_warshall

# # Create a graph with fake cities, places, and weights
# G = nx.Graph()
# G.add_nodes_from(['Delhi', 'CP', 'Lajpat Nagar', 'Kolkata', 'Mumbai', 'Chennai', 'Jaipur', 'Hyderabad'])
# G.add_edges_from([('Delhi', 'CP', {'weight': 2}),
#                   ('Delhi', 'Lajpat Nagar', {'weight': 1}),
#                   ('CP', 'Kolkata', {'weight': 3}),
#                   ('Lajpat Nagar', 'Mumbai', {'weight': 4}),
#                   ('Kolkata', 'Chennai', {'weight': 5}),
#                   ('Mumbai', 'Chennai', {'weight': 2}),
#                   ('Chennai', 'Jaipur', {'weight': 3}),
#                   ('Jaipur', 'Delhi', {'weight': 4}),
#                   ('Hyderabad', 'Jaipur', {'weight': 6})])

# # Apply Floyd-Warshall algorithm
# shortest_paths_matrix = floyd_warshall(G)

# # Matplotlib setup
# pos = nx.spring_layout(G)  # Layout for better visualization
# fig, ax = plt.subplots()

# # Animation function
# def update(frame):
#     ax.clear()
#     # Draw the graph
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)
#     # Highlight the edges in the shortest path from 'Hyderabad' to 'Jaipur'
#     path_edges = []
#     start_node = st.selectbox("Select starting node:", G.nodes)
#     end_node = st.selectbox("Select ending node:", G.nodes)
#     if shortest_paths_matrix[start_node][end_node] < float('inf'):
#         path = nx.shortest_path(G, source=start_node, target=end_node)
#         path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
#     nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=1, interval=1000, repeat=False)


# gif_path = "Floyd_animation.gif"
# ani.save(gif_path, writer="pillow", fps=1)

# # Display the saved GIF using Streamlit
# with open(gif_path, "rb") as file:
#     gif_bytes = file.read()

# st.image(gif_bytes, use_column_width=True)

import streamlit as st
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from floydwarshall import floyd_warshall

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

# Animation function
def update(frame):
    ax.clear()
    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)
    # Highlight the edges in the shortest path from 'Hyderabad' to 'Jaipur'
    path_edges = []
    start_node = st.selectbox("Select starting node:", list(range(len(G.nodes))))
    end_node = st.selectbox("Select ending node:", list(range(len(G.nodes))))
    if shortest_paths_matrix[start_node][end_node] < float('inf'):
        path = nx.shortest_path(G, source=list(G.nodes)[start_node], target=list(G.nodes)[end_node])
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# Create an animation
ani = animation.FuncAnimation(fig=fig, func=update, frames=1, interval=1000, repeat=False)

# Display the animation frame by frame
for i in range(len(shortest_paths_matrix)):
    update(i)
    st.pyplot(fig)
