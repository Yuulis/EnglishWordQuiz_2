import discord
from discord.ext import commands
import os
import asyncio
from keep_alive import keep_alive

INTENTS = discord.Intents.all()
INTENTS.message_content = True
bot = commands.Bot(command_prefix='/', intents=INTENTS)


# Cog読み込み
async def setup_hook():
  cogs = os.listdir('./cog')
  for cog in cogs:
    if (cog.endswith('.py')):
      await bot.load_extension(f'cog.{cog[:-3]}')


# bot起動
try:
  keep_alive()
  asyncio.run(setup_hook())

except Exception as e:
  print(str(e))
  os.system("kill 1")


@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  await bot.tree.sync()


bot.run(os.getenv('TOKEN'))
