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

@bot.command(pass_context = True)    
async def editemoji(ctx, emoji_name):
    msg: discord.message = ctx.message
    edited_emoji = await bot.edit_custom_emoji(ctx.message.server, name = emoji_name)
    await bot.say("Emoji {} edited!".format(edited_emoji))
    
@bot.command(pass_context=True)
    async def now(self, ctx):
        """Date time module."""
        opt = dataIO.load_json('settings/optional_config.json')
        thebool = True
        try:
            if opt['24hours'] == "true":
                thebool = True
            else:
                thebool = False
        except IndexError:
            # No 24 hour bool given so default to true
            pass
        dandt, tzerror = self.get_datetime()
        if embed_perms(ctx.message):
            em = discord.Embed(color=discord.Color.blue())
            if thebool:
                em.add_field(name=u'\u23F0 Time', value="{:%H:%M:%S}".format(dandt), inline=False)
            else:
                em.add_field(name=u'\u23F0 Time', value="{:%I:%M:%S %p}".format(dandt), inline=False)
            em.add_field(name=u'\U0001F4C5 Date', value="{:%d %B %Y}".format(dandt), inline=False)
            if tzerror:
                em.add_field(name=u'\u26A0 Warning', value="Invalid timezone specified, system timezone was used instead.", inline=False)

            await ctx.send(content=None, embed=em)
        else:
            msg = '**Local Date and Time:** ```{:Time: %H:%M:%S\nDate: %Y-%m-%d```}'.format(dandt)
            await ctx.send(self.bot.bot_prefix + msg)
        await ctx.message.delete()



safe_token = "{}".format(tokens)
bot.run(safe_token)

