import discord
import asyncio

class BitwiseOperators:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def bitand(self, ctx, x:int, y:int):
        '''**Bitwise AND** Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0'''
        result = x & y
        await ctx.send(result)
