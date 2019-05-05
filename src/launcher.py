import requests
import scratchapi
import json
import sys

global mostRecentVersion
global version

def update(VERSION):
    print("Downloading most recent version (" + VERSION + ")")
    getFile("https://raw.githubusercontent.com/Snipet/scratchBot/master/src/scratchCommands.py", "scratchCommands.py")
    setVersion(mostRecentVersion)

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
  
def setVersion(v):
    j = {
        "version": v
    }
    
    with open("version.json", "w") as f:
        f.write(json.dumps(j))
    
def askForData():
    isValid = 0
    while isValid != 1:
        user = input("Enter the bot's username > ")
        pas = input("Enter the bot's password > ")
        try:
            scratch = scratchapi.ScratchUserSession(user, pas)
            isValid = 1
        except:
            print("Invalid username or password")
    
    j = {
        "version": mostRecentVersion,
        "username": user,
        "password": pas
    }
    
    with open("version.json", "w") as f:
        f.write(json.dumps(j))
    
def main():
    try:
        with open("version.json", "r") as f:
            data = json.loads(f.read())
            version = data["version"]
    except:
        version = None
        
    if mostRecentVersion != version:
        if version:
            inp = str(input("A new version of ScratchBot is available. Would you like to download it? > (yes/no) "))
            if inp == "yes":
                update(mostRecentVersion)
                print("ScratchBot has been updated")
        else:
            update(mostRecentVersion)
            askForData()
            print("ScratchBot has been downloaded")

mostRecentVersion = getFileContents("https://raw.githubusercontent.com/Snipet/scratchBot/master/version.txt")[0]
main()
