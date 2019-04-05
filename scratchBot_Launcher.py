import sqlite3
import requests
import json
import time
import scratchCommands

global mostRecentVersion
global sql
global cursor

def update():
    cursor.execute("CREATE TABLE if not exists Data(Version TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NUL);")
    cursor.execute("INSERT INTO Data (Version) " + "VALUES ('" + mostRecentVersion + "'))
    print("Downloading most recent version (" + mostRecentVersion + ")")
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

sql = sqlite3.connect('version.db')
cursor = sql.cursor()
mostRecentVersion = getFileContents("https://raw.githubusercontent.com/BonfireScratch/scratchBot/master/version.txt")
if mostRecentVersion != cursor.execute("SELECT Version FROM Data"):
    update()
main()
