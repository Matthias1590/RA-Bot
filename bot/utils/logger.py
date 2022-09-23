from aiohttp import ClientSession
from bot.utils.status_embed import StatusEmbed, EmbedStatus

import discord


class Logger:
    webhook_url: str

    def __init__(self, webhook_url: str) -> None:
        self.webhook_url = webhook_url

    # TODO: Consider moving this into utils (maybe even create some webhook wrapper), also it should probably return something
    async def send_embed(self, embed: discord.Embed) -> None:
        async with ClientSession() as session:
            await discord.Webhook.from_url(url=self.webhook_url, session=session).send(
                embed=embed
            )

    async def log(self, level: EmbedStatus, title: str, message: str) -> None:
        await self.send_embed(
            StatusEmbed()
            .set_title(title)
            .set_description(message)
            .set_status(level)
            .build()
        )

    async def info(self, message: str) -> None:
        await self.log(EmbedStatus.INFO, "Info", message)

    async def debug(self, message: str) -> None:
        await self.log(EmbedStatus.DEBUG, "Debug", message)

    async def warning(self, message: str) -> None:
        await self.log(EmbedStatus.WARNING, "Warning", message)

    async def error(self, message: str) -> None:
        await self.log(EmbedStatus.ERROR, "Error", message)
