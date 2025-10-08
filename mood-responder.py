#!/usr/bin/env python3
"""
Emoji Mood Responder
Simple CLI program that detects mood keywords and replies with an emoji + message.
Type "exit" or "quit" (without quotes) to end the program.
"""

import re

MOODS = {
    "happy": {
        "keywords": ["happy", "joy", "glad", "good", "great", "awesome", "fantastic", "cheerful", "content", "pleased"],
        "emoji": "😊",
        "response": "That's great to hear! Keep smiling!"
    },
    "sad": {
        "keywords": ["sad", "unhappy", "down", "depressed", "blue", "melancholy", "tearful"],
        "emoji": "😔",
        "response": "Cheer up! Here's a hug 🤗"
    },
    "angry": {
        "keywords": ["angry", "mad", "furious", "irritated", "annoyed", "upset"],
        "emoji": "😡",
        "response": "Take a deep breath. You've got this."
    },
    "tired": {
        "keywords": ["tired", "exhausted", "sleepy", "drained", "worn out"],
        "emoji": "😴",
        "response": "Rest well! A short break or nap might help."
    },
    "excited": {
        "keywords": ["excited", "pumped", "thrilled", "stoked", "eager"],
        "emoji": "🥳",
        "response": "Let's celebrate! 🎉"
    }
}

PATTERNS = {}
for mood, info in MOODS.items():
    joined = "|".join(re.escape(k) for k in info["keywords"])
    PATTERNS[mood] = re.compile(rf"\b(?:{joined})\b", flags=re.IGNORECASE)

def detect_mood(text: str) -> str:
    """
    Returns the mood key if any pattern matches the text, otherwise returns None.
    Priority is the insertion order of MOODS (happy, sad, angry, tired, excited).
    """
    for mood in MOODS.keys():
        if PATTERNS[mood].search(text):
            return mood
    return None

def main():
    print("Emoji Mood Responder — tell me how you're feeling! (type 'exit' to quit)\n")
    while True:
        try:
            user = input("How are you feeling? ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye! Take care.")
            break

        if not user:
            print("You didn't type anything — try describing how you feel (or 'exit').\n")
            continue

        lower = user.lower()
        if lower in ("exit", "quit"):
            print("Bye! Stay lovely. 😊")
            break

        mood = detect_mood(user)
        if mood:
            info = MOODS[mood]
            print(f"{info['emoji']}  {info['response']}\n")
        else:
            print("I couldn't quite detect your mood from that. Could you use words like 'happy', 'sad', 'tired', 'angry', or 'excited'? Or describe how you feel in one word.\n")

if __name__ == "__main__":
    main()
