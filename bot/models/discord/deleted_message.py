import datetime
import discord

# TODO: Just have the original message as a field and the deleted data as other fields instead of inheriting discord.Message
class DeletedMessage(discord.Message):
    deleted_at: datetime.datetime
