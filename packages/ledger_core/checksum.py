import hashlib
import json

class LedgerAuditChecksum:
    @staticmethod
    def compute_entry_hash(entry_dict: dict, previous_hash: str = "") -> str:
        payload = {
            "entry_id": entry_dict.get("entry_id"),
            "timestamp": str(entry_dict.get("timestamp")),
            "reference": entry_dict.get("reference"),
            "postings": entry_dict.get("postings"),
            "previous_hash": previous_hash
        }
        raw_bytes = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(raw_bytes).hexdigest()

    @staticmethod
    def verify_chain(journal_entries: list) -> bool:
        prev_hash = "GENESIS_BLOCK_00000000000000000000000000000000"
        for entry in journal_entries:
            expected = LedgerAuditChecksum.compute_entry_hash(entry, prev_hash)
            if entry.get("checksum") and entry.get("checksum") != expected:
                return False
            prev_hash = expected
        return True
