from __future__ import annotations
from typing import List, Union
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

    def add_page(self, page: discord.Embed) -> MultiPageEmbed:
        self.pages.append(page)

        return self

    def add_pages(self, pages: List[discord.Embed]) -> MultiPageEmbed:
        self.pages.extend(pages)

        return self

    def set_timeout(self, timeout: float) -> MultiPageEmbed:
        self.timeout = timeout

        return self

    async def on_timeout(self) -> None:
        """
        This method will be called when the timeout occurs, overwrite it to use it.
        """

    async def send(
        self, ctx: discord.ApplicationContext
    ) -> Union[discord.Interaction, discord.WebhookMessage]:
        raise NotImplementedError(
            "Keep track of the message, update the index and buttons on a button press"
        )
