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


    
@client.event
async def on_message(message):
    server = message.server
    global annoyance
    message.content = message.content.lower()

    if message.author == client.user:
        return
    
    elif message.content.startswith("connor how many stab wounds"):
        annoyance = annoyance + random.randint(1,5)
        await client.send_typing(message.channel)
        time.sleep(0.8)
        embed = discord.Embed(title="Gavin Reed", color=0xc70000)
        embed.add_field(name='\u200b', value="28 sTaB wOuNdS", inline=False)
        await client.send_message(message.channel, embed=embed)
        
    elif message.content.startswith("calm your tits gav"):
        annoyance = annoyance - random.randint(1,5)
        await client.send_message(message.channel, "yeah yeah whatever")
        
    elif message.content.startswith("how annoyed?"):
        await client.send_message(message.channel, annoyance)

    elif message.content.startswith("calm your tits gav"):
        annoyance = annoyance - random.randint(1,5)
        await client.send_message(message.channel, "yeah yeah whatever")

    elif "gavin" in message.content:
        if "what do you think about connor" in message.content:   
            annoyance = annoyance + random.randint(1,5)
            await client.send_typing(message.channel)
            time.sleep(0.8)
            if annoyance <= 30:
                possible_responses = [
                    "he's an android prick, what the hell do you want to hear?",
                    "He's a little bitch and he should've been back with my coffee by now.",
                    "Anderson's plastic pet, huh? Dipshit should just get lost."
                    ]
                embed = discord.Embed(title="Gavin Reed", color=0xc70000)
                embed.add_field(name='\u200b', value=random.choice(possible_responses), inline=False)
                await client.send_message(message.channel, embed=embed)
            elif 30< annoyance <51:
                annoyance = annoyance + random.randint(1,5)
                possible_responses = [
                    "he's- what the fuck do you want from me?! I- I hate him, that's what I think!",
                    "The fuck do you want from me? I hate him."
                    ]
                embed = discord.Embed(title="Gavin Reed", color=0xc70000)
                embed.add_field(name='\u200b', value=random.choice(possible_responses), inline=False)
                await client.send_message(message.channel, embed=embed)
            elif 50< annoyance <71:
                annoyance = annoyance + random.randint(1,10)
                possible_responses = [
                    "Shut the hell up, I think he should suck my dick! W-Wait I diDN'T MEAN THAT LITERALLY!"
                    ]
                embed = discord.Embed(title="Gavin Reed", color=0xc70000)
                embed.add_field(name='\u200b', value=random.choice(possible_responses), inline=False)
                await client.send_message(message.channel, embed=embed)
                
            elif annoyance >70:
                annoyance = annoyance + random.randint(1,5)
                possible_responses = [
                    "I THINK HE'S A PRICK, I HATE HIM! I HATE HIS SMILE, AND HIS LAUGH, A-AND THE WAY HE...he always runs a hand through his...pretty soft hair...I'll fucking kill you."
                    ]
                embed = discord.Embed(title="Gavin Reed", color=0xc70000)
                embed.add_field(name='\u200b', value=random.choice(possible_responses), inline=False)
                await client.send_message(message.channel, embed=embed)
                
    elif message.content.startswith("connor"):
        annoyance = annoyance + random.randint(1,3)
        await client.send_typing(message.channel)
        time.sleep(1)
        if annoyance <= 40:
            possible_responses = [
                "we talking about the tin can?",
                "Why are we talking about the Tin Can?",
                "oh, get lost, Connor.",
                "bugger off"
                    ]
            embed = discord.Embed(title="Gavin Reed", color=0xc70000)
            embed.add_field(name='\u200b', value=random.choice(possible_responses), inline=False)
            await client.send_message(message.channel, embed=embed)
        elif 40< annoyance <61:
            possible_responses = [
                "we still talking about the fucking tin can?",
                "Ugh not him. Can we change the topic?",
                "oh shut up Connor",
                    ]
            embed = discord.Embed(title="Gavin Reed", color=0xc70000)
            embed.add_field(name='\u200b', value=random.choice(possible_responses), inline=False)
            await client.send_message(message.channel, embed=embed)
        elif annoyance >60:
            possible_responses = [
                "Can we please shut the fuck up about the tin can?! I'm fucking sick of hearing of about that fucking prick.",
                "Can we please not? I don’t wanna think about that pre-p-pretty big bitch! Yeah....that’s what I was going to say.",
                "What about him?! Connor is stupid? Connor is obnoxious? Connor’s pretty? Connor’s gonna be eating my foot if you keep talking about him!",
                "SHUT THE FUCK UP CONNOR"
                    ]
            embed = discord.Embed(title="Gavin Reed", color=0xc70000)
            embed.add_field(name='\u200b', value=random.choice(possible_responses), inline=False)
            await client.send_message(message.channel, embed=embed)

    await client.process_commands(message)

@client.command(name='inc')

async def inc():
    global annoyance
    annoyance = annoyance + 10
    await client.say(annoyance)

@client.command(name='dec')

async def dec():
    global annoyance
    annoyance = annoyance - 10
    await client.say(annoyance)
                                     

client.run(TOKEN)
