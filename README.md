# DiscordRSSCodeClosers
This bot make new announcements via rss forum on codeclosers forum

First of all you need to know this project was created with python 3.9.5

You need to work with virtual enviroment 

How to do in windows?
 ```
 in cmd or powershell (with admin permission)
 python3 -m venv env
 use env\Scripts\activate to enter in virtual enviroment
 ```

Also you need to create a .env file with this tokens
```
 TOKEN= here will be your discord bot token
 RSS= here will be your link of RSS forum
 TOKENCHKR= here will be your channel id where you want to be announced
 RSS2= working....
 ```

 If you want to execute the bot with a bat file you need to create one with this
 ```
@echo off
cmd /k "cd /d (here will be your virtual environment route without parenthesis)  & activate & cd /d (here will be your bot route without parenthesis) & py bot.py"
pause
 ```