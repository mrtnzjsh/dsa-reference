from typing import Any, Optional

class Node:
    def __init__(self, 
                 data: Any, 
                 next: Optional[Node] = None, 
                 prev: Optional[Node] = None
                 ) -> None:
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_first_with_value(self, data: Any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev_node.next = current_node.next
        current_node = None

    def delete_last(self) -> Any:
        current_node = self.head
        if current_node and current_node.next is None:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.next is not None:
            prev_node = current_node
            current_node = current_node.next

        deleted_value = current_node.data
        prev_node.next = None
        current_node = None

        return deleted_value

    def size(self) -> int:
        current_node = self.head
        ll_length = 0
        while current_node and current_node.next is not None:
            ll_length += 1
            current_node = current_node.next

        return ll_length
