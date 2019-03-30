import scratchapi
import datetime
import requests
import json
import random
import time
from bs4 import BeautifulSoup
global last

askerPre = ''
commandPre = ''
followLast = ''
followSecond = ''
swap = 0
def scratchCheck(USER, PASSWORD):
    global askerPre
    global commandPre
    global followLast
    global followSecond
    global swap
    parse = []
    r = requests.get("https://scratch.mit.edu/site-api/comments/user/" + USER)
    soup = BeautifulSoup(r.text, "html.parser")
    command = soup.findAll("div", {'class':'content'})[0]
    asker = soup.findAll("a")[1]
    f = open("UserData.txt", "r")
    users = f.read()
    users = str(users)
    f.close()
    users = users.replace("\n", " ")
    users = users.split(" ")
    if asker.text not in users:

        u = requests.get("https://scratch.mit.edu/users/" + asker.text + "/followers")
        page = BeautifulSoup(u.text, "html.parser")
        count = page.findAll("h2")[0]
        count = count.text
        count = count.replace("\n", "")
        num = count.split(" ")[10]
        num = num.split("(")[1]
        num = num.split(")")[0]
        num = int(num)
        print(asker.text)
        print(num)
        f = open("UserData.txt", "a")
        f.write(asker.text + " " + str(num) + "\n")
        f.close()
    
    
    command = command.text
    command = command.replace("\n", "")
    rawparse = command.split(" ")
    for item in rawparse:
        if item != "":
            parse.append(item)
    if parse[0] == "/follow" and len(parse) == 2:
        f = open("followers.txt", "r")
        following = f.read()
        f.close()
        username = parse[1]
        username = username.replace("@", "")
        t = requests.get("https://scratch.mit.edu/users/" + username)
        if username not in following and t.status_code != 404:
            try:
                scratch = scratchapi.ScratchUserSession(USER, PASSWORD)
                scratch.users.follow(username)
            except:
                pass
            f = open("followers.txt", "a")
            f.write(username)
            f.close()
            print(command)
            scratch.users.comment(asker.text, "[ScratchBot]:Followed " + username + ". =)")

        else:
            if t.status_code == 404:
                #print("ERROR: User doesn't exist!")
                pass
    
    if parse[0] == "/info" and len(parse) == 2:
        if asker.text != askerPre or commandPre != command:
            ID = parse[1]
            p = requests.get("https://api.scratch.mit.edu/projects/" + ID)
            if p.status_code != 404:
                y = json.loads(p.text)
                views = y["stats"]["views"]
                loves = y["stats"]["loves"]
                favorites = y["stats"]["favorites"]
                comments = y["stats"]["comments"]
                remixes = y["stats"]["remixes"]
                title = y["title"]
                creator = y["author"]["username"]
                try:
                    scratch = scratchapi.ScratchUserSession(USER, PASSWORD)
                    scratch.users.comment(asker.text, "[ScratchBot]: Info for \"" + title + "\" by " + creator + ": Views: " + str(views) + "--- Loves: " + str(loves) + " --- Favorites: " + str(favorites))
                    scratch.users.follow(asker.text)
                    scratch.users.follow(y["author"]["username"])
                except:
                    pass
                print(ID)
                f = open("projectsData.txt", "a")
                f.write(ID + "\n")
                f.close()
                askerPre = asker.text
                commandPre = command
                
                
    r = requests.get("https://api.scratch.mit.edu/proxy/featured")
    y = json.loads(r.text)
    if y["community_most_loved_projects"][0]["creator"] != followLast:
        try:
            scratch = scratchapi.ScratchUserSession(USER, PASSWORD)
            scratch.users.follow(y["community_most_loved_projects"][0]["creator"])
        except:
            pass
        
        followLast = y["community_most_loved_projects"][0]["creator"]
        followSecond = followLast
        print("-Followed " + y["community_most_loved_projects"][0]["creator"])
    else:
        if random.randint(0, 5) != 3 and swap == 0:
            p = requests.get("https://api.scratch.mit.edu/users/" + followSecond + "/following")
            d = json.loads(p.text)
            try:
                user = d[random.randint(0, 1)]["username"]
                if user != followSecond:
                    scratch = scratchapi.ScratchUserSession(USER, PASSWORD)
                    scratch.users.follow(user)
                    print("Followed " + user)
                    followSecond = user
                    f = open("followers.txt", "a")
                    f.write(user + "\n")
                    f.close()
                else:
                    swap = 1
            except:
                pass        
        
        else:
            swap = 0
            print("Spapped follow paths")
            f = open("followers.txt", "r")
            s = f.read()
            f.close()
            s = s.replace("\n", " ")
            following = s.split(" ")
            del following[-1]
            followSecond = following[random.randint(0, len(following)-1)]
        


