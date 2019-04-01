import requests
import json
import time
import sys
import scratchCommands

def update():
    print("Getting most recent version...")
    info = requests.get("https://api.github.com/repos/BonfireScratch/scratchBot/contents/")
    info = json.loads(info.text)
    getFile("https://raw.githubusercontent.com/BonfireScratch/scratchBot/master/scratchCommands.py", "scratchCommands.py")
    print("ScratchBot has been downloaded")

def getFile(URL, FILE):
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
