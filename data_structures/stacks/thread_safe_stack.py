import threading

class ThreadSafeStack:
    def __init__(self) -> None:
        self.stack = []
        self.lock = threading.Lock()

    def push(self, item: Any) -> None:
        with self.lock:
            self.stack.append(item)

    def pop(self) -> Any:
        with self.lock:
            if not self.stack:
                return None
            return self.stack.pop(-1)

    def is_empty(self) -> bool:
        with self.lock:
            return len(self.stack) == 0

    def size(self) -> int:
        with self.lock:
            return len(self.stack)

