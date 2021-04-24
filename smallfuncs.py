import os
from difflib import SequenceMatcher
import webbrowser
from pywhatkit import search, playonyt
import wikipedia
from concurrent.futures import ThreadPoolExecutor


def calculate(expression):
    try:
        return eval(expression)
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

