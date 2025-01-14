# Voice Assistant - IRONMAN

This project implements a voice assistant named "IRONMAN" that interacts with users using voice commands. It performs various tasks such as fetching weather information, setting timers and alarms, opening websites, and engaging in intelligent conversations using Google's generative AI model.

---

## Features

1. **Voice Recognition**:
   - Detects and processes user voice commands using the `speech_recognition` library.

2. **Text-to-Speech (TTS)**:
   - Converts assistant responses into speech using `pyttsx3`.

3. **Weather Updates**:
   - Retrieves the user's location using the Windows Geolocation API.
   - Fetches weather data via the WeatherAPI.

4. **Timer and Alarm**:
   - Sets a timer or alarm and provides audible alerts when the time elapses.

5. **Generative AI Integration**:
   - Leverages Google Generative AI (`gemini-pro`) for answering queries and engaging in conversations.

6. **Web Browsing**:
   - Opens websites like YouTube upon user command.

7. **Graphical User Interface (GUI)**:
   - A simple GUI built with Tkinter to display interactions and control the assistant.

---

## Prerequisites

- **Python**: Version 3.7 or later.
- **Hardware**: A microphone and speakers are required for voice interaction.

---

## Installation

### Clone the Repository
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

### Install Dependencies
   Ensure Python is installed on your system. Then run:
   ```bash
   pip install -r requirements.txt
   ```
   Required dependencies:
   - `pyttsx3`
   - `SpeechRecognition`
   - `requests`
   - `winsdk`
   - `google-generativeai`
   - `pillow`
   - `keyboard`

### Install PyAudio
   - For Windows:
     1. Download the appropriate `.whl` file from [Unofficial Python Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).
     2. Install it using:
        ```bash
        pip install <path_to_downloaded_whl>
        ```

   - For Linux/Mac:
     ```bash
     pip install pyaudio
     ```

### API Keys
   - Add your Google Maps API key and WeatherAPI key in the script:
     ```python
     google_maps_api_key = "YOUR_GOOGLE_MAPS_API_KEY"
     api_key = "YOUR_WEATHER_API_KEY"
     ```

---

## Usage

1. Run the script:
   ```bash
   python IRONMAN.py
   ```

2. The assistant will begin listening for the trigger phrase `Iron Man`.

3. **Available Commands**:
   - "What's the weather?": Fetches the current weather.
   - "Set a timer for X seconds": Starts a timer.
   - "Set an alarm for X seconds": Sets an alarm.
   - "Open YouTube": Launches YouTube in a web browser.
   - "Exit": Terminates the assistant.

4. **Response**:
   - The assistant's responses will be displayed in the GUI and spoken aloud.

---

## Code Structure

- **Main Script**: Contains all the logic for voice recognition, TTS, weather integration, and generative AI responses.
- **GUI**: Built using Tkinter for user interaction.

---

## Troubleshooting

### Common Issues

1. **PyAudio Installation Error**:
   - Ensure you have installed the correct `.whl` file for your Python version and system architecture.

2. **Microphone Not Detected**:
   - Verify that the microphone is enabled and properly connected.

3. **API Key Errors**:
   - Double-check that your API keys are valid and correctly entered in the script.

4. **Internet Dependency**:
   - Ensure an active internet connection for weather and generative AI features.

---

## Future Improvements

- Add support for more complex commands.
- Implement additional integrations (e.g., calendar, email).
- Enhance GUI design for better usability.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

---

## Author
Developed by UDAY KUMAR KONANKI.

