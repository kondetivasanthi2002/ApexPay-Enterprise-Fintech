import json
import random

def generate_synthetic_transactions(count=1000):
    txs = []
    statuses = ["SETTLED", "PROCESSING", "SETTLED", "SETTLED"]
    methods = ["ACH", "WIRE", "CARD", "SEPA"]
    for i in range(count):
        txs.append({
            "id": f"TXN-{100000 + i}",
            "source_acc": f"ACC-{random.randint(100, 999)}",
            "dest_acc": f"ACC-{random.randint(100, 999)}",
            "amount": round(random.uniform(10.0, 5000.0), 2),
            "status": random.choice(statuses),
            "method": random.choice(methods)
        })
    return txs

if __name__ == "__main__":
    data = generate_synthetic_transactions(500)
    print(f"Generated {len(data)} synthetic transactions.")
