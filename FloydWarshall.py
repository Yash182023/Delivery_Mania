# floydwarshall.py
import numpy as np

def floyd_warshall(graph):
    num_nodes = len(graph.nodes)
    inf = float('inf')
    shortest_paths_matrix = np.full((num_nodes, num_nodes), inf)

    for i, j, data in graph.edges(data=True):
        weight = data.get('weight', 1)  # Default weight is 1 if not specified
        node_i = list(graph.nodes).index(i)
        node_j = list(graph.nodes).index(j)
        shortest_paths_matrix[node_i, node_j] = weight
        shortest_paths_matrix[node_j, node_i] = weight

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if shortest_paths_matrix[i, k] + shortest_paths_matrix[k, j] < shortest_paths_matrix[i, j]:
                    shortest_paths_matrix[i, j] = shortest_paths_matrix[i, k] + shortest_paths_matrix[k, j]

    return shortest_paths_matrix
