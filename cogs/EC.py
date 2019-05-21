import discord
import asyncio
from discord.ext import commands

class EC(commands.Cog):
     def __init__(self, bot):
          self.bot = bot
     
     @commands.command()
     async def kflip(self, ctx):
         """(づ｡◕‿‿◕｡)づ︵ ┻━┻"""
         await ctx.send("(づ｡◕‿‿◕｡)づ︵ ┻━┻")
     
     @commands.command()
     async def thumbs(self, ctx):
         """(👍' - ')👍"""
         await ctx.send("(👍' - ')👍")
    
     @commands.command(aliases = ["bye"])
     async def hi(self, ctx):
         """(  ^ - ^)/"""
         await ctx.send("(  ^ - ^)/")
     
     @commands.command()
     async def ghost(self, ctx):
         """〜(  ' - '  )〜"""
         await ctx.send("〜(  ' - '  )〜")
     
     @commands.command()
     async def wow(self, ctx):
         """(   ' O ')"""
         await ctx.send("(   ' O ')")
          
     @commands.command()
     async def cookie(self, ctx, user : discord.Member = None):
         """(  ^ - ^)-🍪"""
         if user is not None:
             await ctx.send(f"(  ^ - ^)-🍪 {user.mention}")
         else:
             await ctx.send("(  ^ - ^)-🍪")
          
     @commands.command()
     async def cat(self, ctx):
         await ctx.send("""{ \  / }
( ^ - ^ )
( u   u )～""")
     
     @commands.command()
     async def pew(self, ctx):
         """(   ' - ')>------------ pew pew"""
         await ctx.send("(   ' - ')>------------ pew pew")
     
     @commands.command()
     async def lpew(self, ctx):
         """pew pew ------------<(' - '   )"""
         await ctx.send("pew pew ------------<(' - '   )")
    
     @commands.command()
     async def dawae(self, ctx):
         """shows you DA WAE"""
         await ctx.send(""".....::::::･''･::::::.... ..... 
:::::･'''　　　　　'''･:::::
::　　　　　　　　　::
:　　  DA WAE   　         :
::　　　　　　　　　::
::･...　　　　　　...･::
　　'''::::::･,,･::::::'''
　     　∩∧_∧∩
　　　(　･ω･)
　　 　/　　ﾉ
　　　しーU""")                               
     
                                
     
     
     
def setup(bot):
    bot.add_cog(EC(bot))
