from dataclasses import dataclass
from bot.models.patreon.benefits.benefit import Benefit


@dataclass
class UsableBenefit(Benefit):
    # The amount of times this benefit can be used per month
    monthly_uses: int
