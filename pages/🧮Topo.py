# import streamlit as st
# import networkx as nx
# import matplotlib.pyplot as plt
# from Topologicalsort import topological_sort
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation

# def draw_graph(G, pos, ax):
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# def topological_sort(graph):
#     """
#     Perform topological sorting on a directed acyclic graph (DAG).
    
#     Parameters:
#     - graph: Dictionary representing the graph. Keys are nodes, and values are lists of adjacent nodes.
    
#     Returns:
#     - List containing a topological ordering of the nodes.
#     """
#     # Initialize variables
#     in_degree = {node: 0 for node in graph}
#     for node in graph:
#         for neighbor in graph[node]:
#             in_degree[neighbor] += 1

#     # Perform topological sorting using Kahn's algorithm
#     queue = [node for node in graph if in_degree[node] == 0]
#     topological_order = []
#     while queue:
#         current_node = queue.pop(0)
#         topological_order.append(current_node)
#         for neighbor in graph[current_node]:
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)

#     # Check if the graph is acyclic
#     if len(topological_order) != len(graph):
#         raise ValueError("Graph contains cycles and cannot be topologically sorted.")

#     return topological_order

# def draw_graph(G, pos, ax):
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# def update(frame):
#     ax.clear()
#     sorted_nodes = topological_order[:frame+1]
#     subgraph = G.subgraph(sorted_nodes)
#     draw_graph(subgraph, pos, ax)

# def main():
#     st.title("Topological Sort Visualization")

#     # Create a graph with fake nodes and edges
#     G = nx.DiGraph()
#     G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
#     G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')])

#     # Matplotlib setup
#     pos = nx.spring_layout(G)  # Layout for better visualization
#     fig, ax = plt.subplots()

#     # Draw the initial graph
#     draw_graph(G, pos, ax)

#     # Perform topological sorting
#     try:
#         global topological_order
#         topological_order = topological_sort({'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['E'], 'E': []})
#         st.write("Topological order:", topological_order)
#     except ValueError as e:
#         st.error(str(e))

#     # Create an animation
#     ani = animation.FuncAnimation(fig=fig, func=update, frames=len(topological_order), interval=1000, repeat=False)

#     # Display the animation
#     st.pyplot(fig)
#     st.write("Animating topological sorting...")

# if __name__ == "__main__":
#     main()


# import streamlit as st
# import networkx as nx
# import matplotlib.pyplot as plt
# from Topologicalsort import topological_sort
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation

# def topological_sort(graph):
#     """
#     Perform topological sorting on a directed acyclic graph (DAG).
    
#     Parameters:
#     - graph: Dictionary representing the graph. Keys are nodes, and values are lists of adjacent nodes.
    
#     Returns:
#     - List containing a topological ordering of the nodes.
#     """
#     # Initialize variables
#     in_degree = {node: 0 for node in graph}
#     for node in graph:
#         for neighbor in graph[node]:
#             in_degree[neighbor] += 1

#     # Perform topological sorting using Kahn's algorithm
#     queue = [node for node in graph if in_degree[node] == 0]
#     topological_order = []
#     while queue:
#         current_node = queue.pop(0)
#         topological_order.append(current_node)
#         for neighbor in graph[current_node]:
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)

#     # Check if the graph is acyclic
#     if len(topological_order) != len(graph):
#         raise ValueError("Graph contains cycles and cannot be topologically sorted.")

#     return topological_order

# def draw_graph(G, pos, ax):
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

# def update(frame, G, pos, ax, start_frame, end_frame):
#     ax.clear()
#     sorted_nodes = topological_order[start_frame:end_frame+1]
#     subgraph = G.subgraph(sorted_nodes)
#     draw_graph(subgraph, pos, ax)

# def main():
#     st.title("Topological Sort Visualization")

#     # Create a graph with fake nodes and edges
#     graph_data = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['E'], 'E': []}
#     G = nx.DiGraph(graph_data)

#     # Matplotlib setup
#     pos = nx.spring_layout(G)  # Layout for better visualization
#     fig, ax = plt.subplots()

