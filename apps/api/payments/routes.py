from fastapi import APIRouter, Header, HTTPException
from apps.api.payments.gateway import PaymentProcessor, PaymentRequest
from apps.api.payments.idempotency import IdempotencyEngine

router = APIRouter(prefix="/api/v1/payments", tags=["Payments Gateway"])
processor = PaymentProcessor()
idempotency_engine = IdempotencyEngine()

@router.post("/charge")
def charge_payment(req: PaymentRequest, x_idempotency_key: str = Header(None)):
    key = x_idempotency_key or req.idempotency_key
    cached = idempotency_engine.get_response(key)
    if cached:
        return cached

    res = processor.process_payment(req)
    idempotency_engine.save_response(key, res)
    return res
