import discord
import asyncio

class BitwiseOperators:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def bitand(self, ctx, *, x:int, y:int):
        '''**Bitwise AND** Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0'''
        result = x & y
        await ctx.send(result)
        
    @commands.command()
    async def bitor(self, ctx, *, x:int, y:int):
        '''**Bitwise OR** Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1'''
        result = x | y
        await ctx.send(result)
        
    @commands.command()
    async def bitxor(self, ctx, *, x:int, y:int):
        '''**Bitwise XOR** Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1'''
        result = x ^ y
        await ctx.send(result)
        
