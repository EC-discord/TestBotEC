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

class Misc: 
     def __init__(self, bot):
         self.bot = bot
     
     @commands.command(aliases=['bn'])
     async def binary(self, ctx, number:int = None):
         '''converts the given number into binary'''
         if number is None:
             await ctx.send('Enter a number :D')
         else:
             num = bin(number)[2:]
             if ctx.author.guild_permissions.embed_links == True:
                 em = discord.Embed(color = 0xffd500)
                 em.description = num
                 await ctx.send(embed = em)
             else:
                 await ctx.send(num)
            
     @commands.command(aliases=['hex'])
     async def hexu(self, ctx, number:int = None):
         '''returns hexadecimal form of the specified number'''
         if number is None:
             await ctx.send('Enter a number :D')
         else:
             await ctx.send(hex(number)[2:])
     
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
        
     @commands.command()
     async def picsu(self, ctx, *, member : discord.Member = None):
         """gets the profile pic of the user"""
         if ctx.author.guild_permissions.manage_messages == True:
             await ctx.message.delete()
         mem = member or ctx.author
         avatar = mem.avatar_url_as(format = "png")
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
