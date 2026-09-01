import xml.etree.ElementTree as ET
from datetime import datetime
from decimal import Decimal
from typing import Dict

class SEPAInstantProcessor:
    @staticmethod
    def validate_iban(iban: str) -> bool:
        clean = iban.replace(" ", "").upper()
        if len(clean) < 15 or len(clean) > 34:
            return False
        rearranged = clean[4:] + clean[:4]
        digits = "".join(str(10 + ord(ch) - ord("A")) if ch.isalpha() else ch for ch in rearranged)
        return int(digits) % 97 == 1

    @staticmethod
    def generate_pain001_xml(msg_id: str, debtor_name: str, creditor_name: str, amount: Decimal) -> str:
        root = ET.Element("Document", attrib={"xmlns": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.03"})
        cstmr_pmt_init = ET.SubElement(root, "CstmrPmtInfInitn")
        
        grp_hdr = ET.SubElement(cstmr_pmt_init, "GrpHdr")
        ET.SubElement(grp_hdr, "MsgId").text = msg_id
        ET.SubElement(grp_hdr, "CreDtTm").text = datetime.utcnow().isoformat()
        
        pmt_inf = ET.SubElement(cstmr_pmt_init, "PmtInf")
        ET.SubElement(pmt_inf, "Dbtr").text = debtor_name
        
        cdt_trf_tx_inf = ET.SubElement(pmt_inf, "CdtTrfTxInf")
        ET.SubElement(cdt_trf_tx_inf, "Cdtr").text = creditor_name
        amt_elem = ET.SubElement(cdt_trf_tx_inf, "Amt")
        ET.SubElement(amt_elem, "InstdAmt", attrib={"Ccy": "EUR"}).text = str(amount)
        
        return ET.tostring(root, encoding="utf-8").decode("utf-8")
