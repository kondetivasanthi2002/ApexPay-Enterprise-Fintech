from datetime import datetime
import xml.etree.ElementTree as ET

class SARReportGenerator:
    @staticmethod
    def generate_fincen_sar_xml(filing_id: str, suspect_name: str, reason: str, amount: str) -> str:
        root = ET.Element("FinCEN_SAR_Filing", attrib={"id": filing_id, "timestamp": datetime.utcnow().isoformat()})
        header = ET.SubElement(root, "Header")
        ET.SubElement(header, "FilerName").text = "ApexPay Financial Systems Inc"
        
        subject = ET.SubElement(root, "SubjectInformation")
        ET.SubElement(subject, "FullName").text = suspect_name
        ET.SubElement(subject, "SuspiciousAmount").text = amount
        ET.SubElement(subject, "Narrative").text = reason

        return ET.tostring(root, encoding="utf-8").decode("utf-8")
