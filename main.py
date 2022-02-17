import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing ZAK...")


listener = sr.Recognizer()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")


def speak(text):
    engine.say(text)
    engine.runAndWait()
# speak("Hallo Tom. I am your virtual assistant")


speak("initializing ZAK")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

# time()


def date():
    speak("The corrent date is: ")
    date = int(datetime.datetime.now().year)
    date2 = int(datetime.datetime.now().month)
    date3 = int(datetime.datetime.now().day)
    speak("Year: ")
    speak(date)
    speak("Month: ")
    speak(date2)
    speak("Day: ")
    speak(date3)

# date()


def wishMe():
    print("Initializing is Done!")
    speak("Initializing is Done!")
    speak("Welcome back sir!")
    print("Welcome back sir!")
    speak("the corrent time is: ")
    time()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening sir!")
    else:
        speak("Good night sir!")
    speak("How can I help you with?")
    print("How can I help you with?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # sk-SK or en-in
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
    server.login('tt.tomicraft@gmail.com', 'w3cbAlvAn.')
    server.sendmail('tt.tomicraft@gmail.com', to, content)
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
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query.lower():
            webbrowser.get("https://youtube.com")
            print("OK. I opened YouTube")
            speak("OK. I opened YouTube")
        elif "open google" in query.lower():
            webbrowser.open("http://www.google.com")
            print("OK. I opened Google")
            speak("OK. I opened Google")
        elif "open google" in query.lower():
            webbrowser.open("https://zsbahon.edupage.org/user/?c2fa=1")
            print("OK. I opened Edupage")
            speak("OK. I opened Edupage")
        elif "the time" in query.lower():
            speak("Now is: ")
            time()
        elif "the date" in query.lower():
            speak("Now is date: ")
            date()
        elif 'email to cousin' in query.lower():
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "zemiak52@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                # print(e)
                print("Sorry my friend. I am not able to send this email.")
                speak("Sorry my friend. I am not able to send this email.")
        elif 'email to dad' in query.lower():
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vladky@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                # print(e)
                print("Sorry my friend. I am not able to send this email.")
                speak("Sorry my friend. I am not able to send this email.")
        elif 'email to mom' in query.lower():
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "tarabova@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                # print(e)
                print("Sorry my friend. I am not able to send this email.")
                speak("Sorry my friend. I am not able to send this email.")
