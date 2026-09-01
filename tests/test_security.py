import pytest
import time
from apps.api.security.rate_limiter import SlidingWindowRateLimiter
from apps.api.security.request_signing import RequestSigner

def test_rate_limiter_permits_under_limit():
    limiter = SlidingWindowRateLimiter(max_requests=5, window_seconds=60)
    for _ in range(5):
        assert limiter.is_allowed("client_1") is True
    assert limiter.is_allowed("client_1") is False

def test_request_signature_verification():
    secret = "super_secret_api_key"
    payload = b'{"amount": 1000, "currency": "USD"}'
    sig = RequestSigner.sign_request(payload, secret)
    assert RequestSigner.verify_request(payload, secret, sig) is True
    assert RequestSigner.verify_request(payload, "wrong_key", sig) is False
