import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from io import BytesIO
import base64

# Streamlit setup
st.title("Animated Plot in Streamlit")

# Matplotlib setup
fig, ax = plt.subplots()
t = np.linspace(0, 3, 40)
g = -9.81
v0 = 12
z = g * t**2 / 2 + v0 * t

scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()

# Animation function
def update(frame):
    x = t[:frame]
    y = z[:frame]
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    return (scat,)

# Create an animation
ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=30, repeat=False)

# Save the animation as a GIF locally
gif_path = "animated_plot.gif"
ani.save(gif_path, writer='imagemagick', fps=30)

# Display the saved GIF using Streamlit
st.image(gif_path, use_column_width=True)
