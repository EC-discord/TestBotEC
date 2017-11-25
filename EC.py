import os
import discord
from aiohttp import ClientSession
from discord.ext import commands

bot = commands.Bot(
    command_prefix = "*",
    description = "I'm a simple man. I see a command, I call it.")

session = ClientSession(loop = bot.loop)

tokens = os.environ.get("TOKEN")

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

async def deleteemoji(ctx, emoji_name):
    delete_custom_emoji(emoji_name)

safe_token = "{}".format(tokens)
bot.run(safe_token)

