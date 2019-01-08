import random
from random import randint
import discord
import time
from time import sleep
from discord.ext.commands import Bot
from discord.ext import commands
import threading
import sys
import queue
import json
import os
import asyncio
from discord.ext.commands import has_permissions, CheckFailure


BOT_PREFIX = 'g!'
client = Bot(command_prefix=BOT_PREFIX)
client.remove_command("help")


@client.event
async def on_ready():
    print("I'm in")
    await client.change_presence(game=discord.Game(name="Merry Crisis!"))


@client.event
async def on_server_join(server):
   with open("servers.json", "r") as f:
       servers = json.load(f)

   await update_data(servers, server)

   with open("servers.json", "w") as f:
       json.dump(servers, f)


async def update_data(servers, server):
    if not server.id in servers:
        servers[server.id] = {}
        servers[server.id]["annoyance"] = 20
        client.loop.create_task(annoyancecounter(servers, server, 1))


async def add_annoyance(servers, server, annoyance):
    servers[server.id]["annoyance"] = min(max(servers[server.id]["annoyance"] + random.randint(1,annoyance), 0), 100)


async def remove_annoyance(servers, server, annoyance):
    servers[server.id]["annoyance"] = min(max(servers[server.id]["annoyance"] - random.randint(1,annoyance), 0), 100)


async def annoyancecounter(servers, server, annoyance):

   while not client.is_closed:
        if 100 >= servers[server.id]["annoyance"] > 20:
            if server.id == "520283348438876160":
                print("{}:{}".format(server.id, servers[server.id]["annoyance"]))
            with open("servers.json", "r") as f:
                servers = json.load(f)
            servers[server.id]["annoyance"] -= annoyance
            with open("servers.json", "w") as f:
                json.dump(servers, f)
            await asyncio.sleep(600)
        elif servers[server.id]["annoyance"] == 20:
            if server.id == "520283348438876160":
                print("{}:{}".format(server.id, servers[server.id]["annoyance"]))
            with open("servers.json", "r") as f:
                servers = json.load(f)
            servers[server.id]["annoyance"] = 20
            if server.id == "520283348438876160":
                print("{}:{}".format(server.id, servers[server.id]["annoyance"]))
            with open("servers.json", "w") as f:
                json.dump(servers, f)
            await asyncio.sleep(600)
        elif 0 <= servers[server.id]["annoyance"] < 20:
            if server.id == "520283348438876160":
                print("{}:{}".format(server.id, servers[server.id]["annoyance"]))
            with open("servers.json", "r") as f:
                servers = json.load(f)
            servers[server.id]["annoyance"] += annoyance
            if server.id == "520283348438876160":
                print("{}:{}".format(server.id, servers[server.id]["annoyance"]))
            with open("servers.json", "w") as f:
                json.dump(servers, f)
            await asyncio.sleep(600)

async def update_users(users, user):
    if not user.name in users:
        users[user.name] = {}
        users[user.name]["text"] = "no info"

em = {"title":"Gavin Reed", "color":0xc70000}

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


@client.command(name="reset", pass_context=True)
@has_permissions(administrator=True)
async def reset(context):
    server = context.message.author.server
    with open("servers.json", "r") as f:
        servers = json.load(f)
    servers[server.id]["annoyance"] = 20
    with open("servers.json", "w") as f:
        json.dump(servers, f)
    embed = discord.Embed(**em)
    embed.set_thumbnail(url=winkwonk)
    embed.add_field(name='\u200b', value= "Annoyance has been reset to 20%.", inline=True)
    await client.send_message(context.message.channel, embed=embed)

@reset.error
async def reset_error(error, context):
    if isinstance(error, CheckFailure):
        embed = discord.Embed(**em)
        embed.set_thumbnail(url=smug)
        embed.add_field(name='\u200b', value= "Sorry, fuckface, looks like you don't have the permission to use that.", inline=True)
        await client.send_message(context.message.channel, embed=embed)


@client.command(pass_context=True)
async def start(context):
    server = context.message.author.server
    with open("servers.json", "r") as f:
        servers = json.load(f)
    client.loop.create_task(annoyancecounter(servers, server, 1))
    with open("servers.json", "w") as f:
        json.dump(servers, f)
    await client.delete_message(context.message)

###### help commands ######

@client.command(pass_context=True)
async def help(context):
    embed = discord.Embed(title = "Help", color=0xc70000)
    embed.set_author(name="Gavin Reed")
    embed.set_thumbnail(url=winkwonk)
    embed.add_field(name='\u200b', value= "**GENERAL**", inline=False)
    embed.add_field(name='pingtime', value= "Gavin's Pingtime", inline=True)
    embed.add_field(name='commands', value= "General commands", inline=True)
    embed.add_field(name='triggers', value= "Shows you **some** of the words Gavin reacts to in chat", inline=True)
    embed.add_field(name='\u200b', value= "**ANNOYANCE-SYSTEM**", inline=False)
    embed.add_field(name='annoyance', value= "Infos on the Annoyance system", inline=True)
    embed.add_field(name='annoyed', value= "Gavin's annoyance level", inline=True)
    embed.add_field(name='reset', value= "admin command", inline=True)
    embed.add_field(name='\u200b', value= "**DEVELOPMENT**", inline=False)
    embed.add_field(name='support', value= "Something wrong?", inline=True)
    embed.add_field(name='updates', value= "What's new?", inline=True)
    embed.add_field(name='credits', value= "Art credits.", inline=True)


    await client.say(embed=embed)

@client.command(pass_context=True)
async def commands(context):
    embed = discord.Embed(title = "Commands", description= "A list of the current commands you can use.", color=0xc70000)
    embed.set_author(name="Gavin Reed")
    embed.set_thumbnail(url=winkwonk)

    embed.add_field(name='\u200b', value= "**COMMANDS**", inline=False)
    embed.add_field(name='ded', value= "I'm ded", inline=True)
    embed.add_field(name='love', value= "Show some love!", inline=True)
    embed.add_field(name='horny', value= "Why are y'all so horny?", inline=True)
    embed.add_field(name='wink', value= "winkwonk", inline=True)
    embed.add_field(name='nsfw', value= "That's NSFW!", inline=True)
    embed.add_field(name='roast', value= "Hah, buuurn.", inline=True)
    embed.add_field(name='verse', value= ":eyes:", inline=True)
    embed.add_field(name='nut', value= "You'll nut. Trust me.", inline=True)
    embed.add_field(name='add', value= "Add info to a member.", inline=True)
    embed.add_field(name='whois', value= "Who a member is.", inline=True)
    embed.add_field(name='clear', value= "Clears all info on a member.", inline=True)
    embed.add_field(name='say', value= "Make Gavin say shit in a specified channel. Admin command.", inline=True)
    embed.add_field(name='tiddies', value= "Have a random picture of Gavin's tiddies.", inline=True)

    await client.send_message(context.message.author, embed=embed)


