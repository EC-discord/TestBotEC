import discord
import asyncio
from discord.ext import commands
import aiohttp

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
            await bot.say("No valid emoji provided.")
            return
    
        created_emoji = await bot.create_custom_emoji(ctx.message.server, name = emoji_name, image = image)
        await bot.say("Emoji {} created!".format(created_emoji))
          
def setup(bot):
    bot.add_cog(emojis(bot))
