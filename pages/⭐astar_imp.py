# # import networkx as nx
# # import numpy as np
# # import matplotlib.pyplot as plt
# # from matplotlib.animation import FuncAnimation
# # import matplotlib.animation as animation
# # from pages.astar import astar  # Import the A* algorithm
# # import streamlit as st


# # st.title("Astar Graph")
# # # Create a graph with fake vertices, edges, and weights
# # G = nx.Graph()
# # G.add_nodes_from(['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Hyderabad', 'Jaipur', 'Ahmedabad', 'Pune', 'Lucknow'])
# # G.add_edges_from([('Delhi', 'Mumbai', {'weight': 2}),
# #                   ('Delhi', 'Kolkata', {'weight': 1}),
# #                   ('Mumbai', 'Chennai', {'weight': 3}),
# #                   ('Kolkata', 'Bangalore', {'weight': 4}),
# #                   ('Chennai', 'Bangalore', {'weight': 5}),
# #                   ('Hyderabad', 'Bangalore', {'weight': 2}),
# #                   ('Jaipur', 'Delhi', {'weight': 3}),
# #                   ('Ahmedabad', 'Mumbai', {'weight': 2}),
# #                   ('Pune', 'Mumbai', {'weight': 1}),
# #                   ('Lucknow', 'Delhi', {'weight': 2})])

# # # Matplotlib setup
# # pos = nx.spring_layout(G)  # Layout for better visualization
# # fig, ax = plt.subplots()

# # # Draw the graph
# # nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# # # Animation function
# # def update(frame):
# #     # Highlight the edges in the shortest path
# #     path_edges = []
# #     for i in range(frame):
# #         path_edges.append((shortest_path[i], shortest_path[i + 1]))

# #     # Draw the graph with highlighted edges
# #     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)
# #     nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# # # Choose the starting and ending nodes
# # start_node = 'Hyderabad'
# # end_node = 'Jaipur'

# # # Define a heuristic function (example: straight-line distance)
# # def heuristic(node, goal):
# #     return np.linalg.norm(np.array(pos[node]) - np.array(pos[goal]))

# # # Calculate the shortest path using A* algorithm
# # shortest_path_length = astar(G, start_node, end_node, heuristic=heuristic)
# # shortest_path = nx.shortest_path(G, source=start_node, target=end_node)

# # # Create an animation
# # ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_path), interval=1000, repeat=False)

# # # Show the animation
# # plt.show()
# import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation
# from pages.astar import astar  # Import the A* algorithm
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

# st.title("A* Algorithm Visualization")

# # Create a graph with fake vertices, edges, and weights
# G = nx.Graph()
# G.add_nodes_from(['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Hyderabad', 'Jaipur', 'Ahmedabad', 'Pune', 'Lucknow'])
# G.add_edges_from([('Delhi', 'Mumbai', {'weight': 2}),
#                   ('Delhi', 'Kolkata', {'weight': 1}),
#                   ('Mumbai', 'Chennai', {'weight': 3}),
#                   ('Kolkata', 'Bangalore', {'weight': 4}),
#                   ('Chennai', 'Bangalore', {'weight': 5}),
#                   ('Hyderabad', 'Bangalore', {'weight': 2}),
#                   ('Jaipur', 'Delhi', {'weight': 3}),
#                   ('Ahmedabad', 'Mumbai', {'weight': 2}),
#                   ('Pune', 'Mumbai', {'weight': 1}),
#                   ('Lucknow', 'Delhi', {'weight': 2})])

# # Matplotlib setup
# pos = nx.spring_layout(G)  # Layout for better visualization
# fig, ax = plt.subplots()

# # Draw the initial graph
# draw_graph(G, pos, ax)

# # User input for starting and ending nodes
# start_node = st.selectbox("Select starting node:", G.nodes)
# end_node = st.selectbox("Select ending node:", G.nodes)

# # Define a heuristic function (example: straight-line distance)
# def heuristic(node, goal):
#     return np.linalg.norm(np.array(pos[node]) - np.array(pos[goal]))

# # Calculate the shortest path using A* algorithm
# shortest_path_length = astar(G, start_node, end_node, heuristic=heuristic)
# shortest_path = nx.shortest_path(G, source=start_node, target=end_node)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_path), fargs=(G, pos, shortest_path, ax),
#                               interval=1000, repeat=False)