@client.command(pass_context=True)
async def triggers(context):
    embed = discord.Embed(title = "Triggers", description= "A few examples of words Gavin reacts to in chat.", color=0xc70000)
    embed.set_author(name="Gavin Reed")
    embed.set_thumbnail(url=winkwonk)

    embed.add_field(name='\u200b', value= "**GREETINGS**", inline=False)
    embed.add_field(name='For example:', value= "Hello Gavin, Hi Gavin, Bye Gavin, Good morning Gavin, etc.", inline=True)
    embed.add_field(name='\u200b', value= "**INSULTS**", inline=False)
    embed.add_field(name='For example:', value= "Fuck you Gavin, Fuck off Gavin, etc.", inline=True)
    embed.add_field(name='\u200b', value= "**QUESTIONS**", inline=False)
    embed.add_field(name='For example:', value= "Asking what he thinks about characters, how characters are, asking who a character is, asking him to talk about his cats, asking if he wants a coffe,", inline=True)
    embed.add_field(name='\u200b', value= "Don't forget to add his name!", inline=False)

    await client.send_message(context.message.author, embed=embed)


@client.command(pass_context=True)
async def annoyance(context):
    embed = discord.Embed(title = "Annoyance-System", description= "Gives you some information on the annoyance system.", color=0xc70000)
    embed.set_author(name="Gavin Reed")
    embed.set_thumbnail(url=winkwonk)

    embed.add_field(name='\u200b', value= "**GENERAL INFORMATION**", inline=False)
    embed.add_field(name='\u200b', value= "Some things, words, questions etc piss GavBot off, however, some calm him. His annoyance-level affects how, and if, he responds to certain words. \n You can receive information about his annoyance by using the g!annoyed command or asking him how he is. \n Over time, his annoyance returns to 20%.", inline=True)
    embed.add_field(name='\u200b', value= "**ISSUES?**", inline=False)
    embed.add_field(name='\u200b', value= "Please DM me, or join the support server using g!support.", inline=True)

    await client.send_message(context.message.author, embed=embed)



###### regular commands ######


@client.command(pass_context=True)
async def support(context):
    embed = discord.Embed(**em)
    embed.set_thumbnail(url=winkwonk)
    embed.add_field(name='**Got any issues or suggestions? Please join the support server!**', value= "https://discord.gg/E6GBEjV", inline=False)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def updates(context):
    embed = discord.Embed(**em)
    embed.set_thumbnail(url=winkwonk)
    embed.add_field(name='**RECENT UPDATES**', value= "**UPDATE 25/12/18:** GavBot now reacts to asking who certain characters are. \n **UPDATE 27/12/18:** Added the g!add, g!whois and g!clear commands, fixed some minor typos. \n **UPDATE 29/12/18:** Added the g!say command and the ability to ask who Gavin is, fixed some more minor things. \n **UPDATE 30/12/18:** You can ask him how certain characters are, and his opinon on them. He now reacts to being called cute, adorable and a good boy. \n **UPDATE 05/01/19:** Added the g!tiddies command, edited the g!nsfw command and added long overdue art credits, which you can see using g!credits.", inline=False)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def credits(context):
    embed = discord.Embed(**em)
    embed.set_thumbnail(url=winkwonk)
    embed.add_field(name='**Art Credits**', value= "\u200b", inline=False)
    embed.add_field(name='**Faces/thumbanils: Me**', value= "\u200b", inline=False)
    embed.add_field(name='**Art for g!nut, g!love, and "who is nines": Same-Side**', value= "Tumblr: https://same-side.tumblr.com", inline=False)
    embed.add_field(name='**Art for g!tiddies": Same-Side, DIM, JolieMariella**', value= "Same-Side: https://same-side.tumblr.com \n DIM: https://deep-in-mind67.tumblr.com \n JolieMariella: https://joliemariella.tumblr.com", inline=False)
    await client.say(embed=embed)

#@has_permissions(administrator=True)
@client.command(pass_context = True)
async def add(context,target: discord.Member, *, stuff):
     embed = discord.Embed(**em)
     with open("users.json", "r") as f:
         users = json.load(f)
     await update_users(users, target)
     if users[target.name]["text"] == "no info":
         users[target.name]["text"] = stuff
     else:
         users[target.name]["text"] = users[target.name]["text"] + ", " + stuff
     with open("users.json", "w") as f:
         json.dump(users, f)

     embed.set_thumbnail(url=winkwonk)
     embed.add_field(name='\u200b', value= "'{}' has been added to {}.".format(stuff, target.mention), inline=False)
     await client.say(embed=embed)

@client.command(pass_context = True)
async def whois(context,target: discord.Member):
     embed = discord.Embed(**em)
     with open("users.json", "r") as f:
         users = json.load(f)
     if users[target.name]["text"] == "no info":
         embed.add_field(name='\u200b', value= "I don't know shit about {}.".format(target.mention), inline=False)
         embed.set_thumbnail(url=eyeroll)
     elif target.id == "476176194522316801":
         embed.add_field(name='\u200b', value= "Hah, hah, ha. Very funny, asshole.", inline=False)
         embed.set_thumbnail(url=eyeroll)
     else:
         embed.add_field(name='\u200b', value= "{} is {}.".format(target.mention, users[target.name]["text"]), inline=False)
         embed.set_thumbnail(url=winkwonk)
     await client.say(embed=embed)

@client.command(pass_context = True)
async def clear(context,target: discord.Member):
     embed = discord.Embed(**em)
     with open("users.json", "r") as f:
         users = json.load(f)
     users[target.name]["text"] = "no info"

     with open("users.json", "w") as f:
         json.dump(users, f)

     embed.set_thumbnail(url=winkwonk)
     embed.add_field(name='\u200b', value= "Info for {} has been cleared.".format(target.mention), inline=False)
     await client.say(embed=embed)

@client.command(name="say", pass_context=True)
@has_permissions(administrator=True)
async def say(context, channel: discord.Channel, *, stuff):
    server = context.message.author.server
    embed = discord.Embed(**em)
    embed.add_field(name='\u200b', value= stuff, inline=False)
    embed.set_thumbnail(url=winkwonk)
    await client.send_message(channel, embed=embed)
    await client.delete_message(context.message)

@say.error
async def say_error(error, context):
    if isinstance(error, CheckFailure):
        embed = discord.Embed(**em)
        embed.set_thumbnail(url=smug)
        embed.add_field(name='\u200b', value= "Sorry, fuckface, looks like you don't have the permission to use that.", inline=True)
        await client.send_message(context.message.channel, embed=embed)


