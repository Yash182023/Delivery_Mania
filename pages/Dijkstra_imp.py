# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation
# from pages.Dijkstra import dijkstra  # Import the dijkstra function

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

# # Matplotlib setup
# pos = nx.spring_layout(G)  # Layout for better visualization
# fig, ax = plt.subplots()

# # Draw the graph
# nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# # Animation function
# def update(frame):
#     # Highlight the edges in the shortest path
#     path_edges = []
#     for i in range(frame):
#         path_edges.append((shortest_path[i], shortest_path[i + 1]))

#     # Draw the graph with highlighted edges
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)
#     nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# # Shortest path calculation using Dijkstra's algorithm
# start_node = 'Delhi'
# end_node = 'Chennai'
# shortest_path = dijkstra(G, start_node, end_node)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_path), interval=1000, repeat=False)

# # Show the animation
# # plt.show()
# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation
# from pages.Dijkstra import dijkstra  # Import the dijkstra function
# import streamlit as st

# def draw_graph(G, pos, ax):
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# def update(frame, G, pos, shortest_path, ax):
#     # Highlight the edges in the shortest path
#     path_edges = []
#     for i in range(frame):
#         path_edges.append((shortest_path[i], shortest_path[i + 1]))

#     # Draw the graph with highlighted edges
#     draw_graph(G, pos, ax)
#     nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# st.title("Dijkstra's Algorithm Visualization")

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

# # Matplotlib setup
# pos = nx.spring_layout(G)  # Layout for better visualization
# fig, ax = plt.subplots()

# # Draw the initial graph
# draw_graph(G, pos, ax)

# # User input for starting and ending nodes
# start_node = st.selectbox("Select starting node:", G.nodes)
# end_node = st.selectbox("Select ending node:", G.nodes)

# # Calculate the shortest path using Dijkstra's algorithm
# shortest_path = dijkstra(G, start_node, end_node)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_path), fargs=(G, pos, shortest_path, ax),
#                               interval=1000, repeat=False)

# # Display the animation in the Streamlit app
# # st.pyplot(fig)
# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation
# from pages.Dijkstra import dijkstra  # Import the dijkstra function
# import streamlit as st

# def draw_graph(G, pos, ax):
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# def update(frame, G, pos, shortest_path, ax):
#     # Highlight the edges in the shortest path
#     path_edges = []
#     for i in range(frame):
#         path_edges.append((shortest_path[i], shortest_path[i + 1]))

#     # Draw the graph with highlighted edges
#     draw_graph(G, pos, ax)
#     nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

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

# # Matplotlib setup
# pos = nx.spring_layout(G)  # Layout for better visualization
# fig, ax = plt.subplots()

# # Draw the initial graph
# draw_graph(G, pos, ax)

# # User input for starting and ending nodes
# start_node = 'Delhi'
# end_node = 'Jaipur'

# # Calculate the shortest path using Dijkstra's algorithm
# shortest_path = dijkstra(G, start_node, end_node)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_path), fargs=(G, pos, shortest_path, ax),
#                               interval=1000, repeat=False)

# gif_path = "dijkstra_animation.gif"
# ani.save(gif_path, writer='pillow', fps=1)


# # Display the saved GIF using Streamlit
# st.image(gif_path, use_column_width=True)

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from dijkstra import dijkstra  # Import the dijkstra function
import streamlit as st

def draw_graph(G, pos, ax):
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

def update(frame, G, pos, shortest_path, ax):
    # Highlight the edges in the shortest path
    path_edges = []
    for i in range(frame):
        path_edges.append((shortest_path[i], shortest_path[i + 1]))

    # Draw the graph with highlighted edges
    draw_graph(G, pos, ax)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# Create a graph with fake cities, places, and weights
G = nx.Graph()
G.add_nodes_from(['Delhi', 'CP', 'Lajpat Nagar', 'Kolkata', 'Mumbai', 'Chennai', 'Jaipur'])
G.add_edges_from([('Delhi', 'CP', {'weight': 2}),
                  ('Delhi', 'Lajpat Nagar', {'weight': 1}),
                  ('CP', 'Kolkata', {'weight': 3}),
                  ('Lajpat Nagar', 'Mumbai', {'weight': 4}),
                  ('Kolkata', 'Chennai', {'weight': 5}),
                  ('Mumbai', 'Chennai', {'weight': 2}),
                  ('Chennai', 'Jaipur', {'weight': 3}),
                  ('Jaipur', 'Delhi', {'weight': 4})])

# Matplotlib setup
pos = nx.spring_layout(G)  # Layout for better visualization
fig, ax = plt.subplots()

# Draw the initial graph
draw_graph(G, pos, ax)

# User input for starting and ending nodes
start_node = st.selectbox("Select starting node:", G.nodes)
end_node = st.selectbox("Select ending node:", G.nodes)

# Calculate the shortest path using Dijkstra's algorithm
shortest_path = dijkstra(G, start_node, end_node)

# Create an animation
ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_path), fargs=(G, pos, shortest_path, ax),
                              interval=1000, repeat=False)

# Save the animation as a GIF
gif_path = "dijkstra_animation.gif"
ani.save(gif_path, writer='pillow', fps=1)

# Display the saved GIF using Streamlit
st.image(gif_path, use_column_width=True)
