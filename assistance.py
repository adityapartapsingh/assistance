import subprocess
import playsound
import pyttsx3
import SpeechRecognition as sr
import datetime
import calendar
import wikipedia
import webbrowser
import os
import pywhatkit
import ctypes
import winshell
import pyjokes
import time
import sys
import random

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
print("i am alexa")
engine.say('i am alexa')
print('what can i do for you')
engine.say('what can i do for you')
engine.runAndWait()


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
    try:
        # print("Recognizing...")
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')

    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return command


if __name__ == '__main__':
    while True:
        command = take_command()
        if 'hello' in command:
            speak("Hello Dear")

        elif "what's up" in command or "how are you" in command:
            msg = ['Just doing my things!', 'I am perfectly fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(msg))
            speak("and you?")

        elif 'fine' in command or 'good' in command or 'perfect' in command:
            speak("It's good to know that you are fine.")

        elif 'who are you' in command or 'define yourself' in command or 'tell me about yourself' in command:
            me = (
                "Hello, i am your friend. I am here to make your life easier. you can ask me to perform various "
                "tasks such as solving mathematical questions or opening applications etc..")
            speak(me)

        elif 'who am i' in command:
            speak('Aditya Partap Singh')

        elif 'why do you exist' in command:
            speak('it is secret')

        elif 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M:%p')
            speak('Current time is ' + time)

        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 3)
            speak(info)

        elif 'open youtube' in command:
            speak("Opening...")
            webbrowser.open("www.youtube.com")

        elif 'open google' in command:
            speak("Opening...")
            webbrowser.open("www.google.com")

        elif 'open stack overflow' in command:
            speak("Opening...")
            webbrowser.open("www.stackoverflow.com")

        elif 'open gmail' in command:
            speak("Opening...")
            webbrowser.open("www.gmail.com")

        elif 'weather' in command:
            webbrowser.open(
                "https://www.msn.com//en-us//weather//today//weather-today//we-city?el=yJTV9sMueHI%2FJDSKwuUII9E6BR0Advwn3ralyft%2B1uc7yYGyfhNZjg%2BxkBvUfJOw%2BrfN7TYiAW5sHNBITk3zt4NIFyK7sXOeO6HdtYP5zZ%2FMkL6j7vDWxaTK5Z08rrdE&weadegreetype=C&ocid=winp1taskbar&pfr=1")

        elif 'day' in command:
            now = datetime.datetime.now()
            date_now = datetime.datetime.today()
            week_now = calender.day_name[date_now.weekday()]
            month_now = now.month
            day_now = now.day
            month = ["January", "February", "March", "April", "May", "june", "July", "August", "September",
                     "October",
                     "November", "December"]
            ordinals = ["1st", '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                        '13th',
                        '14th', '15th', '16th', '17th', '18th', '19th', '20th', "21st", "22nd", "23rd", "24th",
                        "25th",
                        "26th", "27th", "28th", "29th", "30th", "31st"]
            speak(f'Today is {week_now},{month[month_now - 1]} the {ordinals[day - 2]} .')

        elif 'who am i' in command:
            speak('Aditya Partap Singh')

        elif 'why do you exist' in command:
            speak('it is secret')

        elif 'where is' in command:
            ind = command.split().index("is")
            location = command.split()[ind + 1:]
            url = "https://www.google.com/maps/place/" + "".join(location)
            speak("This is where" + str(location) + "is.")
            webbrowser.open(url)

        elif 'joke' in command:
            speak(pyjokes.get_joke())

        elif "don't listen" or "stop listening" or "do not listen" in command:
            speak('for how many seconds do you want me to sleep')
            take_command()
            time.sleep(command)
            speak(str(command) + 'seconds completed. Now you can ask me anything')

        elif 'exit' or 'quit' in command:
            exit()


        elif 'nothing' or 'abort' or 'stop' or 'Bye' in command:
            speak("Ok Dear")
            speak('Bye Dear, have a good day')
            sys.exit()

        else:
            print('Please say the command again.')
            speak('Please say the command again.')
