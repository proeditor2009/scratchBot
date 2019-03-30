import scratchapi
import datetime
import requests
import json
import random
import time
import sys
from bs4 import BeautifulSoup
import scratchCommands
global last

def update():
    print("Getting most recent version...")
    info = requests.get("https://api.github.com/repos/Snipet/scratchBot/contents/")
    info = json.loads(info.text)
    getFile("https://raw.githubusercontent.com/Snipet/scratchBot/master/scratchCommands.py", "scratchCommands.py")
    f = open("scratchCommands.py", "r")
    code = f.read()
    f.close()
    print("\nDownloaded ScratchBot")
    print("File Size: " + str(info[3]["size"]))

def getFile(URL, FILE):
    global lines
    global online
    r = requests.get(URL)
    online = r.text
    code = r.text
    code = code.split("\n")
    lines = []
    for line in code:
        lines.append(line.replace("\r", ""))
    open(FILE, 'w').close()
    f = open(FILE, "a")
    for line in lines:
        f.write(line + "\n")
    f.close()

update()
print("\nStarting... ")


while True:
    scratchCommands.scratchCheck(":BOT ACCOUNT", ":YOUR MAIN ACCOUNT", ":YOUR PASSWORD")
    time.sleep(5)
