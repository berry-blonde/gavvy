import random
import discord
import asyncio
import time
from discord.ext.commands import Bot


BOT_PREFIX = 'g!'
TOKEN = 'NDc2MTc2MTk0NTIyMzE2ODAx.DloksA.QBYAQGbKPoBgF9D-rLqHEWBL5oQ'
client = Bot(command_prefix=BOT_PREFIX)

@client.command(pass_context=True)
async def say(ctx):
    msg = ctx.message.content.split(" ", 1)
    await client.delete_message(ctx.message)
    await client.send_message(ctx.message.channel, msg)
