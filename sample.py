import discord

TOKEN = 'NDc2MTc2MTk0NTIyMzE2ODAx.Dkp7pg.1KHBt69SM0J1b5FXPrhFWw56vks'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('g!hello'):
        msg = 'Fuck off, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('Gavin?'):
        await client.send_message(message.channel, 'What the fuck do ya want, dipshit?')
    elif message.content.startswith('g!coffee'):
        await client.send_message(message.channel, 'Bring me a coffee, dipshit!')        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
