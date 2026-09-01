import pytest
from decimal import Decimal
from apps.api.payments.sepa_instant import SEPAInstantProcessor

def test_iban_validation():
    # Valid German IBAN sample
    assert SEPAInstantProcessor.validate_iban("DE89370400440532013000") is True
    assert SEPAInstantProcessor.validate_iban("INVALID_IBAN_123") is False

def test_sepa_xml_generation():
    xml_output = SEPAInstantProcessor.generate_pain001_xml("MSG-001", "Acme GmbH", "Berlin Tech AG", Decimal("250.50"))
    assert "<MsgId>MSG-001</MsgId>" in xml_output
    assert "EUR" in xml_output
