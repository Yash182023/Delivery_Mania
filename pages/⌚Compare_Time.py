import streamlit as st
import plotly.graph_objects as go

style = """
<style>
     @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
    .main{
        background: rgb(61,88,4);
        background: linear-gradient(164deg, rgba(61,88,4,1) 0%, rgba(0,242,24,1) 100%);
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

st.title("Time taken by all Algorithms")

algorithms = ["A*", "Floyd-Warshall", "Dijkstra", "Topological Sort"]

# Average execution times (in seconds)
execution_times = [0.000020, 0.000542, 0.000042, 0.000000]

# Create a Plotly bar chart
fig = go.Figure(data=[go.Bar(x=algorithms, y=execution_times)])

# Customize the layout
fig.update_layout(
    title="Average Execution Times of Algorithms",
    xaxis_title="Algorithm",
    yaxis_title="Average Execution Time (seconds)"
)

fig_1 = go.Figure(data=go.Scatter(x=algorithms, y=execution_times, mode='lines+markers'))

# Customize the layout
fig_1.update_layout(
    title="Average Execution Times of Algorithms",
    xaxis_title="Algorithm",
    yaxis_title="Average Execution Time (seconds)"
)
# Show the plot on Streamlit
st.plotly_chart(fig, use_container_width=True)
st.plotly_chart(fig_1, use_container_width=True)