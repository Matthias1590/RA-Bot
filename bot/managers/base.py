from bot.context.context import Context


class BaseManager:
    context: Context

    def __init__(self) -> None:
        self.context = Context.get()
