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
    print("ScratchBot has been downloaded")
    print("File Size: " + str(info[4]["size"]))

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

def main():
    while True:
        scratchCommands.scratchCheck("BOT", "REG ACCOUNT", "PASSWORD")
        time.sleep(5)
    
update()
main()
