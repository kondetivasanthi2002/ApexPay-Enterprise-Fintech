# ApexPay Enterprise Fintech Platform

ApexPay is a high-performance, modular enterprise financial ledger, payment gateway, compliance engine, and trading platform built with FastAPI, SQLAlchemy, and React.

## Key Features
- **Double-Entry Ledger Engine**: Immutable transaction journal, multi-currency support, cryptographic checksum verification.
- **Payment Processing Gateway**: ACH (NACHA), Wire, Card settlement pipelines with idempotency keys and signed webhooks.
- **KYC & Compliance System**: OFAC/UN sanction fuzzy matching engine, real-time transaction velocity checks, SAR filing generator.
- **Credit & Loan Origination**: FICO-style credit risk scoring, equal monthly installment (EMI) amortization schedule engine.
- **Wealth & Portfolio Trading**: Limit/Market order execution engine, tax-lot accounting (FIFO/LIFO/HIFO).
- **Financial Reporting**: Real-time Balance Sheet, Trial Balance, Income Statement, and Cash Flow statement generation.

## Test Suite
Run unit & integration tests:
```bash
pytest -v
```
