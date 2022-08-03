from bot.constants.discord import roles
from bot.constants.patreon import benefits
from bot.models.patreon.tier import Tier

REDSTONE = Tier(
    id=0,
    name="Redstone",
    role=roles.REDSTONE_TIER,
    inherits=None,
    benefits=[
        benefits.EARLY_ACCESS,
    ],
)

TORCH = Tier(
    id=1,
    name="Torch",
    role=roles.TORCH_TIER,
    inherits=REDSTONE,
    benefits=[
        benefits.VIDEO_CREDITS,
        benefits.DISCORD_ROLE,
    ],
)

REPEATER = Tier(
    id=2,
    name="Repeater",
    role=roles.REPEATER_TIER,
    inherits=TORCH,
    benefits=[
        benefits.DISCORD_STATUS,
    ],
)

LAMP = Tier(
    id=3,
    name="Lamp",
    role=roles.LAMP_TIER,
    inherits=REPEATER,
    benefits=[
        benefits.DISCORD_PFP,
    ],
)

SWORD = Tier(
    id=4,
    name="Sword",
    role=roles.SWORD_TIER,
    inherits=LAMP,
    benefits=[
        benefits.DISCORD_ANNOUNCEMENT,
    ],
)

TIERS = [
    REDSTONE,
    TORCH,
    REPEATER,
    LAMP,
    SWORD,
]
