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
    with open("version.json", "r") as f:
        f = f.read()
        j = json.loads(f)
        return j["version"]
  
def setVersion(v):
    j = {
        "version": v,
    }
    
    with open("version.json", "w") as f:
        f.write(json.dumps(j))
    
def askForData():
    user = input("Enter the bot's username > ")
    pas = input("Enter the bot's password > ")
    
    j = {
        "username": user,
        "password": pas
    }
    
    with open("version.json", "a") as f:
        f.write(json.dumps(j))
    
def getBotData():
    with open("version.json", "r") as f:
        f = f.read()
        j = json.loads(f)
        username = j["username"]
        password = j["password"]
        return (username, password)
    
def main():
    try:
        f = open("version.json")
        f.close()
    except:
        setVersion(0)
        
    myVersion = getVersion()
    if mostRecentVersion != myVersion:
        update()
        askForData()
    
    username, password = getBotData()
    
    while True:
        scratchCommands.scratchCheck(username, password)
        time.sleep(5)

mostRecentVersion = getFileContents("https://raw.githubusercontent.com/BonfireScratch/scratchBot/master/version.txt")
main()
