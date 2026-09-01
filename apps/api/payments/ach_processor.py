class NACHAGenerator:
    @staticmethod
    def validate_routing_number(routing_num: str) -> bool:
        if len(routing_num) != 9 or not routing_num.isdigit() or routing_num == "000000000":
            return False
        weights = [3, 7, 1, 3, 7, 1, 3, 7]
        checksum = sum(int(routing_num[i]) * weights[i] for i in range(8))
        return (checksum % 10) == (10 - int(routing_num[8])) % 10

    @staticmethod
    def generate_nacha_file_header(immediate_destination: str, immediate_origin: str) -> str:
        # NACHA File Header Record (Type 1)
        return f"101 {immediate_destination:>10} {immediate_origin:>10} 230901 2140 A094101 ApexPay Bank        ApexPay ACH Gateway    "
