"""
Sliding Window Rate Limiter using Redis

This implementation uses Redis to track request timestamps within a sliding window.
The algorithm maintains a record of all requests in the current time window
and calculates the actual rate based on the time elapsed within the window.

Time Complexity: O(n) where n is the number of requests in the window
Space Complexity: O(n) for storing request timestamps
"""

from typing import final
import time

try:
    import redis
except ImportError:
    redis = None


@final
class RateLimiterWindow:
    """
    Sliding Window Rate Limiter using Redis

    This implementation uses Redis to track request timestamps within a sliding window.
    The algorithm maintains a record of all requests in the current time window
    and calculates the actual rate based on the time elapsed within the window.

    Time Complexity: O(n) where n is the number of requests in the window
    Space Complexity: O(n) for storing request timestamps
    """

    def __init__(
        self, redis_client: redis.Redis, window_size: int = 60, max_requests: int = 100
    ):
        """
        Initialize the sliding window rate limiter.

        Args:
            redis_client: Redis client instance
            window_size: Size of the sliding window in seconds (default: 60)
            max_requests: Maximum number of requests allowed in the window (default: 100)
        """
        self.redis = redis_client
        self.window_size = window_size
        self.max_requests = max_requests
        self.prefix = "rate_limit"

    def allow_request(self, identifier: str) -> tuple[bool, str]:
        """
        Check if a request should be allowed based on the sliding window algorithm.

        Args:
            identifier: Unique identifier for the client (e.g., IP address, user ID)

        Returns:
            Tuple of (allowed, message)
        """
        now = time.time()
        key = f"{self.prefix}:{identifier}"
        window_start = now - self.window_size

        try:
            # Pipeline for atomic operations
            pipe = self.redis.pipeline()

            # 1. Get all request timestamps in the window
            pipe.zrangebyscore(key, window_start, now)

            # 2. Get the count of requests
            pipe.zcount(key, window_start, now)

            # 3. Get all request timestamps (for cleanup)
            pipe.zrange(key, 0, -1)

            # 4. Add the current request timestamp
            pipe.zadd(key, {str(now): now})

            # 5. Remove requests outside the window
            pipe.zremrangebyscore(key, 0, window_start - 1)

            # 6. Set expiration (TTL) to automatically clean up old keys
            pipe.expire(key, self.window_size)

            # Execute all commands
            timestamps, current_count, all_timestamps, added, removed, ttl = (
                pipe.execute()
            )

            # Calculate actual rate and time in window
            time_in_window = now - window_start
            rate = (
                (current_count / time_in_window)
                if time_in_window > 0
                else current_count
            )

            allowed = current_count < self.max_requests

            message = (
                f"Request {'allowed' if allowed else 'denied'} "
                f"({current_count}/{self.max_requests} requests in window, "
                f"rate: {rate:.2f}/sec)"
            )

            return allowed, message

        except redis.RedisError as e:
            # Handle Redis errors - consider the request denied to prevent blocking
            return False, f"Redis error: {str(e)}"

    def get_statistics(self, identifier: str) -> dict:
        """
        Get detailed statistics for a rate limiter instance.

        Args:
            identifier: Unique identifier for the client

        Returns:
            Dictionary containing statistics about the rate limiter state
        """
        key = f"{self.prefix}:{identifier}"
        window_start = time.time() - self.window_size

        try:
            pipe = self.redis.pipeline()

            # Get current count
            pipe.zcount(key, window_start, time.time())

            # Get requests in the last window
            pipe.zrangebyscore(key, window_start, time.time())

            # Get oldest request timestamp
            pipe.zrange(key, 0, 0, withscores=True)

            # Get newest request timestamp
            pipe.zrevrange(key, 0, 0, withscores=True)

            count, timestamps, oldest, newest = pipe.execute()

            if not timestamps:
                return {
                    "identifier": identifier,
                    "allowed_requests": 0,
                    "denied_requests": 0,
                    "current_count": 0,
                    "timestamp": [],
                    "oldest_timestamp": None,
                    "newest_timestamp": None,
                    "window_usage_percent": 0.0,
                }

            timestamps = [float(ts) for ts in timestamps]

            return {
                "identifier": identifier,
                "allowed_requests": int(count),
                "denied_requests": max(0, count - self.max_requests),
                "current_count": int(count),
                "timestamp": timestamps,
                "oldest_timestamp": float(oldest[0][1]) if oldest else None,
                "newest_timestamp": float(newest[0][1]) if newest else None,
                "window_usage_percent": (count / self.max_requests) * 100,
            }

        except redis.RedisError:
            return {
                "identifier": identifier,
                "error": "Failed to retrieve statistics",
            }

    def reset(self, identifier: str) -> bool:
        """
        Reset the rate limiter state for a specific identifier.

        Args:
            identifier: Unique identifier for the client

        Returns:
            True if successful, False otherwise
        """
        key = f"{self.prefix}:{identifier}"
        try:
            self.redis.delete(key)
            return True
        except redis.RedisError:
            return False

    def get_rate_limit_config(self, identifier: str) -> dict:
        """
        Get the current rate limit configuration for an identifier.

        Args:
            identifier: Unique identifier for the client

        Returns:
            Dictionary containing rate limit configuration
        """
        key = f"{self.prefix}:{identifier}"
        try:
            ttl = self.redis.ttl(key)
            return {
                "identifier": identifier,
                "window_size": self.window_size,
                "max_requests": self.max_requests,
                "current_ttl": ttl,
                "rate": (
                    (self.max_requests / self.window_size)
                    if self.window_size > 0
                    else 0
                ),
            }
        except redis.RedisError:
            return {
                "identifier": identifier,
                "error": "Failed to retrieve configuration",
            }


