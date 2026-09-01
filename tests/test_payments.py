import pytest
from decimal import Decimal
from apps.api.payments.gateway import PaymentProcessor, PaymentRequest, PaymentMethod, PaymentStatus
from apps.api.payments.idempotency import IdempotencyEngine
from apps.api.payments.ach_processor import NACHAGenerator
from apps.api.payments.webhooks import WebhookDispatcher

def test_payment_processing_success():
    processor = PaymentProcessor()
    req = PaymentRequest(
        payment_id="PAY-001",
        source_account="ACC-1",
        destination_account="ACC-2",
        amount=Decimal("150.00"),
        method=PaymentMethod.ACH,
        idempotency_key="KEY-123"
    )
    res = processor.process_payment(req)
    assert res["status"] == PaymentStatus.SETTLED

def test_idempotency_deduplication():
    engine = IdempotencyEngine()
    engine.save_response("IDEM-KEY-1", {"status": "SETTLED", "id": "PAY-1"})
    cached = engine.get_response("IDEM-KEY-1")
    assert cached["id"] == "PAY-1"

def test_nacha_routing_checksum():
    assert NACHAGenerator.validate_routing_number("121000358") is True
    assert NACHAGenerator.validate_routing_number("000000000") is False

def test_webhook_hmac_verification():
    dispatcher = WebhookDispatcher("secret_key_123")
    timestamp = 1700000000
    payload = {"event": "payment.settled", "amount": 100}
    sig = dispatcher.generate_signature(payload, timestamp)
    assert len(sig) == 64
