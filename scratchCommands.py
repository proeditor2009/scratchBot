import requests
import json

def scratchCheck(USER, PASSWORD):
    if userExists(USER):
        print("user exists")
    else:
        print("couldn't find user with given username")

def userExists(USER):
    r = requests.get('https://api.scratchstats.com/scratch/users/' + USER)
    response = json.loads(r.text)
    try:
        x = response['id']
    except:
        return False
    return True

