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

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am an A.I assistant, how may I help you today?")

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
    return query

def takeTextCommand():
    query = input("Type your command: ")
    return query.lower()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abdulrehmanthe07@gmail.com', 'your_password')
    server.sendmail('abdulrehmanthe06@gmail.com', to, content)
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

# def translate_to_english(hindi_text):
#     prompt = f"Translate the following Hindi text to English: {hindi_text}"
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=100  # Adjust as needed
#     )
#     translated_text = response.choices[0].message['content'].strip()
#     return translated_text

if __name__ == "__main__":
    wishMe()
    
    # Choose input method once
    input_method = input("Would you like to speak or type your command? (speak/type): ").strip().lower()
    
    if input_method not in ["speak", "type"]:
        speak("Invalid input method. Please restart the program and choose 'speak' or 'type'.")
    else:
        while True:
            if input_method == "speak":
                query = takeCommand().lower()
            elif input_method == "type":
                query = takeTextCommand()

            if 'quit' in query:
                speak("Goodbye!")
                break
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia: ")
                print(results)
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
                music_dir = 'D:\\Abdul Rehman\\6th Semester\\AI\\music'
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
            # elif 'translate' in query:
            #     speak("Please tell me the text in Hindi.")
            #     hindi_text = takeCommand()
            #     translated_text = translate_to_english(hindi_text)
            #     speak("The translation is: ")
            #     speak(translated_text)
            else:
                speak("Sorry I am unable to answer, may I help you with something else")
