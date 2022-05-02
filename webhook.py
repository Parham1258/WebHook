import os
from time import sleep
from discord_webhook import DiscordWebhook

class color : 
    Red = '\033[91m'
    Orange='\033[93m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'

def slowprint(text: str, speed: float, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        sleep(speed)
    if newLine:
        print()

slowprint(color.Blue+"Web Hook! "+color.Cyan+"Made By Parham! "+color.Yellow+"This Project Is Education Purpose Only!",0.1)
sleep(1)

try:
  webhook=open("webhook.txt").read()
  if webhook=="env":
    webhook=os.environ['webhook']
except IOError:
  webhook=""
  while webhook=="": #Check If Web Hook URL Empty
    webhook=input(color.Cyan+"Web Hook URL? ('env' For 'webhook' Replit Secret) ")
    if webhook=="":
      print(color.Red+"Web Hook URL Is Empty. Please When Ask Them, Respone Them")
    elif webhook=="env":
      webhook==os.environ['webhook']
      open("webhook.txt", "w").write("env")
    else:
      open("webhook.txt", "w").write(webhook)

try:
  username=open("username.txt").read()
except IOError:
  username=""
  while username=="": #Check If User Name Empty
    username=input(color.Yellow+"User Name? ")
    open("username.txt", "w").write(username)

message=""
while message=="": #Check If Message Empty
  message=input(color.Green+"Message? ")
  if message=="":
    print(color.Red+"Message Is Empty. Please When Ask Them, Respone Them")

limit=""
while limit=="": #Check If Limit Empty
  limit=input(color.Magenta+"Limit? ('0' To Forever) ")
  if limit=="":
    print(color.Red+"Limit Is Empty. Please When Ask Them, Respone Them")
  else:
    try:
      limit=int(limit)
    except:
      print(color.Red+"Please Enter A Number")
      limit=""

current=0
if limit==0: #For Forever
  while True:
    try:
      DiscordWebhook(url=webhook, username=username, content=message, rate_limit_retry=True).execute()
    except:
      print(color.Red+"Incorrect Web Hook URL! Try Again.")
      break
    current=1+current
    print(color.Red+str(current), "Time!")
    sleep(1)
else: #Limited
  while limit>current:
    try:
      DiscordWebhook(url=webhook, username=username, content=message, rate_limit_retry=True).execute()
    except:
      print(color.Red+"Incorrect Web Hook URL! Try Again.")
      break
    current=1+current
    print(color.Red+str(current), "Time!")
    if limit>=current:
      print(color.Red+"Reached Limit!")
    else:
      sleep(1)