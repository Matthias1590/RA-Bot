from bot.cogs.base import BaseCog
from discord.ext import commands
import discord

from bot.utils.errors import InternalServerError, SendableError


class ListenersCog(BaseCog):
    @commands.Cog.listener()
    async def on_application_command_error(
        self,
        ctx: discord.ApplicationContext,
        error: discord.ClientException,  # TODO: Get the actual type of error for type hinting (its not discord.ClientException)
    ) -> None:
        if isinstance(error.original, SendableError):
            await error.original.send(ctx)
        else:
            await InternalServerError(error.original).send(ctx)
