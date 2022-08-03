from dataclasses import dataclass


@dataclass
class Benefit:
    # The benefit id, used to identify the benefit
    id: int

    # A description of the benefit
    description: str
