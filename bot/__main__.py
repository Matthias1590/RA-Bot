import argparse
import discord
from bot.constants.discord import bot as constants
from bot.managers.manager import Manager

parser = argparse.ArgumentParser()
parser.add_argument("token", type=str, help="The token to run the bot with.")
parser.add_argument("-d", "--debug", action="store_true", help="Enables debug mode.")
args = parser.parse_args()

intents = discord.Intents.default()

bot = discord.Bot(
    debug_guilds=[constants.DEBUG_GUILD if args.debug else constants.PRODUCTION_GUILD],
    intents=intents,
    owner_id=constants.OWNER_ID,
)

manager = Manager()


# TODO: Get rid of this, it's just for debugging
@bot.event
async def on_ready() -> None:
    print(f"Running bot as {bot.user} in {'debug' if args.debug else 'release'} mode")


for cog in constants.COGS:
    bot.add_cog(cog(bot=bot, manager=manager))


bot.run(args.token)
