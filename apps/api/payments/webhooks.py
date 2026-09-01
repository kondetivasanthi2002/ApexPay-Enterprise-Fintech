import hmac
import hashlib
import json
import time

class WebhookDispatcher:
    def __init__(self, secret_key: str):
        self.secret = secret_key.encode("utf-8")

    def generate_signature(self, payload: dict, timestamp: int) -> str:
        raw = f"{timestamp}.{json.dumps(payload, sort_keys=True)}"
        return hmac.new(self.secret, raw.encode("utf-8"), hashlib.sha256).hexdigest()

    def verify_signature(self, payload: dict, timestamp: int, signature: str) -> bool:
        if abs(time.time() - timestamp) > 300: # 5-minute tolerance
            return False
        expected = self.generate_signature(payload, timestamp)
        return hmac.compare_digest(expected, signature)
