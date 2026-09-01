import time
from typing import Dict, List

class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window = window_seconds
        self.history: Dict[str, List[float]] = {}

    def is_allowed(self, client_id: str) -> bool:
        now = time.time()
        if client_id not in self.history:
            self.history[client_id] = []
        
        # Evict timestamps outside current window
        self.history[client_id] = [t for t in self.history[client_id] if now - t <= self.window]
        
        if len(self.history[client_id]) >= self.max_requests:
            return False
        
        self.history[client_id].append(now)
        return True
