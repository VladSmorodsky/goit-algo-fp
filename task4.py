from typing import List
import uuid
import heapq

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())

    def __eq__(self, node: 'Node'):
        return self.val == node.val

    def __gt__(self, node: 'Node'):
        return self.val > node.val

    def __lt__(self, node: 'Node'):
        return self.val < node.val


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(arr: List[int]) -> Node:
    """
    Build a binary heap tree from the given array.
    """
    if not arr:
        return

    nodes = [Node(val) for val in arr]
    heapq.heapify(nodes)

    for i in range(len(arr)):
        left = 2*i + 1
        right = 2*i + 2
        if left < len(arr):
            nodes[i].left = nodes[left]
        if right < len(arr):
            nodes[i].right = nodes[right]
    return nodes[0]


heap_array = [9, 11, 3, 5, 7, 9, 8, 10, 2]
heap_root = build_heap_tree(heap_array)
print("heap_root:", heap_root)
draw_tree(heap_root)