#     # Draw the initial graph
#     draw_graph(G, pos, ax)

#     # Perform topological sorting
#     try:
#         global topological_order
#         topological_order = topological_sort(graph_data)
#         st.write("Topological order:", topological_order)
#     except ValueError as e:
#         st.error(str(e))

#     # User input for starting and ending frames
#     start_frame = st.slider("Starting Frame", 0, len(topological_order) - 1, 0)
#     end_frame = st.slider("Ending Frame", start_frame, len(topological_order) - 1, len(topological_order) - 1)

#     # Create an animation
#     ani = animation.FuncAnimation(fig=fig, func=update, frames=1, fargs=(G, pos, ax, start_frame, end_frame), interval=1000, repeat=False)

#     # Display the animation
#     st.pyplot(fig)
#     st.write("Animating topological sorting...")

# if __name__ == "__main__":
#     main()
# import streamlit as st
# import networkx as nx
# import matplotlib.pyplot as plt
# from Topologicalsort import topological_sort
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation

# style = """
# <style>
#      @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
#     .main{
#         background: rgb(249,0,93);
#         background: linear-gradient(164deg, rgba(249,0,93,1) 0%, rgba(255,0,164,1) 51%, rgba(242,0,50,1) 100%);
#     }
    
#     h1{
#         font-family: "Poppins", sans-serif;
#         font-weight: 700;
#         font-style: normal;
#         color: #ffffff;
#     }
# </style>
# """


# st.markdown(style, unsafe_allow_html=True)


# def topological_sort(graph):
#     """
#     Perform topological sorting on a directed acyclic graph (DAG).
    
#     Parameters:
#     - graph: Dictionary representing the graph. Keys are nodes, and values are lists of adjacent nodes.
    
#     Returns:
#     - List containing a topological ordering of the nodes.
#     """
#     # Initialize variables
#     in_degree = {node: 0 for node in graph}
#     for node in graph:
#         for neighbor in graph[node]:
#             in_degree[neighbor] += 1

#     # Perform topological sorting using Kahn's algorithm
#     queue = [node for node in graph if in_degree[node] == 0]
#     topological_order = []
#     while queue:
#         current_node = queue.pop(0)
#         topological_order.append(current_node)
#         for neighbor in graph[current_node]:
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)

#     # Check if the graph is acyclic
#     if len(topological_order) != len(graph):
#         raise ValueError("Graph contains cycles and cannot be topologically sorted.")

#     return topological_order

# def draw_graph(G, pos, ax, start_node, end_node):
#     try:
#         shortest_path = nx.shortest_path(G, source=start_node, target=end_node)
#         path_exists = True
#     except nx.NetworkXNoPath:
#         st.error(f"No path exists between {start_node} and {end_node}.")
#         path_exists = False
        
#     if path_exists:
#         nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

#         # Highlight the shortest path from start_node to end_node with a red trace
#         shortest_path = nx.shortest_path(G, source=start_node, target=end_node)
#         nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)], edge_color='r', width=2, ax=ax)

# def update(frame):
#     ax.clear()
#     sorted_nodes = topological_order[:frame+1]
#     subgraph = G.subgraph(sorted_nodes)
#     draw_graph(subgraph, pos, ax, start_node, end_node)

# def main():
#     st.title("Topological Sort Visualization")

#     # Create a graph with fake nodes and edges
#     graph_data = {
#     'Ahmedabad': ['Baroda', 'Chennai'],
#     'Baroda': ['Delhi'],
#     'Chennai': ['Delhi'],
#     'Delhi': ['England'],
#     'England': []
#     }
#     G = nx.DiGraph(graph_data)

#     # Matplotlib setup
#     global pos, ax, start_node, end_node
#     pos = nx.spring_layout(G)  # Layout for better visualization
#     fig, ax = plt.subplots()

#     # Draw the initial graph
#     start_node = st.selectbox("Enter starting node:", graph_data)
#     end_node = st.selectbox("Enter ending node:", graph_data)

#     # Draw the initial graph with specified starting and ending nodes
#     draw_graph(G, pos, ax, start_node, end_node)

