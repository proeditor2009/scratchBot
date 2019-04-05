import sqlite3
import requests
import json
import time
import scratchCommands

def update():
    mostRecentVersion = getFileContents("https://raw.githubusercontent.com/BonfireScratch/scratchBot/master/version.txt")
    print("Downloading most recent version (" + version + ")")
    info = json.loads(requests.get("https://api.github.com/repos/BonfireScratch/scratchBot/contents/"))
    getFile("https://raw.githubusercontent.com/BonfireScratch/scratchBot/master/scratchCommands.py", "scratchCommands.py")
    print("ScratchBot has been downloaded")

def getFile(URL, FILE):
    lines = getFileContents(URL)
    open(FILE, 'w').close()
    f = open(FILE, "a")
    for line in lines:
        f.write(line + "\n")
    f.close()

def getFileContents(URL):
    r = requests.get(URL)
    online = r.text
    code = r.text
    code = code.split("\n")
    lines = []
    for line in code:
        lines.append(line.replace("\r", ""))
    return lines
    
def main():
    while True:
        scratchCommands.scratchCheck("BOT", "REG ACCOUNT", "PASSWORD")
        time.sleep(5)
    
update()
main()
