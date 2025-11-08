from collections import defaultdict
from typing import List, Dict
from .base import ReportBase


class AverageRatingReport(ReportBase):
    name = "average-rating"

    def generate(self, rows: List[Dict[str, str]]):
        brand_ratings = defaultdict(list)
        for row in rows:
            try:
                brand = row.get("brand", "").strip().lower()
                rating_str = row.get("rating", "").strip()

                if not brand or not rating_str:
                    continue

                rating = float(rating_str)
                brand_ratings[brand].append(rating)

            except (KeyError, ValueError, TypeError):
                continue

        averages = [
            (brand.capitalize(), round(sum(ratings) / len(ratings), 2))
            for brand, ratings in brand_ratings.items()
            if ratings
        ]
        averages.sort(key=lambda x: x[1], reverse=True)
        return averages