@client.command(name="annoyed", pass_context=True)
async def annoyed(context):
    server = context.message.author.server
    with open("servers.json", "r") as f:
        servers = json.load(f)
    embed = discord.Embed(**em)
    embed.add_field(name='\u200b', value= "Annoyance: {}%".format(servers[server.id]["annoyance"]), inline=False)
    if servers[server.id]["annoyance"] <=10:
        embed.set_thumbnail(url=happy)
    elif 10< servers[server.id]["annoyance"] <56:
        embed.set_thumbnail(url=default)
    elif 55< servers[server.id]["annoyance"] <=100:
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
    embed.set_thumbnail(url=mad2)
    embed.add_field(name='\u200b', value= "THIS IS NSFW!", inline=False)
    embed.set_footer(text="The previous image is going to be replaced soon, dw!")
    await client.say(embed=embed)


@client.command(name="roast", pass_context=True)
async def roast(context, target: discord.Member):
    embed = discord.Embed(**em)
    server = context.message.author.server
    with open("servers.json", "r") as f:
        servers = json.load(f)
    if target.id == "476176194522316801":
       embed.set_thumbnail(url=eyeroll)
       embed.add_field(name='\u200b', value= "Oh, you think you're smart, huh? Phcking bitch.", inline=False)
    elif target.id == "477027536660856872":
        possible_responses = [
            "Your uh... your ass looks like plastic! Not that I've been checking, dipshit.",
            "Your eyes are so confusing, I keep getting fucking lost. Wait, no, that, uh, that's not what i meant -",
            "Has your smile caused a car accident yet? I bet people keep getting distracted. BECAUSE IT'S SO UGLY OF COURSE PHCK -",
            "Uh... shit, phck off why should I do what you say?! You're not the boss of me!",
            "If i wanted a bitch i would've gotten a dog, guess i'll have to settle for you....wAIT SHIT!",
            "The smartest thing that's ever come out of your mouth has been my dick...not that i'd ever have sex with you of course...",
            "Take a deep breath and then hold it for about twenty minutes....dammit i just remembered you don't need to breathe"
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
       server = context.message.author.server
       with open("servers.json", "r") as f:
           servers = json.load(f)
       await add_annoyance(servers, server, 1)
       with open("servers.json", "w") as f:
            json.dump(servers, f)
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

@client.command(name="nut")
async def nut():
    embed = discord.Embed(**em)
    embed.set_image(url = "https://cdn.discordapp.com/attachments/506607750630080512/523269447910293515/cheers.png")
    await client.say(embed=embed)


@client.command(name="tiddies")
async def tiddies():
    embed = discord.Embed(**em)
    pics = [
    "https://cdn.discordapp.com/attachments/506242430375428107/531217153341521952/image0.jpg",
    "https://cdn.discordapp.com/attachments/506242430375428107/531217167853682688/image0.png",
    "https://cdn.discordapp.com/attachments/506242430375428107/531217219556868116/image0.jpg",
    "https://cdn.discordapp.com/attachments/506242430375428107/531217421504348181/image0.png",
    "https://cdn.discordapp.com/attachments/506242430375428107/531217431352573982/image0.png",
    "https://cdn.discordapp.com/attachments/506242430375428107/531217806507638814/image0.png",
    "https://cdn.discordapp.com/attachments/506242430375428107/531218712129306626/image0.png",
    "https://cdn.discordapp.com/attachments/506242430375428107/531218722652684298/image0.png",
    "https://cdn.discordapp.com/attachments/506242430375428107/531218739270778905/image0.png",
    "https://cdn.discordapp.com/attachments/481001195016552453/531644268171886592/160832224-288-k274234.jpg",
    "https://cdn.discordapp.com/attachments/481001195016552453/531642143652052992/Screenshot_20190106-1915072.png",
    "https://cdn.discordapp.com/attachments/481001195016552453/531641038700281856/baby_gil.png",
    "https://cdn.discordapp.com/attachments/481001195016552453/531641038167736320/tid_grab.png",
    "https://cdn.discordapp.com/attachments/481001195016552453/531641037656162314/CropperCapture1355.png",
    "https://cdn.discordapp.com/attachments/511378182990069767/531634698938613760/gtiddies1.png",
    "https://cdn.discordapp.com/attachments/511378182990069767/531634704927948800/gtiddies2.png",
    ]
    embed.set_image(url=random.choice(pics))
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
    message.content = message.content.lower()
    embed = discord.Embed(**em)
    with open("servers.json", "r") as f:
        servers = json.load(f)
    await update_data(servers, server)
    with open("servers.json", "w") as f:
        json.dump(servers, f)
    if message.author == client.user:
        return


    elif "connor how many stab wound" in message.content:
        possible_responses = [
            "***28 sTaB wOuNdS***"
            ]
        embed.set_thumbnail(url=smug)

    elif message.content == "connor":

        if servers[server.id]["annoyance"] <= 40:
            possible_responses = [
                "we talking about the tin can?",
                "Why are we talking about the Tin Can?",
                "oh, get lost, Connor.",
                "Bugger off, tin can."
                    ]
            embed.set_thumbnail(url=eyeroll)
        elif 40< servers[server.id]["annoyance"] <61:
            with open("servers.json", "r") as f:
                servers = json.load(f)
            await add_annoyance(servers, server, 1)
            with open("servers.json", "w") as f:
                json.dump(servers, f)
            possible_responses = [
                "we still talking about the fucking tin can?",
                "Ugh not him. Can we change the topic?",
                "oh shut up Connor",
                    ]
            embed.set_thumbnail(url=mad1)
        elif 40< servers[server.id]["annoyance"]:
            with open("servers.json", "r") as f:
                servers = json.load(f)
            await add_annoyance(servers, server, 1)
            with open("servers.json", "w") as f:
                json.dump(servers, f)
            possible_responses = [
                "Can we please shut the fuck up about the tin can?! I'm fucking sick of hearing of about that fucking prick.",
                "Can we please not? I don’t wanna think about that pre-p-pretty big bitch! Yeah....that’s what I was going to say.",
                "What about him?! Connor is stupid? Connor is obnoxious? Connor’s pretty? Connor’s gonna be eating my foot if you keep talking about him!",
                "SHUT THE FUCK UP CONNOR"
                ]
            embed.set_thumbnail(url=mad2)


        with open("servers.json", "r") as f:
            servers = json.load(f)
        await add_annoyance(servers, server, 1)
        with open("servers.json", "w") as f:
            json.dump(servers, f)

###### opinions on characters ######

    elif message.content.startswith ("gavin what do you think about connor"):
        if servers[server.id]["annoyance"] <5:
           possible_responses = [
              "He's... I have to admit, he's pretty. And nice. And... god i have it bad, huh?",
              "I might act like I hate him all the time but... He's a good person.",
              "I don't understand how he can be so nice, after all i've done. He's great, you know?"
              ]
           embed.set_thumbnail(url=smitten)
        elif 4< servers[server.id]["annoyance"] <=10:
            possible_responses = [
                "He's... he's not so bad I guess.",
                "He... I've met worse.",
                "Connor, huh? He's... something else. Something special."
                ]
            embed.set_thumbnail(url=happy)
        elif 10< servers[server.id]["annoyance"] <31:
           with open("servers.json", "r") as f:
               servers = json.load(f)

           await add_annoyance(servers, server, 1)

           with open("servers.json", "w") as f:
               json.dump(servers, f)
           possible_responses = [
                    "he's an android prick, what the hell do you want to hear?",
                    "He's a little bitch and he should've been back with my coffee by now.",
                    "Anderson's plastic pet, huh? Dipshit should just get lost."
                    ]
           embed.set_thumbnail(url=eyeroll)
        elif 30< servers[server.id]["annoyance"] <51:
            with open("servers.json", "r") as f:
                servers = json.load(f)
            await add_annoyance(servers, server, 1)
            with open("servers.json", "w") as f:
                json.dump(servers, f)
            possible_responses = [
                "he's- what the fuck do you want from me?! I- I hate him, that's what I think!",
                "The fuck do you want from me? I hate him."
                ]
            embed.set_thumbnail(url=emb1)
        elif 50< servers[server.id]["annoyance"] <71:
            with open("servers.json", "r") as f:
                servers = json.load(f)
            await add_annoyance(servers, server, 3)
            with open("servers.json", "w") as f:
                json.dump(servers, f)
            possible_responses = [
                "Shut the hell up, I think he should suck my dick! W-Wait I diDN'T MEAN THAT LITERALLY!"
                ]
            embed.set_thumbnail(url=emb2)
        elif servers[server.id]["annoyance"] >70:
            with open("servers.json", "r") as f:
                servers = json.load(f)
            await add_annoyance(servers, server, 3)
            with open("servers.json", "w") as f:
                json.dump(servers, f)
            possible_responses = [
                "I THINK HE'S A PRICK, I HATE HIM! I HATE HIS SMILE, AND HIS LAUGH, A-AND THE WAY HE...he always runs a hand through his...pretty soft hair...I'll fucking kill you."
                ]
            embed.set_thumbnail(url=emb3)

    elif message.content.startswith ("gavin what do you think about hank"):
        with open("servers.json", "r") as f:
            servers = json.load(f)
        await add_annoyance(servers, server, 1)
        with open("servers.json", "w") as f:
            json.dump(servers, f)
        if servers[server.id]["annoyance"] < 66:
           possible_responses = [
                    "What am I supposed to think? He's my shitty colleague.",
                    "Hank? Lieutenant drunk-at-eleven-in-the-morning?",
                    "Not much good shit, that's for sure."
                    ]
           embed.set_thumbnail(url=smug)
        elif servers[server.id]["annoyance"] >65:
            possible_responses = [
                "Oh fuck off, I don't care about that asshole.",
                "Fucker doesn't deserve to be a lieutentant."
                ]
            embed.set_thumbnail(url=eyeroll)

    elif message.content.startswith ("gavin what do you think about markus"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "What? Robo-Jesus? Why the fuck are you asking me for him?",
                "What the hell am i supposed to think about Robo-Jesus?"
                "Dafaq you asking me?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content.startswith ("gavin what do you think about fowler"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "There are worse bosses, I guess.",
                "He's my boss, what do you want to hear?"
                "I just fucking wish he'd give me some more interesting cases."
                ]
        embed.set_thumbnail(url=eyeroll)

    elif message.content.startswith ("gavin what do you think about tina"):
        possible_responses = [
                "Tina is just the best human being ever. Seriously.",
                "Love her. She's probably my best friend."
                "She's awesome!"
                ]
        embed.set_thumbnail(url=winkwonk)

    elif message.content.startswith ("gavin what do you think about nines"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "You mean that android that looks like Connor but with a resting bitch face? Uh, no clue man.",
                "Nines? Barely know him, to be honest.",
                "The android with the gun dick?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content.startswith ("gavin what do you think about chris"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "He's probably the best person here at the precinct, right after Tina.",
                "One of my best friends, a great dude.",
                "He's a good cop, and a really fucking great friend."
                ]
        embed.set_thumbnail(url=winkwonk)

    elif message.content.startswith (("gavin what do you think about kamski", "gavin what do you think about elijah")):
        await add_annoyance(servers, server, 3)
        possible_responses = [
                "Dude created androids, what the hell do you think?",
                "A dickhead. Just. A fucking dickhead. Too bad I'm related to that fucker.",
                "Why the fuck are you asking me?!"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content.startswith ("gavin what do you think about north"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "The android revolution chick? Not much tbh",
                "Don't care for her.",
                "Isn't she Robo-Jesus' girlfriend or something?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content.startswith ("gavin what do you think about simon"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "The android revolution dude? Not much tbh",
                "Don't care for him.",
                "Isn't he Robo-Jesus' boyfriend or something?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content.startswith ("gavin what do you think about josh"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "The android revolution dude? Not much tbh",
                "Don't care for him.",
                "Isn't he one of Robo-Jesus' friends or something?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content.startswith ("gavin what do you think about rupert"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "He's a weird bird android dude, right?",
                "Whomst?",
                "Who's that again?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content.startswith ("gavin what do you think about ralph"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Don't fucking know who that is, my dude.",
                "Who's that again?",
                "Whomst?"
                ]
        embed.set_thumbnail(url=eyeroll)

    elif message.content.startswith ("gavin what do you think about the tracis"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Those android lesbians? They're a cute couple I guess.",
                "I mean, they're a cute couple but other than that, i don't give a shit.",
                "Don't really give a shit, sorry."
                ]
        embed.set_thumbnail(url=default)

    elif message.content.startswith ("gavin what do you think about alice"):
        if servers[server.id]["annoyance"] >15:
            await add_annoyance(servers, server, 1)
            possible_responses = [
                    "A creepy android kid.",
                    "I swear to God, these child androids are fucking creepy.",
                    "Isn't she one of those child androids?"
                    ]
            embed.set_thumbnail(url=disgusting)

        elif servers[server.id]["annoyance"] <16:
            await add_annoyance(servers, server, 1)
            possible_responses = [
                    "Gotta admit, for a robot, she's adorable.",
                    "The robo kid? Not gonna lie, she looks just like a real kid.",
                    ]
            embed.set_thumbnail(url=default)

    elif message.content.startswith ("gavin what do you think about kara"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Whomst?",
                "Dafaq you're asking me? I have literally nothing to do with her.",
                "Who's that again?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content.startswith ("gavin what do you think about luther"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Dafaq you're asking me? I have literally nothing to do with him.",
                "Whomst?",
                "Who's that again?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content.startswith ("gavin what do you think about perkins"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Dafaq you're asking me? I have literally nothing to do with him.",
                "Whomst?",
                "Who's that again?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content.startswith ("gavin what do you think about sumo"):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "A walking flea circus. Stupid fucking dog.",
                "Annoying overgrown puppy.",
                "Why the hell are you asking me for Anderson's dog?!"
                ]
        embed.set_thumbnail(url=disgusting)


###### who is ######

    elif message.content == "gavin who is connor":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "What is he always says? The android sent by CyberLife? What a prick.",
                "Fuckin' android detective.",
                "A fucking prick, that's who he is.",
                "Anderson's plastic pet, lol."
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is hank":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "A shitty Lieutentant at the DPD.",
                "Anderson? A fucking drunkard.",
                "Why are you asking me?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is markus":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Isn't that the Robo-Jesus dude?",
                "The revolution guy? With the blue and green eye? What are you asking me for?",
                "He's like jesus but an android or some shit."
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is fowler":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "My shitty ass boss, that's who.",
                "Shouting bald guy? That's my boss.",
                ]
        embed.set_thumbnail(url=eyeroll)

    elif message.content == "gavin who is tina":
        possible_responses = [
                "The only decent person in this shithole, besides Chris.",
                "Only my best fucking friend."
                "The best person ever. Seriously."
                ]
        embed.set_thumbnail(url=winkwonk)

    elif message.content == "gavin who is nines":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Isn't that the android that looks like Connor but with a resting bitch face? This one?",
                "You mean this fucker?",
                "The android with the gun dick?"
                ]
        embed.set_image(url = "https://cdn.discordapp.com/attachments/526813196103712799/527201131219386383/gunc.png")
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is chris":
        possible_responses = [
                "The only decent person in this shithole, besides Tina.",
                "A good fucking dude.",
                "One of my colleagues, one of the better ones."
                ]
        embed.set_thumbnail(url=default)

    elif message.content == "gavin who is elijah":
        if servers[server.id]["annoyance"] <66:
            await add_annoyance(servers, server, 1)
            possible_responses = [
                    "As in, Kamski? Fucker made androids, right?",
                    "The idiot bitch who created me is into him. Horrible taste, really.",
                    "That's the android fucker dude, right?"
                    ]
            embed.set_thumbnail(url=disgusting)
        elif servers[server.id]["annoyance"] >65:
            await add_annoyance(servers, server, 1)
            possible_responses = [
                    "What do you want from me?! He's my shitty, brother, alright?! Happy?!",
                    "WHY THE FUCK- He's- He's my fucking brother.",
                    "Will you shut the fuck up if I tell you he's my half-brother?!"
                    ]
            embed.set_thumbnail(url=mad2)

    elif message.content == "gavin who is kamski":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "A-android creator dude. Yeah, that's him.",
                "The idiot bitch who created me is into him. Horrible taste, really.",
                "Elijah Kamski? Dude can suck my ass. I mean, he, uh, he created androids.",
                "I don't fucking care about my asshole of a broth- i mean, about the dude."
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is north":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Uh, rings a bell, but I have no clue who exactly.",
                "Android revolution chick? Fuck if I know.",
                "The opposite of south?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is simon":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Android revolution dude? The blond one? Fuck if I know.",
                "Uh, shit, no clue.",
                "Isn't that one of the androids?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is josh":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "One of the android revolution dudes? Fuck if I know.",
                "Uh, rings a bell, but I have no clue who exactly.",
                "Isn't that one of the androids?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is rupert":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "The bird dude?",
                "Whomst've?",
                "The fuck do I know?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is ralph":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Who?",
                "Whomst've?",
                "The fuck do I know?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is traci":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "The android from the Eden club? No clue, man.",
                "Whomst've?",
                "The fuck do I know?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who are the tracis":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Those androids from the Eden club? No clue, man.",
                "Whomst've?",
                "The fuck do I know?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is alice":
        if servers[server.id]["annoyance"] >15:
            await add_annoyance(servers, server, 1)
            possible_responses = [
                    "Isn't that that android kid?",
                    "Some kid android, right? Those are so fucking creepy I swear to God.",
                    "Isn't she one of those child androids?"
                    ]
            embed.set_thumbnail(url=disgusting)

        elif servers[server.id]["annoyance"] <16:
            await add_annoyance(servers, server, 1)
            possible_responses = [
                    "The android kid? Gotta admit, for a robot, she's adorable.",
                    "The robo kid? Not gonna lie, she looks just like a real kid.",
                    ]
            embed.set_thumbnail(url=default)

    elif message.content == "gavin who is kara":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "A household android, right?",
                "Didn't the tin can chase her down a highway?",
                "Isn't she like the mother of that android kid?"
                "The fuck do I know?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is luther":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "That's one of the androids, right?",
                "isn't he like the android kid's dad?",
                "The fuck do I know?"
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is perkins":
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Fuckin' fed, that's who.",
                "The FBI agent Hank punched, right?",
                "Some FBI asshole."
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is sumo":
        possible_responses = [
                "Why the hell are you asking me for Anderson's dog? The one that's not Connor I mean.",
                "Isn't that that walking flee hotel Connor loves so much?"
                "One word: huge, drooling dog. Gag."
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content == "gavin who is gavin":
        possible_responses = [
                "Are you fucking shitting me?",
                "Yeah, fuck you too."
                "Ha. Ha. Ha. SO funny."
                ]
        embed.set_thumbnail(url=eyeroll)

###### how is... ######
    elif message.content.startswith (("gavin how is hank", "gavin how is fowler", "gavin how is connor","gavin how is nines", "gavin how is chris")):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Uh, he's good I guess?",
                "No clue, haven't talked to him lately.",
                "I think he's doing well. I think."
                ]
        embed.set_thumbnail(url=default)

    elif message.content.startswith (("gavin how is markus", "gavin how is simon", "gavin how is josh","gavin how is perkins", "gavin how is luther", "gavin how is rupert", "gavin how is ralph")):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "What do I care?",
                "I've literally never talked to him, what do I care?",
                ]
        embed.set_thumbnail(url=disgusting)

    elif message.content.startswith (("gavin how is sumo")):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "He's literally a dog, how the hell is that flee circus supposed to be?"
                ]
        embed.set_thumbnail(url=default)

    elif message.content.startswith (("gavin how is gilbert")):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "Gil's pretty good!",
                "Gil's doing pretty well, Fucknugget too!"
                ]
        embed.set_thumbnail(url=default)

    elif message.content.startswith (("gavin how is tina")):
        possible_responses = [
                "She's good! She recently got engaged to her girlfriend!",
                "I think she's doing well.",
                "Good, I hope!"
                ]
        embed.set_thumbnail(url=winkwonk)

    elif message.content.startswith (("gavin how is north", "gavin how is traci", "gavin how is kara","gavin how is alice")):
        await add_annoyance(servers, server, 1)
        possible_responses = [
                "What do I care?",
                "I've literally never talked to her, what do I care?",
                ]
        embed.set_thumbnail(url=disgusting)


