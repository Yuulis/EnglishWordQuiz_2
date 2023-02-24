import discord
from discord.ext import commands, tasks
import os
from keep_alive import keep_alive

INTENTS = discord.Intents.all()
INTENTS.message_content = True


class Bot(commands.Bot):

  def __init__(self):
    super().__init__(command_prefix='/', intents=INTENTS)

  async def setup_hook(self):
    cogs = os.listdir('./cog')
    for cog in cogs:
      if (cog.endswith('.py')):
        await self.load_extension(f'cog.{cog[:-3]}')

    async def close(self):
      await super().close()
      await self.session.close()

    @tasks.loop(minutes=10)
    async def background_task(self):
      print('Running background task...')

    async def on_ready(self):
      print('We have logged in as {0.user}'.format(self))
      await self.tree.sync()


# bot起動
try:
  keep_alive()

except Exception as e:
  print(str(e))
  os.system("kill 1")

bot = Bot()
bot.run(os.getenv('TOKEN'))
