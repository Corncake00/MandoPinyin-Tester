import os
from google import genai
from google.genai import types

# Set your API key
os.environ["GEMINI_API_KEY"] = "AIzaSyBk7XJe6bw13bkFFAfSjLVsuC2UZqALE5Y"
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Create a chat model
chat = client.chats.create(model="gemini-2.5-flash")

# Send system instruction
chat.send_message(
    "Translate English sentences into Mandarin Pinyin (no tones). Start with 5 word sentences with basic wordsand no adjectives using many alphabet letters. Increase difficulty over time. If the user makes mistakes, track incorrect letters and emphasize them in future questions. Accept accurate alternatives. Respond with concise translations only — no pleasantries."
)

# Score counter
score = 0

# Start
start = input("Enter 'y' to start practicing: ").strip().lower()

if start == "y":
    while True:
        # Ask Gemini to generate a new question
        ai_question = chat.send_message(
            "Ask the user to translate an English sentence into Mandarin Pinyin (no tones). Start with 5 word sentences with basic words and no adjectives using many alphabet letters. If the last answer was wrong, make it easier; if correct, increase difficulty making it longer and more complex"
        ).text
        print("\nAI Question:", ai_question)
         # Get user's answer
        user_answer = input("Your answer (or type 'terminate' to quit): ").strip()
        if user_answer.lower() == "terminate":
            print("Thanks for playing! Qs Answered:", score)
            break

        # Get feedback from Gemini
        feedback = chat.send_message(
            f"The user answered: '{user_answer}'. Provide concise feedback. "
            "Give the exact correct Pinyin (no tones). The user must match it exactly. If a letter is wrong, remember it and emphasize that letter in future questions. Keep answers concise, minimal pleasantries — just the correct translation or valid alternatives, if the pinyin up to 2 words but the point is the same and nothing is misspelled say its correct but write the ideal answer."
        ).text
        print("\nFeedback:", feedback)

        # Update score if correct
        if "correct" in feedback.lower():
            score += 1
            print("Qs. Answered +1!")
else:
    print("bye")