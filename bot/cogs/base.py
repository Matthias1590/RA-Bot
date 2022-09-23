import discord

from discord.ext import commands
from bot.managers.manager import Manager
from bot.utils.logger import Logger


class BaseCog(commands.Cog):
    bot: discord.Bot
    manager: Manager
    logger: Logger

    def __init__(self, bot: discord.Bot, manager: Manager, logger: Logger) -> None:
        self.bot = bot
        self.manager = manager
        self.logger = logger
