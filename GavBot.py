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

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="woirking on some shit"))


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
         
         while annoyance <20:

            def annoyanceincrease():
               global annoyance
               if annoyance > 0:
                  threading.Timer(1800,annoyanceincrease).start()
                  lock.acquire()
                  annoyance += 1
                  lock.release()

            threading.Timer(1800,annoyanceincrease).start()
            lock.acquire()

            while annoyance <20:
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

    

###### faces ######
    
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
winkwonk = "https://cdn.discordapp.com/attachments/476197973861203968/518842136129699850/wink.png"
weeb = "https://cdn.discordapp.com/attachments/476197973861203968/518554218039083052/weeb.png"
lewd = "https://cdn.discordapp.com/attachments/476197973861203968/518924590936883210/lewd.png"

###### commands ######

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

    
@client.command(name="pingtime",
                pass_context=True)

async def pingtime(context):
    pingtime = time.time()
    pingms = await client.say("Pinging...")
    ping = time.time() - pingtime
    await client.edit_message(pingms, "Pong! Current pingtime is %.01f seconds" % ping)


@client.command(name="ded",
                pass_context=True)

async def ded():
    embed = discord.Embed(**em)
    embed.set_image(url = "https://cdn.discordapp.com/attachments/506242430375428107/507585948947578881/Screen_Shot_2018-11-01_at_9.04.04_AM.png")
    await client.say(embed=embed)


@client.command(name="love")

async def love():
    embed = discord.Embed(**em)
    embed.set_image(url = "https://media.discordapp.net/attachments/475918776857133056/508744255875842061/Screen_Shot_2018-11-04_at_12.44.09_PM.png")
    await client.say(embed=embed)


@client.command(name="horny")

async def horny():
    embed = discord.Embed(**em)
    embed.set_image(url = "https://media.discordapp.net/attachments/476189549366738944/490559000631443466/DbozB11V0AMVmgN.jpg")
    await client.say(embed=embed)
    

@client.command(name="wink")

async def wink():
    embed = discord.Embed(**em)
    embed.set_image(url="https://78.media.tumblr.com/f5d09004bbc90e513437b85ab1624b47/tumblr_inline_p9wi304wm91tb0p74_500.gif")
    await client.say(embed=embed)


@client.command(name="kinkshame", pass_context=True)

async def kinkshame(context, target: discord.Member):
    embed = discord.Embed(**em)
    embed.add_field(name='\u200b', value= "You've been kinkshamed by {}, you filthy little bastard {}".format(context.message.author.mention, target.mention), inline=False)
    embed.set_thumbnail(url=disgusting)
    await client.say(embed=embed)
    


@client.command(name="nsfw")

async def nsfw():
    embed = discord.Embed(**em)
    embed.set_image(url="https://media.discordapp.net/attachments/475918776857133056/477203747509108756/1533844628299.png?width=623&height=670")
    await client.say(embed=embed)


@client.command(name="roast")

