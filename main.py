# import the required packages...........

import speech_recognition as sr
import smtplib
from dotenv import load_dotenv
import os
import json
import wikipedia
import webbrowser
from wikipedia.wikipedia import search
import pyjokes
from gtts import gTTS
from playsound import playsound
import datetime

#Loading all the variables from .env file................
load_dotenv()
password = os.getenv("PASS")
defaultEmail = os.getenv("DEFAULT_EMAIL")
Email = os.getenv("EMAIL")
now = datetime.datetime.now()
assistant = ""
#Loading the json file..............
with open("data.json", "r") as File:
    data = json.load(File)
#Function which speaks with the master(Simply a tts engine)..............
def speak(text):
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save("audio.mp3")
    playsound('audio.mp3')
#Function which greets the master..........
def greet():
    if (now.hour == 12) and (now.hour <= 4):
        speak("Good Afternoon!")
    elif ((now.hour == 0) or (now.hour == 00) and (now.hour < 12)):
        speak("Good morning!")
    elif (now.hour >= 16) and (now.hour <= 19):
        speak("Good evening!")
    elif (now.hour >= 19) and (now.hour <= 23):
        speak("Good night!")
    speak("I'm your personal voice assistant, how may I help you sir?")

#Building a voice-to-text engine's function........
def takeCommand():
    microphone = sr.Recognizer()
    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
        print("Listening...")
        #microphone.pause_threshold = 1
        audio = microphone.listen(source)
    try:
        print("Recognizing...")   
        query = microphone.recognize_google(audio) 
        print("Master:", query)   

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.") 
        return "None"

    return query


greet()
#Starting the program's loop.........
while True:
    order = takeCommand().lower()

    if "open youtube" == order:
        speak("Opening Youtube.")
        webbrowser.open("https://www.google.com/")

    elif "open google" == order:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com/")

    elif "wikipedia" in order:
        query = order.replace("search in wikipedia for", "")
        results = wikipedia.summary(query, sentences = 3)
        speak("According to Wikipedia...")
        print(results)
        speak(results)

    elif "search in youtube for" in order:
        query = order.replace("search in youtube for", "")
        speak("Opening Youtube.")
        webbrowser.open('https://www.youtube.com/results?search_query=%s' % query)

    elif "search in google for" in order:
        query = order.replace('search in google for', "")
        speak("Opening Google.")
        webbrowser.open("https://www.google.com/search?q=%s" % query)

    elif 'how are you' in order:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

    elif 'fine' in order or "good" in order:
        speak("It's good to know that your fine sir.")

    elif "change your name to" in order:
        query = order.replace("change your name to", "")
        with open("data.json", "r") as File:
            data = json.load(File)
            data["name"] = query

        with open("data.json", "w") as File:
            json.dump(data, File)
        speak("Thanks for naming me sir.")

    elif 'your name' in order:
        with open("data.json", "r") as File:
            data = json.load(File)
            assistant = data["name"]
        speak(assistant)

    elif "exit" in order or "terminate" in order or "bye" in order or "shut up" in order:
        speak('Bye, sir. Have a good day!')
        break

    elif 'joke' in order:
            speak(pyjokes.get_joke())

    elif "who are you" in order:
        speak("I'm a Simple and Intelligent Voice Assistant.")

    elif "last command" in order or "last order" in order:
        playsound('audio.mp3')

    elif "i love you" in order or "will you be my wife" in order or "will you be my girl friend" in order or "will you be my soulmate" in order:
        speak("I'm virtual, you can't feel my vagina.")

    elif "my birthday" in order or "was born" in order :
        speak("Do you think you're that famous, how the hell I know your birthday!")

    elif "do you know me" in order:
         speak("Do you think you're that famous, how the hell I know you")
         
    elif "who i am" in order:
        speak("If you can operate me, surely you're a human!")

    elif 'where is' in order:
        query = order.replace("where is", "")
        speak(query)
        webbrowser.open('https://www.google.com/maps/place/%s/' % query)

    elif 'where iam' in order or "my location" in order:
        speak("Opening Map.")
        webbrowser.open("https://www.google.com/maps/")

    elif "who invented you" in order or "made you" in order:
        speak("I was made by my master Uday Kiran. And I was initialized on Sunday May 16th at 12:00 AM")    

    elif "when you were made" in order or "when you are made" in order:
        speak("I was initialized on Sunday May 16th at 12:00 AM")



