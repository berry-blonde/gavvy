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
        "He's a Maine Coon."
    ]

    await client.say(random.choice(possible_responses) + ' ' + context.message.author.mention)

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


@client.event
async def on_message(message):
    
##    message.content = message.content.lower()
    ##if message.author == client.user:
        ##return
    if message.content.startswith('gavin, what do you think about connor?'):
        msg = [
            "Connor? Stupid fucking android.",
            "I mean, he doesn't look that bad, but he's still a piece of plastic.",
            "Phck, what's it to you, asswipe?"

        ]
        await client.send_message(message.channel, random.choice(msg))
        
    elif message.content.startswith('gavin?'):
        await client.send_message(message.channel, 'What the fuck do ya want, dipshit?')
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
    elif message.content.startswith('i love you gavin'):
         possible_responses = [
             "A horrible decision, really.",
             "Oh, really?",
        ]
         await client.send_message(message.channel,random.choice(possible_responses))
    elif message.content.startswith('g!roast Connor'):
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

         
    elif 'convin' in message.content:
        embed = discord.Embed()
        embed.set_image(url="https://78.media.tumblr.com/f5d09004bbc90e513437b85ab1624b47/tumblr_inline_p9wi304wm91tb0p74_500.gif")
        msg=await client.send_message(message.channel,embed=embed)
##        time.sleep(1.5)
##        await client.delete_message(msg)
    elif 'connor' or "Connor" in message.content:
        embed = discord.Embed()
        embed.set_image(url="https://media.discordapp.net/attachments/476152751458353162/476177336023121920/image.gif")
        msg=await client.send_message(message.channel,embed=embed)
##        time.sleep(3)
##        await client.delete_message(msg)
    elif 'bromance' or "Bromance" in message.content:
        embed = discord.Embed()
        embed.set_image(url="https://78.media.tumblr.com/6e4fb644833574292fb15f3ca7d93330/tumblr_p9v5o26HCJ1qfinneo4_540.gif")
        msg=await client.send_message(message.channel,embed=embed)
##        time.sleep(3)
##        await client.delete_message(msg)
    elif 'gavin' or "Gavin" in message.content:
        embed = discord.Embed()
        embed.set_image(url="https://78.media.tumblr.com/f5c25cdcc64cca0120592fc7c4a7ff56/tumblr_pbw64kScnN1xvdju4o4_500.gif")
        msg=await client.send_message(message.channel,embed=embed)
##        time.sleep(2.5)
##        await client.delete_message(msg)
    elif ':3' in message.content:
        await client.send_message(message.channel, 'Meoww >:3')
    elif 'owo' in message.content:
        await client.send_message(message.channel, '*glomps* ' + message.author.mention)
    elif 'fuck' in message.content:
        await client.send_message(message.channel, 'Phck')
    elif 'gun' in message.content:
        await client.send_message(message.channel, "I'm sorry, but the word 'gun' is banned. In the future, please use 'rooty tooty point and shooty' instead. Dipshit.")


    await client.process_commands(message)


@client.command(name='wink',
                brief= " = make Gavin wink.")
async def wink():
    embed = discord.Embed()
    embed.set_image(url="https://78.media.tumblr.com/f5d09004bbc90e513437b85ab1624b47/tumblr_inline_p9wi304wm91tb0p74_500.gif")
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
    await client.say(random.choice(possible_responses) + target.mention)

@client.command(name='triggers',
                brief= " = shows you what Gavin responds to in chats and dms.")
async def triggers():
    embed = discord.Embed(title="Chat Triggers", color=0x582014)
    embed.add_field(name="Gavin will resonds to the following keywords in chat:", value=" - Connor \n - convin \n - Gavin \n - bromance \n - fuck off gavin \n - oh fuck off gavin \n - fuck you gavin \n - oh fuck you gavin \n - fuck yourself gavin \n - fuck me gavin \n - I love you gavin", inline=False)
    await client.say(embed=embed)
    

     
client.run(TOKEN)

