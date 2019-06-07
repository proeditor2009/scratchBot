from bs4 import BeautifulSoup
import scratchapi
import launcher
import requests
import encryptor
import json
import sys

COMMANDS = ["/follow", "/info"]
ASKERUSER = ""
mode = ""

def run(USER, PASSWORD, COMMAND):
    com = COMMAND.split()
    command = getCommand(com)
    if command == None:
        return
    if com[0] == "/follow":
        fol(com[1], USER, PASSWORD)
    elif com[0] == "/info":
        info(com[1], USER, PASSWORD)

def fol(USER, BOTUSER, PASSWORD):
    if userExists(USER):
        with open("following.txt", "a") as f:
            fol = f.read()
            if not USER in fol:
                scratch = scratchapi.ScratchUserSession(BOTUSER, PASSWORD)
                scratch.users.follow(USER)
                print("ScratchBot followed " + USER)
                f.write(USER)
                if mode == "prompt":
                    scratch.users.comment(BOTUSER, "ScratchBot followed " + USER)
                else:
                    scratch.users.comment(ASKERUSER, "ScratchBot followed " + USER)
            else:
                print("Have already followed user")
    else:
        print("Could not find user with given username")

def info(PROJECT, BOTUSER, PASSWORD):
    try:
        p = requests.get("https://api.scratch.mit.edu/projects/" + PROJECT)
        p = json.loads(p.text)
        views = p["stats"]["views"]
        loves = p["stats"]["loves"]
        favorites = p["stats"]["favorites"]
        comments = p["stats"]["comments"]
        remixes = p["stats"]["remixes"]
        title = p["title"]
        creator = p["author"]["username"]
        info = "Info for \"" + title + "\" by " + creator + ":\nViews: " + str(views) + "\nLoves: " + str(loves) + "\nFavorites: " + str(favorites) + "\nComments: " + str(comments) + "\nRemixes: " + str(remixes)
        print(info)
        try:
            if mode == "prompt":
                scratch.users.comment(BOTUSER, info)
            else:
                scratch.users.comment(ASKERUSER, info)
        except:
            print("Could not comment on user profile")
    except:
        print("Project not found") 

def getCommand(COMMAND):
    if COMMAND[0] in COMMANDS and len(COMMAND) == 2:
        return COMMAND
    return

def runFromProfile(USER):
    username, password = getBotData()

    r = requests.get(getUrlFromUser(USER, "https://scratch.mit.edu/site-api/comments/user/"))
    soup = BeautifulSoup(r.text, "html.parser")
    comms = soup.findAll("div", class_='content')
    i = 0

    for comm in comms:
        text = comm.text
        text = text.replace("\n", "")
        words = text.split()
        asker = soup.findAll("a")[i]
        ASKERUSER = asker.text
        for word in words:
            if word in COMMANDS:
                run(username, password, text)
        i += 1

def getUrlFromUser(USER, URL):
    username = USER
    if username[0] == "@":
        username = username[1:len(username) - 1]
    if not userExists(username):
        print("Could not find user with given username")
        quit()
    return URL + username

def userExists(USER):
    r = requests.get('https://api.scratchstats.com/scratch/users/' + USER)
    response = json.loads(r.text)
    try:
        response = response['id']
    except:
        return False
    return True

def runPrompt():
    username, password = getBotData()
    
    if not userExists(username):
        print("Could not find user with given username")
        quit()

    while True:
        run(username, password, str(input("ScratchBot > ")))

def getBotData():
    with open("version.json", "r") as f:
        j = json.loads(f.read())
        username = j["username"]
        pas = str(encryptor.decrypt(str.encode(j["password"])), 'utf-8')
        return username, pas

def main():
    launcher.main()
    if len(sys.argv) == 1:
        mode = "prompt"
        runPrompt()
    else:
        mode = "profile"
        runFromProfile(sys.argv[1])
    
main()
