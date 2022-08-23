from enum import Enum
from typing import List
from typing_extensions import Self
import discord


class EmbedStatus(Enum):
    INFO = 0x00AE86
    SUCCESS = 0x00FF00
    WARNING = 0xFFD800
    ERROR = 0xFF0000

class StatusEmbed:
    status: EmbedStatus
    title: str
    description: str
    fields: List[discord.EmbedField]

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

    def add_field(self, field: discord.EmbedField) -> Self:
        self.fields.append(field)

        return self
    
    def add_fields(self, fields: List[discord.EmbedField]) -> Self:
        self.fields.extend(fields)

        return self

    def build(self) -> discord.Embed:
        return discord.Embed(
            title=self.title,
            description=self.description,
            color=self.status.value,
            fields=self.fields,
        )
