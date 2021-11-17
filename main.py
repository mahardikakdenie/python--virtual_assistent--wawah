from urllib.parse import quote
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from urllib.request import urlopen
import json

from wikipedia.wikipedia import search
# from googlesearch import search

print("initializing Wawah VA")


MASTER = "mahardika"
engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
print(voices)
engine.setProperty("voice", voices[0].id)
engine.setProperty('languages', 'id-ID')
engine.setProperty('gender', 'famale')

# speaks


def speak(text):
    engine.say(text)
    engine.runAndWait()

# function


def wishMe():
    hours = int(datetime.datetime.now().hour)
    if hours >= 12 and hours < 12:
        speak("good morning " + MASTER)
    elif hours >= 12 and hours < 18:
        speak("Good AfterNoon " + MASTER)
    else:
        speak("Good Evenning" + MASTER)
        speak("")

# Microphone


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning ...")
        audio = r.listen(source)

    try:
        print("recognizing .. ")
        query = r.recognize_google(audio, language="id-ID")
        print(f"user said : {query}\n")

    except Exception as e:
        print("say that again please : ")
        query = None

    return query


# main program
i = True

speak("Helo my name is Wawah, i can help you !")
speak("sorry i cant speak indonesia but i understand what you are saying".format(MASTER))
speak("saya ini wawah")
wishMe()
while i == True:
    query = takeCommand()
    # print(query)
    #

    if 'wikipedia' in query.lower():
        speak("search wikipedia ...")
        query = query.replace("wikipedia", '')
        result = wikipedia.summary(query, sentences=2)
        print(result)
        i = False
        speak(result)
    elif "buka youtube" in query.lower():
        url = 'youtube.com'
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
        i = False
        speak("Youtube Open")
    elif "buka ensiklo tari" in query.lower():
        url = 'ensiklotari.com'
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
        i = False
        speak("ensiklotari open")
    elif "buka wa" in query.lower():
        url = 'web.whatsapp.com'
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
        speak("wa open")
        i = False
    elif "buka google" in query.lower():
        i = False
        url = 'google.com'
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
        speak("Google Open")
    elif "buka tutorial" in query.lower():
        i = False
        url = 'https://www.youtube.com/watch?v=NTuvvEueuz4&t=2361s'
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
        speak("Google Open")
    elif "wawah" in query.lower():
        i = False
        speak("yes i can help you")
        query_2 = takeCommand()
        if 'siapa' in query_2.lower():
            print("Searching Google...")
            speak('Searching Google...')
            query = query_2.replace("google", "")
            print(query)
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.open("https://google.com/search?q=%s" %
                            query_2.lower())
            print("This is what I found according to your search")
            speak("This is what I found according to your search")
        elif 'apa' in query_2.lower():
            print("Searching Google...")
            speak('Searching Google...')
            query = query_2.replace("google", "")
            print(query)
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.open("https://google.com/search?q=%s" %
                            query_2.lower())
            print("This is what I found according to your search")
            speak("This is what I found according to your search")
        elif 'bagaimana' in query_2.lower():
            print("Searching Google...")
            speak('Searching Google...')
            query = query_2.replace("google", "")
            print(query)
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.open("https://google.com/search?q=%s" %
                            query_2.lower())
            print("This is what I found according to your search")
            speak("This is what I found according to your search")
        elif "carikan" in query_2.lower():
            url = 'google.com/search?q=' + query_2
            chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.open("https://google.com/search?q=%s" %
                            query_2.lower())
            speak(query_2.lower())
    elif "lagu" in query.lower():
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.open("https://www.youtube.com/results?search_query=%s" %
                        query.lower())
        speak("Youtube is Open to search your request")
    elif "dimana" in query.lower():
        query = query.replace("dimana", "")
        location = query.lower()
        speak("User asked to Locate")
        speak(location)
        webbrowser.open(
            "https://www.google.nl/maps/place/" + location + "")
    else:
        speak("i cant hear you, can you repeat please ?")
        i = True
