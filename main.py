from keep_alive import keep_alive
import discord
from discord_slash import SlashCommand, SlashContext
import os
import requests
import json
import gspread
import datetime
from google.oauth2 import service_account
from google_api import get_secrets

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

credentials = get_secrets.load_user_secrets_from_local()
gc = gspread.authorize(credentials)

# log用スプレッドシートの取得
book_log = gc.open_by_key(os.getenv('SHEET_KEY_LOG'))
sheet_log = book_log.sheet1

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = [
  "Cheer up!", "Hang in there.", "You are a great person / bot!"
]


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
# ユーザ発言時
async def on_message(message):
  # bot自身の時はスルー
  if message.author == client.user:
    return

  # 発言が"$inspire"の時
  if message.content.startswith('$inspire'):
    quote = get_quote()

    # ユーザidをlogに記録
    sheet_log.insert_row([str(datetime.datetime.now()), str(message.author.id)], 2)
    await message.channel.send(quote)


keep_alive()
client.run(os.getenv('TOKEN'))

try:
  keep_alive()
  client.run(os.getenv('TOKEN'))

except Exception as e:
  print(str(e))
  os.system("kill 1")
