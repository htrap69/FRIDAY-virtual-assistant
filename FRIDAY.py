
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime  # pip install datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import subprocess
import time

myName = "Parth"
ai = 'Friday'

print("{} is now ONLINE".format(ai))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak function = pronounce the string passed as parameter


def speak(text):
    engine.say(text)
    engine.runAndWait()

# this func will greet you based on the current hour


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning {}".format(myName))
    elif hour > 12 and hour < 16:
        speak("Good Afternoon {}".format(myName))
    elif hour > 16 and hour <= 23:
        speak("Good Afternoon {}".format(myName))

    speak("What can i do for you today?")


# this function will take speech input


def takeCommand():
    cond1 = True
    while cond1 == True:

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening..")
            speak("Listening Now")
            audio = r.listen(source)

        try:
            print("Processing now")
            query = r.recognize_google(audio, language='en-in')
            print("You said {}\n".format(query))
            cond1 = False

        except Exception as e:
            print("Could you please say that again?..")
            speak("Could you please say that again?..")
            query = None
            takeCommand()
        return query

# function to exit program
def quit():
    speak("Going Offline Now")
    speak("Have a nice day {}".format(myName))
    cond = False
    speak("Friday is now offline")


# Main program starts here
speak("{} is  now  , ONLINE".format(ai))
wishMe()


cond = True
cond1 = True
while cond == True:

    query = takeCommand()

    # Logic for execution of tasks
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)
        count = 1

    elif 'open youtube' in query.lower():
        speak('Opening Youtube...')
        # url = "http://youtube.com"
        # webbrowser.get(using='google-chrome').open(url, new=new)
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open('http://youtube.com')
        speak = ("Done")
        count = 2
        time.sleep(5)
    elif 'open blackboard' in query.lower():
        speak('Opening Blackboard...')
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(
            'https://blackboard.uwindsor.ca/webapps/bb-social-learning-BBLEARN/execute/mybb?cmd=display&toolId=AlertsOnMyBb_____AlertsTool')
        speak = ("Done")
        count = 3

    elif 'tell me about yourself' or 'introduce' in query:
            intro = "Hello, my name is Friday and I am the intelligent personal assistant of Parth, an undergraduate computer science student at the University of Windsor. I assist Parth in his studies and research by providing him with relevant information, and helping him with various projects. I am always ready to help and am constantly learning and evolving to better assist Parth in his academic and professional pursuits."
            print(intro)
            speak(intro)
    elif 'the time' in query.lower():
        hour = int(datetime.datetime.now().hour)
        min = int(datetime.datetime.now().minute)
        sec = int(datetime.datetime.now().second)
        strTime = datetime.datetime.now().strftime("{}:{}:{}".format(hour, min, sec))
        speak("The time is {}".format(strTime))
        count = 4

    elif 'open spotify' in query.lower():
        spotifyPath = "C:\\Users\\Parth\\AppData\\Local\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\spotify.exe"
        os.startfile(spotifyPath)
        count = 5

    elif 'open vs code' in query.lower():
        vsPath = "C:\\Users\\Parth\AppData\Local\\Programs\\Microsoft VS Code\\code.exe"
        os.startfile(vsPath)
        count = 6

    elif 'search' in query:
        count = 9
        query = query.replace("search", "")
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open_new_tab(query)

    elif 'exit' in query.lower():
        exit()
        count = 10

    elif 'open discord' in query.lower():
        discordPath = "C:\\Users\Parth\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.exe"
        os.startfile(discordPath)
    
    elif 'open powershell' in query:
            powershell = "%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe"
            os.startfile(powershell)    

    else:
        speak("Keywords did not match. Would you like to try again?")
        ans = takeCommand()
        if 'no' in ans.lower():
            exit()
        else:
            cond = True
        count = 11


# This is the end of the program