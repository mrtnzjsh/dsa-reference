from typing import Any

class PriorityStack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, item: Any, priority: Any) -> None:
        if not self.stack:
            self.stack.append((item, priority))
        else:
            inserted = False
            for i in range(len(self.stack)):
                if priority > self.stack[i][1]:
                    self.stack.insert(i, (item, priority))
                    inserted = True
                    break
            if not inserted:
                self.stack.append((item, priority))

    def pop(self) -> Any:
        if not self.stack:
            return None
        return self.stack.pop(-1)[0]

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def size(self) -> int:
        return len(self.stack)



