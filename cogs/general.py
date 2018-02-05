import os
import discord
import json
import random
from discord.ext import commands
from cleverwrap import CleverWrap


class general:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def invite(self,ctx):
        '''invite the bot :D'''

        em = discord.Embed()

        em = discord.Embed(title = "Click Here To Invite", url = "https://discordapp.com/oauth2/authorize?client_id=375138989398687746&scope=bot&permissions=305196166")
        em.colour = discord.Colour.green()
        em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/388676126383276032/390726053561368577/images_23.jpg")
        em.add_field(name = "Jake The Bot", value = """**Support Server** \nServer Link: https://discord.gg/bmeBBdd """, inline = True)
        em.set_footer(text = "Jake",icon_url = self.bot.user.avatar_url)

        await ctx.send(embed = em)



def setup(bot):
	bot.add_cog(general(bot))
