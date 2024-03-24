# bellmanford.py
import networkx as nx

import networkx as nx

def bellman_ford(graph, start_node, end_node=None):
    # Get the number of nodes in the graph
    num_nodes = len(graph.nodes)

    # Initialize distances and predecessors
    distances = {node: float('inf') for node in graph.nodes}
    predecessors = {node: None for node in graph.nodes}
    distances[start_node] = 0

    # Relax edges repeatedly
    for _ in range(num_nodes - 1):
        for edge in graph.edges(data=True):
            source, target, data = edge
            weight = data.get('weight', 1)  # Default weight is 1 if not specified
            if distances[source] + weight < distances[target]:
                distances[target] = distances[source] + weight
                predecessors[target] = source

    # Check for negative cycles
    for edge in graph.edges(data=True):
        source, target, data = edge
        weight = data.get('weight', 1)  # Default weight is 1 if not specified
        if distances[source] + weight < distances[target]:
            raise ValueError("Graph contains a negative cycle")

    # Reconstruct the shortest paths
    shortest_paths = {node: nx.shortest_path(graph, source=start_node, target=node) for node in graph.nodes}
    
    # If end_node is specified, return the shortest path from start_node to end_node
    if end_node is not None:
        shortest_path_start_to_end = nx.shortest_path(graph, source=start_node, target=end_node)
        return shortest_path_start_to_end

    return shortest_paths
