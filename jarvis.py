import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import os
import webbrowser



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    
    else:speak("Good evening!") 

    speak("Hi , I am Jarvis. My speed, none of your matter. Sir How may i help you ")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
    #print(e)
        print("Say that anain please...")
        return"None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        #Logic for executing tasks based on query    
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open google' in query:
            webbrowser.open("github.com")
        elif 'onen stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'pla music' in query:
            music_dir = 'C:\\Users\\Rj\\Downloads\\MUSIC'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Rj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
