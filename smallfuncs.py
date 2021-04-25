import os
from difflib import SequenceMatcher
import webbrowser
from pywhatkit import search, playonyt
import wikipedia
from concurrent.futures import ThreadPoolExecutor
import json

jsonFileObjectForWrite = None
dictObj = None
myDetails = []  # Name, Birthday etc in form of dict
persons = []  # Name of persons name to be saved
personsData = []  # personsData in same order in form of list as in persons
music = []  # path of music files in computer


def calculate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError as z:
        return "ZeroDivisionerror"
    except Exception as e:
        return None


def openApplication(appName, listOfApps):
    """The list of apps contains path to different apps"""
    for items in listOfApps:

        # Matching given name
        if SequenceMatcher(None, appName, os.path.basename(items)).ratio() > 0.5:
            os.system(f"open {items}")
            return


def searchGoogle(query):
    """Search the google for query,open result in new tab"""
    search(query)


def firstOnYoutube(query):
    """Plays the first video on youtube, open result in new tab"""
    playonyt(query)


def searchYoutube(query):
    """Search the youtube for query , open result in new tab"""
    webbrowser.open_new_tab(
        f"https://www.youtube.com/results?search_query={query}")


def searchWikipediaOpenWindow(query):
    """Search the wikipedia in new browser window"""
    webbrowser.open_new_tab(f"https://en.wikipedia.org/wiki/{query}")


def searchWikipedia(query, noOfLines=10):
    """search wikipedia for query and return by default 10 lines can change it"""
    return wikipedia.summary(query, sentences=noOfLines)


def propSearchWiki(query) -> list:
    """return possible options for query in  list, Could be ran before other wiki options for a
    accurate results"""
    return wikipedia.search(query)


def createNewThread(target, *args):
    """Creates a new thread and returns it. Can get it result from thread.result()"""
    thread = ThreadPoolExecutor().submit(target, *args)
    return thread



#######################--------Json file methods-----------#######################
def loadDataJson():
    """
        loads data in form of list and dictinoary from file into memory and creates a write file io object 
        Data.json structure
        my: --> list of owners details[Name, birthday, extrainfo can be added]
        persons:  --> list of names of people whose data to be saved
        personsData --> Contains details in list [birthday, anniversary, extraInfo] in same order as persons list
        music --> Contains list of path of music in computer
    """

    global music, myDetails, persons, personsData, jsonFileObjectForWrite
    jsonFileObjectForRead = open("data.json", 'r')
    dictObj = json.load(jsonFileObjectForRead)
    myDetails = dictObj['my']
    persons = dictObj['persons']
    personsData = dictObj['personsData']
    music = dictObj['music']
    jsonFileObjectForRead.close()
    jsonFileObjectForWrite = open("data.json", 'w')


def getPersonsData(index):
    """Index of person in persons list
        Return list of data of person with program
    """
    try:
        return personsData[index]
    except IndexError as e:
        return None


def addPerson(personName):
    """
    Adds a person to json file and updates list
    True: name added succesfully
    False: name already exists
    """

    # checking if it is already in list
    if personName.lower() not in dictObj['persons']:

        # updating in memory
        persons.append(personName.lower())
        personsData.append([None, None, None])

        # Data to be dumped in file
        dictObj['persons'].append(personName.lower())
        # Creating empty list of data
        dictObj['personsData'].append([None, None, None])
        json.dump(dictObj, jsonFileObjectForWrite)


def addPersonBirthday(personName, birthday):
    """
    Adds birthday to list
    if person not exists then adds it
    """

    addPerson(personName)  # automatically checks if not exists then adds it
    personsIndex = dictObj['persons'].index(personName.lower())
    personsData[personsIndex][0] = birthday
    dictObj['personsData'][personsIndex][0] = birthday
    json.dump(dictObj, jsonFileObjectForWrite)


def addPersonAnniversary(personName, anniversary):
    """
    Adds anniversary to list
    if person not exists then adds it
    """
    addPerson(personName)  # automatically checks if not exists then adds it
    personsIndex = dictObj['persons'].index(personName.lower())
    personsData[personsIndex][1] = anniversary
    dictObj['personsData'][personsIndex][1] = anniversary
    json.dump(dictObj, jsonFileObjectForWrite)

def addExtraInfo(personName, extraInfo):
    """
    Adds extra info to list
    if person not exists then adds it
    Note: ExtraInfo should be in dictionary form
    """
    addPerson(personName)  # automatically checks if not exists then adds it
    personsIndex = dictObj['persons'].index(personName.lower())
    personsData[personsIndex].append(extraInfo)
    dictObj['personsData'][personsIndex].append(extraInfo)
    json.dump(dictObj, jsonFileObjectForWrite)
