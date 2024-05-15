import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
import pyjokes
import openai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

openai.api_key = 'your_openai_api_key'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Us man I am an A.I assistant, how may I help you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Kindly repeat again")
        return "None"
    return query.lower()

def takeTextCommand():
    query = input("Type your command: ")
    return query.lower()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com', 'password')
    server.sendmail('abc@gmail.com', to, content)
    server.close()

def getWeather():
    api_key = "your_openweather_api_key"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Islamabad"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    weather_data = response.json()
    
    if weather_data["cod"] != "404":
        main = weather_data["main"]
        temperature = main["temp"] - 273.15  # Convert from Kelvin to Celsius
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather_data["weather"][0]["description"]
        
        speak(f"The temperature in Islamabad is {temperature:.2f} degrees Celsius.")
        speak(f"Atmospheric pressure is {pressure} hPa.")
        speak(f"Humidity is {humidity} percent.")
        speak(f"Weather description: {weather_description}.")
    else:
        speak("City not found")

def tellJoke():
    joke = pyjokes.get_joke()
    speak(joke)

def defaultAnswer():
    speak("Sorry, I am unable to answer that.")

def openai_response(prompt):
    response = openai.Completion.create(
        engine="davinci",  # Use the Davinci model
        prompt=prompt,
        max_tokens=150  # Adjust as needed
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        
        # Process query
        if 'speak or type' in query:
            speak("Would you like to speak or type your command? Please say 'speak' or 'type'.")
            continue
        elif 'speak' in query:
            query = takeCommand()
        elif 'type' in query:
            query = takeTextCommand()
        elif 'stop' in query:
            speak("Stopping execution.")
            break
        
        # Perform actions based on the query
        print("User query:", query)

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia: ")
            speak(results)
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            speak("Opening facebook")
            webbrowser.open("facebook.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Dell\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'how are you' in query:
            speak("I'm doing well, thank you for asking!")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time right now is {strTime}")
        elif 'open code' in query:
            speak("Opening Visual Studio Code")
            codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak("What should I say in Email?")
                content = takeCommand()
                to = "abdulrehmanthe07@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Can't send the email at the moment")
        elif 'weather' in query:
            getWeather()
        elif 'joke' in query:
            tellJoke()
        elif 'translate' in query:
            response = openai_response(query)
            speak(response)
        else:
            defaultAnswer()
