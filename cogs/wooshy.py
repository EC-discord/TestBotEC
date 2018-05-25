import discord
from discord.ext import commands

class wooshy:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.commands()
    async def embedsu(self, ctx):
        em = discord.Embed()
        em.author = (name = "bla_bla", icon_url = "https://cdn.discordapp.com/attachments/274880071779614722/449475791865118721/emote.png" )
        em.add_field = (name = "bla_bla", value = 'bla bla', inline = False)
        await ctx.send(embed = em)
    
