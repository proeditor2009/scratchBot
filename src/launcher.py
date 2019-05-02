import requests
import scratchapi
import json

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
        j = json.loads(f.read())
        return j["version"]
  
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
            isValid = 0
    
    j = {
        "version": mostRecentVersion,
        "username": user,
        "password": pas
    }
    
    with open("version.json", "w") as f:
        f.write(json.dumps(j))
    
def main():
    try:
        myVersion = getVersion()
    except:
        myVersion = 0
        
    if mostRecentVersion != myVersion:
        update()
        askForData()
        print("Downloading process executed")

mostRecentVersion = getFileContents("https://raw.githubusercontent.com/Snipet/scratchBot/master/version.txt")[0]
main()
