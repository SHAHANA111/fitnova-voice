import pyttsx3

def speak(text: str):
    """
    Converts text to speech and plays it out loud.
    Later, this could be swapped for a cloud TTS service
    (like OpenAI TTS) for higher quality voices.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)   # speaking speed
    engine.setProperty('volume', 1.0) # volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Hello! I am FitNova, your fitness assistant.")