from typing import Dict, List
import discord

class MessageContext:
    sniped_messages: Dict[int, List[discord.Message]]  # Maps a channel id to a list of deleted messages

    def __init__(self) -> None:
        self.sniped_messages = {}