import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from time import sleep
import os
import random
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour < 20:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("Hello, I am Alex. Please tell me how may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Say something!")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        return "None"
    return query

def chooseBrowser():
    speak("Which browser would you like to use? You can choose Chrome or   Edge.")
    browser_choice = takeCommand().lower()
    if 'chrome' in browser_choice or 'open chrome' in browser_choice:
        return 'chrome'
    elif 'edge' in browser_choice or 'open microsoft edge' in browser_choice:
        return 'edge'
    else:
        speak("Sorry, I didn't get that. Using default browser.")
        return 'default'

def openWithBrowser(url):
    browser = chooseBrowser()
    speak("Opening browser...")
    try:
        if browser == 'chrome':
            webbrowser.get('chrome').open(url)
        elif browser == 'edge':
            webbrowser.get('edge').open(url)
        else:
            webbrowser.open(url)
    except Exception as e:
        speak("Sorry, I couldn't open the browser.")
        print(e)
        
def alex_intro():
    introduction = ["Hello! I am Alex, your friendly AI companion. My purpose is to assist you in various tasks, "
                    "from managing your daily activities to providing you with information and entertainment. "
                    "I aim to be helpful and engaging, making your experience enjoyable and productive. "
                    "Feel free to ask me anything, and I'll do my best to assist you...Thank you!!"]

    speak(" ".join(introduction))

def respond_to_user(input_text):
    if "joke" in input_text.lower():
        tell_joke()
    elif "introduce" in input_text.lower():
        alex_intro()
    elif "tell me about yourself" in input_text.lower():
        alex_intro()
    else:
        speak("I'm not sure how to respond to that. Can you ask me something else?")   

def tell_joke():
    jokes = [
        "Name the kind of tree you can hold in your hand? A palm tree!",
        "What did the left eye say to the right eye? Between us, something smells!",
        "What social events do spiders love to attend? Webbings.",
        "What is a room with no walls? A mushroom.",
        "Why was six afraid of seven? Because seven eight nine.",
        "What’s a dog’s favorite homework assignment? A lab report."
    ]
    
    last_joke_index = -1
    joke_index = random.randint(0, len(jokes) - 1)
    
    while joke_index == last_joke_index:
        joke_index = random.randint(0, len(jokes) - 1)
    
    last_joke_index = joke_index
    joke = jokes[joke_index]
    speak(joke)

def set_speaking_rate(rate):
    engine.setProperty('rate', rate)

if __name__ == "__main__":
    set_speaking_rate(250)
    
    # Register browsers
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
    except Exception as e:
        print(f"Error during registering browsers: {e}")

    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(result)
                speak(result)
            except Exception as e:
                speak("Sorry, I couldn't find any information on that topic.")
                print(e)
                
        elif 'show trending news' in query:
            openWithBrowser("https://timesofindia.indiatimes.com/")
                
        elif 'open google' in query:
            openWithBrowser("https://www.google.com")
            
        elif 'open youtube' in query:
            openWithBrowser("https://www.youtube.com")

        elif 'what' in query and 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'tell me a joke' in query or 'joke' in query:
            tell_joke()
            
        elif "introduce" in query or "tell me about yourself"in query:
            alex_intro()

        elif "play music" in query or "play song" in query:
            music_path = "D:\\Users\\rajub\\Downloads\\jungle-jungle-baat-chali-hai-the-jungle-book-2016-19135.mp3"
            music_path = "D:\\Users\\rajub\\Downloads\\world-252010.mp3"
            os.startfile(music_path)
            speak("playing music")
            
        elif 'open files' in query or 'show my files'in query:
            my_files = "C:\\Program Files"
            os.startfile(my_files)
            speak("opening files")
            
        elif 'open powerpoint' in query:
            ppt_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(ppt_path)
            speak("Opening Power Point.....")
            
        elif 'open studio' in query:
            studio_path = "C:\\Program Files\\RStudio\\rstudio.exe"
            os.startfile(studio_path)
            speak("opening studio")
            
        elif 'open zoom meeting' in query:
            zoom_path = "C:\\Users\\rajub\\OneDrive\\Documents\\Desktop\\Zoom Workplace.lnk"
            os.startfile(zoom_path)
            speak("opening Zoom Meeting")
            
        elif 'open word' in query:
            word_path = "C:\\Users\\rajub\\OneDrive\\Documents\\Desktop\\Word.lnk"
            os.startfile(word_path)
            speak("opening word")
            
        elif 'open excel' in query:
            excel_path = "C:\\Users\\rajub\\OneDrive\\Documents\\Desktop\\Excel.lnk"
            os.startfile(excel_path)
            speak("opening excel")
            
        elif 'open task manager' in query:
            task_manager_path= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.lnk"
            os.startfile(task_manager_path)
            speak("opening task manager")
                      
        elif 'open oracle' in query:
            oracle_path= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Oracle Database 10g Express Edition\\Go To Database Home Page.lnk"
            os.startfile(oracle_path)
            speak("opening oracle")
        
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break
        
       