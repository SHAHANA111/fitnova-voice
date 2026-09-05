from stt import listen_and_transcribe
from chatbot import chatbot_response
from tts import speak
from translator import LANGUAGE_OPTIONS, translate_to_english, translate_from_english


def choose_language():
    print("Select your language:")
    for key, value in LANGUAGE_OPTIONS.items():
        print(f"{key}. {value['name']}")

    choice = input("Enter choice: ").strip()

    if choice not in LANGUAGE_OPTIONS:
        print("Invalid choice, defaulting to English.")
        choice = "1"

    return LANGUAGE_OPTIONS[choice]


def run_voice_pipeline():
    # Step 1: Ask the user which language they'll speak in
    selected_lang = choose_language()
    print(f"Selected language: {selected_lang['name']}")

    # Step 2: Get text from voice, using the correct STT language code
    user_text = listen_and_transcribe(language_code=selected_lang["stt_code"])

    # print(f"Raw text length: {len(user_text)}, characters: {list(user_text)}")

    if user_text is None:
        print("No valid input received. Try again.")
        speak("Sorry, I didn't catch that. Please try again.")
        return

    # Step 3: Translate to English ONLY if the user didn't pick English
    if selected_lang["translate_code"] != "en":
        english_text = translate_to_english(user_text, selected_lang["translate_code"])
        print(f"English version: {english_text}")
    else:
        english_text = user_text  # already English, skip translation call entirely

    # Step 4: Send English text to the dummy chatbot
    response = chatbot_response(english_text)
    print(f"FitNova (English): {response}")

    # Step 5: Translate response back ONLY if needed
    if selected_lang["translate_code"] != "en":
        final_response = translate_from_english(response, selected_lang["translate_code"])
        print(f"FitNova (translated): {final_response}")
    else:
        final_response = response  # already English, skip translation call entirely

    # Step 6: Speak the response out loud
    speak(final_response, language_code=selected_lang["translate_code"])


if __name__ == "__main__":
    run_voice_pipeline()