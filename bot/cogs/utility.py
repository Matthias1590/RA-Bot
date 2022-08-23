from discord import ApplicationContext, slash_command
from bot.cogs.base import BaseCog
from discord.ext import commands
import discord

class UtilityCog(BaseCog):
    @slash_command(name="ping", description="Get the bot's latency.")
    async def ping(self, ctx: ApplicationContext) -> None:
        await ctx.respond(f"Pong! {round(self.bot.latency * 1000)}ms")
    
    @commands.Cog.listener()
    def on_message_delete(self, message: discord.Message) -> None:  # TODO: Figure out if we should use on_raw_message_delete instead of this
        self.manager.message.log_deleted_message(message)
    
    ...  # TODO: Add the snipe command
