import sqlite3
import requests
import json
import time
import scratchCommands

global mostRecentVersion
global sql
global cursor

def update():
    cursor.execute('''CREATE TABLE if not exists Data(Version text, Username text, Password text)''')
    cursor.execute("UPDATE Data SET Version='" + mostRecentVersion + "'")
    print("Downloading most recent version (" + mostRecentVersion + ")")
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

conn = sqlite3.connect('version.db')
cursor = conn.cursor()
mostRecentVersion = getFileContents("https://raw.githubusercontent.com/BonfireScratch/scratchBot/master/version.txt")
if mostRecentVersion != cursor.execute("SELECT Version FROM Data"):
    update()
main()
