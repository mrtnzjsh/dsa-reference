from typing import Any, Optional

class Node:
    def __init__(self, min_degree: int, is_leaf: bool, keys: Optional[list] = [], children: Optional[list] = [], next: Optional[Node] = None) -> None:
        self.min_degree = min_degree
        self.is_leaf = is_leaf
        self.keys = keys
        self.children = children
        self.next = next


class BPlusTree:
    def __init__(self, min_degree: int) -> None:
        this.root = Node(min_degree, True)
        this.min_degree = min_degree

    def search(self, key: Any) -> Optional[Node]:
        return self.search_util(self.root, key)

    def search_util(self, node: Node, key: Any) -> Optional[Node]:
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node.keys[i]
        if node.is_leaf:
            return None
        return self.search_util(node.children[i], key)

    def insert(self, key: Any) -> None:
        root = self.root
        if len(root.keys) == 2 * self.min_degree - 1:
            tmp = Node(self.min_degree, False)
            tmp.children.insert(0, root)
            self.split_child(tmp, 0)
            self.root = tmp
        self.insert_non_full(self.root, key)

    def insert_non_full(self, node: Node, key: Any) -> None:
        index = len(node.keys) - 1
        if node.is_leaf:
            node.keys.insert(index + 1, key)
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.min_degree - 1:
                self.split_child(node, index)
                if key > node.keys[index]:
                    i += 1
            self.insert_non_full(node.children[index], key)

    def split_child(self, parent: Node, index: int) -> None:
        md = self.min_degree
        y = parent.children[indedx]
        z = Node(y.is_leaf, md)
        parent.children.insert(index + 1, z)
        parent.keys.insert(index, y.keys[md - 1])
        z.keys = y.keys[md:(2 * t - 1)]
        if not y.is_leaf:
            z.children = y.children[md:(2 * md)]
            z.next = y.next
        y.keys = y.keys[:md - 1]
        y.children = y.children[:md]
        y.next = z
