import argparse
import discord
from bot.constants.discord import bot as constants
from bot.managers.manager import Manager
from bot.utils.logger import Logger

parser = argparse.ArgumentParser()
parser.add_argument("token", type=str, help="The token to run the bot with.")
parser.add_argument("logurl", type=str, help="The webhook url to send logs to.")
parser.add_argument("-d", "--debug", action="store_true", help="Enables debug mode.")
args = parser.parse_args()

intents = discord.Intents.default()

bot = discord.Bot(
    debug_guilds=[constants.DEBUG_GUILD if args.debug else constants.PRODUCTION_GUILD],
    intents=intents,
    owner_id=constants.OWNER_ID,
)

manager = Manager()

logger = Logger(webhook_url=args.logurl)


# TODO: Get rid of this, it's just for debugging
@bot.event
async def on_ready() -> None:
    await logger.debug("Bot online.")


for cog in constants.COGS:
    bot.add_cog(cog(bot=bot, manager=manager, logger=logger))


bot.run(args.token)
