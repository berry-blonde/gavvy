import random
import discord
import time
from discord.ext.commands import Bot


BOT_PREFIX = 'g!'
TOKEN = 'NDc2MTc2MTk0NTIyMzE2ODAx.DloksA.QBYAQGbKPoBgF9D-rLqHEWBL5oQ'
client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="with Connor's dick"))

@client.command(name='cat',
                brief=" = Gavin tells you something about his cat. Maybe.",
                pass_context=True)
async def cat(context):
    possible_responses = [
        "His name is Gilbert.",
        "What's it to ya?",
        "Gil's a Maine Coon.",
        "I also got a kitten, called it Fucknugget. Not that Connor is too happy about the name.",
        "Gilbert might be a bitch, but Fucknugget is chaotic evil i swear.",
        "Both Gil and Fucknugget are way too fucking needy for their own good. Keep stealing my bed and boyfriend."
    ]

    await client.say(random.choice(possible_responses))


@client.command(name='hello',
                brief= " = Say hello to Gavin.",
                pass_context=True)

async def hello(context):
    
    await client.say('Fuck off, ' + context.message.author.mention)

@client.command(name='coffee',
                brief= " = Gavin tells you to get him a coffee.")

async def coffee():
    embed = discord.Embed()
    embed.set_image(url="https://em.wattpad.com/3064755cac3c2827f01e17df6e7ab606f232b7ac/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f434c617534526b7a4967746e4a413d3d2d3539333133313936322e313533616162303462623633626138633836353132383932383532362e676966?s=fit&w=720&h=720")
    await client.say(embed=embed)

@client.command(name='horny',
                brief= " = What do you expect from that one, huh?")

async def horny():
    embed = discord.Embed()
    embed.set_image(url="https://media.discordapp.net/attachments/476189549366738944/490559000631443466/DbozB11V0AMVmgN.jpg")
    await client.say(embed=embed)
    
