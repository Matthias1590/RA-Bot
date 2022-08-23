from bot.managers.message import MessageManager
from bot.managers.patreon import PatreonManager


class Manager:
    patreon: PatreonManager
    message: MessageManager

    def __init__(self) -> None:
        self.patreon = PatreonManager()
        self.message = MessageManager()
