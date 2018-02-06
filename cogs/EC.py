
import discord
import asyncio
from discord.ext import commands

class EC: 
     def __init__(self, bot):
          self.bot = bot


     @commands.command()
     async def shrug(self, ctx):
         """¯\\_(ツ)_/¯"""
         await ctx.send("¯\\\_(ツ)\_/¯")

     @commands.command()
     async def tflip(self, ctx):
         """(╯°□°）╯︵ ┻━┻"""
         await ctx.send('(╯°□°）╯︵ ┻━┻')

     @commands.command()
     async def cool(self, ctx):
         """(  * O *  )"""
         await ctx.send("(  * O *  )")

     @commands.command()
     async def lenny(self, ctx):
         """( ͡° ͜ʖ ͡°)"""
         await ctx.send("( ͡° ͜ʖ ͡°)")
    
     @commands.command()
     async def gib(self, ctx):
         """(づ｡◕‿‿◕｡)づ"""
         await ctx.send("(づ｡◕‿‿◕｡)づ")
     
     @commands.command()
     async def kflip(self, ctx):
         """(づ｡◕‿‿◕｡)づ︵ ┻━┻"""
         await ctx.send("(づ｡◕‿‿◕｡)づ︵ ┻━┻")
     
     @commands.command()
     async def thumbs(self, ctx):
         """(👍' - ')👍"""
         await ctx.send("(👍' - ')👍")
     
     @commands.command()
     async def warp(self, ctx):
         """(   ' - ')__(warp drive)"""
         await ctx.send("(   ' - ')__(warp drive)")
    
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
     async def noble(self, ctx):
         """\\(  . - .  )/ i am noble!"""
         await ctx.send("\\\(  . - .  )/ i am noble!")
          
     @commands.command()
     async def cookie(self, ctx):
         """(  ^ - ^)-🍪"""
         await ctx.send("(  ^ - ^)-🍪")
          
     @commands.command()
     async def cat(self, ctx):
         await ctx.send("""{ \  / }
( ^ - ^ )
( u   u )～""")
     
     @commands.command()
     async def chaos(self, ctx):
         """Everything will fall into CHAOS"""
         await ctx.send("Everything will fall into CHAOS")
     
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
