# Voice Assistant

A simple Python voice assistant built using speech recognition, text-to-speech, and web services.

## Features

- Listens for the wake word `Jarvis`
- Plays YouTube songs on voice command
- Opens Google and searches the web
- Reads Wikipedia summaries
- Tells jokes
- Announces the current time
- Uses your microphone and system speech output

## Requirements

- Python 3.8 or newer
- A working microphone
- Internet connection for speech recognition, search, and YouTube playback

## Python Dependencies

- `speech_recognition`
- `pyttsx3`
- `wikipedia`
- `pyjokes`
- `pywhatkit`

> Note: On Windows, `pyttsx3` uses the `sapi5` speech engine.

## Installation

1. Clone or download this repository.
2. Install dependencies:

```bash
pip install speechrecognition pyttsx3 wikipedia pyjokes pywhatkit
```

## Usage

1. Run the assistant:

```bash
python assistant.py
```

2. Say `Jarvis` to wake the assistant.
3. Ask a command, for example:

- `Jarvis play never gonna give you up`
- `Jarvis what is artificial intelligence`
- `Jarvis search python tutorials`
- `Jarvis open google`
- `Jarvis tell me a joke`
- `Jarvis what time is it`

## Notes

- The assistant will respond using the system voice and open web pages in your default browser.
- If the assistant cannot understand your speech, it will ask you to try again.
- The script ends after playing a song on YouTube.

## File

- `assistant.py` - main voice assistant script
