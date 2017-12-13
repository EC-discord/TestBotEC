import os
import discord
from aiohttp import ClientSession
from discord.ext import commands

bot = commands.Bot(
    command_prefix = "*",
    description = "I'm a simple man. I see a command, I call it.")


session = ClientSession(loop = bot.loop)

tokens = os.environ.get("TOKEN")


@bot.command()
async def woosh():
   await bot.say('Woosh Woosh')

@bot.command(pass_context = True)
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

async def editemoji(ctx, emoji_name):
    msg: discord.message = ctx.message

@bot.command(aliases=['attach'])
async def linkify(self,ctx):
        link = ctx.message.attachments[0].url
        await ctx.send(link)
    

safe_token = "{}".format(tokens)
bot.run(safe_token)

