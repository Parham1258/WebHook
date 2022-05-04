#A Web Hook Tool For Discord! Made By Parham
import os
from time import sleep

class color : #Credits: Doci Team
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'

def slowprint(text: str, speed: float, newLine=True): #Credits: Doci Team
    for i in text:
        print(i, end="", flush=True)
        sleep(speed)
    if newLine:
        print()

def clear_console(): #Credits: Doci Team
    if os.name in ('nt', 'dos'): #Check OS Name
        try:
            os.system("cls")
        except:
            pass
    else:
        try:
            os.system("clear")
        except:
            pass

clear_console()

try: #Try To Find Module
  from discord_webhook import DiscordWebhook
except:
  print(color.Red+"Module 'discord_webhook' Not Found!")
  exit()

slowprint(color.Blue+"Discord WebHook!",0.1)
slowprint(color.Cyan+"Made By Parham!",0.1)
slowprint(color.Red+"Use With Your Own Risk!",0.1)
slowprint(color.Yellow+"This Project Is Education Purpose Only!",0.1)
print()
sleep(1)

try:
  webhook=open("WebHook URL.txt").read()
  if webhook=="env":
    try:
      webhook=os.environ['WebHook']
    except:
      print(color.Red+"Can't Found Replit Secret! Try Again.")
      os.remove("WebHook URL.txt")
      exit()
except IOError:
  webhook=""
  while webhook=="": #Check If WebHook URL Empty
    webhook=input(color.Cyan+"WebHook URL? ('env' For 'WebHook' Replit Secret) ")
    if webhook=="":
      print(color.Red+"WebHook URL Is Empty. Please When Ask Them, Respone Them")
    elif webhook=="env":
      try:
        webhook=os.environ['WebHook']
        open("WebHook URL.txt", "w").write("env")
      except:
        print(color.Red+"Can't Found Replit Secret!")
        webhook=""
    else:
      open("WebHook URL.txt", "w").write(webhook)

try:
  username=open("User Name.txt").read()
except IOError:
  username=input(color.Yellow+"User Name? ")
  open("User Name.txt", "w").write(username)

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

print()

current=0
if limit==0: #For Forever
  while True:
    try:
      DiscordWebhook(url=webhook, username=username, content=message, rate_limit_retry=True).execute()
    except:
      print(color.Red+"Incorrect WebHook URL! Try Again.")
      os.remove("WebHook URL.txt")
      break
    current=1+current
    print(color.Red+str(current), "Time!")
    sleep(1)
else: #Limited
  while limit>current:
    try:
      DiscordWebhook(url=webhook, username=username, content=message, rate_limit_retry=True).execute()
    except:
      print(color.Red+"Incorrect WebHook URL! Try Again.")
      os.remove("WebHook URL.txt")
      break
    current=1+current
    print(color.Red+str(current), "Time!")
    if limit<=current:
      print(color.Red+"Reached Limit!")
    else:
      sleep(1)