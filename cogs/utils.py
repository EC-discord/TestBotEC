import discord
from discord.ext import commands
from discord.ext.commands import TextChannelConverter
from contextlib import redirect_stdout
from ext.utility import load_json
from urllib.parse import quote as uriquote
from lxml import etree
from ext import fuzzy
from ext import embedtobox
from PIL import Image
import unicodedata
import traceback
import textwrap
import aiohttp
import inspect
import asyncio
import time
import re
import io
import os
import random

class Utility(commands.Cog):
    '''Useful commands to make your life easier'''
    def __init__(self, bot):
        self.bot = bot
        self.lang_conv = load_json('data/langs.json')
        self._last_embed = None
        self._rtfm_cache = None
        self._last_google = None
        self._last_result = None
        
    @commands.command()
    async def banner(self, ctx, *, guild = None):
        """gets a guild's banner image
        __**Parameters**__
        • guild - the name or id of the guild
        """
        if guild is None:
            guild = ctx.guild
        elif type(guild) == int:
            guild = discord.utils.get(self.bot.guilds, id = guild)
        elif type(guild) == str:
            guild = discord.utils.get(self.bot.guilds, name = guild)
        banner = guild.banner_url_as(format = "png")
        async with ctx.session.get(str(banner)) as resp:
            image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file = discord.File(file, "banner.png"))

    async def is_owner(ctx):
       return ctx.author.id == 453941160612986880

    @commands.command()
    @commands.check(is_owner)
    async def cpres(self, ctx, status : str, Type:str = None, *, message:str = None):
        '''Sets a custom presence, the Type argument can be "playing", "streaming", "listeningto" or "watching"
        status can be "online", "dnd", "idle", "invisible"
        Example : (prefix)cpres idle watching a movie'''
        types = {"playing" : "Playing", "streaming" : "Streaming", "listeningto" : "Listening to", "watching" : "Watching"}
        stats = {"online" : discord.Status.online, "dnd" : discord.Status.dnd, "idle" : discord.Status.idle, "invisible" : discord.Status.invisible}
        em = discord.Embed(color=0x6ed457, title="Presence")
        if message is None:
            await self.bot.change_presence(status=discord.Status.online, activity= message, afk = True)
        else:
            if Type == "playing":
                await self.bot.change_presence(status=stats[status], activity=discord.Game(name=message), afk = True)
            elif Type == "streaming":
                await self.bot.change_presence(status=stats[status], activity=discord.Streaming(name=message, url=f'www.twitch.tv/{message}'), afk = True)
            elif Type == "listeningto":
                await self.bot.change_presence(status=stats[status], activity=discord.Activity(type=discord.ActivityType.listening, name=message), afk = True)
            elif Type == "watching":
                await self.bot.change_presence(status=stats[status], activity=discord.Activity(type=discord.ActivityType.watching, name=message), afk = True)
            em.description = f"Presence : {types[Type]} {message}"
            if ctx.author.guild_permissions.embed_links:
                await ctx.send(embed = em)
            else:
                await ctx.send(f"Presence : {types[Type]} {message}")


    @commands.command(name='logout')
    @commands.check(is_owner)
    async def _logout(self, ctx):
        '''
        equivalent to a restart if you are hosting the bot on heroku.
        '''
        await ctx.send('`Jake Logging out...(' - '   )`')
        await self.bot.logout()
      


    @commands.command(pass_context=True, hidden=True, name='eval')
    @commands.check(is_owner)
    async def _eval(self, ctx, *, body: str):
        """Evaluates python code"""

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result,
            'source': inspect.getsource
        }

        env.update(globals())

        body = self.cleanup_code(body)
        #await self.edit_to_codeblock(ctx, body)
        stdout = io.StringIO()
        err = out = None

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
            return await err.add_reaction('\u2049')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            if ret is None:
                if value:
                    try:
                        out = await ctx.send(f'```py\n{value}\n```')
                    except:
                        paginated_text = ctx.paginate(value)
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = await ctx.send(f'```py\n{page}\n```')
                                break
                            await ctx.send(f'```py\n{page}\n```')
            else:
                self._last_result = ret
                try:
                    out = await ctx.send(f'```py\n{value}{ret}\n```')
                except:
                    paginated_text = ctx.paginate(f"{value}{ret}")
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')

        if out:
            await out.add_reaction('\u2705') #tick
        if err:
            await err.add_reaction('\u2049') #x

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    def get_syntax_error(self, e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'
            
            
            

def setup(bot):
    bot.add_cog(Utility(bot))
