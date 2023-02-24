import discord
from discord.ext import commands
from discord import app_commands
import datetime
import requests
import json
from google_api.spreadsheet_api import spreadsheet


class Register(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name='register', description='ユーザ登録を行います。')
  async def inspire(self, interaction: discord.Interaction):
    quote = get_quote()

    # logに記録
    contents = [str(datetime.datetime.now()), str(interaction.user.id), 'register']
    spreadsheet.add_log(contents, 2)

    await interaction.response.send_message(quote, ephemeral=True)


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)


async def setup(bot):
  await bot.add_cog(Register(bot))
  print('[cog] Register was loaded!')
