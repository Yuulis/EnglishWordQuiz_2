import discord
from discord.ext import commands
from discord import app_commands
import datetime
from google_api.spreadsheet_api import spreadsheet


class Register(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name='register', description='ユーザ登録を行います。')
  async def register(self, interaction: discord.Interaction):
    userList = spreadsheet.get_userList()
    if str(interaction.user.id) not in userList:
      spreadsheet.add_userList(interaction.user.id)

      contents = [
        str(datetime.datetime.now()),
        str(interaction.user.id), 'register', 'Successfully registered. '
      ]
      spreadsheet.add_log(contents)

      await interaction.response.send_message('ユーザ登録を完了しました。', ephemeral=True)

    else:
      contents = [
        str(datetime.datetime.now()),
        str(interaction.user.id), 'register', 'Already registered.'
      ]
      spreadsheet.add_log(contents)

      await interaction.response.send_message('既にユーザ登録はされています。',
                                              ephemeral=True)


async def setup(bot):
  await bot.add_cog(Register(bot))
  print('[cog] Register was loaded!')
