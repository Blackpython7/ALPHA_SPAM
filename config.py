import logging

from telethon import TelegramClient

from os import getenv
from RAUSHAN.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = "29994788"
API_HASH = "fde39a82c05d1ea6aba52b4b36b2e205"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "cb2147ff-d743-49fc-a18e-6a40aec75e77")

BOT_TOKEN = getenv("BOT_TOKEN", default=7785652335:AAE90U9sXln67lTR0iOzt2Cz6dR5uNFIrzw)
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=7990059942:AAFUhWmZ8eiwpO7uauwL-iSDd9b8k_FWUhU)
BOT_TOKEN3 = getenv("BOT_TOKEN3", default=7810752396:AAGAPOl5HliuangEtqBEVlc1UZ13R3xCFeI)
BOT_TOKEN4 = getenv("BOT_TOKEN4", default=7940821390:AAG4Nsa4NKKBugMRXBQqky0ZsbyK_Co_cAI)
BOT_TOKEN5 = getenv("BOT_TOKEN5", default=8177085196:AAEv_LqVweB1xYM28NwT8N32sprJQ0eDfss)
BOT_TOKEN6 = getenv("BOT_TOKEN6", default=7319062681:AAEBp6GPo9lYN_FeUfduGvpLfDcMcieHrKo)
BOT_TOKEN7 = getenv("BOT_TOKEN7", default=8074413331:AAHnUj8wHbJtNBL0dRkNjK2gagFggA3IhiQ)
BOT_TOKEN8 = getenv("BOT_TOKEN8", default=8156681498:AAGD8hNefu6mbDkePOBEAsENJ9a0_72mYUY)
BOT_TOKEN9 = getenv("BOT_TOKEN9", default=7762885462:AAGKbzGGuPmcX2tk9Zs56dV0s1Y-6N982Dg)
BOT_TOKEN10 = getenv("BOT_TOKEN10", default=8195599372:AAFfSA3uslyTNhGNoJ25ugEz2bf1r0NRyp0)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7398522183 8123663143 6523652993 6853231635").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6219473300"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
