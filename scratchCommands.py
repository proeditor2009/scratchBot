import requests
import json

def scratchCheck(BOTUSER, USER, PASSWORD):
    if userExists(USER):
        print("user exists")
    else:
        print("couldn't find user with given username")

def userExists(USER):
    response = json.loads(requests.post('https://api.scratchstats.com/scratch/users/' + USER))
    try:
        x = response['id']
    expect:
        return False
    return True
