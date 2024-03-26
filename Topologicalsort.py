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
