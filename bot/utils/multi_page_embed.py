from typing import List, Optional
from typing_extensions import Self
from bot.utils.sendable import Sendable
import discord

class MultiPageEmbed(Sendable):
    pages: List[discord.Embed]
    timeout: float
    index: int

    def __init__(self) -> None:
        self.pages = []
        self.timeout = 60.0
        self.index = 0
    
    def add_page(self, page: discord.Embed) -> Self:
        self.pages.append(page)

        return self
    
    def add_pages(self, pages: List[discord.Embed]) -> Self:
        self.pages.extend(pages)

        return self

    def set_timeout(self, timeout: float) -> Self:
        self.timeout = timeout

        return self

    async def send(self, ctx: discord.ApplicationContext) -> discord.Message:
        ...