from task4 import Node, draw_tree, build_heap_tree


def change_hex_color(hex_color: str, factor: float = 0.1) -> str:
    hex_color = hex_color.lstrip('#')
    r, g, b = (int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r = int(r + (255 - r) * factor)
    g = int(g + (255 - g) * factor)
    b = int(b + (255 - b) * factor)
    return f"#{r:02X}{g:02X}{b:02X}"


def dfs(start_vertex: Node):
    visited = set()
    stack = [(start_vertex)]
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


if __name__ == "__main__":
    heap_array = [9, 11, 3, 5, 7, 9, 8, 10, 2]
    heap_root = build_heap_tree(heap_array)
    print("heap_root:", heap_root)
    dfs(heap_root)
    draw_tree(heap_root)
