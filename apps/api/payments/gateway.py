from enum import Enum
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, Field

class PaymentMethod(str, Enum):
    ACH = "ACH"
    WIRE = "WIRE"
    CARD = "CARD"
    SEPA = "SEPA"

class PaymentStatus(str, Enum):
    INITIATED = "INITIATED"
    PROCESSING = "PROCESSING"
    SETTLED = "SETTLED"
    FAILED = "FAILED"

class PaymentRequest(BaseModel):
    payment_id: str
    source_account: str
    destination_account: str
    amount: Decimal
    currency: str = "USD"
    method: PaymentMethod
    idempotency_key: str

class PaymentProcessor:
    def __init__(self):
        self.processed_payments = {}

    def process_payment(self, req: PaymentRequest) -> dict:
        if req.amount <= Decimal("0.00"):
            return {"status": PaymentStatus.FAILED, "reason": "Invalid amount"}
        
        self.processed_payments[req.payment_id] = {
            "payment_id": req.payment_id,
            "status": PaymentStatus.SETTLED,
            "amount": str(req.amount),
            "currency": req.currency,
            "method": req.method,
            "timestamp": datetime.utcnow().isoformat()
        }
        return self.processed_payments[req.payment_id]
