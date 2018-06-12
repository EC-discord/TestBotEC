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
        if ctx.author.guild_permissions.manage_emojis == True:
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
        else:
            await ctx.send("You do not have the **Manage emojis** perm")
        
    @commands.command()
    async def getemoji(self, ctx, emoji_name):
        for guilds in self.bot.guilds:
            emoji = discord.utils.get(guilds.emojis, name=emoji_name)
        await ctx.send(emoji)
    
    @commands.command()
    async def emojiurl(self, ctx, emoji: discord.Emoji):
        id = emoji.id
        await ctx.send(f"https://cdn.discordapp.com/emojis/{id}.png?v=1")
          
def setup(bot):
    bot.add_cog(emojis(bot))
