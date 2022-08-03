from bot.managers.patreon import PatreonManager


class Manager:
    patreon: PatreonManager

    def __init__(self) -> None:
        self.patreon = PatreonManager()
