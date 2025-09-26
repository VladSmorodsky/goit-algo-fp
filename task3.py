import heapq
from typing import List, Tuple, Hashable, Dict
from math import inf

Graph = Dict[Hashable, List[Tuple[Hashable, int]]]


def dijkstra(graph: Graph, start: Hashable) -> tuple[Dict[Hashable, int]]:
    """
    Implements Dijkstra's algorithm to find the shortest path from a starting node to all other nodes in a weighted graph.

    Args:
        graph (Graph): A dictionary representing the graph where keys are node identifiers and values are lists of tuples (neighbor, weight).
        start (Hashable): The starting node identifier.
    Returns:
        Tuple[Dict[Hashable, int], Dict[Hashable, Hashable]]: A tuple containing two dictionaries:
            - distances: A dictionary mapping each node to its shortest distance from the start node.
            - parent: A dictionary mapping each node to its predecessor in the shortest path.
    """
    distances = {vertex: inf for vertex in graph}
    parent = {u: None for u in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        weight, vertex = heapq.heappop(heap)
        if weight != distances[vertex]:
            continue
        for v, v_weight in graph.get(vertex, []):
            new_distance = weight + v_weight
            if new_distance < distances[v]:
                distances[v] = new_distance
                parent[v] = vertex
                heapq.heappush(heap, (new_distance, v))
    return distances, parent


def get_optimal_path(parent: Dict, target) -> List:
    """
    Reconstructs the shortest path from the start node to the target node using the parent dictionary.
    Args:
        parent (Dict): A dictionary mapping each node to its predecessor in the shortest path.
        target: The target node identifier.
    Returns:
        List: A list of nodes representing the shortest path from the start node to the target node.
    """
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    return list(reversed(path))


graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'D': [('F', 11)],
    'E': [('D', 4)],
    'F': [],
}

if __name__ == "__main__":
    distances, parent = dijkstra(graph, 'A')
    print(distances)
    print(get_optimal_path(parent, 'D'))
