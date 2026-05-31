import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes
import pywhatkit
import time
import urllib.parse

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            print("Recognizing...")
            query = recognizer.recognize_google(
                audio,
                language='en-in'
            )

            print(f"You said: {query}")
            return query.lower()

        except sr.WaitTimeoutError:
            print("No speech detected")
            return ""

        except sr.UnknownValueError:
            print("Could not understand")
            return ""

        except sr.RequestError:
            print("Internet issue")
            return ""

        except Exception as e:
            print(f"Error: {e}")
            return ""


def wait_for_name():
    while True:
        query = listen()

        if 'jarvis' in query:
            speak("Yes, I am listening")
            return


def execute_command(query):
    query = query.strip()

    if 'play' in query:
        song = query.replace('play', '').strip()

        if not song:
            speak("Please tell me the song name.")
            return 'none'

        speak(f"Searching and playing {song}")
        pywhatkit.playonyt(song)
        return 'play'

    elif 'explain' in query or 'what is' in query or 'who is' in query or 'tell me about' in query:
        topic = query
        for phrase in ['explain', 'what is', 'who is', 'tell me about']:
            topic = topic.replace(phrase, '')

        topic = topic.strip()
        if not topic:
            speak("Please tell me what to explain.")
            return 'none'

        speak(f"Searching for {topic}")
        search_url = f"https://www.google.com/search?q={urllib.parse.quote(topic)}"
        webbrowser.open(search_url)
        return 'search'

    elif 'wikipedia' in query:
        topic = query.replace('wikipedia', '').strip()

        if not topic:
            speak("Please tell me what to search on Wikipedia.")
            return 'none'

        speak("Searching Wikipedia")

        try:
            result = wikipedia.summary(topic, sentences=2)
            print(result)
            speak(result)
            wiki_url = f"https://en.wikipedia.org/wiki/{urllib.parse.quote(topic.replace(' ', '_'))}"
            webbrowser.open(wiki_url)
            return 'wiki'

        except Exception:
            speak("Sorry, I could not find anything on Wikipedia.")
            return 'none'

    elif 'open google' in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")
        return 'open'

    elif 'search' in query or ('google' in query and 'open google' not in query):
        topic = query
        for phrase in ['search', 'google', 'open']:
            topic = topic.replace(phrase, '')

        topic = topic.strip()
        if not topic:
            speak("Please tell me what to search.")
            return 'none'

        speak(f"Searching for {topic}")
        search_url = f"https://www.google.com/search?q={urllib.parse.quote(topic)}"
        webbrowser.open(search_url)
        return 'search'

    elif 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")
        return 'time'

    elif 'joke' in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
        return 'joke'

    elif 'open google' in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")
        return 'open'

    elif 'bye' in query:
        speak("Goodbye")
        exit()

    else:
        speak("I did not understand")
        return 'none'


def run_assistant():
    speak("Assistant is now in standby mode")
    while True:
        query = listen()

        if 'jarvis' in query:
            speak("Yes, I am listening")

            command = query.replace("jarvis", "").strip()

            if not command:
                command = listen()

            if command:
                action = execute_command(command)

                # CRITICAL CHANGE HERE:
                if action == 'play':
                    speak("Playing your song on YouTube. Closing the assistant script. Goodbye!")
                    exit()  # This completely stops the script and stops all listening.
                else:
                    speak("Returning to standby mode")
                    time.sleep(2)
            else:
                speak("Returning to standby mode")

if __name__ == "__main__":
    run_assistant()