from typing import List, Optional, Set
from bot.constants.patreon.tiers import TIERS
from bot.managers.base import BaseManager

from bot.models.patreon.benefits.benefit import Benefit
from bot.models.patreon.benefits.usable_benefit import UsableBenefit

from bot.models.patreon.tier import Tier
from bot.models.patreon.use import Use

import discord


class PatreonManager(BaseManager):
    def get_tier(self, member: discord.Member) -> Optional[Tier]:
        for tier in TIERS:
            if tier.role in member.roles:
                return tier

        return None

    def get_benefits(self, tier: Optional[Tier]) -> List[Benefit]:
        benefits = []
        while tier is not None:
            benefits.extend(tier.benefits)
            tier = tier.inherits

        return benefits

    def get_uses(self, member: discord.Member, benefit: UsableBenefit) -> List[Use]:
        return [
            use
            for use in self.context.patreon.uses
            if use.user == member and use.benefit == benefit
        ]

    def uses_left(self, member: discord.Member, benefit: UsableBenefit) -> int:
        return benefit.monthly_uses - len(self.get_uses(member, benefit))

    def can_use(self, member: discord.Member, benefit: UsableBenefit) -> bool:
        return benefit.monthly_uses == -1 or self.uses_left(member, benefit) > 0
