from task4 import Node, draw_tree, build_heap_tree
from collections import deque


def change_hex_color(hex_color: str, factor: float = 0.1) -> str:
    """
    Change hex color brightness by a given factor.
    Args:
        hex_color (str): The original hex color (e.g., "#RRGGBB").
        factor (float): The factor to adjust brightness (0.0 to 1.0).
    Returns:
        str: The adjusted hex color.
    """
    hex_color = hex_color.lstrip('#')
    r, g, b = (int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r = int(r + (255 - r) * factor)
    g = int(g + (255 - g) * factor)
    b = int(b + (255 - b) * factor)
    return f"#{r:02X}{g:02X}{b:02X}"


def dfs(start_vertex: Node):
    """
    Depth-First Search (DFS) algorithm to traverse the binary tree.
    Args:
        start_vertex (Node): The starting node for DFS traversal.
    """
    visited = set()
    stack = [start_vertex]
    color = "#1193CF"
    i = 0
    while stack:
        vertex = stack.pop()
        vertex.color = change_hex_color(color, 0.1 * i)
        vertex_id = id(vertex)
        if vertex_id not in visited:
            visited.add(vertex_id)
            if vertex.right:
                stack.append(vertex.right)
            if vertex.left:
                stack.append(vertex.left)
        i += 1


def bfs(start_vertex: Node):
    """
    Breadth-First Search (BFS) algorithm to traverse the binary tree.
    Args:
        start_vertex (Node): The starting node for BFS traversal.
    """
    visited = set()
    queue = deque([start_vertex])
    color = "#1193CF"
    i = 0
    while queue:
        vertex = queue.popleft()
        vertex.color = change_hex_color(color, 0.1 * i)
        vertex_id = id(vertex)
        if vertex_id not in visited:
            visited.add(vertex_id)
            if vertex.left:
                queue.append(vertex.left)
            if vertex.right:
                queue.append(vertex.right)
        i += 1


if __name__ == "__main__":
    heap_array = [9, 11, 3, 5, 7, 9, 8, 10, 2]
    heap_root = build_heap_tree(heap_array)
    print("heap_root:", heap_root)
    # DFS
    dfs(heap_root)
    draw_tree(heap_root)
    # BFS
    bfs(heap_root)
    draw_tree(heap_root)
