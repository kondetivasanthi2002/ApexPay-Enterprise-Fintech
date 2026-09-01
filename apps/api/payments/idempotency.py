import time
from typing import Dict, Any, Optional

class IdempotencyEngine:
    def __init__(self, ttl_seconds: int = 86400):
        self.store: Dict[str, Dict[str, Any]] = {}
        self.ttl = ttl_seconds

    def get_response(self, key: str) -> Optional[Dict[str, Any]]:
        record = self.store.get(key)
        if not record:
            return None
        if time.time() - record["timestamp"] > self.ttl:
            del self.store[key]
            return None
        return record["response"]

    def save_response(self, key: str, response: Dict[str, Any]):
        self.store[key] = {
            "timestamp": time.time(),
            "response": response
        }
