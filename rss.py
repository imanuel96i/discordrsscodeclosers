import os
import feedparser
import db

from discord.ext import tasks

check = 'closers kr'

@tasks.loop(hours=1)
async def feedRSSKR(token,rss,client):
    NewsFeed = feedparser.parse(f'{rss}')
    for feed in NewsFeed.entries:
        if check in feed.title.lower():
            #!Si entra en este if significa que no encontro el id de la publicacion y mayor a los id registrados
            if db.listkrupdates(feed.id)=='New Update':
                #Recolecta los datos para registrar y registra
                data = [(feed.id, feed.title, feed.link)]
                db.regkrupdates(data)
                #Se anuncia en el canal de discord asociado
                channel = client.get_channel(token)
                await channel.send(
                                'Actualizacion: 'f'{feed.title}' '\n' 'Link: 'f'{feed.link}'
                )
                print('New Update: 'f'{feed.title}')
            #!Si entra en este if significa que encontro el id o este es menor a los id ya registrados
            elif db.listkrupdates(feed.id)=='No Update' or db.listkrupdates(feed.id)=='Already Update Announced':
                # db.regkrupdates(data)
                print('No Update')
            elif db.listkrupdates(feed.id)=='Error':
                print('error')

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
