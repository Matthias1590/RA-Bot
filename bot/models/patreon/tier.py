from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional

from bot.models.discord.role import Role
from bot.models.patreon.benefits.benefit import Benefit


@dataclass
class Tier:
    # The tier id, used to identify the tier
    id: int

    # The display name of the tier
    name: str

    # The role that users will have if they have this tier
    role: Role

    # The tier this tier inherits from
    inherits: Optional[Tier]

    # The benefits this tier adds
    benefits: List[Benefit]
