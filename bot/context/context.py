from __future__ import annotations
import os
from typing import Optional

from bot.context.patreon import PatreonContext
from bot.context.message import MessageContext

from bot.constants import context as constants
from bot.utils.utils import get_data_path

import pickle


class Context:
    instance: Optional[Context] = None

    patreon: PatreonContext
    message: MessageContext

    def __init__(self) -> None:
        self.patreon = PatreonContext()
        self.message = MessageContext()

    @staticmethod
    def get() -> Context:
        if Context.instance:
            return Context.instance

        # Load the context from the file if it exists, otherwise create a new one
        Context.instance = (
            Context.load() if os.path.exists(constants.CONTEXT_PATH) else Context()
        )

        return Context.instance

    @staticmethod
    def load() -> Context:
        with open(get_data_path(constants.CONTEXT_PATH), "rb") as f:
            return pickle.load(f)

    def save(self) -> None:
        with open(get_data_path(constants.CONTEXT_PATH), "wb") as f:
            pickle.dump(self, f)
