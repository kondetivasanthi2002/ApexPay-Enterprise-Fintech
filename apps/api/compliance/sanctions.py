from typing import List, Dict

class SanctionScreeningEngine:
    def __init__(self):
        # Simulated OFAC Specially Designated Nationals (SDN) List
        self.sdn_list = [
            "VIKTOR ANATOLYEVICH BOUT",
            "SERGEI IVANOVICH PETROV",
            "GLOBAL TRADE MANAGEMENT LLC",
            "CARIBBEAN OFFSHORE TRUST LTD",
            "ALEXANDER KUZNETSOV"
        ]

    def levenshtein_distance(self, s1: str, s2: str) -> int:
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)
        if len(s2) == 0:
            return len(s1)
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]

    def screen_entity(self, name: str, threshold_similarity: float = 0.7) -> Dict[str, any]:
        name_clean = name.upper().strip()
        hits = []
        tokens = set(name_clean.split())
        for target in self.sdn_list:
            target_tokens = set(target.split())
            token_overlap = len(tokens.intersection(target_tokens)) / max(len(tokens), 1)
            dist = self.levenshtein_distance(name_clean, target)
            max_len = max(len(name_clean), len(target))
            similarity = 1.0 - (dist / max_len)
            if similarity >= threshold_similarity or token_overlap >= 0.5:
                hits.append({"matched_name": target, "similarity": round(max(similarity, token_overlap), 4)})

        return {
            "flagged": len(hits) > 0,
            "query_name": name,
            "matched_count": len(hits),
            "hits": hits
        }
