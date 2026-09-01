from typing import Dict

class ESGRiskEngine:
    def calculate_esg_score(self, carbon_intensity_g_per_dollar: float, board_diversity_pct: float, data_privacy_compliance: bool) -> Dict[str, any]:
        # Environmental score (0 - 100)
        env_score = max(0, min(100, int(100 - (carbon_intensity_g_per_dollar / 5.0))))
        
        # Social score (0 - 100)
        social_score = max(0, min(100, int(board_diversity_pct * 2.0)))
        
        # Governance score (0 - 100)
        gov_score = 100 if data_privacy_compliance else 40

        composite_esg = int((env_score * 0.4) + (social_score * 0.3) + (gov_score * 0.3))
        
        rating = "AAA" if composite_esg >= 85 else ("BBB" if composite_esg >= 60 else "CCC")

        return {
            "environmental": env_score,
            "social": social_score,
            "governance": gov_score,
            "composite_score": composite_esg,
            "esg_rating": rating
        }
