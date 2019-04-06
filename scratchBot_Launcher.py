import requests
import json
import time
import scratchCommands

global mostRecentVersion
global myVersion

def update():
    print("Downloading most recent version (" + mostRecentVersion + ")")
    getFile("https://raw.githubusercontent.com/BonfireScratch/scratchBot/master/scratchCommands.py", "scratchCommands.py")
    setVersion(mostRecentVersion)
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
  
def setVersion(v):
    j = {
        "version": v,
    }
    
    f = open("version.json", "w")
    f.write(json.dumps(j))
    f.close()
    
def askForData:
    user = input("Enter the bot's username > ")
    pas = input("Enter the bot's password > ")
    
    j = {
        "username": user,
        "password": pas
    }
    
    f = open("version.json", "a")
    f.write(json.dumps(j))
    f.close()
    
def getBotData():
    pass
    
def main():
    try:
        f = open("version.json")
        f.close()
    except:
        setVersion(0)
        
    mostRecentVersion = getFileContents("https://raw.githubusercontent.com/BonfireScratch/scratchBot/master/version.txt")
    myVersion = getVersion()
    if mostRecentVersion != myVerion:
        update()
        askForData()
        
    getBotData()
    
    while True:
        scratchCommands.scratchCheck("BOT", "REG ACCOUNT", "PASSWORD")
        time.sleep(5)

main()
