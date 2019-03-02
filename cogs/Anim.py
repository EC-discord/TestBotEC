import discord
import asyncio
from discord.ext import commands

class Anim(commands.Cog): 
     def __init__(self, bot):
          self.bot = bot
     
     @commands.command()
     async def cathi(self, ctx):
         msg = await ctx.send("""ຸ 　　　＿＿_＿＿
　　／　／　  ／|"
　　|￣￣￣￣|　|
　　|　　　　|／
　　￣￣￣￣""")
         await asyncio.sleep(1.3)
         await msg.edit(content="""ຸ 　　　Hi...♡
 　   　 ∧＿∧＿_
　　／(´･ω･`)  ／＼
　／|￣￣￣￣|＼／
　　|　　　　|／
　　￣￣￣￣""")
         await asyncio.sleep(1.3)
         for i in range(1 ,6 , 1):
             await msg.edit(content="""ຸ 　　　＿＿_＿＿
　　／　／　  ／|"
　　|￣￣￣￣|　|
　　|　　　　|／
　　￣￣￣￣""")
             await asyncio.sleep(1.3)
             await msg.edit(content="""ຸ 　　　Hi...♡
 　   　 ∧＿∧＿_
　　／(´･ω･`)  ／＼
　／|￣￣￣￣|＼／
　　|　　　　|／
　　￣￣￣￣""")
             await asyncio.sleep(1.3)
             
     
     @commands.command()
     async def catsu(self, ctx):
         msg = await ctx.send("""{  |  |  }
( ^ - ^ )
( u   u )～""")
         await asyncio.sleep(1)
         await msg.edit(content="""{ \  / }
( ^ - ^ )
( u   u )～""")
         await asyncio.sleep(1)
         for i in range(1, 10, 1):
             await msg.edit(content="""{  |  |  }
( ^ - ^ )
( u   u )～""")
             await asyncio.sleep(1)
             await msg.edit(content="""{ \  / }
( ^ - ^ )
( u   u )～""")
             await asyncio.sleep(1)
     
     @commands.command()
     async def virus(self, ctx, member : discord.Member = None, *, virus : str = "trojan horse"):
         wheelList = ['/', '-', '\\', '|']
         wheelIter = iter(wheelList)
         msg = await ctx.send('`Preparing virus`')
         for i in range(2, 17, 2):
             try:
                 wheel = next(wheelIter)
             except StopIteration:
                 wheelIter = iter(wheelList)
                 wheel = next(wheelIter)
             await msg.edit(content=f"`[{('▓' * i).ljust(16)}] {wheel} {virus}-virus.exe Packing files.`")
             await asyncio.sleep(1)
         await msg.edit(content=f"`Injecting virus.   |`")
         await asyncio.sleep(1)
         await msg.edit(content=f"`Injecting virus..  /`")
         await asyncio.sleep(1)  
         await msg.edit(content=f"`Injecting virus... -`")
         await asyncio.sleep(1)
         await msg.edit(content=f"`Successfully Injected {virus}-virus.exe into {member.name}`")

     async def boom(self, ctx):
         for c in range(5, -1, -1):
             await message.edit(content=f"`THIS MESSAGE WILL SELF DESTRUCT IN {c}`")
             await asyncio.sleep(1)
         await message.edit(content="💣")
         await asyncio.sleep(1)
         await message.edit(content="💥")
          
     
     @commands.command()
     async def table(self, ctx):
         m = await ctx.send(content="`(\°-°)\     ┬─┬`")
         await asyncio.sleep(1)
         await m.edit(content="`(\°□°)\     ┬─┬`")
         await asyncio.sleep(1)
         await m.edit(content="`(-°□°)-     ┬─┬`")
         await asyncio.sleep(1)
         await m.edit(content="`(╯°□°)╯     ┬─┬`")
         await asyncio.sleep(1)
         wheelList = [']', '┻━┻', '[',  '┬─┬']
         wheelIter = iter(wheelList)
         for i in range(7, 39, 4):
             try:
                 wheel = next(wheelIter)
             except StopIteration:
                 wheelIter = iter(wheelList)
                 wheel = next(wheelIter)
             await m.edit(content=f"`(\°-°)\{(i * ' ')}{wheel}`")
             await asyncio.sleep(1)
       
     @commands.command()
     async def warning(self, ctx):
         msg = await ctx.send("`LOAD !! WARNING !! SYSTEM OVER`")
         await asyncio.sleep(1)
         await msg.edit(content="`OAD !! WARNING !! SYSTEM OVERL`")
         await asyncio.sleep(1)
         await msg.edit(content="`AD !! WARNING !! SYSTEM OVERLO`")
         await asyncio.sleep(1)
         await msg.edit(content="`D !! WARNING !! SYSTEM OVERLOA`")
         await asyncio.sleep(1)
         await msg.edit(content="`! WARNING !! SYSTEM OVERLOAD !`")
         await asyncio.sleep(1)
         await msg.edit(content="`WARNING !! SYSTEM OVERLOAD !!`")
         await asyncio.sleep(1)
         await msg.edit(content="`ARNING !! SYSTEM OVERLOAD !! W`")
         await asyncio.sleep(1)
         await msg.edit(content="`RNING !! SYSTEM OVERLOAD !! WA`")
         await asyncio.sleep(1)
         await msg.edit(content="`NING !! SYSTEM OVERLOAD !! WAR`")
         await asyncio.sleep(1)
         await msg.edit(content="`ING !! SYSTEM OVERLOAD !! WARN`")
         await asyncio.sleep(1)
         await msg.edit(content="`NG !! SYSTEM OVERLOAD !! WARNI`")
         await asyncio.sleep(1)
         await msg.edit(content="`G !! SYSTEM OVERLOAD !! WARNIN`")
         await asyncio.sleep(1)
         await msg.edit(content="`!! SYSTEM OVERLOAD !! WARNING`")
         await asyncio.sleep(1)
         await msg.edit(content="`! SYSTEM OVERLOAD !! WARNING !`")
         await asyncio.sleep(1)
         await msg.edit(content="`SYSTEM OVERLOAD !! WARNING !!`")
         await asyncio.sleep(1)
         await msg.edit(content="`IMMINENT SHUT-DOWN IN 0.5 SEC!`")
         await asyncio.sleep(1)
         await msg.edit(content="`WARNING !! SYSTEM OVERLOAD !!`")
         await asyncio.sleep(1)
         await msg.edit(content="`IMMINENT SHUT-DOWN IN 0.2 SEC!`")
         await asyncio.sleep(1)
         await msg.edit(content="`SYSTEM OVERLOAD !! WARNING !!`")
         await asyncio.sleep(1)
         await msg.edit(content="`IMMINENT SHUT-DOWN IN 0.01 SEC!`")
         await asyncio.sleep(1)
         await msg.edit(content="`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯`")
         await asyncio.sleep(1)
         await msg.edit(content="`CTRL + R FOR MANUAL OVERRIDE..`")
     
     @commands.command()
     async def woah(self, ctx):
         m = await ctx.send("(   ' O ')")
         await asyncio.sleep(1)
         await m.edit(content="(  ' O ' )")
         await asyncio.sleep(1)
         await m.edit(content="( ' O '  )")
         await asyncio.sleep(1)
         await m.edit(content="(' O '   )")
         await asyncio.sleep(1)
         await m.edit(content="( ' O '  )")
         await asyncio.sleep(1)
         await m.edit(content="(  ' O ' )")
         await asyncio.sleep(1)
         await m.edit(content="(   ' O ')")
     
     @commands.command()
     async def deadchat(self, ctx):
         msg = await ctx.send('DEAD CHAT')
         wheelList = ['T DEAD CHA', 'AT DEAD CH', 'HAT DEAD C', 'CHAT DEAD', 'D CHAT DEA', 'AD CHAT DE', 'EAD CHAT D', 'DEAD CHAT']
         wheelIter = iter(wheelList)
         for i in range(1, 10, 1):
             try:
                 wheel = next(wheelIter)
             except StopIteration:
                 wheelIter = iter(wheelList)
                 wheel = next(wheelIter)
             await msg.edit(content=f"`{wheel}`")
             await asyncio.sleep(1)
    
def setup(bot):
   bot.add_cog(Anim(bot))
