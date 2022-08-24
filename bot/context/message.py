from typing import Dict, List
import discord

from bot.models.discord.deleted_message import DeletedMessage

class MessageContext:
    sniped_messages: Dict[int, List[DeletedMessage]]  # Maps a channel id to a list of deleted messages

    def __init__(self) -> None:
        self.sniped_messages = {}