###### other stuff ######

    elif message.content == "gavin no":
        if servers[server.id]["annoyance"] <81:
           possible_responses = [
              "Gavin YES"
              ]
           embed.set_thumbnail(url=smug)

    elif message.content == "gavin you're cute":
       possible_responses = [
          "What the fuck, I'm not cute.",
          "Oh, back off, I'm not fucking cute.",
          "Fuck you, I'm not fucking cute."
          ]
       embed.set_thumbnail(url=emb3)

    elif message.content == "gavin you're adorable":
       possible_responses = [
          "What the fuck, I'm not adorable.",
          "Oh, back off, I'm not fucking adorable.",
          "Fuck you, I'm not fucking adorable."
          ]
       embed.set_thumbnail(url=emb3)

    elif message.content == "gavin you're a good boy":
       possible_responses = [
          "Do I look like a fucking dog to you?!.",
          "Hah, hah, hah. Funny.",
          "Fuck you, I'm not a dog. Or Connor, for that matter.",
          "Uh, thanks? What kind of compliment is that?!"
          ]
       embed.set_thumbnail(url=emb3)

###### how are you? ######

    elif message.content.startswith(("gavin how are you", "how are you gavin")):
        if servers[server.id]["annoyance"] <=10:
            possible_responses = [
                "I- I'm actually pretty good right now."
                ]
            embed.set_thumbnail(url=happy)

        elif 10< servers[server.id]["annoyance"] <41:
            possible_responses = [
                    "Eh, I'm pretty okay right now."
                    ]
            embed.set_thumbnail(url=default)
        elif 40< servers[server.id]["annoyance"] <61:
            possible_responses = [
                "Could be worse, but I seriously need some fucking coffee right now."
                ]
            embed.set_thumbnail(url=eyeroll)
        elif 60< servers[server.id]["annoyance"] <86:
            with open("servers.json", "r") as f:
                servers = json.load(f)
            await add_annoyance(servers, server, 3)
            with open("servers.json", "w") as f:
                json.dump(servers, f)
            possible_responses = [
                "You know what? I- Don't even get me fucking started."
                ]
            embed.set_thumbnail(url=disgusting)
        elif servers[server.id]["annoyance"] >85:
            with open("servers.json", "r") as f:
                servers = json.load(f)
            await add_annoyance(servers, server, 3)
            with open("servers.json", "w") as f:
                json.dump(servers, f)
            possible_responses = [
                "Oh fuck *off*, fuck this shit, I'm out."
                ]
            embed.set_thumbnail(url=mad2)

