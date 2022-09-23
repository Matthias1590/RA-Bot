from typing import Any, Union
from bot.utils.sendable import Sendable
import discord

from bot.utils.status_embed import EmbedStatus, StatusEmbed


class SendableError(Exception, Sendable):
    title: str
    description: str

    async def send(
        self, ctx: discord.ApplicationContext
    ) -> Union[discord.Interaction, discord.WebhookMessage]:
        embed = (
            StatusEmbed()
            .set_status(EmbedStatus.ERROR)
            .set_title(self.title)
            .set_description(self.description)
            .build()
        )

        return await ctx.respond(embed=embed)


class InternalServerError(SendableError):
    title = "Internal Server Error"

    def __init__(self, exception: Exception) -> None:
        self.exception = exception

        self.description = str(self.exception)


class InvalidArgumentError(SendableError):
    title = "Invalid Argument"


class InvalidArgumentTypeError(InvalidArgumentError):
    title = "Invalid Argument Type"

    def __init__(self, got: type, expected: type) -> None:
        self.got = got
        self.expected = expected

        self.description = f"Expected `{self.expected.__name__}` but got `{self.got.__name__}` instead."


# TODO: Add constraints which we can use to validate arguments (IntConstraint(min, max), CustomContstraint(func), etc.)
# class InvalidArgumentValueError(InvalidArgumentError):
#     title = "Invalid Argument Value"

#     def __init__(self, got: Any, constraint: Constraint) -> None:
#         self.got = got
#         self.constraint = constraint

#     @property
#     def description(self) -> str:
#         return f"Expected {self.constraint}, got {self.got}"
