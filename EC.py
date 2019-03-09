
'''
Originally Base-Derived
Owner - Mirai#6898
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

class jakeBot(commands.Bot):
    '''
    A Bot Made by ~ Mirai#6898 Denka#8264 and Quanta#5556
    '''
    mentions_transforms = {
          '@everyone': '@\u200beveryone',
          '@here': '@\u200bhere'
    }
    mention_pattern = re.compile('|'.join(mentions_transforms.keys()))

    def __init__(self, **attrs):
        super().__init__(command_prefix = self.get_pre)
        self.session = aiohttp.ClientSession(loop = self.loop)
        self._extentions = [x.replace('.py', '') for x in os.listdir('cogs') if x.endswith('.py')]
        self.process = psutil.Process()
        self.load_extensions()
   
    def load_extensions(self, cogs = None, path = 'cogs.'):
        '''Loading the Extentions ;)'''
        for extension in cogs or self._extentions:
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
        jakebot = bot()
        with open('data/config.json') as f:
            config = json.load(f)
            if config["TOKEN"] == "your_token_here":
                token = os.environ.get("TOKEN")
                token = str(token)
            else:
                token = config["TOKEN"]
        try:
            jakebot.run(token, bot = True, reconnect = True)
        except Exception as e:
            print(e)

    async def on_connect(self):
        print('-------------\n'+ 'Jake Logged in!')

    async def on_ready(self):
        '''SET THE UPTIME'''
        self.uptime = datetime.datetime.utcnow()
        server = str(+len(self.guilds))
        await self.change_presence(activity=discord.Game(name="jake help (' O '   ) O:"))

    async def process_commands(self, message):
        '''Utilize the CustomContext subclass'''
        ctx = await self.get_context(message, cls = CustomContext)
        if ctx.command is None:
            return
        await self.invoke(ctx)
    
    async def on_message_delete(self, message):
        guild = self.get_server(485764935222296586)
	    log_channel = guild.get_channel(486025207195369482)
	    name = message.author.nick or message.author.name
	    async with self.session.get(message.author.avatar_url_as(static_format = "png")) as resp:
	        image = await resp.read()
	    wb = await log_channel.create_webhook(name = name, avatar = image)
	    await wb.send(`message.content`)
        await wb.delete()
      
    async def on_message_edit(self, before, after):
        await self.process_command(after)

    def get_server(self, id):
        return discord.utils.get(self.guilds, id = id)

if __name__ == '__main__':
    jakeBot.init()
