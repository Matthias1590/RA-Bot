from bot.models.patreon.benefits.passive_benefit import PassiveBenefit
from bot.models.patreon.benefits.usable_benefit import UsableBenefit

EARLY_ACCESS = PassiveBenefit(
    id=0,
    description="Early access to videos, projects and world downloads.",
)

VIDEO_CREDITS = PassiveBenefit(
    id=1,
    description="Your name at the end of all videos.",
)

DISCORD_ROLE = UsableBenefit(
    id=2,
    description="Custom discord role & color.",
    monthly_uses=-1,
)

DISCORD_STATUS = UsableBenefit(
    id=3,
    description="Choose my status for a day.",
    monthly_uses=1,
)

DISCORD_PFP = UsableBenefit(
    id=4,
    description="Choose my profile picture for a day.",
    monthly_uses=1,
)

DISCORD_ANNOUNCEMENT = UsableBenefit(
    id=5,
    description="Make an announcement.",
    monthly_uses=1,
)
