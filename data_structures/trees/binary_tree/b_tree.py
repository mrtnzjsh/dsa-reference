from typing import Any, Optional

class Node:
    def __init__(self, min_degree: int, is_leaf: bool, keys: list = [], children: list = []) -> None:
        self.min_degree = min_degree
        self.keys = keys
        self.children = children
        self.is_leaf = is_leaf

class BTree:
    def __init__(self, min_degree: int) -> None:
        self.root = Node(min_degree, True)
        self.min_degree = min_degree

    def search(self, key: Any) -> bool:
        return self.search_util(self.root, key)

    def search_util(self, node: Node, key: Any) -> bool:
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        if node.is_leaf:
            return False
        return self.search_util(node.children[i], key)

    def insert(self, key: Any) -> None:
        root = self.root
        if len(root.keys) == 2 * self.min_degree - 1:
            tmp = Node(self.min_degree, False)
            tmp.children.insert(0, root)
            self.split_child(s, 0)
            self.root = tmp
        self.insert_non_full(self.root, key)

    def insert_non_full(self, node: Node, key: Any) -> None:
        i = len(node.keys) - 1
        if node.is_leaf:
            node.keys.insert(i + 1, key)
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.min_degree - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent: Node, index):
        md = self.min_degree
        y = parent.children[index]
        z = Node(md, y.is_leaf)
        parent.children.insert(index + 1, z)
        parent.keys.insert(index, y.keys[md - 1])
        z.keys = y.keys[t:(2 * md - 1)]
        if not y.is_leaf:
            z.children = y.children[t:(2 * md)]
        y.keys = y.keys[:md - 1]
        y.children = y.children[:md]


