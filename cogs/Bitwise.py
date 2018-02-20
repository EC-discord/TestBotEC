import discord
import asyncio
from discord.ext import commands

class BitwiseOperators:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def bitand(self, ctx, x:int, y:int):
        '''Bitwise AND : Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0'''
        result = x & y
        kappa = bin(x)[2:]
        kappa2 = bin(y)[2:]
        result2 = bin(result)[2:]
        if x > y:
            diff = x - y
            kappa = kappa.rjust(diff, '0')
        elif y > x:
            diff = y - x
            kappa2 = kappa2.rjust(diff, '0')
        await ctx.send("```%s\n%s\n----------------\n%s```" % (kappa, kappa2, result2))
        await asyncio.sleep(0.5)
        await ctx.send("**Base 10** : %s\n**Base 2** : %s" % (result, result2))
        
    @commands.command()
    async def bitor(self, ctx, x:int, y:int):
        '''Bitwise OR : Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1'''
        result = x | y
        result2 = bin(result)[2:]
        await ctx.send("**Base 10** : %s\n**Base 2** : %s" % (result, result2))
        
    @commands.command()
    async def bitxor(self, ctx, x:int, y:int):
        '''Bitwise XOR : Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1'''
        result = x ^ y
        result2 = bin(result)[2:]
        await ctx.send("**Base 10** : %s\n**Base 2** : %s" % (result, result2))
        
    @commands.command()
    async def bitlshift(self, ctx, x:int, y:int):
         '''Left Shifts Bits : Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y'''
         result = x << y
         result2 = bin(result)[2:]
         await ctx.send("**Base 10** : %s\n**Base 2** : %s" % (result, result2))
          
    @commands.command()
    async def bitrshift(self, ctx, x:int, y:int):
          '''Right Shifts Bits : Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y'''
          result = x >> y
          result2 = bin(result)[2:]
          await ctx.send("**Base 10** : %s\n**Base 2** : %s" % (result, result2))
            
    @commands.command()
    async def bitnot(self, ctx, x:int):
          '''Bitwise NOT : Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1'''
          result = ~x
          result2 = bin(result)[2:]
          await ctx.send("**Base 10** : %s\n**Base 2** : %s" % (result, result2))
        
        
def setup(bot):
    bot.add_cog(BitwiseOperators(bot))
