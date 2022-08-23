from typing import List
from bot.constants.patreon.tiers import TIERS
from bot.managers.base import BaseManager
from bot.constants import context as constants

import discord

class MessageManager(BaseManager):
    def get_sniped_messages(self, channel: discord.TextChannel) -> List[discord.Message]:
        return self.context.message.sniped_messages.get(channel.id, [])
    
    def log_deleted_message(self, message: discord.Message) -> None:
        messages = self.context.message.sniped_messages

        if message.channel.id not in messages:
            messages[message.channel.id] = []
        elif len(messages[message.channel.id]) >= constants.MAX_SNIPED_MESSAGES:
            messages[message.channel.id] = messages[message.channel.id][:constants.MAX_SNIPED_MESSAGES - 1]  # - 1 cause we're adding a message right after this

        messages[message.channel.id].insert(0, message)

        self.context.save()