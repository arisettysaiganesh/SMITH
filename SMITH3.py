import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import time as tm
import tkinter as tk
from tkinter import Label, Button, Entry, StringVar

# Initialize the speech engine
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak("The current time is")
    speak(Time)
    result.set(f"The current time is {Time}")

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)
    result.set(f"The current date is {day}/{month}/{year}")

def wishme():
    hour = datetime.datetime.now().hour
    greeting = ""
    if hour >= 4 and hour < 12:
        greeting = "Good Morning Sir!!"
    elif hour >= 12 and hour < 16:
        greeting = "Good Afternoon Sir!!"
    elif hour >= 16 and hour < 24:
        greeting = "Good Evening Sir!!"
    else:
        greeting = "Good Night Sir, See You Tomorrow"

    speak(greeting)
    speak("SMITH at your service sir, please tell me how may I help you.")
    result.set(f"{greeting}\nSMITH at your service sir, please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    img_dir = os.path.expanduser("~\\Pictures")
    img_path = os.path.join(img_dir, "ss.png")

    # Ensure the directory exists
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    img.save(img_path)
    speak("Screenshot taken, please check your Pictures folder.")
    result.set("Screenshot taken, please check your Pictures folder.")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
    except Exception as e:
        speak("Please say that again")
        return "Try Again"
    return query

def weather():
    speak("Fetching weather information...")
    url = "https://www.weather.com/weather/today"
    wb.open(url)

def news():
    speak("Fetching latest news headlines...")
    url = "https://news.google.com/topstories"
    wb.open(url)

def set_alarm(time):
    alarm_time = datetime.datetime.strptime(time, "%I:%M %p")
    current_time = datetime.datetime.now()
    time_diff = (alarm_time - current_time).total_seconds()
    if time_diff < 0:
        time_diff += 86400  # add a day in seconds
    speak(f"Setting an alarm for {time}")
    tm.sleep(time_diff)
    speak("Time to wake up!")

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts."
    ]
    joke = random.choice(jokes)
    speak(joke)
    result.set(joke)

def open_application(app_name):
    if "notepad" in app_name:
        os.system("notepad.exe")
    elif "calculator" in app_name:
        os.system("calc.exe")
    else:
        speak("Application not available.")
        result.set("Application not available.")

def execute_command():
    query = takecommand().lower()
    
    if "time" in query:
        time()

    elif "date" in query:
        date()

    elif "who are you" in query:
        speak("I'm SMITH created by Mr. Sai Ganesh and I'm a desktop voice assistant.")
        result.set("I'm SMITH created by Mr. Sai Ganesh and I'm a desktop voice assistant.")

    elif "how are you" in query:
        speak("I'm fine sir, What about you?")
        result.set("I'm fine sir, What about you?")

    elif "fine" in query or "good" in query:
        speak("Glad to hear that sir!!")
        result.set("Glad to hear that sir!!")

    elif "wikipedia" in query:
        try:
            speak("Ok wait sir, I'm searching...")
            query = query.replace("wikipedia","")
            result_text = wikipedia.summary(query, sentences=2)
            result.set(result_text)
            speak(result_text)
        except:
            speak("Can't find this page sir, please ask something else")

    elif "open youtube" in query:
        wb.open("youtube.com") 

    elif "open google" in query:
        wb.open("google.com") 

    elif "open stack overflow" in query:
        wb.open("stackoverflow.com")

    elif "play music" in query:
        song_dir = os.path.expanduser("~\\Music")
        songs = os.listdir(song_dir)
        x = len(songs)
        y = random.randint(0, x-1)
        os.startfile(os.path.join(song_dir, songs[y]))

    elif "open chrome" in query:
        chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chromePath)

    elif "search on chrome" in query:
        try:
            speak("What should I search?")
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            search = takecommand()
            wb.get(chromePath).open_new_tab(search)
            result.set(f"Searched: {search}")
        except Exception as e:
            speak("Can't open now, please try again later.")
            result.set("Can't open now, please try again later.")
        
    elif "remember that" in query:
        speak("What should I remember?")
        data = takecommand()
        speak("You said me to remember that " + data)
        with open("data.txt", "w") as remember:
            remember.write(data)

    elif "do you remember anything" in query:
        try:
            with open("data.txt", "r") as remember:
                data = remember.read()
                speak("You told me to remember that " + data)
                result.set("You told me to remember that " + data)
        except FileNotFoundError:
            speak("You haven't told me to remember anything.")
            result.set("You haven't told me to remember anything.")

    elif "screenshot" in query:
        screenshot()

    elif "weather" in query:
        weather()

    elif "news" in query:
        news()

    elif "set alarm" in query:
        speak("What time should I set the alarm for?")
        alarm_time = takecommand()
        set_alarm(alarm_time)

    elif "tell me a joke" in query:
        tell_joke()

    elif "open notepad" in query or "open calculator" in query:
        open_application(query)

    elif "shutdown" in query:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")

    elif "restart" in query:
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")

    elif "offline" in query:
        speak("Goodbye sir, have a nice day!")
        quit()

# Create GUI
root = tk.Tk()
root.title("SMITH - Desktop Voice Assistant")

result = StringVar()
result.set("Welcome! Click 'Execute Command' to start listening.")

lbl = Label(root, textvariable=result, wraplength=400)
lbl.pack(pady=10)

execute_btn = Button(root, text="Execute Command", command=execute_command)
execute_btn.pack(pady=10)

wishme()

root.mainloop()
