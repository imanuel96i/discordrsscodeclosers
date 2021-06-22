import os
import sqlite3

con = sqlite3.connect('mydb.db')

cur = con.cursor()

cur.execute('create table if not exists krupdates (id integer, title text, link text)')
cur.execute('create table if not exists ccupdates (id integer, title text, link text)')

#!Register new KR update to DB
def regkrupdates(data):
    cur.executemany("INSERT INTO krupdates VALUES(?, ?, ?)", data)
    con.commit()
    con.close

#!Register new CC update to DB
def regccupdates(data):
    cur.executemany("INSERT INTO ccupdates VALUES(?, ?, ?)", data)
    con.commit()
    con.close

#!Check if exist new update on DB
def listkrupdates(id):
    list = cur.execute('SELECT id from krupdates where id="'f'{id}"')
    row = list.fetchone()
    if row==None:
        list = cur.execute('SELECT id from krupdates order by id desc')
        row = list.fetchone()
        if row==None:
            return 'New Update'
        elif row[0]<int(id):
            return 'New Update'
        elif row[0]>=int(id):
            return 'No Update'
    elif row[0]==int(id):
        return 'Already Update Announced'
    else:
        return 'Error'

#!Check if exist new update on DB
def listccupdates(id):
    list = cur.execute('SELECT id from ccupdates where id="'f'{id}"')
    row = list.fetchone()
    if row==None:
        list = cur.execute('SELECT id from ccupdates order by id desc')
        row = list.fetchone()
        if row[0]<int(id):
            return 'New Update'
        elif row[0]>=int(id):
            return 'No Update'
    elif row[0]==int(id):
        return 'Already Update Announced'
    else:
        return 'Error'