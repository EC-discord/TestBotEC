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
from io import BytesIO
import string

class Misc(commands.Cog): 
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

     @commands.command(name='emoji', aliases=['emote', 'e'])
     async def _emoji(self, ctx, *, emoji : discord.Emoji):
        '''displays an enlarged pic of an emoji
        __**Parameters**__
        • emoji - The name(case sensitive) or id of the emoji
        '''
        async with ctx.session.get(emoji.url) as resp:
            image = await resp.read()
        if emoji.animated:
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, "emote.gif"))
        else:
            with io.BytesIO(image) as file:
                await ctx.send(file = discord.File(file, "emote.png"))
        await ctx.delete()
        
     @commands.command()
     async def picsu(self, ctx, *, member : discord.Member = None):
         """gets the profile pic of the user"""
         mem = member or ctx.author
         avatar = mem.avatar_url_as(format = None, static_format = 'png')
         if ctx.author.guild_permissions.embed_links == True:
             em = discord.Embed(url = avatar, color = 0xffd500)
             em.set_author(name = mem.name, icon_url = avatar)
             em.set_image(url = avatar)
             await ctx.send(embed = em)
         else:
             await ctx.send(avatar)
     
     @commands.command()
     async def plt(self, ctx, *, words):
        """PigLatin Translator"""
        translated = []
        words1 = words.split()
        for word in words1:
            py = "ay"
            first_word = word[0]
            if word is None:
                await ctx.send("Type something O:")
            else:
                new_word = word[1:]
                new_word = new_word + first_word + py
                kappa = translated.append(new_word)
        platin = ' '.join(translated)
        em = discord.Embed(color = 0xffd500)
        em.description = platin
        if ctx.author.guild_permissions.embed_links == True:
            await ctx.send(embed = em)
        else:
            await ctx.send(platin)
          
def setup(bot):
    bot.add_cog(Misc(bot))
