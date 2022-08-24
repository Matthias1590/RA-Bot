from typing import List
from bot.managers.base import BaseManager
from bot.constants import context as constants

from bot.models.discord.deleted_message import DeletedMessage

class MessageManager(BaseManager):
    def get_sniped_messages(self, channel_id: int) -> List[DeletedMessage]:
        return self.context.message.sniped_messages.get(channel_id, [])
    
    def log_deleted_message(self, message: DeletedMessage) -> None:
        messages = self.context.message.sniped_messages

        if message.channel.id not in messages:
            messages[message.channel.id] = []
        elif len(messages[message.channel.id]) >= constants.MAX_SNIPED_MESSAGES:
            messages[message.channel.id] = messages[message.channel.id][:constants.MAX_SNIPED_MESSAGES - 1]  # - 1 cause we're adding a message right after this

        messages[message.channel.id].insert(0, message)

        self.context.save()