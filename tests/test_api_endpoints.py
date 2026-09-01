import pytest
from fastapi.testclient import TestClient
from apps.api.ledger.routes import router as ledger_router

def test_ledger_accounts_endpoint():
    from fastapi import FastAPI
    app = FastAPI()
    app.include_router(ledger_router)
    client = TestClient(app)

    res = client.get("/api/v1/ledger/accounts")
    assert res.status_code == 200
    assert len(res.json()) >= 3
