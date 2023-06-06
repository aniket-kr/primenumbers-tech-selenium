from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class InfoItem:
    description: str
    est_value_notes: tuple[float, float]
    closing_date: str
