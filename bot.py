import os
import discord

from rss import feedRS
from discord.ext import tasks, commands
from dotenv import load_dotenv

load_dotenv(override=True)
TOKEN = os.getenv('TOKEN')
TOKENCH = int(os.getenv('TOKENCH'))
RSS = os.getenv('RSS')
RSS2 = os.getenv('RSS2')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    feedRS.start(TOKENCH,RSS2,client)


client.run(TOKEN)


