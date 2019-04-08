from bs4 import BeautifulSoup
import requests
import json
import sys

COMMANDS = ["/follow", "/info"]

def run(USER, PASSWORD, COMMAND):
    command = getCommand(COMMAND)
    if command != None:
        print(command)

def getCommand(COMMAND):
    com = COMMAND.split()
    if com[0] in COMMANDS and len(com) == 2:
        return COMMAND
    return

def runFromProfile(USER):
    username, password = getBotData()

    r = requests.get(getUrlFromUser(USER, "https://scratch.mit.edu/site-api/comments/user/"))
    soup = BeautifulSoup(r.text, "html.parser")
    comms = soup.findAll("div", class_='content')

    for comm in comms:
        text = comm.text
        text = text.replace("\n", "")
        words = text.split()
        for word in words:
            if word in COMMANDS:
                run(username, password, text)

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
    
    while True:
        if not userExists(username):
            print("Could not find user with given username")
            quit()
        run(username, password, str(input("ScratchBot > ")))

def getBotData():
    with open("version.json", "r") as f:
        j = json.loads(f.read())
        return (j["username"], j["password"])

def main():
    if len(sys.argv) == 0:
        runPrompt()
    else:
        runFromProfile(sys.argv[1])
    
main()
