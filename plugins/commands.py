# Author: Doreamonfans (https://github.com/disneyteam77) (@doreamonfans1)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.info import *

START_TEXT = """Hello {}
I am Disney Team movie information finder bot.
> `I can find information of all movies.`
Made In By  By @doreamonfans1"""

JOIN_BUTTONS = [
    InlineKeyboardButton(
        text='Updates Channel',
        url='https://telegram.me/disneygrou'
    )
]

BUTTONS = InlineKeyboardMarkup(
    [JOIN_BUTTONS]
)

@Client.on_message(filters.private & filters.command(["start"]), group=-1)
async def start(bot, update):
    if update.text == "/start":
        await update.reply_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )
    else:
        movie = update.text.split(" ", 1)[1]
        await get_movie(bot, update, movie)
