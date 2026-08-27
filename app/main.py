from stt import listen_and_transcribe
from chatbot import chatbot_response
from tts import speak

def run_voice_pipeline():
    # Step 1: Get text from voice
    user_text = listen_and_transcribe()

    if user_text is None:
        print("No valid input received. Try again.")
        speak("Sorry, I didn't catch that. Please try again.")
        return

    # Step 2: Send that text to the dummy chatbot
    response = chatbot_response(user_text)
    print(f"FitNova: {response}")

    # Step 3: Speak the response out loud
    speak(response)


if __name__ == "__main__":
    run_voice_pipeline()