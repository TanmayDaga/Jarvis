import pyjokes
import requests

def getJokeProgrammer():
    return pyjokes.get_joke()

def getJoke():
    """Return tuple with setup and punchline of joke"""
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    return (response.json()["setup"], response.json()["punchline"])
   

