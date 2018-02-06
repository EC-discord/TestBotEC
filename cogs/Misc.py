import discord
from discord.ext import commands
from discord.ext.commands import TextChannelConverter
from contextlib import redirect_stdout
from ext.utility import load_json
from urllib.parse import quote as uriquote
from lxml import etree
from ext import fuzzy
from ext import embedtobox
from PIL import Image
import unicodedata
import traceback
import textwrap
import aiohttp
import inspect
import asyncio
import time
import re
import io
import os
import random
from mtranslate import translate
from io import BytesIO
import string

class Misc: 
     def __init__(self, bot):
         self.bot = bot
     
     def getColor(self, colorHex):
        return discord.Colour(int(f'0x{colorHex}', 16))

     def randomcolor(self):
       color = ''.join([random.choice(string.hexdigits) for _ in range(6)])
       return self.getColor(color)  

     @commands.command()
     async def rc(self, ctx):
        '''Generates a random color'''
        file = io.BytesIO()
        color = self.randomcolor()
        Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
        file.seek(0)
        em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
        em.set_image(url='attachment://color.png')
        await ctx.send(file=discord.File(file, 'color.png'), embed=em)

     
     @commands.command()
     async def getchanid(self, ctx):
         lel = ctx.channel.id
         await ctx.send(lel)

     @commands.command()
     async def emoji(ctx, *, emoji: str):
         """send emoji pic"""
         emoji = emoji.split(":")
         emoji_check = self.check_emojis(ctx.bot.emojis, emoji)
         if emoji_check[0]:
             emo = emoji_check[1]
         else:
             emoji = [e.lower() for e in emoji]
             if emoji[0] == "<" or emoji[0] == "":
                 emo = discord.utils.find(lambda e: emoji[1] in e.name.lower(), ctx.bot.emojis)
             else:
                 emo = discord.utils.find(lambda e: emoji[0] in e.name.lower(), ctx.bot.emojis)
             if emo == None:
                 em = discord.Embed(title="None", description="No emoji found.")
                 em.color = await ctx.get_dominant_color(ctx.author.avatar_url)
                 await ctx.send(embed=em)
                 return
         async with ctx.session.get(emo.url) as resp:
             image = await resp.read()
         with io.BytesIO(image) as file:
             await ctx.message.delete()
             await ctx.send(file=discord.File(file, 'emote.png'))
        
def setup(bot):
    bot.add_cog(Misc(bot))
