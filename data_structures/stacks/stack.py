from typing import Any

from dsa_reference.linked_lists.linked_list import LinkedList

# Stack using an underlying array
class StackList:

    def __init__(self) -> None:
        self.stack = []

    def push(self, item: Any) -> None:
        self.stack.append(item)

    def pop(self) -> Any:
        popped_value = self.stack.pop(-1)
        return popped_value

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def size(self) -> int:
        return len(self.stack)


# Stack using an underlying linked list
class StackLinkedList:
    def __init__(self) -> None:
        self.stack = LinkedList()

    def push(self, item: Any) -> None:
        self.stack.append(item)

    def pop(self) -> Any:
        popped_value = self.stack.delete_last()
        return popped_value

    def is_empty(self) -> bool:
        return self.stack.size() == 0

    def size(self) -> int:
        return self.stack.size()
