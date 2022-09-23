from __future__ import annotations
from enum import Enum
from typing import List, Optional

import discord
import datetime


class EmbedStatus(Enum):
    DEBUG = 0x665D5D
    INFO = 0x00AE86
    SUCCESS = 0x00FF00
    WARNING = 0xFFD800
    ERROR = 0xFF0000


class StatusEmbed:
    status: EmbedStatus
    title: str
    description: str
    timestamp: Optional[datetime.datetime]
    fields: List[discord.EmbedField]

    def __init__(self) -> None:
        self.status = EmbedStatus.INFO
        self.title = ""
        self.description = ""
        self.timestamp = datetime.datetime.now()
        self.fields = []

    def set_status(self, status: EmbedStatus) -> StatusEmbed:
        self.status = status

        return self

    def set_title(self, title: str) -> StatusEmbed:
        self.title = title

        return self

    def set_description(self, description: str) -> StatusEmbed:
        self.description = description

        return self

    def set_timestamp(self, timestamp: Optional[datetime.datetime]) -> StatusEmbed:
        self.timestamp = timestamp

        return self

    def add_field(self, field: discord.EmbedField) -> StatusEmbed:
        self.fields.append(field)

        return self

    def add_fields(self, fields: List[discord.EmbedField]) -> StatusEmbed:
        self.fields.extend(fields)

        return self

    def build(self) -> discord.Embed:
        return discord.Embed(
            title=self.title,
            description=self.description,
            color=self.status.value,
            timestamp=self.timestamp,
            fields=self.fields,
        )
