import random
from random import randint
import discord
import time
from time import sleep
from discord.ext.commands import Bot
import threading
import sys
import queue

BOT_PREFIX = 'g!'
TOKEN = 'NDc2MTc2MTk0NTIyMzE2ODAx.DloksA.QBYAQGbKPoBgF9D-rLqHEWBL5oQ'
client = Bot(command_prefix=BOT_PREFIX)

annoyance = 20
    
lock = threading.Lock()


class annoyancecounter(object):


   def __init__(self, interval=1):

      self.interval = interval

      thread = threading.Thread(target=self.run, args=())
      thread.daemon = True                            
      thread.start()                                  

   def run(self):
      while True:
         while annoyance >20:

            def annoyancedecrease():
               global annoyance
               if annoyance > 0:
                  threading.Timer(1800,annoyancedecrease).start()
                  lock.acquire()
                  annoyance -= 1
                  lock.release()

            threading.Timer(1800,annoyancedecrease).start()
            lock.acquire()

            while annoyance >20:
               lock.release()
               time.sleep(0.5)
               lock.acquire()
            return annoyance
               
               

         time.sleep(self.interval)


    

annoyancecounter()

em = {"title":"Gavin Reed", "color":0xc70000}

def annoy(value):
    global annoyance
    annoyance = min(max(annoyance+value, 0), 100)
    
default = "https://cdn.discordapp.com/attachments/476197973861203968/518437517129678887/Default.png"
disgusting = "https://cdn.discordapp.com/attachments/476197973861203968/518435553558134794/disgusting.png"
emb1 = "https://cdn.discordapp.com/attachments/476197973861203968/518435560935784449/embarrassed1.png"
emb2 = "https://cdn.discordapp.com/attachments/476197973861203968/518435568795910145/embarrassed2.png"
emb3 = "https://cdn.discordapp.com/attachments/476197973861203968/518435575980752942/embarrassed3.png"
eyeroll = "https://cdn.discordapp.com/attachments/476197973861203968/518435583714918401/eye_roll.png"
happy = "https://cdn.discordapp.com/attachments/476197973861203968/518435590602096655/happy.png"
mad1 = "https://cdn.discordapp.com/attachments/476197973861203968/518435600450322455/mad1.png"
mad2 = "https://cdn.discordapp.com/attachments/476197973861203968/518569816919900170/mad2.png"
sad = "https://cdn.discordapp.com/attachments/476197973861203968/518435613905649667/sad.png"
smitten = "https://cdn.discordapp.com/attachments/476197973861203968/518435622231212032/smitten.png"
smug = "https://cdn.discordapp.com/attachments/476197973861203968/518437521986813952/smug.png"
wink = "https://cdn.discordapp.com/attachments/476197973861203968/518435637125316609/wink.png"
weeb = "https://cdn.discordapp.com/attachments/476197973861203968/518554218039083052/weeb.png"

@client.command(name="annoyed")

async def annoyed():
    embed = discord.Embed(**em)
    embed.add_field(name='\u200b', value= "Annoyance: {}%".format(annoyance), inline=False)
    if annoyance <=10:
        embed.set_thumbnail(url=happy)
    elif 10< annoyance <56:
        embed.set_thumbnail(url=default)
    elif 55< annoyance <=100:
        embed.set_thumbnail(url=eyeroll)
    await client.say(embed=embed)

    

