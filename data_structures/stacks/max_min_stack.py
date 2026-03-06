from typing import Any

class MaximumStack:
    def __init__(self) -> None:
        self.stack = []
        self.max_stack = []

    def push(self, item: Any) -> None:
        self.stack.append(item)
        if item > self.max_stack[-1]:
            self.max_stack.append(item)

    def peek(self) -> Any:
        return self.stack[-1]

    def pop(self) -> Any:
        popped_element = self.stack.pop(-1)
        if popped_element == self.max_stack[-1]:
            self.max_stack.pop(-1)

    def max(self) -> Any:
        return self.max_stack[-1]

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def size(self) -> int:
        return len(self.stack)

class MinimumStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, item: Any) -> None:
        self.stack.append(item)
        if item < self.min_stack[-1]:
            self.min_stack.append(item)

    def peek(self) -> Any:
        return self.stack[-1]

    def pop(self) -> Any:
        popped_element = self.stack.pop(-1)
        if popped_element == self.min_stack[-1]:
            self.min_stack.pop(-1)

    def min(self) -> Any:
        return self.min_stack[-1]

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def size(self) -> int:
        return len(self.stack)
