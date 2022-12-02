import requests
import asyncio
from bs4 import BeautifulSoup as BS
from pprint import pprint
import urllib
from urllib.request import urlopen
from urllib.parse import quote as urlquote
from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardMarkup
from pyromod import listen
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import CallbackQuery
import shutil
import os
import re
import urllib.request
import time
import json
import time
import random
from pyrogram import enums
from pyrogram.errors import BadRequest
from config import Config as C
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
import pyrogram



import requests
import asyncio
from bs4 import BeautifulSoup as BS
from pprint import pprint
import urllib
from urllib.request import urlopen
from urllib.parse import quote as urlquote
from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardMarkup
# from pyromod import listen
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import CallbackQuery
import shutil
import os
import re
import urllib.request
import time
import json
import time
import random
from pyrogram import enums
from pyrogram.errors import BadRequest
from config import Config as C
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
import pyrogram



from text import p
import random
app = Client("bot", C.API_ID, C.API_HASH, bot_token=C.TOKEN)
@app.on_message(filters.private &  filters.command(["start"]))
async def start(bot, message):
     await message.reply('hi')
  

@app.on_inline_query()
async def inline_search(bot, query: InlineQuery):



    #THE QUERRY SHOULD BE END WITH SPACE
    search = query.query.strip()
    print(search)
    t = '‏🗣⁉️ {}\n\n‏👁 {}'.format(search,random.choice(p))
    await query.answer(
        results=[
            InlineQueryResultArticle(title=search,
                input_message_content=InputTextMessageContent(
                    t
                ))],cache_time=1)

    



# @app.on_callback_query()
# async def cm(c, query):
#   print(query)
#   print(query.data)

#   await app.edit_inline_text(query.inline_message_id, 'در حال دریافت اطلاعات ')
#   a = gp(query.data)
#   print(a)
  
#   texti = get_data(query.data)+'\n'+f'[⁪⁬⁮⁮⁮ ⁪⁬⁮⁮⁮⁮⁪⁬⁮⁮⁮⁮]({a})'

#   await app.edit_inline_text(query.inline_message_id, texti)



@app.on_message(filters.command(["i"]) & filters.private)
async def find(c,ms):
 pass


@app.on_message(filters.private &  filters.command(["p"]))
async def price1(c, m):
 
   pass
     

@app.on_message(filters.private &  filters.command(["help"]))
async def help(c, m):
   pass
  
if __name__ == '__main__':
    print('[Bot] : listening :)')
    app.run()



