def chatbot_response(user_text: str) -> str:
    """
    Dummy chatbot logic.
    Later, this function's INSIDE will be replaced by a call
    to the real FitNova chatbot API. The rest of your pipeline
    (stt.py, tts.py, main.py) won't need to change.
    """
    text = user_text.lower()

    if "workout" in text or "exercise" in text:
        return "Sure! Today's workout is 3 sets of squats, 20 push-ups, and a 15-minute walk."
    elif "meal" in text or "eat" in text or "food" in text:
        return "For today's meal, I'd suggest grilled chicken, brown rice, and steamed vegetables."
    elif "water" in text or "hydrate" in text or "drink" in text:
        return "Try to drink at least 8 glasses of water today to stay hydrated."
    else:
        return "I'm your FitNova fitness assistant. You can ask me about workouts, meals, or hydration."

if __name__ == "__main__":
    # Quick manual test without needing STT
    test_input = "what about meals and workout"
    print(f"You said: {test_input}")
    print(f"Bot says: {chatbot_response(test_input)}")