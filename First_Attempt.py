#Ver: 3.8
import os
import random
import discord
from dotenv import load_dotenv
#import FOAAS_calls
from foaas import fuck

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
#-----------------================print when the bot joins/goes online================-----------------
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
            f'{client.user.name} has connected to Discord!'
            f'{guild.name}(id: {guild.id})'
    )

    #members = '\n - '.join([member.name for member in guild.members])
    #print(f'Guild Members:\n - {members}')
#-----------------================Respond to messages================-----------------
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #lists
    agree_with_me = ["They Right","That's Factual","Oh on god","They do be spitting facts right now","No cap","This is true", "No no, he got a point"]
    retorts = ["Look, I'm just a bot. There's no need to harass me", "Aye, why you copying me?", "Bro, quit mocking me, just doing my job."]
    waiting = ["its being implemented, just wait"]

    #if the command !right is called, send a msg back
    if message.content == '!right':
        response = random.choice(agree_with_me)
        await message.channel.send(response)
    #if a user sends a msg that copies one of the bots, send a retort
    elif message.content in agree_with_me or message.content in retorts:
        response = random.choice(retorts)
        await message.channel.send(response)
    #if !fuck sends a random fuck you
    elif '!fuck' in message.content:
        author = str(message.author)
        len_author = len(author) - 5
        msg = message.content
        msgA = msg.split()
        if len(msgA) == 2:
            response = fuck.random(name=msgA[1], from_=author[:len_author]).text
        else:
            response = "Formatting error, try '!fuck name'"
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(TOKEN)