async def roast(target: discord.Member):
    embed = discord.Embed(**em)
    if target.id == "476176194522316801":
       embed.set_thumbnail(url=eyeroll)
       embed.add_field(name='\u200b', value= "Oh, you think you're smart, huh? Phcking bitch.", inline=False)
    elif target.id == "477027536660856872":
        possible_responses = [
            "Your uh... your ass looks like plastic! Not that I've been checking, dipshit.",
            "Your eyes are so confusing, I keep getting fucking lost. Wait, no, that, uh, that's not what i meant -",
            "Has your smile caused a car accident yet? I bet people keep getting distracted. BECAUSE IT'S SO UGLY OF COURSE PHCK -",
            "Uh... shit, phck off why should I do what you say?! You're not the boss of me!",
        ]
        embed.add_field(name='\u200b', value= random.choice(possible_responses), inline=False)
        embed.set_thumbnail(url=emb3)
    else:  
       possible_responses = [
           "Words can't describe how beautiful you are. But numbers can. 2/10.",
           "You're the reason the gene pool needs a life guard.",
           "You look like you wear a seatbelt on the toilet.",
           "My phone battery lasts longer than your relationships.",
           "Which sexual position produces the ugliest children? Ask your mother.",
           "It’s a shame you can’t Photoshop your personality.",
           "If I had a face like yours I’d sue my parents.",
           "Whatever kind of look you were going for, you missed.",
           "I don’t know what makes you so stupid, but it really works.",
           "Were you born this stupid or did you take lessons?",
           "You’re such a beautiful, intelligent, wonderful person. Oh I’m sorry, I thought we were having a lying competition.",
           "When you were born, the doctor came out to the waiting room and said to your parents, 'I’m very sorry. We did everything we could. But they pulled through.'",
           "I thought of you today. It reminded me to take the garbage out.",
           "You look like your face caught fire and someone tried to put it out with a hammer."
       ]
       embed.set_thumbnail(url=smug)
       embed.add_field(name='\u200b', value= "{} {}".format(random.choice(possible_responses), target.mention), inline=False)
   
    await client.say(embed=embed)


@client.command(name="verse")

async def verse(target: discord.Member):
    embed = discord.Embed(**em)
    if target.id == "476176194522316801":
       annoy(2)
       possible_responses = [
            "That's none of your fucking business!",
            "What the fuck do I look like to you?!",
            "That's personal, you fucking asswipe!",           
        ]
       embed.set_thumbnail(url=mad2)
    elif target.id == "477027536660856872":
        possible_responses = [
            "Why would I care? Phck off! I've never thought about that! Now back the fuck off!",
            "Why are you asking me?! Go ask him yourself!",
            "I don't care! Don't ask me! I- Why would I even think about that?!",            
        ]
        embed.set_thumbnail(url=emb3)
    else:  
       possible_responses = [
           "A little bottom bitch. Tsk.",
           "Hm, I'd say thy're a switch or something.",
           "Bottom leaning switch, I mean have ya looked at them?",
           "Wow, we got us an actual top here, didn't expect that.",
           "Dumbass thinks they're a top, but they're a fucking bottom.",
           "A top leaning switch, who would've thought.",
       ]
       embed.set_thumbnail(url=smug)   

    embed.add_field(name='\u200b', value= random.choice(possible_responses), inline=False)
    await client.say(embed=embed)

##@client.command(name="")
##
##async def ():
##    embed = discord.Embed(**em)
##    embed.set_image(url = "")
##    await client.say(embed=embed)


 
###### events ######
    

@client.event
async def on_message(message):
    server = message.server
    global annoyance
    message.content = message.content.lower()

    if message.author == client.user:
        return
        
        
    elif message.content.startswith("connor"):
        embed = discord.Embed(**em)

        if "how many stab wound" in message.content:
            possible_responses = [
                "***28 sTaB wOuNdS***"
                ]
            embed.set_thumbnail(url=smug)
        elif annoyance <=40:
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
        elif "connor " in message.content:
            return



        annoy(1)
        await client.send_typing(message.channel)
        time.sleep(1)   
        embed.add_field(name='\u200b', value= random.choice(possible_responses), inline=False)
        await client.send_message(message.channel, embed=embed)

        
###### gavin in the beginning ######

###### opinion on Connor ######

    elif message.content.startswith ("gavin"):
        

        embed = discord.Embed(**em)

        if "what do you think about connor" in message.content:
            if annoyance <5:
               possible_responses = [
                  "He's... I have to admit, he's pretty. And nice. And... god i have it bad, huh?",
                  "I might act like I hate him all the time but... He's a good person.",
                  "I don't understand how he can be so nice, after all i've done. He's great, you know?"
                  ]
               embed.set_thumbnail(url=smitten)
            elif 4< annoyance <=10:
                possible_responses = [
                    "He's... he's not so bad I guess.",
                    "He... I've met worse.",
                    "Connor, huh? He's... something else. Something special."
                    ]
                embed.set_thumbnail(url=happy)
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