#475904821518532629
#478418418727518208
@client.event
async def on_message(message):
    server = message.server

    if message.author == client.user:
        return
    elif message.content.startswith("g!say"):
        await client.send_message(client.get_channel('475904821518532629'), message.content[5:])
        await client.delete_message(message)
    message.content = message.content.lower()
    if message.content.startswith('gavin, what do you think about connor?'):
        msg = [
            "Connor? Stupid fucking android.",
            "I mean, he doesn't look that bad, but he's still a piece of plastic.",
            "Phck, what's it to you, asswipe?"

        ]
        await client.send_message(message.channel, random.choice(msg))
    elif message.content.startswith('gavin no'):
        await client.send_message(message.channel, "Gavin YES")
    elif message.content.startswith('gavin yes'):
        await client.send_message(message.channel, "HELL YEAH") 
    elif message.content.startswith('gavin?'):
        await client.send_message(message.channel, 'What the fuck do ya want, dipshit?')
    elif 'right gavin' in message.content:
        await client.send_message(message.channel, "hell yeah")
        
    elif message.content.startswith('g!verse connor'):
        possible_respones = [
            "Why would I care? Phck off! I've never thought about that! Now back the fuck off!",
            "Why are you asking me?! Go ask him yourself!",
            "I don't care! Don't ask me! I- Why would I even think about that?!",
            
        ]
        await client.send_message(message.channel, random.choice(possible_respones))
    elif message.content.startswith('g!verse gavin'):
        possible_respones = [
            "That's none of your fucking business!",
            "What the fuck do I look like to you?!",
            "That's personal, you fucking asswipe!",
            
        ]

        await client.send_message(message.channel, random.choice(possible_respones))
    elif message.content.startswith('fuck you gavin'):
        possible_responses = [
            "Name a time and a place, sweetheart.",
            "At work? Kinky.",
            "Sorry, I don't fuck whiny bitches.",
            "Sorry, but I don't do charity work."
            ]
        await client.send_message(message.channel, random.choice(possible_responses))
            
    elif message.content.startswith('oh fuck you gavin'):
        possible_responses = [
            "Name a time and a place, sweetheart.",
            "At work? Kinky.",
            "Sorry, I don't fuck whiny bitches.",
            "Sorry, but I don't do charity work."
        ]
        await client.send_message(message.channel, random.choice(possible_responses))
    elif message.content.startswith('go fuck yourself gavin'):
         possible_responses = [
             "Don't mind if I do, babe.",
             "At work? Kinky.",
        ]
         await client.send_message(message.channel,random.choice(possible_responses))
    elif message.content.startswith('fuck off gavin'):
         possible_responses = [
             "Wouldn't want to spend anymore time near you than I gotta, fuckface.",
             "Jealous?",
             "You compensating for something?"
        ]
         await client.send_message(message.channel,random.choice(possible_responses))
    elif message.content.startswith('oh fuck off gavin'):
         possible_responses = [
             "Wouldn't want to spend anymore time near you than I gotta, fuckface.",
             "Jealous?",
             "You compensating for something?"
        ]
         await client.send_message(message.channel,random.choice(possible_responses))
    elif message.content.startswith('kill yourself gavin'):
         possible_responses = [
             "If I don't have to talk to you anymore? Gladly.",
             "Oh wow. Such clever. Much insult. I am truly hurt.",
             "only if you go first, babe ~ "
        ]
         await client.send_message(message.channel,random.choice(possible_responses))
    elif message.content.startswith('i love you gavin'):
         possible_responses = [
             "A horrible decision, really.",
             "Oh, really?",
        ]
         await client.send_message(message.channel,random.choice(possible_responses))
    elif message.content.startswith('g!roast connor'):
        possible_responses = [
            "Your uh... your ass looks like plastic! Not that I've been checking, dipshit.",
            "Your eyes are so confusing, I keep getting fucking lost. Wait, no, that, uh, that's not what i meant -",
            "Has your smile caused a car accident yet? I bet people keep getting distracted. BECAUSE IT'S SO UGLY OF COURSE PHCK -",
            "Uh... shit, phck off why should I do what you say?! You're not the boss of me!",
        ]
        await client.send_message(message.channel,random.choice(possible_responses))   
    elif 'markus is a bottom' in message.content:
        await client.send_message(message.channel,'he fucking is')
    elif 'fuck me gavin' in message.content:
        embed = discord.Embed()
        embed.set_image(url="https://78.media.tumblr.com/f5d09004bbc90e513437b85ab1624b47/tumblr_inline_p9wi304wm91tb0p74_500.gif")
        await client.send_message(message.channel,embed=embed)
        await client.send_message(message.channel,'Name a time and a place, babe.')
    elif message.content.startswith("i'm certainly going to miss our bromance."):
         await client.send_message(message.channel,"Oh? Is that so? Prick.")
    elif 'shut up gavin' in message.content:
        await client.send_message(message.channel, "I say whatever the fuck I want, asshole.")
    elif 'gavin shut up' in message.content:
        await client.send_message(message.channel, "I say whatever the fuck I want, asshole.")
         
    elif 'convin' in message.content:
        embed = discord.Embed()
        embed.set_image(url="https://78.media.tumblr.com/f5d09004bbc90e513437b85ab1624b47/tumblr_inline_p9wi304wm91tb0p74_500.gif")
        msg=await client.send_message(message.channel,embed=embed)
        time.sleep(1.5)
        await client.delete_message(msg)
    elif 'connor' in message.content:
        embed = discord.Embed()
        embed.set_image(url="https://media.discordapp.net/attachments/476152751458353162/476177336023121920/image.gif")
        msg=await client.send_message(message.channel,embed=embed)
        time.sleep(3)
        await client.delete_message(msg)
    elif 'bromance' in message.content:
        embed = discord.Embed()
        embed.set_image(url="https://78.media.tumblr.com/6e4fb644833574292fb15f3ca7d93330/tumblr_p9v5o26HCJ1qfinneo4_540.gif")
        msg=await client.send_message(message.channel,embed=embed)
        time.sleep(3)
        await client.delete_message(msg)
    elif 'gavin' in message.content:
         ##await client.send_message(message.channel,"IT'S MY FUCKING BIRTHDAY, BITCHES")
        embed = discord.Embed()
        embed.set_image(url="https://78.media.tumblr.com/f5c25cdcc64cca0120592fc7c4a7ff56/tumblr_pbw64kScnN1xvdju4o4_500.gif")
        msg=await client.send_message(message.channel,embed=embed)
        time.sleep(2.5)
        await client.delete_message(msg)
    elif ':3' in message.content:
        if message.author.id == "172002275412279296":
            return
        elif message.author.id == "213466096718708737":
            return
        else:
            await client.send_message(message.channel, 'Meoww >:3')
    elif 'owo' in message.content:
        if '=owo' in message.content:
            return
        else:
            await client.send_message(message.channel, '*glomps* ' + message.author.mention)
