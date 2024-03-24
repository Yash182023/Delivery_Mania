import heapq
import networkx as nx

def astar(graph, start, end, heuristic=None):
    if heuristic is None:
        raise ValueError("Heuristic function must be provided for A* algorithm")

    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            return current_cost

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                priority = current_cost + weight['weight'] + heuristic(neighbor, end)
                heapq.heappush(priority_queue, (priority, neighbor))

    return float('inf')