# # Display the animation in the Streamlit app
# st.pyplot(fig)
# import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation
# from pages.astar import astar  # Import the A* algorithm
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

# st.title("A* Algorithm Visualization")

# # Create a graph with fake vertices, edges, and weights
# G = nx.Graph()
# G.add_nodes_from(['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Hyderabad', 'Jaipur', 'Ahmedabad', 'Pune', 'Lucknow'])
# G.add_edges_from([('Delhi', 'Mumbai', {'weight': 2}),
#                   ('Delhi', 'Kolkata', {'weight': 1}),
#                   ('Mumbai', 'Chennai', {'weight': 3}),
#                   ('Kolkata', 'Bangalore', {'weight': 4}),
#                   ('Chennai', 'Bangalore', {'weight': 5}),
#                   ('Hyderabad', 'Bangalore', {'weight': 2}),
#                   ('Jaipur', 'Delhi', {'weight': 3}),
#                   ('Ahmedabad', 'Mumbai', {'weight': 2}),
#                   ('Pune', 'Mumbai', {'weight': 1}),
#                   ('Lucknow', 'Delhi', {'weight': 2})])

# # Matplotlib setup
# pos = nx.spring_layout(G)  # Layout for better visualization
# fig, ax = plt.subplots()

# # Draw the initial graph
# draw_graph(G, pos, ax)

# # User input for starting and ending nodes
# start_node = st.selectbox("Select starting node:", G.nodes)
# end_node = st.selectbox("Select ending node:", G.nodes)

# # Define a heuristic function (example: straight-line distance)
# def heuristic(node, goal):
#     return np.linalg.norm(np.array(pos[node]) - np.array(pos[goal]))

# # Calculate the shortest path using A* algorithm
# shortest_path_length = astar(G, start_node, end_node, heuristic=heuristic)
# shortest_path = nx.shortest_path(G, source=start_node, target=end_node)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_path), fargs=(G, pos, shortest_path, ax),
#                               interval=1000, repeat=False)

# # Display the animation in the Streamlit app
# st.pyplot(fig)
# import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation
# from astar import astar  # Import the A* algorithm
# import streamlit as st
# from io import BytesIO
# import base64

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

# st.title("A* Algorithm Visualization")

# # Create a graph with fake vertices, edges, and weights
# G = nx.Graph()
# G.add_nodes_from(['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Hyderabad', 'Jaipur', 'Ahmedabad', 'Pune', 'Lucknow'])
# G.add_edges_from([('Delhi', 'Mumbai', {'weight': 2}),
#                   ('Delhi', 'Kolkata', {'weight': 1}),
#                   ('Mumbai', 'Chennai', {'weight': 3}),
#                   ('Kolkata', 'Bangalore', {'weight': 4}),
#                   ('Chennai', 'Bangalore', {'weight': 5}),
#                   ('Hyderabad', 'Bangalore', {'weight': 2}),
#                   ('Jaipur', 'Delhi', {'weight': 3}),
#                   ('Ahmedabad', 'Mumbai', {'weight': 2}),
#                   ('Pune', 'Mumbai', {'weight': 1}),
#                   ('Lucknow', 'Delhi', {'weight': 2})])

# # Matplotlib setup
# pos = nx.spring_layout(G)  # Layout for better visualization
# fig, ax = plt.subplots()

# # Draw the initial graph
# draw_graph(G, pos, ax)

# # User input for starting and ending nodes
# start_node = st.selectbox("Select starting node:", G.nodes)
# end_node = st.selectbox("Select ending node:", G.nodes)

# # Define a heuristic function (example: straight-line distance)
# def heuristic(node, goal):
#     return np.linalg.norm(np.array(pos[node]) - np.array(pos[goal]))

# # Calculate the shortest path using A* algorithm
# shortest_path_length = astar(G, start_node, end_node, heuristic=heuristic)
# shortest_path = nx.shortest_path(G, source=start_node, target=end_node)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_path), fargs=(G, pos, shortest_path, ax),
#                               interval=1000, repeat=False)

# # Save the animation as a GIF
# # Save the animation as a GIF using PillowWriter
# gif_path = "C:/Users/sharm/OneDrive/Desktop/Delivery_Mania/astar_animation.gif"
# ani.save(gif_path, writer='pillow', fps=1)


# # Display the saved GIF using Streamlit
# st.image(gif_path, use_column_width=True)
# import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import streamlit as st
# from astar import astar  # Import the A* algorithm

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

