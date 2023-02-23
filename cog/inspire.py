import discord
from discord.ext import commands
from discord import app_commands
import datetime
import requests
import json
from google_api.spreadsheet_api import spreadsheet


class Inspire(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name='inspire', description='偉人の格言をランダムで返す。')
  async def inspire(self, interaction: discord.Interaction):
    quote = get_quote()

    # 現在時刻とユーザidをlogに記録
    contents = [str(datetime.datetime.now()), str(interaction.user.id)]
    spreadsheet.add_log(contents, 2)

    await interaction.response.send_message(quote, ephemeral=True)


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)


async def setup(bot):
  await bot.add_cog(Inspire(bot))
  print('[cog] Inspire was loaded!')
