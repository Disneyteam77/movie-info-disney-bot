# Author: Doreamonfans (https://github.com/disneyteam77) (@doreamonfans1)

import os
from pyrogram import Client

bot_token = os.environ["BOT_TOKEN"]
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

plugins = dict(
    root="plugins"
)

Bot = Client(
    "Movie-Info-Disney-Bot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=plugins
)

Bot.run()
