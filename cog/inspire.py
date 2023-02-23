import datetime
import requests
import json
from discord.ext import commands
from google_api.spreadsheet_api import spreadsheet


class Inspire(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener(name='on_message')
  async def inspire(self, message):
    # bot自身の時はスルー
    if message.author.bot:
      return

    # 発言が"$inspire"の時
    if message.content.startswith('$inspire'):
      quote = get_quote()

      # 現在時刻とユーザidをlogに記録
      contents = [str(datetime.datetime.now()), str(message.author.id)]
      spreadsheet.add_log(contents, 2)

      await message.channel.send(quote)


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)


async def setup(bot):
  await bot.add_cog(Inspire(bot))
  print('[cog] Inspire was loaded!')