###### Do you like? ######

    elif message.content.startswith("gavin do you like cats"):
          if servers[server.id]["annoyance"] < 56:
             if servers[server.id]["annoyance"] > 10:
                with open("servers.json", "r") as f:
                    servers = json.load(f)
                await remove_annoyance(servers, server, 1)
                with open("servers.json", "w") as f:
                    json.dump(servers, f)
             possible_responses = [
                "Yeah, I even got two. Gilbert and Fucknugget.",
                "Sure, they're great.",
                "Little Gremlins. I love them."
                ]
             embed.set_thumbnail(url=default)
          elif servers[server.id]["annoyance"] > 55:
             possible_responses = [
                "What's it to you?",
                "Sure. Now fuck off.",
                "Yeah, and?"
                ]
             embed.set_thumbnail(url=eyeroll)

    elif message.content.startswith("gavin do you like dogs"):
      if servers[server.id]["annoyance"] < 56:
         possible_responses = [
            "Eh, I'm more of a cat person.",
            "Dogs? Pff, have you seen Connor? Follows Anderson around like a goddamn poodle.",
            "Hm, yeah, why not. Kinda remind me of Con- No one. I mean no one."
            ]
         embed.set_thumbnail(url=default)
      elif servers[server.id]["annoyance"] > 55:
         possible_responses = [
            "Cats are way better, now fuck off",
            "Why are you even asking?",
            "Dogs like Anderson's plastic pet? Ye- No! I mean not at all. Ugh."
            ]
         embed.set_thumbnail(url=eyeroll)

