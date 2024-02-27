# dijkstra.py
import networkx as nx

def dijkstra(graph, start_node, end_node):
    # Implementation of Dijkstra's algorithm
    distances = {node: float('infinity') for node in graph.nodes}
    previous_nodes = {node: None for node in graph.nodes}
    distances[start_node] = 0

    nodes = list(graph.nodes)
    while nodes:
        current_node = min(nodes, key=lambda node: distances[node])
        nodes.remove(current_node)
        if distances[current_node] == float('infinity'):
            break

        for neighbor, weight in graph[current_node].items():
            potential_route = distances[current_node] + weight.get('weight', 1)
            if potential_route < distances[neighbor]:
                distances[neighbor] = potential_route
                previous_nodes[neighbor] = current_node

    shortest_path = []
    current_node = end_node
    while previous_nodes[current_node] is not None:
        shortest_path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    shortest_path.insert(0, start_node)

    return shortest_path
