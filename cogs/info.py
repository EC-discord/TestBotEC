import discord
from discord.ext import commands
from ext import embedtobox
import datetime
import asyncio
import psutil
import random
import os
import io
import json


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['sicon'], no_pm=True)
    async def serverlogo(self, ctx):
        '''Return the server's icon url.'''
        icon = ctx.guild.icon_url_as(format='png')
        color = await ctx.get_dominant_color(icon)
        server = ctx.guild
        em = discord.Embed(color=color, url=icon)
        em.set_author(name=server.name, icon_url=icon)
        em.set_image(url=icon)
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            em_list = await embedtobox.etb(em)
            for page in em_list:
                await ctx.send(page)
            try:
                async with ctx.session.get(icon) as resp:
                    image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, 'serverlogo.png'))
            except discord.HTTPException:
                await ctx.send(icon)

    @commands.command(aliases=['server','si','svi'], no_pm=True)
    @commands.guild_only()
    async def serverinfo(self, ctx, server_id : int=None):
        '''Server Info'''
        server = self.bot.get_server(id=server_id) or ctx.guild
        total_users = len(server.members)
        online = len([m for m in server.members if m.status != discord.Status.offline])
        text_channels = len([x for x in server.channels if isinstance(x, discord.TextChannel)])
        voice_channels = len([x for x in server.channels if isinstance(x, discord.VoiceChannel)])
        categories = len(server.channels) - text_channels - voice_channels
        passed = (ctx.message.created_at - server.created_at).days
        created_at = "Created: {}. {} days ago.".format(server.created_at.strftime("%d %b %Y"), passed)
        colour = await ctx.get_dominant_color(server.icon_url)
        data = discord.Embed(description=created_at,colour=colour)
        data.add_field(name="Region", value=str(server.region), inline = False)
        data.add_field(name="Users", value="{}/{}".format(online, total_users), inline = False)
        data.add_field(name="Text Channels", value=text_channels, inline = False)
        data.add_field(name="Voice Channels", value=voice_channels, inline = False)
        data.add_field(name="Categories", value=categories, inline = False)
        data.add_field(name="Roles", value=len(server.roles), inline = False)
        data.add_field(name="Owner", value=str(server.owner), inline = False)
        data.set_footer(text="Server ID: " + str(server.id))
        data.set_author(name=server.name, icon_url=None or server.icon_url_as(format='png'))
        data.set_thumbnail(url=None or server.icon_url_as(format='png'))    
        try:
            await ctx.send(embed=data)
        except discord.HTTPException:
            em_list = await embedtobox.etb(data)
            for page in em_list:
                await ctx.send(page)

    @commands.command(aliases=['ui'], no_pm=True)
    @commands.guild_only()
    async def user(self, ctx, *, member : discord.Member=None):
        '''Gets the Users Information'''
        server = ctx.guild
        user = member or ctx.message.author
        avi = user.avatar_url
        roles = sorted(user.roles, key=lambda c: c.position)

        for role in roles:
            if str(role.color) != "#000000":
                color = role.color
        if 'color' not in locals():
            color = 0

        rolenames = ', '.join([r.name for r in roles if r.name != "@everyone"]) or 'None'
        time = ctx.message.created_at
        passed = (ctx.message.created_at - user.created_at).days
        created_at = "{}.  **({})** days ago.".format(user.created_at.strftime("%d %b %Y"), passed)
        passed1 = (ctx.message.created_at - user.joined_at).days
        joined_at = "{}.  **({})** days ago.".format(user.joined_at.strftime("%d %b %Y"), passed1)
        member_number = sorted(server.members, key=lambda m: m.joined_at).index(user) + 1
        em = discord.Embed(colour=color, timestamp=time)
        em.set_thumbnail(url=avi)
        em.add_field(name='Name:', value=user.name, inline = True)
        em.add_field(name='NickName:', value=user.nick, inline = True)
        em.add_field(name='Member No:',value=str(member_number), inline = False)
        em.add_field(name='Status:', value=user.status, inline = False)
        #em.add_field(name='Account Created:', value=user.created_at.__format__('%A, %d. %B %Y'), inline = False)
        em.add_field(name='Account Created:', value= created_at, inline = False)
        #em.add_field(name='Join Date:', value=user.joined_at.__format__('%A, %d. %B %Y'), inline = False)
        em.add_field(name='Join Date:', value=joined_at, inline = False)
        em.add_field(name='Roles:', value=rolenames, inline=True)
        em.set_footer(text='User ID: '+str(user.id))
        em.set_author(name=user, icon_url=server.icon_url_as(format='png'))
        em.set_thumbnail(url = user.avatar_url_as(format = None, static_format = 'png'))
        await ctx.send(embed=em)

    @commands.command(aliases=['8ball'])
    async def ask(self, ctx, *, question=None):
        with open('data/answers.json') as f:
            choices = json.load(f)
        author = ctx.message.author
        emb = discord.Embed()
        emb.color = await ctx.get_dominant_color(url=author.avatar_url)
        emb.set_author(name ="Prediction" ,icon_url = author.avatar_url_as(static_format = 'png'))
        emb.add_field(name='\N{BILLIARDS} Your answer:', value=random.choice(choices), inline=True)
        await ctx.send(embed=emb)


    @commands.command(aliases=['bot', 'info'])
    async def about(self, ctx):
        '''About The bot, info, usage, process'''
        about = """created by EC#7115, **Support Server:** https://discord.gg/bmeBBdd"""
        colorsu = await ctx.get_dominant_color(ctx.author.avatar_url)
        embed = discord.Embed(color = colorsu)
        embed.set_author(name='Jake', icon_url=ctx.author.avatar_url_as(format='png'))
        total_members = sum(1 for _ in self.bot.get_all_members())
        total_online = len({m.id for m in self.bot.get_all_members() if m.status is discord.Status.online})
        total_unique = len(self.bot.users)



        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)


        fmt = '{h}h {m}m {s}s'
        if days:
            fmt = '{d}d ' + fmt
        uptime = fmt.format(d=days, h=hours, m=minutes, s=seconds)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/274387797140570112/409323858437472257/image.png")
        embed.add_field(name='Owner', value='Mirai#6538', inline = False)
        embed.add_field(name='About', value=about, inline = False)
        embed.add_field(name='Uptime', value=uptime, inline = False)
        embed.add_field(name='Guilds', value=len(self.bot.guilds), inline = False)
        embed.add_field(name='Total Users (Online/Total)', value=f'{total_online}/{total_unique}', inline = False)
        memory_usage = self.bot.process.memory_full_info().uss / 1024**2
        cpu_usage = self.bot.process.cpu_percent() / psutil.cpu_count()
        embed.add_field(name='Process: ', value=f'{memory_usage:.2f} MiB\n{cpu_usage:.2f}% CPU', inline = False)
        embed.set_footer(text="""(👍' - ')👍""", icon_url = self.bot.user.avatar_url_as(static_format = "png"))
        await ctx.send(embed=embed)



def setup(bot):
	bot.add_cog(Information(bot))
