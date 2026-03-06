from typing import Any, Optional

# Implemented in non-decreasing. To have non-increasing,
# just invert the logic
class MonotonicStack:
    def __init__(self, item: Any) -> None:
        self.stack = []

    def push(self, item: Any) -> None:
        while self.stack and self.stack[-1] > item:
            self.stack.pop(-1)
        self.stack.append(item)

    def pop(self) -> Optional[Any]:
        if self.stack:
            return self.stack.pop(-1)
        return None

    def peek(self) -> Optional[Any]:
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def size(self) -> bool:
        return len(self.stack)

