import time
from typing import final


@final
class RateLimiter:
    def __init__(self, capacity: int, refill_rate: int) -> None:
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill_time = time.time()

    def allow_request(self, tokens_requested: int = 1) -> bool:
        now = time.time()

        # Calculate tokens gained since last check
        elapsed = now - self.last_refill_time
        self.tokens = min(self.capacity, self.tokens + (elapsed * self.refill_rate))
        self.last_refill_time = now

        if self.tokens > tokens_requested:
            self.tokens -= tokens_requested
            return True
        return False
