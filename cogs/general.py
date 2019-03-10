import discord
import json
import random
from discord.ext import commands
from cleverwrap import CleverWrap
import asyncio
from ext.paginator import Paginator
import requests


class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def invite(self,ctx):
        '''invite the bot :D'''
        em = discord.Embed(color = 0xffd500, title = "Click Here To Invite", url = "https://discordapp.com/oauth2/authorize?client_id=467973617536335872&scope=bot&permissions=305196166")
        em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/274387797140570112/409323858437472257/image.jpg")
        em.add_field(name = "Jake The Bot", value = "A bot made by Mirai", inline = True)
        em.set_footer(text = "Jake",icon_url = self.bot.user.avatar_url_as(static_format='png'))
        await ctx.send(embed = em)

    @commands.command()
    async def say(self, ctx, *, text = None):
        await ctx.send(text)
        await ctx.message.delete()
	
    @commands.command()
    async def emsay(self, ctx, *, args = None):
        if args is None:
            await ctx.send("Type something (' - '   )")
        else:
	        em = discord.Embed(color=0xffd500)
	        em.description = args
	        await ctx.send(embed = em)
     
    @commands.command()
    async def getems(self, ctx, *, guild = None):
        if int(guild):
          guild = discord.utils.get(self.bot.guilds, id = guild)
        elif guild is not None:
          guild = discord.utils.get(self.bot.guilds, name = guild)
        elif guild is None:
          guild = ctx.guild
        liststatic = [f"{e}" for e in guild.emojis if not e.animated]
        listanimated = [f"{e}" for e in guild.emojis if e.animated]
        notanim = " ".join(liststatic)
        anim = " ".join(listanimated)
        await ctx.send(f"**Static emotes:**")
        await ctx.send(f"{notanim}")
        await ctx.send(f"**Animated emotes:**")
        await ctx.send(f"{anim}")

def setup(bot):
	bot.add_cog(general(bot))
