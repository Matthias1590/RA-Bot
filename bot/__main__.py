import discord
from bot.constants.discord import bot as constants
from bot.managers.manager import Manager

intents = discord.Intents.default()

bot = discord.Bot(
    debug_guilds=constants.DEBUG_GUILDS,
    intents=intents,
    owner_id=constants.OWNER_ID,
)

manager = Manager()


# TODO: Get rid of this, it's just for debugging
@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user}")


for cog in constants.COGS:
    bot.add_cog(cog(bot=bot, manager=manager))


bot.run(constants.TOKEN)
