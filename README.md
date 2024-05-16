AI Assistant
This project implements a simple AI assistant capable of performing various tasks based on voice or text commands. It utilizes Python and several libraries for different functionalities.

Features
Voice Recognition: The assistant can understand voice commands using the speech_recognition library.
Wikipedia Search: It can search for topics on Wikipedia and provide a summary.
Web Browsing: Capable of opening websites like YouTube, Google, and Facebook using webbrowser.
Music Playback: Can play music stored in a specified directory.
Time Display: Displays the current time upon request.
Email Sending: Allows the user to compose and send emails.
Weather Information: Fetches current weather data for a specified location using the OpenWeatherMap API.
Jokes: Provides random jokes using the pyjokes library.
Translation (Commented Out): Includes functionality to translate text from Hindi to English using OpenAI's GPT-3.5, although it's currently commented out.

Requirements
Python 3.x
pyttsx3 for text-to-speech conversion.
speech_recognition for voice recognition.
wikipedia for searching Wikipedia.
requests for making HTTP requests.
pyjokes for fetching jokes.
OpenAI's GPT-3.5 API (for translation functionality).

Usage
Clone the repository or download the code files.
Install the required libraries using pip: pip install -r requirements.txt.
Replace placeholder values like Gmail credentials and OpenWeatherMap API key with your actual credentials.
Run the main.py file.
Choose whether to input commands via voice or text.
Interact with the assistant by giving commands such as "open YouTube", "tell me a joke", or "what's the weather".