##    elif 'fuck' in message.content:
##        await client.send_message(message.channel, 'Phck')
    elif 'gun' in message.content:
        await client.send_message(message.channel, "I'm sorry, but the word 'gun' is banned. In the future, please use 'rooty tooty point and shooty' instead. Dipshit.")
    elif 'vore' in message.content:
        await client.send_message(message.channel, "SHUT YOUR FUCKING MOUTH WE DON'T TALK ABOUT THAT HERE")
    elif 'dick' in message.content:
        await client.send_message(message.channel, "Mhmmm dick. Slurp.")
    elif 'bye' in message.content:
        await client.send_message(message.channel, "Bye. Dickhead.")
    elif message.content.startswith('oof'):
        await client.send_message(message.channel, "OOF")
    elif ' oof' in message.content:
        await client.send_message(message.channel, "OOF")
    elif 'hewwo' in message.content:
        if message.author.id == "467913111551082518":
            return
        else:
            await client.send_message(message.channel, "hewwo owo")
    elif message.content.startswith('good morning'):
        if message.author.id == "467913111551082518":
            return
        else:
            await client.send_message(message.channel, "Morning, SLUTS")
    elif message.content.startswith('morning'):
        if message.author.id == "467913111551082518":
            return
        else:
            await client.send_message(message.channel, "Morning, SLUTS")
    elif 'licc' in message.content:
        await client.send_message(message.channel, "licc this DICK")
    elif message.content.startswith('hello'):
        await client.send_message(message.channel, "hello, SLUTS")
    elif 'gavin stop' in message.content:
        await client.send_message(message.channel, "I'M A BAD BITCH YOU CAN'T STOP ME")
    elif 'stop gavin' in message.content:
        await client.send_message(message.channel, "I'M A BAD BITCH YOU CAN'T STOP ME")
    elif 'gay' in message.content:
        await client.send_message(message.channel, "MOVE I'M GAY")
    elif 'xd' in message.content:
        await client.send_message(message.channel, "very rawr XD so random omfg lulz")
    elif 'cats' in message.content:
        possible_responses = [
            "Did someone say cats??? Anyone wanna see a pic of Gilbert???",
            "Cats? I got a cat too, y'know. his name is Gil and he's a fucking prick.",
            "Cats are great, seriously. Unlike people, fuck those."
        ]
        await client.send_message(message.channel, random.choice(possible_responses))
    elif 'ß' in message.content:
        if message.author.id == "448609719641309190":
                return
        elif message.author.id == "265507501007568899":
                return
        elif 'scheiße' in message.content:
            return
        else:
            await client.send_message(message.channel, "stop fucking abusing the ß you freaks")
    elif 'ü' in message.content:
        if message.author.id == "448609719641309190":
                return
        elif 'nüt' in message.content:
            if message.author.id == "265507501007568899":
                await client.send_message(message.channel, "no, just, no. stop using that fucking word, fitz. fuck you. \nEvie's gonna defenestrate you at that rate.")
            else:
                await client.send_message(message.channel, "no, just, no. stop using that fucking word, fuck you.")
        elif message.author.id == "265507501007568899":
                return
        else:
            await client.send_message(message.channel, "leave the fucking ü alone, you fucking degenerates")
    elif 'ö' in message.content:
        if message.author.id == "448609719641309190":
                return
        elif message.author.id == "265507501007568899":
                return
        else:
            await client.send_message(message.channel, "what the fuck did the german language ever do to you? let the fucking ö be, asshat")
    elif 'ä' in message.content:
        if message.author.id == "448609719641309190":
                return
        elif message.author.id == "265507501007568899":
                return
        else:
            await client.send_message(message.channel, "really now? fucking really? the ä? what the fuck is wrong with you, stop absuing it wtf")
    elif "i#m a top" in message.content:
        if message.author.id == "471890374277726209":
            await client.send_message(message.channel, "nah you're fucking not dude")
        else:
            return
    elif "i'm a top" in message.content:
        if message.author.id == "471890374277726209":
            await client.send_message(message.channel, "nah you're fucking not dude")
    elif "gavpocalypse" in message.content:
        await client.send_message(message.channel, ":ban:")
        else:
            return

##    elif message.content.startswith("g!say"):
##        await client.send_message(message.channel, message.content[5:])
##        await client.delete_message(message)
##    elif message.content.startswith("g!say"):
##        await client.send_message(client.get_channel('475904821518532629'), message.content[5:])
##        await client.delete_message(message)
        
    await client.process_commands(message)


    

@client.command(name='wink',
                brief= " = make Gavin wink.")
async def wink():
    embed = discord.Embed()
    embed.set_image(url="https://78.media.tumblr.com/f5d09004bbc90e513437b85ab1624b47/tumblr_inline_p9wi304wm91tb0p74_500.gif")
    await client.say(embed=embed)
    
