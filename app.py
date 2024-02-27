import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

# Define six vertices and their coordinates
vertices = {'A': (0, 0), 'B': (1, 1), 'C': (2, 0), 'D': (4, 0), 'E': (3, 2), 'F': (5, 1)}

# Define edges with weights
edges = [('A', 'B', 1), ('A', 'C', 2), ('B', 'C', 1), ('B', 'E', 3),
         ('C', 'D', 2), ('C', 'E', 2), ('D', 'F', 1), ('E', 'F', 2)]

# Create a graph and add edges with weights
G = nx.Graph()
G.add_weighted_edges_from(edges)

# Find the shortest path using Dijkstra's algorithm
shortest_path = nx.shortest_path(G, source='A', target='F', weight='weight')

# Plot the graph
pos = {vertex: coordinates for vertex, coordinates in vertices.items()}
labels = {(i, j): G[i][j]['weight'] for i, j in G.edges()}
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='red', node_size=700)

# Display the plot using Streamlit
st.title("Graph with Shortest Path")
st.pyplot()
