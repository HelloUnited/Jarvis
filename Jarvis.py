import pyttsx3  #pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis, How may I help you")

def takeCommand():
    #It takes microphone input from the user and return string output
    ear=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        ear.pause_threshold=1
        audio=ear.listen(source)

    try:
        print("Recognizing...")
        query=ear.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("May you please repeat....")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()
       

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("Wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open netflix' in query:
            webbrowser.open("netflix.com")
        elif 'play music' in query:
            music_dir='C:\\Personal\\dance\\songs'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            

        elif 'open code' in query:
            code_path='C:\\Program Files\\Microsoft VS Code'
            os.startfile(code_path)
        elif 'shutdown jarvis' in query:
            speak("Adios sir")
            break
