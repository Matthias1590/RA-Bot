import sys
from typing import List, Type
from bot.cogs.base import BaseCog
from bot.cogs.listeners import ListenersCog
from bot.cogs.utility import UtilityCog


OWNER_ID = 789145924235821087

DEBUG_GUILDS = [
    841473212763734027,
]

COGS: List[Type[BaseCog]] = [
    ListenersCog,
    UtilityCog,
]

TOKEN = sys.argv[1]