class RateLimiterWindowFixedSize:
    """
    Fixed Window Rate Limiter with Redis
    Similar to sliding window but uses fixed time intervals instead of a continuous window.
    Less accurate but uses less memory.
    """

    def __init__(
        self, redis_client: redis.Redis, window_size: int = 60, max_requests: int = 100
    ):
        """
        Initialize the fixed window rate limiter.

        Args:
            redis_client: Redis client instance
            window_size: Size of the time window in seconds (default: 60)
            max_requests: Maximum number of requests allowed in the window (default: 100)
        """
        self.redis = redis_client
        self.window_size = window_size
        self.max_requests = max_requests
        self.prefix = "fixed_window"

    def allow_request(self, identifier: str) -> tuple[bool, str]:
        """
        Check if a request should be allowed using fixed window algorithm.

        Args:
            identifier: Unique identifier for the client

        Returns:
            Tuple of (allowed, message)
        """
        now = int(time.time())
        key = f"{self.prefix}:{identifier}:{now // self.window_size}"

        try:
            count = self.redis.incr(key)

            # If this is the first request in this window, set expiration
            if count == 1:
                self.redis.expire(key, self.window_size + 1)

            allowed = count <= self.max_requests
            message = (
                f"Request {'allowed' if allowed else 'denied'} "
                f"({count}/{self.max_requests} requests in this window)"
            )

            return allowed, message

        except redis.RedisError as e:
            return False, f"Redis error: {str(e)}"

    def get_statistics(self, identifier: str) -> dict:
        """
        Get statistics for the fixed window rate limiter.

        Args:
            identifier: Unique identifier for the client

        Returns:
            Dictionary containing statistics
        """
        now = int(time.time())
        current_window = now // self.window_size
        key = f"{self.prefix}:{identifier}:{current_window}"

        try:
            count = self.redis.get(key)
            ttl = self.redis.ttl(key)

            return {
                "identifier": identifier,
                "current_window": current_window,
                "current_count": int(count) if count else 0,
                "window_size": self.window_size,
                "max_requests": self.max_requests,
                "current_ttl": ttl,
            }

        except redis.RedisError:
            return {
                "identifier": identifier,
                "error": "Failed to retrieve statistics",
            }
