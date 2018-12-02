import random
from random import randint
import discord
import time
from time import sleep
from discord.ext.commands import Bot


BOT_PREFIX = 'g!'
TOKEN = 'NDc2MTc2MTk0NTIyMzE2ODAx.DloksA.QBYAQGbKPoBgF9D-rLqHEWBL5oQ'
client = Bot(command_prefix=BOT_PREFIX)


annoyance = 20

def annoyance(i):
    global annoyance
    if message.author == client.user:
        return

@client.event
async def on_message(message):
    def calm1():
        
        if message.content.startswith("calm your tits gav"):
            annoyance = annoyance - random.randint(1,5)
            await client.send_message(message.channel, "yeah yeah whatever")
    
    switcher={
            20: calm1
             }
    return switcher.get(i,"Invalid day of week")



client.run(TOKEN)