#     # Perform topological sorting
#     try:
#         global topological_order
#         topological_order = topological_sort(graph_data)
#         #st.write("Topological order:", topological_order)
#     except ValueError as e:
#         st.write("Soory, You cannot traverse this path")

#     # Create an animation
#     ani = animation.FuncAnimation(fig=fig, func=update, frames=len(topological_order), interval=1000, repeat=False)

#     # Display the animation
#     st.pyplot(fig)
#     st.write("Animating topological sorting...")

# if __name__ == "__main__":
#     main()

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from Topologicalsort import topological_sort
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import time

style = """
<style>
     @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
    .main{
        background: rgb(249,0,93);
        background: linear-gradient(164deg, rgba(249,0,93,1) 0%, rgba(255,0,164,1) 51%, rgba(242,0,50,1) 100%);
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


def topological_sort(graph):
    """
    Perform topological sorting on a directed acyclic graph (DAG).
    
    Parameters:
    - graph: Dictionary representing the graph. Keys are nodes, and values are lists of adjacent nodes.
    
    Returns:
    - List containing a topological ordering of the nodes.
    """
    # Initialize variables
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Perform topological sorting using Kahn's algorithm
    queue = [node for node in graph if in_degree[node] == 0]
    topological_order = []
    while queue:
        current_node = queue.pop(0)
        topological_order.append(current_node)
        for neighbor in graph[current_node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if the graph is acyclic
    if len(topological_order) != len(graph):
        raise ValueError("Graph contains cycles and cannot be topologically sorted.")

    return topological_order

def draw_graph(G, pos, ax, start_node, end_node):
    try:
        shortest_path = nx.shortest_path(G, source=start_node, target=end_node)
        path_exists = True
    except nx.NetworkXNoPath:
        st.error(f"No path exists between {start_node} and {end_node}.")
        path_exists = False
        
    if path_exists:
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, ax=ax)

        # Highlight the shortest path from start_node to end_node with a red trace
        shortest_path = nx.shortest_path(G, source=start_node, target=end_node)
        nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)], edge_color='r', width=2, ax=ax)

def update(frame):
    ax.clear()
    sorted_nodes = topological_order[:frame+1]
    subgraph = G.subgraph(sorted_nodes)
    draw_graph(subgraph, pos, ax, start_node, end_node)

def main():
    st.title("Topological Sort Visualization")

    # Create a graph with fake nodes and edges
    graph_data = {
    'Ahmedabad': ['Baroda', 'Chennai'],
    'Baroda': ['Delhi'],
    'Chennai': ['Delhi'],
    'Delhi': ['England'],
    'England': []
    }
    G = nx.DiGraph(graph_data)

    # Matplotlib setup
    global pos, ax, start_node, end_node
    pos = nx.spring_layout(G)  # Layout for better visualization
    fig, ax = plt.subplots()

    # Draw the initial graph
    start_node = st.selectbox("Enter starting node:", graph_data)
    end_node = st.selectbox("Enter ending node:", graph_data)

    # Draw the initial graph with specified starting and ending nodes
    draw_graph(G, pos, ax, start_node, end_node)

    # Perform topological sorting and measure execution time
    try:
        global topological_order
        num_iterations = 100

        # Initialize a list to store the execution times
        execution_times = []

        # Run the A* algorithm multiple times
        for _ in range(num_iterations):
            start_time = time.time()
            topological_order = topological_sort(graph_data)
            end_time = time.time()
            execution_time_of_Tsort = end_time - start_time
            execution_times.append(execution_time_of_Tsort)

        # Calculate the average execution time
        average_execution_time_tp = sum(execution_times) / num_iterations

        st.write(f"Average execution time over {num_iterations} iterations: {average_execution_time_tp:.6f} seconds")
    except ValueError as e:
        st.write("Sorry, you cannot traverse this path")

    # Create an animation
    ani = animation.FuncAnimation(fig=fig, func=update, frames=len(topological_order), interval=1000, repeat=False)

    # Display the animation
    st.pyplot(fig)
    st.write("Animating topological sorting...")

if __name__ == "__main__":
    main()

