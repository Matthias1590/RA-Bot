from typing import List
from bot.models.patreon.benefits.benefit import Benefit
from bot.models.patreon.tier import Tier
from bot.models.patreon.use import Use


class PatreonContext:
    uses: List[Use]

    def __init__(self) -> None:
        self.uses = []
