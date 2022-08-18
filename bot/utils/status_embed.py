from enum import Enum
from typing_extensions import Self
import discord


class EmbedStatus(Enum):
    INFO = 0
    SUCCESS = 1
    WARNING = 2
    ERROR = 3


class StatusEmbed:
    status: EmbedStatus
    title: str
    description: str
    fields: list[discord.EmbedField]

    def __init__(self) -> None:
        self.status = EmbedStatus.INFO
        self.title = ""
        self.description = ""
        self.fields = []

    def set_status(self, status: EmbedStatus) -> Self:
        self.status = status
        return self

    def set_title(self, title: str) -> Self:
        self.title = title
        return self

    def set_description(self, description: str) -> Self:
        self.description = description
        return self

    def add_field(self, name: str, value: str) -> Self:
        self.fields.append(discord.EmbedField(name=name, value=value))
        return self

    def build(self) -> discord.Embed:
        return discord.Embed(
            title=self.title,
            description=self.description,
            color=self.status.value,
            fields=self.fields,
        )
