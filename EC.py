
'''
Originally Base-Derived
Owner - Kaen#6390
'''
import os
import discord
from discord.ext import commands
from ext.context import CustomContext
import psutil
import re
import json
from collections import defaultdict
import datetime
import aiohttp
import requests

class NyankoBot(commands.Bot):

    def __init__(self, **attrs):
        super().__init__(command_prefix = self.get_pre)
        self.session = aiohttp.ClientSession(loop = self.loop)
        self.extentions = [x.replace('.py', '') for x in os.listdir('cogs') if x.endswith('.py')]
        self.process = psutil.Process()
        self.load_extensions()
   
    def load_extensions(self, cogs = None, path = 'cogs.'):
        '''Loading the Extentions ;)'''
        for extension in cogs or self.extentions:
            try:
                self.load_extension('{0}{1}'.format(path, extension))
                print('Loaded Extention: {}'.format(extension))
            except Exception as e:
                print('CannotLoad: {0}\n'
                      '{type(e).__name__}: {1}'.format(extension, e))

    @staticmethod
    async def get_pre(bot, message):
        '''GET THE PREFIX'''
        with open('data/config.json') as f:
            prefix = json.load(f).get('PREFIX') or "<@467973617536335872> "
        return os.environ.get('PREFIX') or prefix or 'r. '

    def restart(self):
        os.exev(sys.executable, ['python'] + sys.argv)


    @classmethod
    def init(bot, token = None):
        '''RUN THE BOT'''
        nyankobot = bot()
        with open('data/config.json') as f:
            config = json.load(f)
            if config["TOKEN"] == "your_token_here":
                token = os.environ.get("TOKEN")
                token = str(token)
            else:
                token = config["TOKEN"]
        try:
            nyankobot.run(token, bot = True, reconnect = True)
        except Exception as e:
            print(e)

    async def on_connect(self):
        print('-------------\n'+ 'Jake Logged in!')

    async def on_ready(self):
        '''SET THE UPTIME'''
        self.uptime = datetime.datetime.utcnow()
        await self.change_presence(activity=discord.Game(name="yes"))

    async def process_commands(self, message):
        '''Utilize the CustomContext subclass'''
        ctx = await self.get_context(message, cls = CustomContext)
        if ctx.command is None:
            return
        await self.invoke(ctx)
        
    async def on_message(self, m):        
        await self.process_commands(m)
      
    async def on_message_edit(self, before, after):
        await self.process_commands(after)
        
    def get_server(self, id):
        return discord.utils.get(self.guilds, id = id)

if __name__ == '__main__':
    NyankoBot.init()
