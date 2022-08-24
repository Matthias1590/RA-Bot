import datetime
from bot.utils.multi_page_embed import MultiPageEmbed
from bot.utils.status_embed import StatusEmbed
from discord import ApplicationContext, slash_command
from bot.cogs.base import BaseCog
from discord.ext import commands
import discord

class UtilityCog(BaseCog):
    @slash_command(name="ping", description="Get the bot's latency.")
    async def ping(self, ctx: ApplicationContext) -> None:
        await ctx.respond(f"Pong! {round(self.bot.latency * 1000)}ms")
    
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message) -> None:  # TODO: Figure out if we should use on_raw_message_delete instead of this
        # TODO: Figure out a better way to turn a message into a deleted message
        message.deleted_at = datetime.datetime.now()

        self.manager.message.log_deleted_message(message)
    
    # TODO: Add optional channel argument (add when type checking is implemented)
    @slash_command(name="snipe", description="Get recently deleted messages in a given channel.")
    async def snipe(self, ctx: ApplicationContext) -> None:
        embed = MultiPageEmbed()

        messages = self.manager.message.get_sniped_messages(ctx.channel.id)
        page = (
            StatusEmbed()
            .set_title(f"**Deleted Messages in #{ctx.channel.name}**")
            .set_description(f"Showing **{len(messages)}** deleted message(s).")
        )
        
        for message in messages:
            (
                page
                .clear_fields()
                .add_field(discord.EmbedField("**Author**", message.author.mention))
            )

            if message.content:
                page.add_field(discord.EmbedField("**Content**", message.content))

            if message.attachments:
                page.add_field(discord.EmbedField("**Attachments**", "\n".join([attachment.url for attachment in message.attachments])))

            created_at = int(message.created_at.timestamp())
            deleted_at = int(message.deleted_at.timestamp())

            (
                page
                .add_field(discord.EmbedField("**Sent**", f"<t:{created_at}:R> (<t:{created_at}:f>)"))
                .add_field(discord.EmbedField("**Deleted**", f"<t:{deleted_at}:R> (<t:{deleted_at}:f>)"))
            )

            embed.add_page(page.build())
        
        await embed.send(ctx)
