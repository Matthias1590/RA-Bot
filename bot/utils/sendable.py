from discord import ApplicationContext


class Sendable:
    def send(self, ctx: ApplicationContext) -> None:
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement {self.send.__name__}"
        )
