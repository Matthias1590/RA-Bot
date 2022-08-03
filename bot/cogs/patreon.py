from discord.commands import SlashCommandGroup
from bot.cogs.base import BaseCog


class PatreonCog(BaseCog):
    patreon: SlashCommandGroup = SlashCommandGroup(
        name="patreon",
        description="Patreon related commands.",
    )

    ...  # TODO: Add commands (think before you code, think before you code, think before you code)
