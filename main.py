import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install speechrecognition
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib

listener = sr.Recognizer()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# speak("Hallo Tom. I am your virtual assistant")


print("Initializing ZAK...")
speak()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak()

# time()


def date():
    speak()
    date = int(datetime.datetime.now().year)
    date2 = int(datetime.datetime.now().month)
    date3 = int(datetime.datetime.now().day)
    speak()
    speak()
    speak()
    speak()
    speak()
    speak()

# date()


def wishMe():
    print("Initializing is Done!")
    speak()
    speak()
    print("Welcome back sir!")
    speak()
    time()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak()
    elif hour >= 12 and hour < 18:
        speak()
    elif hour >= 18 and hour < 24:
        speak()
    else:
        speak()
    speak()
    print("How can I help you with?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # en-in
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourgmail@gmail.com', 'password')
    server.sendmail('yourgmailt@gmail.com', to, content)
    server.close()


# wishMe()
# query = takeCommand()

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            speak()
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak()
            print(results)
            speak()
        elif "open youtube" in query.lower():
            webbrowser.open("https://youtube.com")
            print("OK. I opened YouTube")
            speak()
        elif "open google" in query.lower():
            webbrowser.open("http://www.google.com")
            print("OK. I opened Google")
            speak()
        elif "open google" in query.lower():
            webbrowser.open("https://zsbahon.edupage.org/user/?c2fa=1")
            print("OK. I opened Edupage")
            speak()
        elif "the time" in query.lower():
            speak()
            time()
        elif "the date" in query.lower():
            speak()
            date()
        elif 'email to somewone' in query.lower():
            try:
                speak()
                content = takeCommand()
                to = "zemiak52@gmail.com"
                sendEmail(to, content)
                speak()
            except Exception as e:
                # print(e)
                print("Sorry my friend. I am not able to send this email.")
                speak()
