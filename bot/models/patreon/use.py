from bot.models.discord.user import User
from bot.models.patreon.benefits.usable_benefit import UsableBenefit


class Use:
    # The user that used the benefit
    user: User

    # The benefit that was used
    benefit: UsableBenefit
