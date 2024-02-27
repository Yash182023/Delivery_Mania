# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation

# # Streamlit setup
# st.title("Animated Plot in Streamlit")

# # Matplotlib setup
# fig, ax = plt.subplots()
# t = np.linspace(0, 3, 40)
# g = -9.81
# v0 = 12
# z = g * t**2 / 2 + v0 * t

# scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
# ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
# ax.legend()

# # Animation function
# def update(frame):
#     x = t[:frame]
#     y = z[:frame]
#     data = np.stack([x, y]).T
#     scat.set_offsets(data)
#     return (scat,)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=30, repeat=False)

# # Display the animation using Streamlit with a player
# player = st.empty()  # Placeholder to add player

# # Function to update animation based on slider value
# def update_plot(frame):
#     update(frame)
#     player.show(fig)

# # Streamlit slider for controlling the frame
# frame_slider = st.slider("Frame", min_value=0, max_value=len(t) - 1, value=0, step=1, key="frame_slider")
# update_plot(frame_slider)
# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation
# from io import BytesIO
# import base64

# # Streamlit setup
# st.title("Animated Plot in Streamlit")

# # Matplotlib setup
# fig, ax = plt.subplots()
# t = np.linspace(0, 3, 40)
# g = -9.81
# v0 = 12
# z = g * t**2 / 2 + v0 * t

# scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
# ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
# ax.legend()

# # Animation function
# def update(frame):
#     x = t[:frame]
#     y = z[:frame]
#     data = np.stack([x, y]).T
#     scat.set_offsets(data)
#     return (scat,)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=30, repeat=False)

# # Convert animation frames to base64 encoding
# ani_base64 = base64.b64encode(ani.to_jshtml()).decode('utf-8')

# # Display the animation using Streamlit
# st.markdown(f'<img src="data:image/gif;base64,{ani_base64}" alt="animated_plot">', unsafe_allow_html=True)


# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation

# # Streamlit setup
# st.title("Animated Plot in Streamlit")

# # Matplotlib setup
# fig, ax = plt.subplots()
# t = np.linspace(0, 3, 40)
# g = -9.81
# v0 = 12
# z = g * t**2 / 2 + v0 * t

# scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
# ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
# ax.legend()

# # Animation function
# def update(frame):
#     x = t[:frame]
#     y = z[:frame]
#     data = np.stack([x, y]).T
#     scat.set_offsets(data)
#     return (scat,)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=30, repeat=False)

# # Display the animation using Streamlit with a player
# player = st.empty()  # Placeholder to add player

# # Function to update animation based on slider value
# def update_plot(frame):
#     update(frame)
#     player.pyplot(fig)

# # Streamlit slider for controlling the frame
# frame_slider = st.slider("Frame", min_value=0, max_value=len(t) - 1, value=0, step=1, key="frame_slider")
# update_plot(frame_slider)
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation

# # Matplotlib setup
# fig, ax = plt.subplots()
# t = np.linspace(0, 3, 40)
# g = -9.81
# v0 = 12
# z = g * t**2 / 2 + v0 * t

# scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
# ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
# ax.legend()

# # Animation function
# def update(frame):
#     x = t[:frame]
#     y = z[:frame]
#     data = np.stack([x, y]).T
#     scat.set_offsets(data)
#     return (scat,)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=30, repeat=False)

# # Display the animation using Matplotlib with a slider
# fig, ax_slider = plt.subplots()
# ax_slider.set(xlim=[0, len(t) - 1], ylim=[0, 1])
# slider = plt.Slider(ax_slider, "Frame", valmin=0, valmax=len(t) - 1, valinit=0, valstep=1)

# # Function to update animation based on slider value
# def update_plot(val):
#     update(int(val))
#     fig.canvas.draw_idle()

# # Connect the slider to the update function
# slider.on_changed(update_plot)

# # Show the animation
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation

# # Matplotlib setup
# fig, ax = plt.subplots()
# t = np.linspace(0, 3, 40)
# g = -9.81
# v0 = 12
# z = g * t**2 / 2 + v0 * t

# scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
# ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
# ax.legend()

# # Animation function
# def update(frame):
#     x = t[:frame]
#     y = z[:frame]
#     data = np.stack([x, y]).T
#     scat.set_offsets(data)
#     return (scat,)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=30, repeat=False)

# # Show the animation
# plt.show()
# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation

# # Create a graph with fake vertices, edges, and weights
# G = nx.Graph()
# G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
# G.add_edges_from([('A', 'B', {'weight': 2}),
#                   ('A', 'C', {'weight': 1}),
#                   ('B', 'D', {'weight': 3}),
#                   ('C', 'E', {'weight': 4}),
#                   ('D', 'F', {'weight': 5}),
#                   ('E', 'F', {'weight': 2})])

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

# # Shortest path calculation
# start_node = 'A'
# end_node = 'F'
# shortest_path = nx.shortest_path(G, source=start_node, target=end_node)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_path) , interval=1000, repeat=False)

# # Show the animation
# plt.show()
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

# # Shortest path calculation
# start_node = 'Delhi'
# end_node = 'Chennai'
# shortest_path = nx.shortest_path(G, source=start_node, target=end_node)

# # Create an animation
# ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_path), interval=1000, repeat=False)

# # Show the animation
# plt.show()
# main_script.py
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from pages.Dijkstra import dijkstra  # Import the dijkstra function

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

# Shortest path calculation using Dijkstra's algorithm
start_node = 'Delhi'
end_node = 'Chennai'
shortest_path = dijkstra(G, start_node, end_node)

# Create an animation
ani = animation.FuncAnimation(fig=fig, func=update, frames=len(shortest_path), interval=1000, repeat=False)

# Show the animation
plt.show()
