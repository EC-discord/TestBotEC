import discord
from discord.ext import commands
import random
import json

class levels:
    def __init__:
        self.bot = bot
        self.lvls = {}
    async def on_message(self, message):
        id = message.author.id
        if id not in self.lvls:
            self.lvls[id] = {'name' : message.author.name, 'xp' : 0, 'level' : {'lvlNo' : 1, 'totalxp' : 100}}
        else:
            self.lvls[id]['xp'] += random.randint(10, 50)
            if self.lvls[id]['xp'] >= self.lvls[id]['level']['totalexp']:
                self.lvls[id]['xp'] = 0
                self.lvls[id]['level']['lvlNo'] += 1
                self.lvls[id]['level']['totalxp'] += self.lvls[id]['level']['totalxp']/2
                await message.channel.send(content = f"congrats {self.lvls[id]['name']} you advanced to level {self.lvls[id]['level']['lvlNo']}")
        data = json.dumps(lvls)
        file = open('data/lvls.json', 'w')
        file.write(data)
        file.close()
        
def setup(bot):
