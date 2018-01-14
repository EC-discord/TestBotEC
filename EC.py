import os
import discord
from aiohttp import ClientSession
from discord.ext import commands
import codecs
import aiohttp

bot = commands.Bot(
    command_prefix = "*",
    description = "I'm a simple man. I see a command, I call it.")


session = ClientSession(loop = bot.loop)

tokens = os.environ.get("TOKEN")


@bot.command()
async def woosh():
   await bot.say('Woosh Woosh')

@bot.command(pass_context = True)
async def addemoji(ctx, emoji_name, emoji_link = ''):
    msg: discord.Message = ctx.message
    if msg.attachments:
      await ctx.message.delete()
 
def load_extensions(self, cogs = None, path = 'cogs.'):

        '''Loading the Extentions ;)'''

        for extension in cogs or self._extentions:

            try:

                self.load_extension('{0}{1}'.format(path, extension))

                print('Loaded Extention: {}'.format(extension))

            except Exception as e:

                print('CannotLoad: {0}\n'

                      '{type(e).__name__}: {1}'.format(extension, e))
                      

                       
safe_token = "{}".format(tokens)
bot.run(safe_token)

