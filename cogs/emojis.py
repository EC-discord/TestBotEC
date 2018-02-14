import discord
import asyncio
from discord.ext import commands
from aiohttp import ClientSession

class emojis:
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command()
    async def addemoji(self, ctx, emoji_name, emoji_link = ''):
        session = ClientSession()
        msg: discord.Message = ctx.message
        if msg.attachments:
            image = msg.attachments[0]
        elif emoji_link:
            async with session.get(emoji_link) as resp:
                image = await resp.read()
        else:
            await ctx.send("No valid emoji provided.")
            return
    
        created_emoji = await ctx.guild.create_custom_emoji(name = emoji_name, image = image)
        await ctx.send("Emoji {} created!".format(created_emoji))
        
    @commands.command()
    async def getemoji(self, ctx, emoji_name):
        emoji = discord.utils.get(ctx.guild.emojis, name=emoji_name)
        await ctx.send(emoji)
        
          
def setup(bot):
    bot.add_cog(emojis(bot))
