import discord
import asyncio
from discord.ext import commands
from aiohttp import ClientSession

class emojis:
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(pass_context = True)
    async def addemoji(ctx, emoji_name, emoji_link = ''):
        msg: discord.Message = ctx.message
        if msg.attachments:
            image = msg.attachments[0]
        elif emoji_link:
            async with session.get(emoji_link) as resp:
                image = await resp.read()
        else:
            await ctx.send("No valid emoji provided.")
            return
    
        created_emoji = await bot.create_custom_emoji(ctx.message.server, name = emoji_name, image = image)
        await ctx.send("Emoji {} created!".format(created_emoji))
          
def setup(bot):
    bot.add_cog(emojis(bot))