###### would you like? ######


    elif message.content.startswith(("gavin would you like a coffe", "gavin would you like some coffe")):
          if servers[server.id]["annoyance"] < 36:
             with open("servers.json", "r") as f:
                 servers = json.load(f)
             await remove_annoyance(servers, server, 2)
             with open("servers.json", "w") as f:
                 json.dump(servers, f)
             possible_responses = [
                "Yeah, thanks, buddy.",
                "Why are you even asking? Of course.",
                "Shit, yeah! Thank you."
                ]
             embed.set_thumbnail(url=winkwonk)
          elif 35 < servers[server.id]["annoyance"] <76:
             with open("servers.json", "r") as f:
                 servers = json.load(f)
             await remove_annoyance(servers, server, 3)
             with open("servers.json", "w") as f:
                 json.dump(servers, f)
             possible_responses = [
                "Fuck, yeah, thank you, coffee saves lives.",
                "Yeah, I really need a fucking cup right now.",
                "Yeah, hurry up and hand it over, dipshit."
                ]
             embed.set_thumbnail(url=mad1)
          elif servers[server.id]["annoyance"] >75:
             with open("servers.json", "r") as f:
                 servers = json.load(f)
             await remove_annoyance(servers, server, 2)
             with open("servers.json", "w") as f:
                 json.dump(servers, f)
             possible_responses = [
                "Yeah, please hurry the fuck up with it, I really need one right now.",
                "Fuck, get a move on, I really need a cup right now.",
                "JUST GIVE ME THE FUCKING COFFEE. Sorry- I'm just. Ugh."
                ]
             embed.set_thumbnail(url=mad2)

    elif message.content == "gavin":

        if servers[server.id]["annoyance"] <36:
            possible_responses = [
                    "Yo, what's the matter?",
                    "What do ya want?",
                    "Ayyy, what's up?",
                    "You called?"
                    ]
            embed.set_thumbnail(url=default)
        elif 35< servers[server.id]["annoyance"] <71:
            possible_responses = [
                "What the fuck do you want?",
                "What is it now?",
                "Yeah, yeah, fuck off",
                "Stop talking and bring me a coffee, dipshit."
                ]
            embed.set_thumbnail(url=eyeroll)
        elif 70< servers[server.id]["annoyance"]:
            possible_responses = [
                "Just fuck off, asshole, don't fucking bother me",
                "I don't fucking care what you want, fuck off",
                "What the *fuck* is it, asshole?"
                ]
            embed.set_thumbnail(url=mad2)