# st.title("A* Algorithm Visualization")

# # Create a graph with fake vertices, edges, and weights
# G = nx.Graph()
# G.add_nodes_from(['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Hyderabad', 'Jaipur', 'Ahmedabad', 'Pune', 'Lucknow'])
# G.add_edges_from([('Delhi', 'Mumbai', {'weight': 2}),
#                   ('Delhi', 'Kolkata', {'weight': 1}),
#                   ('Mumbai', 'Chennai', {'weight': 3}),
#                   ('Kolkata', 'Bangalore', {'weight': 4}),
#                   ('Chennai', 'Bangalore', {'weight': 5}),
#                   ('Hyderabad', 'Bangalore', {'weight': 2}),
#                   ('Jaipur', 'Delhi', {'weight': 3}),
#                   ('Ahmedabad', 'Mumbai', {'weight': 2}),
#                   ('Pune', 'Mumbai', {'weight': 1}),
#                   ('Lucknow', 'Delhi', {'weight': 2})])

# # Matplotlib setup
# pos = nx.spring_layout(G)  # Layout for better visualization
# fig, ax = plt.subplots()

# # Draw the initial graph
# draw_graph(G, pos, ax)

# # User input for starting and ending nodes
# start_node = st.selectbox("Select starting node:", G.nodes)
# end_node = st.selectbox("Select ending node:", G.nodes)

# # Define a heuristic function (example: straight-line distance)
# def heuristic(node, goal):
#     return np.linalg.norm(np.array(pos[node]) - np.array(pos[goal]))

# # Calculate the shortest path using A* algorithm
# shortest_path_length = astar(G, start_node, end_node, heuristic=heuristic)
# shortest_path = nx.shortest_path(G, source=start_node, target=end_node)

# # Create an animation
# ani = FuncAnimation(fig=fig, func=update, frames=len(shortest_path), fargs=(G, pos, shortest_path, ax),
#                               interval=1000, repeat=True)

# # Display the animation in Streamlit
# st.pyplot(fig)
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from astar import astar  # Import the A* algorithm
import streamlit as st
import base64
import time


style = """
<style>
     @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
    .main{
        background: rgb(0,4,33);
        background: linear-gradient(164deg, rgba(0,4,33,1) 0%, rgba(11,0,134,1) 54%, rgba(5,220,255,1) 100%);
    }
    
    h1{
        font-family: "Poppins", sans-serif;
        font-weight: 700;
        font-style: normal;
        color: #ffffff;
    }
</style>
"""


st.markdown(style, unsafe_allow_html=True)

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

st.title("A* Algorithm Visualization")

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

# Draw the initial graph
draw_graph(G, pos, ax)

# User input for starting and ending nodes
start_node = st.selectbox("Select starting node:", G.nodes)
end_node = st.selectbox("Select ending node:", G.nodes)

# Define a heuristic function (example: straight-line distance)
def heuristic(node, goal):
    return np.linalg.norm(np.array(pos[node]) - np.array(pos[goal]))

# Calculate the shortest path using A* algorithm
# start_time = time.time()
# shortest_path_length = astar(G, start_node, end_node, heuristic=heuristic)
# end_time = time.time()

# execution_time = end_time - start_time
# st.write(f"Execution time: {execution_time:.10f} seconds")

# Define the number of iterations to run the algorithm

num_iterations = 10

# Initialize a list to store the execution times
execution_times = []

# Run the A* algorithm multiple times
for _ in range(num_iterations):
    start_time = time.time()
    shortest_path_length = astar(G, start_node, end_node, heuristic=heuristic)
    end_time = time.time()
    execution_time= end_time - start_time
    execution_times.append(execution_time)

# Calculate the average execution time
average_execution_time_astar = sum(execution_times) / num_iterations

st.write(f"Average execution time over {num_iterations} iterations: {average_execution_time_astar:.6f} seconds")


shortest_path = nx.shortest_path(G, source=start_node, target=end_node)

# Create an animation

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_path), fargs=(G, pos, shortest_path, ax),interval=1000, repeat=False)

# Save the animation as a GIF using imagemagick
gif_path = "astar_animation.gif"
ani.save(gif_path, writer="pillow", fps=1)

# Display the saved GIF using Streamlit
with open(gif_path, "rb") as file:
    gif_bytes = file.read()

st.image(gif_bytes, use_column_width=True)
