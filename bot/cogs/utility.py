from discord import ApplicationContext, slash_command
from bot.cogs.base import BaseCog


class UtilityCog(BaseCog):
    @slash_command(name="ping", description="Get the bot's latency.")
    async def ping(self, ctx: ApplicationContext) -> None:
        await ctx.respond(f"Pong! {round(self.bot.latency * 1000)}ms")
