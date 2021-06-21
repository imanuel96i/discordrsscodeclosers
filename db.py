import os
import sqlite3

con = sqlite3.connect('mydb.db')

cur = con.cursor()

cur.execute('create table if not exists krupdates (id integer, title text, link text)')

def registrar(data):
    cur.executemany("INSERT INTO krupdates VALUES(?, ?, ?)", data)
    con.commit()
    con.close

def listar(id):
    cur.execute('SELECT * from krupdates where id="'f'{id}" and id>="'f'{id}"')
    
    if cur.fetchone():
        return True
    else:
        return False