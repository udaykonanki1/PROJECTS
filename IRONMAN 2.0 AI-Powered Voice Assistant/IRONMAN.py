import pyttsx3
import speech_recognition as sr
import webbrowser
import time
import winsound
import keyboard
import tkinter as tk
from tkinter import messagebox
import requests
import winsdk.windows.devices.geolocation as wdg
import asyncio
import google.generativeai as ai
from PIL import Image, ImageTk

# Google Maps API key
google_maps_api_key = "YOUR API KEY"

API_KEY = 'YOUR API KEY'
ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

messages = [{"role": "system", "content": "i am UDAY you need to do whatever i said to do. your name is IRONMAN"}]

async def get_coords():
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return [pos.coordinate.latitude, pos.coordinate.longitude]

def get_user_location():
    try:
        # Fetch user's location coordinates using Windows Geolocation API
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        coords = loop.run_until_complete(get_coords())
        return coords[0], coords[1]
    except Exception as e:
        print("Error fetching user location:", e)
        return None, None

def get_weather(lat, lon, api_key):
    try:
        # Make a request to WeatherAPI.com API to get weather data
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print("Error fetching weather data:", e)
        return None

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    
    if "weather" in user_input.lower():
        lat, lon = get_user_location()
        if lat is None or lon is None:
            return "Sorry, I couldn't fetch your location. Please check your internet connection."
        
        api_key = 'YOUR API KEY'
        weather_data = get_weather(lat, lon, api_key)
        
        if weather_data:
            location = weather_data["location"]["name"]
            temperature = weather_data["current"]["temp_c"]
            condition = weather_data["current"]["condition"]["text"]
            return f"The weather in {location} is {condition} with a temperature of {temperature} degrees Celsius."
        else:
            return "Sorry, I couldn't fetch the weather data at the moment."
    elif "timer" in user_input.lower():
        seconds = extract_seconds(user_input)
        if seconds is not None:
            set_timer(seconds)
            return f"Timer is set for {seconds} seconds."
        else:
            return "Sorry, I couldn't understand the duration for the timer."
    elif "alarm" in user_input.lower():
        seconds = extract_seconds(user_input)
        if seconds is not None:
            set_alarm(seconds)
            return f"Alarm is set to ring in {seconds} seconds."
        else:
            return "Sorry, I couldn't understand the duration for the alarm."
    elif "time" in user_input.lower():
        current_time = get_current_time()
        return f"The current time is {current_time}"
    else:
        response = chat.send_message(user_input)
        return response.text

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for trigger phrase...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except sr.UnknownValueError:
        return None  # Return None if trigger phrase not detected
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None  # Return None if there is an error

def text_to_speech(text):
    engine = pyttsx3.init()
    sentences = text.split(".")  # Split text into sentences
    for sentence in sentences:
        engine.say(sentence)
        engine.runAndWait()
        text_display.insert(tk.END, sentence + ".\n")  # Display sentence in the text box
        root.update()  # Update the Tkinter window to show the new text

def get_current_time():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    return current_time

def set_timer(time_input):
    try:
        for i in range(time_input, -1, -1):
            time.sleep(1)
        text_to_speech("Timer is up!")
    except ValueError:
        text_to_speech("Invalid input. Please enter a valid number of seconds.")

def set_alarm(alarm_time):
    try:
        time.sleep(alarm_time)
        text_to_speech("Alarm is ringing!")
        while True:
            winsound.Beep(5000, 5000)  # Beep sound for 1 second
            if keyboard.is_pressed():
                break
        text_to_speech("Alarm stopped.")
    except ValueError:
        text_to_speech("Invalid input. Please enter a valid number of seconds.")

def extract_seconds(text):
    # Convert text to lowercase for easier matching
    text = text.lower()
    # Look for numerical values in the text
    words = text.split()
    for word_index, word in enumerate(words):
        if word.isdigit():
            # Check if the next word is "second" or "seconds"
            if word_index + 1 < len(words):
                next_word = words[word_index + 1]
                if next_word == "second" or next_word == "seconds":
                    return int(word)
            # If the next word is not present or not "second"/"seconds", assume seconds
            return int(word)
    # If no numerical value followed by "second" or "seconds" is found, return None
    return None

def activate_assistant():
    while True:
        user_input = speech_to_text()
        if user_input is not None and "iron man" in user_input.lower():
            text_to_speech("Hello! How can I assist you?")
            while True:
                user_input = speech_to_text()
                if user_input is None:
                    continue  # Skip iteration if user_input is None
                if "open YouTube" in user_input:
                    webbrowser.open('https://www.youtube.com')
                elif "exit" in user_input.lower():
                    text_to_speech("Goodbye!")
                    break
                else:
                    response = CustomChatGPT(user_input)
                    text_to_speech(response)

def restart_assistant():
    # Clear the conversation history
    messages.clear()
    # Restart the assistant
    activate_assistant()

root = tk.Tk()
root.title("Assistant")
root.geometry("400x400")


label = tk.Label(root, text="IRONMAN-The Voice Assistant", font=("Arial", 16))
label.pack(pady=10)

text_display = tk.Text(root, height=10, width=80) 
text_display.pack(pady=10)

btn_quit = tk.Button(root, text="Quit", command=root.destroy)
btn_quit.pack(pady=10)

btn_restart = tk.Button(root, text="Restart", command=restart_assistant)
btn_restart.pack(pady=10)

root.after(1000, activate_assistant)  # Start listening for the trigger phrase after 1 second

root.mainloop()