@client.command(name='bottom',
                brief= " = THAT'S BOTTOM TEXT.")
async def bottom():
    embed = discord.Embed()
    embed.set_image(url="https://i.kym-cdn.com/photos/images/newsfeed/001/171/241/942.jpg")
    await client.say(embed=embed)

@client.command(name='kinkshame',
                brief= " = kinkshame someone specific.",
                pass_context=True)
async def kinkshame(context, target: discord.Member):
    embed = discord.Embed()
    embed.set_image(url="https://66.media.tumblr.com/38cb8164b99a32bdc1a067075f63ecad/tumblr_opnib7DvNl1uaylcyo1_1280.gif")
    await client.say(embed=embed)
    await client.say("you have been kinkshamed by " + context.message.author.mention + " you horny little bastard " + target.mention)

@client.command(name='genkinkshame',
                brief= " = kinkshame in general.")
async def genkinkshame():
    embed = discord.Embed()
    embed.set_image(url="https://66.media.tumblr.com/38cb8164b99a32bdc1a067075f63ecad/tumblr_opnib7DvNl1uaylcyo1_1280.gif")
    await client.say(embed=embed)



@client.command(name='nsfw',
                brief= " = Gavin tells the Server this is NSFW.")
async def nsfw():
    embed = discord.Embed()
    embed.set_image(url="https://media.discordapp.net/attachments/475918776857133056/477203747509108756/1533844628299.png?width=623&height=670")
    await client.say(embed=embed)

    
@client.command(name='bringcoffee',
                brief= " = bring Gavin a coffee.")
async def bringcoffee():
    embed = discord.Embed()
    embed.set_image(url="https://78.media.tumblr.com/67400984a78433b531889554e02c86da/tumblr_inline_paxa26e2mD1sbxiqs_540.gif")
    await client.say(embed=embed)

@client.command(name='roast',
                description= "have Gavin roast a member by tagging them. Works with 'Connor' too.",
                brief= " = have Gavin roast a member by tagging them.")

async def roast(target: discord.Member):
    if target == client.user:
         await client.say("Oh, you think you're smart, huh? Phcking bitch.")
         return
    if target.id == "467913111551082518":
        possible_responses = [
            "Your uh... your ass looks like plastic! Not that I've been checking, dipshit.",
            "Your eyes are so confusing, I keep getting fucking lost. Wait, no, that, uh, that's not what i meant -",
            "Has your smile caused a car accident yet? I bet people keep getting distracted. BECAUSE IT'S SO UGLY OF COURSE PHCK -",
            "Uh... shit, phck off why should I do what you say?! You're not the boss of me!",
        ]
        await client.say(random.choice(possible_responses))
        return
    
        
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
    await client.say(random.choice(possible_responses) + target.mention)
    embed = discord.Embed()
    embed.set_image(url="https://images-ext-2.discordapp.net/external/7khv_Wu7yRsfXserZo_e0Ek_K3ow20tcNFd6IR9jUzs/https/media.discordapp.net/attachments/476152751458353162/476177535936364545/image.gif")
    await client.say(embed=embed)


@client.command(name='verse',
                description = "Gavin tells you whether the tagged member is a switch, bottom or top. Work with 'Connor' and 'Gavin' too.",
                brief= " = Gavin tells you the the target's preference.")
async def verse(target: discord.Member):
    possible_responses = [
        "A little bottom bitch. Tsk.",
        "Hm, guess they're a switch. Good for them.",
        "Dumbass thinks they're a top, but they're a fucking bottom. heh.",
        "Wow, an actual top. Didn't take you for that at first.",
    ]
    if target.id == "471890374277726209":
        await client.say("Mia thinks she's a top, but she's a fucking bottom. Asshat.")
    elif target.id == "202499161034063873":
        await client.say("Parker thinks he's a top, but he's a fucking bottom. Dumbfuck.")
    else:
        await client.say(random.choice(possible_responses))



@client.command(name='triggers',
                brief= " = shows you what Gavin responds to in chats and dms.")
async def triggers():
    await client.say("```Chat Triggers \n Gavin will resonds to the following keywords in chat: \n - Connor \n - convin \n - Gavin \n - bromance \n - fuck off gavin \n - oh fuck off gavin \n - fuck you gavin \n - oh fuck you gavin \n - fuck yourself gavin \n - fuck me gavin \n - I love you gavin \n as well as a few other, fun ones ;)```")


        


     
client.run(TOKEN)

