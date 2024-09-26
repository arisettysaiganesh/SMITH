# SMITH
A desktop-based voice assistant designed to enhance user productivity through voice commands. Utilizing Python, SMITH integrates speech recognition, text-to-speech synthesis, web browsing, and various other functionalities to offer a hands-free and intuitive user experience. 

# SMITH - Desktop Voice Assistant

SMITH is a desktop voice assistant built with Python that can assist you with various tasks using voice commands. This project utilizes speech recognition, text-to-speech, and other libraries to provide a user-friendly experience.

## Features

- **Voice Interaction**: Communicate with the assistant using your voice.
- **Time and Date**: Retrieve current time and date.
- **Web Browsing**: Open websites like Google, YouTube, and Stack Overflow.
- **Music Playback**: Play random music from your music library.
- **Wikipedia Search**: Search and read summaries from Wikipedia.
- **Screenshot Capture**: Take screenshots and save them to your Pictures folder.
- **Remember Information**: Store and retrieve simple notes.
- **Greeting Messages**: Personalized greetings based on the time of day.

## Requirements

- Python 3.x
- Libraries:
  - `pyttsx3`
  - `pywin32`
  - `speech_recognition`
  - `wikipedia`
  - `pyautogui`
  
You can install the required libraries using pip:

```bash
pip install pyttsx3 pywin32 SpeechRecognition wikipedia pyautogui

-----
Usage
Clone this repository or download the script.
Ensure your microphone is set up correctly.
Run the script:
bash
Copy code
python assistant.py
Follow the spoken instructions to interact with SMITH.
Commands
Here are some voice commands you can use with SMITH:

"time": Get the current time.
"date": Get the current date.
"who are you": Learn about the assistant.
"how are you": Ask about the assistant's well-being.
"wikipedia [search term]": Search for a topic on Wikipedia.
"open [website]": Open a specified website (e.g., YouTube, Google).
"play music": Play a random song from your music library.
"screenshot": Take a screenshot and save it.
"remember that [text]": Save a note.
"do you remember anything": Retrieve the saved note.
"offline": Exit the assistant.
Important Notes
Ensure that your microphone is functioning and accessible.
If you encounter any issues, check the installation of required libraries and your microphone settings.
The script may require administrative permissions depending on your system settings.
License
This project is open-source and available for modification and distribution. Please see the LICENSE file for more details.

Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and suggestions are welcome!
