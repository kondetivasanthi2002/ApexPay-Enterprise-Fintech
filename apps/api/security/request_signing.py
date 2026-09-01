import hmac
import hashlib

class RequestSigner:
    @staticmethod
    def sign_request(body_bytes: bytes, secret_key: str) -> str:
        return hmac.new(secret_key.encode("utf-8"), body_bytes, hashlib.sha256).hexdigest()

    @staticmethod
    def verify_request(body_bytes: bytes, secret_key: str, signature: str) -> bool:
        expected = RequestSigner.sign_request(body_bytes, secret_key)
        return hmac.compare_digest(expected, signature)