####### Hello-Block ######

    elif message.content.startswith(("hello gavin", "hi gavin", "hey gavin", "what's up gavin")):
        if servers[server.id]["annoyance"] <36:
            possible_responses = [
                    "Yo, what's the matter?",
                    "What do ya want?",
                    "Ayyy, what's up?"
                    ]
            embed.set_thumbnail(url=default)
        elif 35< servers[server.id]["annoyance"] <71:
            possible_responses = [
                "What the fuck do you want?",
                "What is it now?",
                "Yeah, yeah, fuck off",
                "Stop talking and bring me a coffee, dipshit."
                ]
            embed.set_thumbnail(url=eyeroll)
        elif 70< servers[server.id]["annoyance"]:
            possible_responses = [
                "Just fuck off, asshole, don't fucking bother me",
                "I don't fucking care what you want, fuck off",
                "What the *fuck* is it, asshole?"
                ]
            embed.set_thumbnail(url=mad2)


    elif message.content.startswith("glomps gavin"):
       if servers[server.id]["annoyance"] < 66:
          embed.set_thumbnail(url=weeb)
          possible_responses = [
             "***OWO what's this?***"
             ]

    elif message.content == "calm your tits gavin":
       if servers[server.id]["annoyance"] <31:
          annoyance = annoyance -1
          possible_responses = [
          "What are you on about? I'm alright."
          ]
          embed.set_thumbnail(url=default)

       elif 30< servers[server.id]["annoyance"] <76:
          annoyance = annoyance -2
          possible_responses = [
          "Yeah, yeah whatever, man."
          ]
          embed.set_thumbnail(url=eyeroll)
       elif 75< servers[server.id]["annoyance"]:
          annoyance = annoyance -1
          possible_responses = [
             "OH FUCK OFF, I AM CALM."
             ]
          embed.set_thumbnail(url=mad2)

    elif message.content == "hugs gavin":
       embed.set_thumbnail(url=weeb)
       if servers[server.id]["annoyance"] <11:
          possible_responses = [
             "I... Thank you, this is actually... nice?"
             ]
          embed.set_thumbnail(url=happy)
       elif 10 < servers[server.id]["annoyance"] <61:
          possible_responses = [
             "Uh, thanks?"
             ]
          embed.set_thumbnail(url=default)
       elif 60 < servers[server.id]["annoyance"]:
          possible_responses = [
             "Oh, get the fuck off of me!"
             ]
          embed.set_thumbnail(url=mad2)

    elif message.content.startswith(("right gavin", "am i right gavin", "do you agree gavin")):
       possible_responses = [
          "Hell yeah!",
          "Fuck yeah!",
          "Yup!",
          "Nope, lol.",
          "Fuck no.",
          "Nope, absolutely not."
          ]
       embed.set_thumbnail(url=default)

    elif message.content.startswith(("tell me about your cats gavin", "can you tell me about your cats gavin", "gavin tell me about your cats", "gavin can you tell me about your cats")):
       if servers[server.id]["annoyance"] <51:
          with open("servers.json", "r") as f:
              servers = json.load(f)
          await remove_annoyance(servers, server, 2)
          with open("servers.json", "w") as f:
              json.dump(servers, f)
          possible_responses = [
             "Sure! I got two, Gilbert and Fucknugget! Connor doesn't really approve of that name haha.",
             "Well for starters, Gil is a Maine Coon.",
             "Gilbert is a stuck up little bitch but I love him.",
             "Fucknugget is chaotic evil, I swear.",
             "Absolutely, I love taking about them! I've had Gil for a while now, can't even remember, Fucknugget was a rescue... ",
             ]
          embed.set_thumbnail(url=smitten)
       elif 50 < servers[server.id]["annoyance"] < 81:
          with open("servers.json", "r") as f:
              servers = json.load(f)
          await remove_annoyance(servers, server, 5)
          with open("servers.json", "w") as f:
              json.dump(servers, f)
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
       elif 80 < servers[server.id]["annoyance"]:
          with open("servers.json", "r") as f:
              servers = json.load(f)
          await remove_annoyance(servers, server, 5)
          with open("servers.json", "w") as f:
              json.dump(servers, f)
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

    elif message.content.startswith(("bye gavin", "goodbye gavin")):
       possible_responses = [
         "Bye. Dickhead.",
         ]


###### a lot of fuck ######

    elif message.content.startswith(("oh fuck you gavin", "fuck you gavin", "gavin fuck you")):
           with open("servers.json", "r") as f:
               servers = json.load(f)
           await add_annoyance(servers, server, 1)
           with open("servers.json", "w") as f:
               json.dump(servers, f)
           if servers[server.id]["annoyance"] < 66:
              possible_responses = [
                 "Name a time and a place, sweetheart.",
                 "At work? Kinky.",
                 "Sorry, I don't fuck whiny bitches.",
                 "Sorry, but I don't do charity work."
                 ]
              embed.set_thumbnail(url=smug)
           elif servers[server.id]["annoyance"] >65 :
              with open("servers.json", "r") as f:
                  servers = json.load(f)
              await add_annoyance(servers, server, 1)
              with open("servers.json", "w") as f:
                  json.dump(servers, f)
              possible_responses = [
                 "Yeah, whatever. Bitch.",
                 "Wow, so smart. Asshat.",
                 "Don't got anything better, dipshit?",
                 ]
              embed.set_thumbnail(url=eyeroll)

    elif message.content.startswith(("oh go fuck yourself gavin", "go fuck yourself gavin")):
       with open("servers.json", "r") as f:
           servers = json.load(f)
       await add_annoyance(servers, server, 1)
       with open("servers.json", "w") as f:
           json.dump(servers, f)
       if servers[server.id]["annoyance"] < 66:
          possible_responses = [
             "Don't mind if I do, babe.",
             "At work? Kinky.",
             ]
          embed.set_thumbnail(url=smug)
       elif servers[server.id]["annoyance"] >65 :
          with open("servers.json", "r") as f:
              servers = json.load(f)
          await add_annoyance(servers, server, 1)
          with open("servers.json", "w") as f:
              json.dump(servers, f)
          possible_responses = [
             "Yeah, whatever. Bitch.",
             "Wow, so smart. Asshat.",
             "Don't got anything better, dipshit?",
             ]
          embed.set_thumbnail(url=eyeroll)

    elif message.content.startswith(("oh fuck off gavin", "fuck off gavin", "gavin fuck off")):
        with open("servers.json", "r") as f:
           servers = json.load(f)
        await add_annoyance(servers, server, 1)
        with open("servers.json", "w") as f:
           json.dump(servers, f)
        if servers[server.id]["annoyance"] < 66:
          possible_responses = [
            "Wouldn't want to spend anymore time near you than I gotta, fuckface.",
            "Jealous?",
            "You compensating for something?"
            ]
          embed.set_thumbnail(url=smug)
        elif servers[server.id]["annoyance"] >65 :
          with open("servers.json", "r") as f:
              servers = json.load(f)
          await add_annoyance(servers, server, 1)
          with open("servers.json", "w") as f:
              json.dump(servers, f)
          possible_responses = [
             "Yeah, whatever. Bitch.",
             "Wow, so smart. Asshat.",
             "Don't got anything better, dipshit?",
             ]
          embed.set_thumbnail(url=eyeroll)

    elif message.content.startswith(("kill yourself gavin", "go kill yourself gavin", "gavin kill yourself", "gavin go kill yourself")):
       with open("servers.json", "r") as f:
           servers = json.load(f)
       await add_annoyance(servers, server, 1)
       with open("servers.json", "w") as f:
           json.dump(servers, f)
       if servers[server.id]["annoyance"] < 66:
           possible_responses = [
              "If I don't have to talk to you anymore? Gladly.",
              "Oh wow. Such clever. Much insult. I am truly hurt.",
              "only if you go first, babe ~ "
              ]
           embed.set_thumbnail(url=smug)
       elif servers[server.id]["annoyance"] >65 :
          with open("servers.json", "r") as f:
              servers = json.load(f)
          await add_annoyance(servers, server, 1)
          with open("servers.json", "w") as f:
              json.dump(servers, f)
          possible_responses = [
             "Yeah, whatever. Bitch.",
             "Wow, so smart. Asshat.",
             "Don't got anything better, dipshit?",
             ]
          embed.set_thumbnail(url=eyeroll)

    elif message.content.startswith(("i love you gavin", "gavin i love you")):
       if servers[server.id]["annoyance"] < 11:
          possible_responses = [
             "I... Thank you.",
             "Wow, well... thanks.",
             ]
          embed.set_thumbnail(url=happy)
       elif 10 < servers[server.id]["annoyance"] < 56:
          possible_responses = [
             "A horrible decision, really.",
             "Oh, really?",
             "Ew, gross."
             ]
          embed.set_thumbnail(url=smug)
       elif 55 < servers[server.id]["annoyance"] < 86:
          with open("servers.json", "r") as f:
              servers = json.load(f)
          await add_annoyance(servers, server, 1)
          with open("servers.json", "w") as f:
              json.dump(servers, f)
          possible_responses = [
             "Yeah, sure you do.",
             "Oh yeah? Sure, man.",
             ]
          embed.set_thumbnail(url=eyeroll)
       elif 85 < servers[server.id]["annoyance"]:
          with open("servers.json", "r") as f:
              servers = json.load(f)
          await add_annoyance(servers, server, 1)
          with open("servers.json", "w") as f:
              json.dump(servers, f)
          possible_responses = [
             "NO, YOU FUCKING DON'T, YOU DON'T EVEN KNOW ME.",
             "Oh fuck off, you don't. You really fucking don't.",
             ]
          embed.set_thumbnail(url=mad2)

    elif message.content.startswith(("fuck me gavin", "gavin fuck me")):
       if servers[server.id]["annoyance"] < 66:
          possible_responses = [
             "Name a time and a place, babe.",
             "Oh, kinky.",
             ]
          embed.set_thumbnail(url=smug)
       elif 65 < servers[server.id]["annoyance"]:
          with open("servers.json", "r") as f:
              servers = json.load(f)
          await add_annoyance(servers, server, 1)
          with open("servers.json", "w") as f:
              json.dump(servers, f)
          possible_responses = [
             "Ew, gross.",
             "Yeah, no, not gonna happen.",
             ]
          embed.set_thumbnail(url=eyeroll)

    elif message.content.startswith(("shut up gavin", "gavin shut up")):
        possible_responses = [
           "I say whatever the fuck I want, asshole.",
           "You can't tell me what to do, fuckface.",
           ]
        embed.set_thumbnail(url=smug)

    elif message.content.startswith(("gavin i'd die for you", "gavin i'll die for you", "gavin i would die for you")):
        possible_responses = [
           "Then perish.",
           "Trust me, you will.",
           ]
        embed.set_thumbnail(url=smug)