###### other stuff ######

        elif "gavin no" in message.content:
            if annoyance <81:
               possible_responses = [
                  "Gavin YES"
                  ]
               embed.set_thumbnail(url=smug)

###### how are you? ######

        elif "how are you" in message.content:
            if annoyance <=10:
                possible_responses = [
                    "I- I'm actually pretty good right now. Calm."
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

###### Do you like? ######
                
        elif "do you like" in message.content:
           if "cats" in message.content:
              if annoyance < 56:
                 if annoyance > 10:
                    annoy(-1)
                 possible_responses = [
                    "Yeah, I even got two. Gilbert and Fucknugget.",
                    "Sure, they're great.",
                    "Little Gremlins. I love them."
                    ]
                 embed.set_thumbnail(url=default)
              elif annoyance > 55:
                 possible_responses = [
                    "What's it to you?",
                    "Sure. Now fuck off.",
                    "Yeah, and?"
                    ]
                 embed.set_thumbnail(url=eyeroll)
                 
           elif "dogs" in message.content:
              if annoyance < 56:
                 possible_responses = [
                    "Eh, I'm more of a cat person.",
                    "Dogs? Pff, have you seen Connor? Follows Anderson around like a goddamn poodle.",
                    "Hm, yeah, why not. Kinda remind me of Con- No one. I mean no one."
                    ]
                 embed.set_thumbnail(url=default)
              elif annoyance > 55:
                 possible_responses = [
                    "Cats are way better, now fuck off",
                    "Why are you even asking?",
                    "Dogs like Anderson's plastic pet? Ye- No! I mean not at all. Ugh."
                    ]
                 embed.set_thumbnail(url=eyeroll)

###### would you like? ######

                 
        elif "would you like" in message.content:
           if "coffee" in message.content:
              if annoyance < 36:
                 annoy(-2)
                 possible_responses = [
                    "Yeah, thanks, buddy.",
                    "Why are you even asking? Of course.",
                    "Shit, yeah! Thank you."
                    ]
                 embed.set_thumbnail(url=winkwonk)
              elif 35 < annoyance <76:
                 annoy(-3)
                 possible_responses = [
                    "Fuck, yeah, thank you, coffee saves lives.",
                    "Yeah, I really need a fucking cup right now.",
                    "Yeah, hurry up and hand it over, dipshit."
                    ]
                 embed.set_thumbnail(url=mad1)
              elif annoyance >75:
                 annoy(-2)
                 possible_responses = [
                    "Yeah, please hurry the fuck up with it, I really need one right now.",
                    "Fuck, get a move on, I really need a cup right now.",
                    "JUST GIVE ME THE FUCKING COFFEE. Sorry- I'm just. Ugh."
                    ]
                 embed.set_thumbnail(url=mad2)
            
           else:
              return
            
        elif "gavin " in message.content:
            return
                 
        else:
            if annoyance <36:
                possible_responses = [
                        "Yo, what's the matter?",
                        "What do ya want?",
                        "ayyy, what's up?",
                        "You called?"
                        ]
                embed.set_thumbnail(url=default)
            elif 35< annoyance <71:
                possible_responses = [
                    "What the fuck do you want?",
                    "What is it now?",
                    "Yeah, yeah, fuck off",
                    "Stop talking and bring me a coffee, dipshit."
                    ]
                embed.set_thumbnail(url=eyeroll)
            elif 70< annoyance:
                possible_responses = [
                    "Just fuck off, asshole, don't fucking bother me",
                    "I don't fucking care what you want, fuck off",
                    "What the *fuck* is it, asshole?"
                    ]
                embed.set_thumbnail(url=mad2)
                
            
        await client.send_typing(message.channel)
        time.sleep(1)
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
                    "Yeah, yeah, fuck off",
                    "Stop talking and bring me a coffee, dipshit."
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
           if annoyance < 66:
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

        elif message.content.startswith("hugs"):
           embed.set_thumbnail(url=weeb)
           if annoyance <11:
              possible_responses = [
                 "I... Thank you, this is actually... nice?"
                 ]
              embed.set_thumbnail(url=happy)
           elif 10 < annoyance <61:
              possible_responses = [
                 "Uh, thanks?"
                 ]
              embed.set_thumbnail(url=default)
           elif 60 < annoyance:
              possible_responses = [
                 "Oh, get the fuck off of me!"
                 ]
              embed.set_thumbnail(url=mad2)
              
        elif message.content.startswith(("right", "am i right", "do you agree")):           
           possible_responses = [
              "Hell yeah!",
              "Fuck yeah!",
              "Yup!",
              "Nope, lol.",
              "Fuck no.",
              "Nope, absolutely not."
              ]
           embed.set_thumbnail(url=default)

        elif message.content.startswith(("tell me about your cats", "can you tell me about your cats",)):           
           if annoyance <51:
              annoy(-2)
              possible_responses = [
                 "Sure! I got two, Gilbert and Fucknugget! Connor doesn't really approve of that name haha.",
                 "Well for starters, Gil is a Maine Coon.",
                 "Gilbert is a stuck up little bitch but I love him.",
                 "Fucknugget is chaotic evil, I swear.",
                 "Absolutely, I love taking about them! I've had Gil for a while now, can't even remember, Fucknugget was a rescue... ",
                 ]
              embed.set_thumbnail(url=smitten)
           elif 50 < annoyance < 81:
              annoy(-4)
              possible_responses = [
                 "Yeah, Yeah, okay, just what I need right now. I got two, Gilbert and Fucknugget! Connor doesn't really approve of that name haha.",
                 "Ugh, sure, so for starters, Gil is a Maine Coon.",
                 "I guess? Fuck, Gilbert is a stuck up little bitch but I love him.",
                 "Fucking hell, if you want. Fucknugget is chaotic evil, I swear.",
                 "Yeah, that's a good idea. I've had Gil for a while now, can't even remember, Fucknugget was a rescue... ",
                 "Fucking hell, they're great. Mean a lot to me.",
                 "Little pricks, just like their owner. Heh.",
                 ]
              embed.set_thumbnail(url=happy)
           elif 80 < annoyance:
              annoy(-6)
              possible_responses = [
                 "Fuck, shit, okay, that's always good. I got two, Gilbert and Fucknugget! Connor doesn't really approve of that name haha.",
                 "Ugh, sure, need to calm the fuck down. Well, Gil is a Maine Coon.",
                 "Ugh, alright, some distraction is just what I need. Gilbert is a stuck up little bitch but I love him.",
                 "Fucking hell, if you want, yeah why not. Fucknugget is chaotic evil, I swear.",
                 "Alright, fucking hell. I've had Gil for a while now, can't even remember, Fucknugget was a rescue... ",
                 "Fuck, I love them. I do, they keep me calm like nothing else. Just what I need right now.",
                 "God I love those pricks. They're assholes, just like their owner, huh?",
                 ]
              embed.set_thumbnail(url=default)


###### a lot of fuck ######

        elif message.content.startswith(("oh fuck you", "fuck you")):
           annoy(2)
           if annoyance < 66:
              possible_responses = [
                 "Name a time and a place, sweetheart.",
                 "At work? Kinky.",
                 "Sorry, I don't fuck whiny bitches.",
                 "Sorry, but I don't do charity work."
                 ]
              embed.set_thumbnail(url=smug)
           elif annoyance >65 :
              annoy(1)
              possible_responses = [
                 "Yeah, whatever. Bitch.",
                 "Wow, so smart. Asshat.",
                 "Don't got anything better, dipshit?",
                 ]
              embed.set_thumbnail(url=eyeroll)

        elif message.content.startswith(("oh go fuck yourself", "go fuck yourself")):
           annoy(2)
           if annoyance < 66:           
              possible_responses = [
                 "Don't mind if I do, babe.",
                 "At work? Kinky.",
                 ]
              embed.set_thumbnail(url=smug)
           elif annoyance >65 :
              annoy(1)
              possible_responses = [
                 "Yeah, whatever. Bitch.",
                 "Wow, so smart. Asshat.",
                 "Don't got anything better, dipshit?",
                 ]
              embed.set_thumbnail(url=eyeroll)

        elif message.content.startswith(("oh fuck off", "fuck off")):
           annoy(2)
           if annoyance < 66:            
              possible_responses = [
                "Wouldn't want to spend anymore time near you than I gotta, fuckface.",
                "Jealous?",
                "You compensating for something?"
                ]
              embed.set_thumbnail(url=smug)
           elif annoyance >65 :
              annoy(1)
              possible_responses = [
                 "Yeah, whatever. Bitch.",
                 "Wow, so smart. Asshat.",
                 "Don't got anything better, dipshit?",
                 ]
              embed.set_thumbnail(url=eyeroll)
              
        elif message.content.startswith(("oh fuck off", "fuck off")):
           annoy(2)
           if annoyance < 66: 
              possible_responses = [
                 "Wouldn't want to spend anymore time near you than I gotta, fuckface.",
                 "Jealous?",
                 "You compensating for something?"
                 ]
              embed.set_thumbnail(url=smug)
           elif annoyance >65 :
              annoy(1)
              possible_responses = [
                 "Yeah, whatever. Bitch.",
                 "Wow, so smart. Asshat.",
                 "Don't got anything better, dipshit?",
                 ]
              embed.set_thumbnail(url=eyeroll)

        elif message.content.startswith(("kill yourself", "go kill yourself")):
           annoy(2)
           if annoyance < 66:
               possible_responses = [
                  "If I don't have to talk to you anymore? Gladly.",
                  "Oh wow. Such clever. Much insult. I am truly hurt.",
                  "only if you go first, babe ~ "
                  ]
               embed.set_thumbnail(url=smug)
           elif annoyance >65 :
              annoy(1)
              possible_responses = [
                 "Yeah, whatever. Bitch.",
                 "Wow, so smart. Asshat.",
                 "Don't got anything better, dipshit?",
                 ]
              embed.set_thumbnail(url=eyeroll)

        elif message.content.startswith("i love you"):
           if annoyance < 11:
              possible_responses = [
                 "I... Thank you.",
                 "Wow, well... thanks.",
                 ]
              embed.set_thumbnail(url=happy)
           elif 10 < annoyance < 56:
              possible_responses = [
                 "A horrible decision, really.",
                 "Oh, really?",
                 "Ew, gross."
                 ]
              embed.set_thumbnail(url=smug)
           elif 55 < annoyance < 86:
              annoy(1)
              possible_responses = [
                 "Yeah, sure you do.",
                 "Oh yeah? Sure, man.",
                 ]
              embed.set_thumbnail(url=eyeroll)
           elif 85 < annoyance:
              annoy(2)
              possible_responses = [
                 "NO, YOU FUCKING DON'T, YOU DON'T EVEN KNOW ME.",
                 "Oh fuck off, you don't. You really fucking don't.",
                 ]
              embed.set_thumbnail(url=mad2)

        elif message.content.startswith("fuck me"):
           if annoyance < 66:
              possible_responses = [
                 "Name a time and a place, babe.",
                 "Oh, kinky.",
                 ]
              embed.set_thumbnail(url=smug)
           elif 65 < annoyance:
              annoy(1)
              possible_responses = [
                 "Ew, gross.",
                 "Yeah, no, not gonna happen.",
                 ]
              embed.set_thumbnail(url=eyeroll)

        elif message.content.startswith(("shut up", "gavin shut up")):
            possible_responses = [
               "I say whatever the fuck I want, asshole.",
               "You can't tell me what to do, fuckface.",
               ]
            embed.set_thumbnail(url=smug)




               
        else:
            return
        
        embed.add_field(name='\u200b', value= random.choice(possible_responses), inline=False)
              
        await client.send_typing(message.channel)
        time.sleep(1)
        if message.content.startswith(("hello", "hi", "hey", "what's up")):
            embed.add_field(name='\u200b', value= "*I'm still working my shit out, in development or whatever, so don't be a dick, 'kay?*", inline=False)
        await client.send_message(message.channel, embed=embed)

###### just words ######

    elif message.content.startswith("owo"):
        if annoyance <66:
           await client.send_typing(message.channel)
           time.sleep(1)
           embed = discord.Embed(**em)
           embed.set_thumbnail(url=weeb)
           embed.add_field(name='\u200b', value= "**uwu**", inline=False)
           await client.send_message(message.channel, embed=embed)

    elif message.content.startswith("uwu"):
        if annoyance <66:
           await client.send_typing(message.channel)
           time.sleep(1)
           embed = discord.Embed(**em)
           embed.set_thumbnail(url=weeb)
           embed.add_field(name='\u200b', value= "***OwO***", inline=False)
           await client.send_message(message.channel, embed=embed)

    elif "vore" in message.content:
        if message.author.id == "508110104726339633":
           return
        else:
           annoy(6)
           await client.send_typing(message.channel)
           time.sleep(0.5)
           embed = discord.Embed(**em)
           embed.set_thumbnail(url=mad2)
           embed.add_field(name='\u200b', value= "SHUT YOUR FUCKING MOUTH WE DON'T TALK ABOUT THAT HERE", inline=False)
           await client.send_message(message.channel, embed=embed)

    elif message.content.startswith("dick"):
        if annoyance <66:
           await client.send_typing(message.channel)
           time.sleep(1)
           embed = discord.Embed(**em)
           embed.set_thumbnail(url=lewd)
           embed.add_field(name='\u200b', value= "Mhmmm dick. Slurp.", inline=False)
           await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(("bye", "good bye")):
        await client.send_typing(message.channel)
        time.sleep(1)
        embed = discord.Embed(**em)
        embed.set_thumbnail(url=default)
        embed.add_field(name='\u200b', value= "Bye. Dickhead.", inline=False)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(("hewwo")):
        await client.send_typing(message.channel)
        time.sleep(1)
        embed = discord.Embed(**em)
        embed.set_thumbnail(url=weeb)
        embed.add_field(name='\u200b', value= "Hewwo owo", inline=False)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(("good morning", "morning")):
        await client.send_typing(message.channel)
        time.sleep(1)
        embed = discord.Embed(**em)
        embed.set_thumbnail(url=default)
        embed.add_field(name='\u200b', value= "Morning, SLUTS!", inline=False)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(("gavin stop", "stop gavin")):
        await client.send_typing(message.channel)
        time.sleep(1)
        embed = discord.Embed(**em)
        embed.set_thumbnail(url=default)
        embed.add_field(name='\u200b', value= "I'M A BAD BITCH YOU CAN'T STOP ME", inline=False)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(("gay")):
        await client.send_typing(message.channel)
        time.sleep(1)
        embed = discord.Embed(**em)
        embed.set_thumbnail(url=smug)
        embed.add_field(name='\u200b', value= "MOVE I'M GAY", inline=False)
        await client.send_message(message.channel, embed=embed)

        
        
    await client.process_commands(message)



###### dev commands ######

@client.command(name='inc',
                brief="these are all deveoper commands right now")

async def inc():
    global annoyance
    annoy(20)
    await client.say(annoyance)

@client.command(name='dec')

async def dec():
    global annoyance
    annoy(-15)
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

                
