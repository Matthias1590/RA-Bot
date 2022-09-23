from typing import Union
import discord


class Sendable:
    async def send(
        self, ctx: discord.ApplicationContext
    ) -> Union[discord.Interaction, discord.WebhookMessage]:
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement {self.send.__name__}"
        )
