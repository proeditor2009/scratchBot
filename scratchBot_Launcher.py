import requests
import json
import time
import scratchCommands

global mostRecentVersion
global myVersion

def update():
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

def getVersion():
    f = open("version.json", "r")
    f = json.loads(f.read())
    return f["version"]
    
def main():
    while True:
        scratchCommands.scratchCheck("BOT", "REG ACCOUNT", "PASSWORD")
        time.sleep(5)

f = open("version.json", "w")
f.write("...")
f.close()
mostRecentVersion = getFileContents("https://raw.githubusercontent.com/BonfireScratch/scratchBot/master/version.txt")
myVersion = getVersion()
if mostRecentVersion != myVerion:
    update()
main()
