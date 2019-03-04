import os
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
    async def getems(self, ctx):
         liststatic = [e for e in ctx.guild.emojis if not e.animated]
         listanimated = [e for e in ctx.guild.emojis if e.animated]
         notanim = "".join(liststatic)
         anim = "".join(listanimated)
         await ctx.send(f"**Static emotes:**\n{notanim}\n**Animated emotes:**\n{anim}")


    @commands.command()
    async def getallemojis(self, ctx):
         """gets all emojis from every server the bot is in"""
         paginator = Paginator()
         for server in self.bot.guilds:
             paginator.addLine(f'{server.name}:')
             all_emoji_names_list = ["<:" + e.name + ':' + str(e.id) + ">" for e in server.emojis]
             all_emoji_names = ' '.join(all_emoji_names_list)

             line_list = []
             while len(all_emoji_names) > 2000:
                 space_index = all_emoji_names[1500:].find(' ') + 1500
                 line_list.append(all_emoji_names[:space_index])
                 all_emoji_names = all_emoji_names[space_index:]
             else:
                 line_list.append(all_emoji_names)

             for line in line_list:
                 paginator.addLine(line)
         for page in paginator.pages:
             await ctx.send(page)
             await asyncio.sleep(1)

def setup(bot):
	bot.add_cog(general(bot))
