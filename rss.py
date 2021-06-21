import os
import feedparser
import db

from discord.ext import tasks
from dotenv import load_dotenv, set_key

load_dotenv(override=True)
ID = os.environ['ID']
check = 'closers kr'


@tasks.loop(seconds=10)
async def feedRS(token,rss,client):
    NewsFeed = feedparser.parse(f'{rss}')
    for feed in NewsFeed.entries:
        if check in feed.title.lower():
            data = [(feed.id, feed.title, feed.link)]
            # db.registrar(data)
            print(db.listar(feed.id))
            break
    # entry = NewsFeed.entries[0]
    # title = entry.title
    # link = entry.link
    # rsid = entry.id
    # if ID != entry.id:
    #     channel = client.get_channel(token)
        # await channel.send(
        #     'Actualizacion: 'f'{title}' '\n' 'Link: 'f'{link}'
    #     # )
    # else:
    #     return
