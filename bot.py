import os
import discord

from rss import feedRSSKR
from discord.ext import tasks, commands
from dotenv import load_dotenv

load_dotenv(override=True)
TOKEN = os.getenv('TOKEN')
TOKENCHKR = int(os.getenv('TOKENCHKR'))
RSS = os.getenv('RSS')
# RSS2 = os.getenv('RSS2')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    feedRSSKR.start(TOKENCHKR,RSS,client)

@client.event
async def on_message(message):
    if message.channel.id == (825529446345736214):
        await client.get_channel(711454318372323399).send(f'{message.content}')
        print(f'{message.author.name}: {message.content}')

client.run(TOKEN)


PRUEBA = False