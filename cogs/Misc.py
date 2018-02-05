import discord
import asyncio
from discord.ext import commands

class Misc: 
     def __init__(bot):
          self.bot = bot


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
