import discord

from discord.ext import commands
from bot.managers.manager import Manager


class BaseCog(commands.Cog):
    bot: discord.Bot
    manager: Manager

    def __init__(self, bot: discord.Bot, manager: Manager) -> None:
        self.bot = bot
        self.manager = manager
