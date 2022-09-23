from discord import Webhook
from enum import Enum
import aiohttp
import datetime
import colorama

from statusembed import StatusEmbed, EmbedStatus


WEBHOOK_URL = ""


class ColoramaStatus(Enum):
    INFO = colorama.Fore.GREEN
    WARNING = colorama.Fore.YELLOW
    ERROR = colorama.Fore.RED
    DEBUG = colorama.Fore.LIGHTBLACK_EX


class WebhookLogger:
    def __init__(self, webhook_url, console_log=None):
        self.webhook = webhook_url
        self.console_log = console_log

    async def info(self, message):
        async with aiohttp.ClientSession() as session:
            log_webhook = Webhook.from_url(self.webhook, session=session)

            log_embed = StatusEmbed()
            log_embed.set_title(f":information_source: Info Log")
            log_embed.set_description(message)
            log_embed.set_timestamp(datetime.datetime.now())
            log_embed.set_status(EmbedStatus.INFO)

            await log_webhook.send(embed=log_embed.build())


    async def debug(self, message):
        async with aiohttp.ClientSession() as session:
            log_webhook = Webhook.from_url(url=self.webhook, session=session)

            log_embed = StatusEmbed()
            log_embed.set_title(f":beetle: Debug Log")
            log_embed.set_description(message)
            log_embed.set_timestamp(datetime.datetime.now())
            log_embed.set_status(EmbedStatus.DEBUG)

            await log_webhook.send(embed=log_embed.build())


    async def warning(self, message):
        async with aiohttp.ClientSession() as session:
            log_webhook = Webhook.from_url(url=self.webhook, session=session)

            log_embed = StatusEmbed()
            log_embed.set_title(f":warning: Warning Log")
            log_embed.set_description(message)
            log_embed.set_timestamp(datetime.datetime.now())
            log_embed.set_status(EmbedStatus.WARNING)

            await log_webhook.send(embed=log_embed.build())


    async def error(self, message):
        async with aiohttp.ClientSession() as session:
            log_webhook = Webhook.from_url(url=self.webhook, session=session)

            log_embed = StatusEmbed()
            log_embed.set_title(f":stop_sign: Error Log")
            log_embed.set_description(message)
            log_embed.set_timestamp(datetime.datetime.now())
            log_embed.set_status(EmbedStatus.ERROR)

            await log_webhook.send(embed=log_embed.build())