@client.event
async def on_message(message):
    server = message.server
    global annoyance
    message.content = message.content.lower()

    if message.author == client.user:
        return
    
    elif message.content.startswith("connor"):
        annoy(1)
        await client.send_typing(message.channel)
        time.sleep(1)
        embed = discord.Embed(**em)
        if annoyance <=40:
            possible_responses = [
                "we talking about the tin can?",
                "Why are we talking about the Tin Can?",
                "oh, get lost, Connor.",
                "Bugger off, tin can."
                    ]
            embed.set_thumbnail(url=eyeroll)
        elif 40< annoyance <61:
            annoy(1)
            possible_responses = [
                "we still talking about the fucking tin can?",
                "Ugh not him. Can we change the topic?",
                "oh shut up Connor",
                    ]
            embed.set_thumbnail(url=mad1)
        elif 40< annoyance:
            annoy(2)
            possible_responses = [
                "Can we please shut the fuck up about the tin can?! I'm fucking sick of hearing of about that fucking prick.",
                "Can we please not? I don’t wanna think about that pre-p-pretty big bitch! Yeah....that’s what I was going to say.",
                "What about him?! Connor is stupid? Connor is obnoxious? Connor’s pretty? Connor’s gonna be eating my foot if you keep talking about him!",
                "SHUT THE FUCK UP CONNOR"
                ]
            embed.set_thumbnail(url=mad2)

            
            
        embed.add_field(name='\u200b', value= random.choice(possible_responses), inline=False)
        await client.send_message(message.channel, embed=embed)
        

    elif message.content.startswith ("gavin"):
        
        await client.send_typing(message.channel)
        time.sleep(1)
        embed = discord.Embed(**em)

        if "what do you think about connor" in message.content:
            if annoyance <=10:
                possible_responses = [
                    "He's... ugh he's not so bad I guess.",
                    "He... I've met worse.",
                    "Connor, huh? He's... something else."
                    ]
                embed.set_thumbnail(url=smitten)
            elif 10< annoyance <31:
                annoy(1)
                possible_responses = [
                        "he's an android prick, what the hell do you want to hear?",
                        "He's a little bitch and he should've been back with my coffee by now.",
                        "Anderson's plastic pet, huh? Dipshit should just get lost."
                        ]
                embed.set_thumbnail(url=eyeroll)
            elif 30< annoyance <51:
                annoy(1)
                possible_responses = [
                    "he's- what the fuck do you want from me?! I- I hate him, that's what I think!",
                    "The fuck do you want from me? I hate him."
                    ]
                embed.set_thumbnail(url=emb1)
            elif 50< annoyance <71:
                annoy(random.randint(1,3))
                possible_responses = [
                    "Shut the hell up, I think he should suck my dick! W-Wait I diDN'T MEAN THAT LITERALLY!"
                    ]
                embed.set_thumbnail(url=emb2)
            elif annoyance >70:
                annoy(random.randint(1,3))
                possible_responses = [
                    "I THINK HE'S A PRICK, I HATE HIM! I HATE HIS SMILE, AND HIS LAUGH, A-AND THE WAY HE...he always runs a hand through his...pretty soft hair...I'll fucking kill you."
                    ]
                embed.set_thumbnail(url=emb3)



        elif "how are you" in message.content:
            if annoyance <=10:
                possible_responses = [
                    "I- I'm actually pretty good right now. calm."
                    ]
                embed.set_thumbnail(url=happy)

            elif 10< annoyance <41:
                possible_responses = [
                        "Eh, I'm pretty okay right now."
                        ]
                embed.set_thumbnail(url=default)
            elif 40< annoyance <61:
                possible_responses = [
                    "Could be worse, but I seriously need some fucking coffee right now."
                    ]
                embed.set_thumbnail(url=eyeroll)
            elif 60< annoyance <86:
                annoy(random.randint(1,3))
                possible_responses = [
                    "You know what? I- Don't even get me fucking started."
                    ]
                embed.set_thumbnail(url=disgusting)
            elif annoyance >85:
                annoy(random.randint(1,3))
                possible_responses = [
                    "Oh fuck *off*, fuck this shit, I'm out."
                    ]
                embed.set_thumbnail(url=mad2)
            

        embed.add_field(name='\u200b', value= random.choice(possible_responses), inline=False)
        await client.send_message(message.channel, embed=embed)




####### Hello-Block ######

    elif "gavin" in message.content:

        embed = discord.Embed(**em)

        if message.content.startswith(("hello", "hi", "hey", "what's up")):
           
            if annoyance <36:
                possible_responses = [
                        "Yo, what's the matter?",
                        "What do ya want?",
                        "ayyy, what's up?"
                        ]
                embed.set_thumbnail(url=default)
            elif 35< annoyance <71:
                possible_responses = [
                    "What the fuck do you want?",
                    "What is it now?",
                    "Yeah, yeah, fuck off"
                    ]
                embed.set_thumbnail(url=eyeroll)
            elif 70< annoyance:
                possible_responses = [
                    "Just fuck off, asshole, don't fucking bother me",
                    "I don't fucking care what you want, fuck off",
                    "What the *fuck* is it, asshole?"
                    ]
                embed.set_thumbnail(url=mad2)
                

###### normal "gavin" in content Block ######

        elif message.content.startswith("glomps"):
           embed.set_thumbnail(url=weeb)
           possible_responses = [
              "***OWO what's this?***"
              ]

        elif "calm your tits" in message.content:
           if annoyance <31:
              annoyance = annoyance -1
              possible_responses = [
              "What are you on about? I'm alright."
              ]
              embed.set_thumbnail(url=default)
              
           elif 30< annoyance <76:
              annoyance = annoyance -2
              possible_responses = [
              "Yeah, yeah whatever, man."
              ]
              embed.set_thumbnail(url=eyeroll)
           elif 75< annoyance:
              annoyance = annoyance -1
              possible_responses = [
                 "OH FUCK OFF, I AM CALM."
                 ]
              embed.set_thumbnail(url=mad2)
               
        else:
            return
        
        embed.add_field(name='\u200b', value= random.choice(possible_responses), inline=False)
        await client.send_typing(message.channel)
        time.sleep(1)
        if message.content.startswith(("hello", "hi", "hey", "what's up")):
            embed.add_field(name='\u200b', value= "*I'm still working my shit out, in development or whatever, so don't be a dick, 'kay?*", inline=False)
        await client.send_message(message.channel, embed=embed)  
        
        
    await client.process_commands(message)



###### dev commands ######

@client.command(name='inc')

async def inc():
    global annoyance
    annoyance = annoyance + 15
    await client.say(annoyance)

@client.command(name='dec')

async def dec():
    global annoyance
    annoyance = annoyance - 15
    await client.say(annoyance)


@client.command(name='reset')

async def rest():
    global annoyance
    annoyance = 20
    await client.say(annoyance)

@client.command(name='sethigh')

async def sethigh():
    global annoyance
    annoyance = 80
    await client.say(annoyance)






client.run(TOKEN)

                
