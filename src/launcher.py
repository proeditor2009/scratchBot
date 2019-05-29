import requests
import scratchapi
import json
import encryptor
import sys

global mostRecentVersion
global version
global j

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

def askForData():
    isValid = False

    while not isValid:
        user = input("Enter the bot's username > ")
        pas = input("Enter the bot's password > ")
        try:
            scratch = scratchapi.ScratchUserSession(user, pas)
            isValid = True
        except:
            print("Invalid username or password")
    
    j["username"] = user
    j["password"] = str(encryptor.encrypt(pas), 'utf-8')
    
    with open("version.json", "w") as f:
        f.write(json.dumps(j))
    
def main():
    mostRecentVersion = getFileContents("https://raw.githubusercontent.com/Snipet/scratchBot/master/version.txt")[0]

    try:
        with open("version.json", "r") as f:
            data = json.loads(f.read())
            version = data["version"]
            username = data["username"]
            pas = data["password"]
    except:
        version = None
        
    if mostRecentVersion != version:
        j = {}
        if version:
            inp = str(input("A new version of ScratchBot is available. Would you like to download it? > (yes/no) "))
            if inp == "yes":
                print("Downloading most recent version (" + mostRecentVersion + ")")
                getFile("https://raw.githubusercontent.com/Snipet/scratchBot/master/src/scratchCommands.py", "scratchCommands.py")
                
                j = {"version": mostRecentVersion, "username": username, "password": pas}

                with open("version.json", "w") as f:
                    f.write(json.dumps(j))
                
                print("ScratchBot has been updated")
        else:
            j["version"] = mostRecentVersion
            askForData()

main()