###### just words ######

    elif message.content.startswith("owo"):
        if servers[server.id]["annoyance"] <66:
            embed.set_thumbnail(url=weeb)
            possible_responses = [
            "uwu"
            ]

    elif message.content.startswith("uwu"):
        if servers[server.id]["annoyance"] <66:
            embed.set_thumbnail(url=weeb)
            possible_responses = [
            "***OwO***"
            ]

    elif "vore" in message.content:
        if message.author.id == "508110104726339633":
           return
        elif message.server.id == "475904821053095967":
           user = message.author
           shame = discord.utils.get(message.server.roles,name='shame corner')
           await client.add_roles(user, shame)
           embed.set_thumbnail(url=mad2)
           possible_responses = [
               "SHUT YOUR FUCKING MOUTH WE DON'T TALK ABOUT THAT HERE"
               ]
        elif "flavor" in message.content:
            pass
        else:
           with open("servers.json", "r") as f:
               servers = json.load(f)
           await add_annoyance(servers, server, 10)
           with open("servers.json", "w") as f:
               json.dump(servers, f)
           embed.set_thumbnail(url=mad2)
           possible_responses = [
               "SHUT YOUR FUCKING MOUTH WE DON'T TALK ABOUT THAT HERE"
               ]

    elif message.content == "dick":
        embed.set_thumbnail(url=lewd)
        if servers[server.id]["annoyance"] <66:
            possible_responses = [
            "Mhh dick. Slurp."
            ]

    elif message.content == "hewwo gavin":
        embed.set_thumbnail(url=weeb)
        possible_responses = [
        "I'M A BAD BITCH YOU CAN'T STOP ME"
        ]

    elif message.content.startswith(("gavin stop", "stop gavin")):
        embed.set_thumbnail(url=smug)
        possible_responses = [
        "I'M A BAD BITCH YOU CAN'T STOP ME"
        ]

    elif message.content == "gay":
        embed.set_thumbnail(url=default)
        possible_responses = [
        "MOVE I'M GAY"
        ]


    else:
        await client.process_commands(message)
        return

    await client.send_typing(message.channel)
    time.sleep(1)
    embed.add_field(name='\u200b', value= random.choice(possible_responses), inline=False)
    if message.content == "gavin":
        embed.set_footer(text="*I'm still working my shit out, in development or whatever, so don't be a dick, 'kay?*")
    elif message.content == "hello gavin":
        embed.set_footer(text="*I'm still working my shit out, in development or whatever, so don't be a dick, 'kay?*")
    elif message.content == "hi gavin":
        embed.set_footer(text="*I'm still working my shit out, in development or whatever, so don't be a dick, 'kay?*")
    elif message.content == "hey gavin":
        embed.set_footer(text="*I'm still working my shit out, in development or whatever, so don't be a dick, 'kay?*")
    await client.send_message(message.channel, embed=embed)
    await client.process_commands(message)





###### dev commands ######

@client.command(name='inc',
                brief="these are all deveoper commands right now",
                pass_context = True)

async def inc(context):
    server = context.message.author.server
    with open("servers.json", "r") as f:
        servers = json.load(f)
    servers[server.id]["annoyance"] = servers[server.id]["annoyance"] + 20
    with open("servers.json", "w") as f:
        json.dump(servers, f)
    await client.say(servers[server.id]["annoyance"])

@client.command(name='dec', pass_context = True)

async def dec(context):
    server = context.message.author.server
    with open("servers.json", "r") as f:
        servers = json.load(f)
    servers[server.id]["annoyance"] = servers[server.id]["annoyance"] - 20
    with open("servers.json", "w") as f:
        json.dump(servers, f)
    await client.say(servers[server.id]["annoyance"])

@client.command(pass_context=True)
async def servers(context):
    await client.say(len(client.servers))


client.run(str(os.environ.get("TOKEN")))
