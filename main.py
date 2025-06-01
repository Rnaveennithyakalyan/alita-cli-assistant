from dotenv import load_dotenv
import google.generativeai as genai
import os
from utils.prompts import INITIAL_PROMPT

# 1. Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Validate the API key
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

# 3. Configure the Gemini SDK
genai.configure(api_key=api_key)

# 4. Create the chat model and session with memory
model = genai.GenerativeModel("gemini-1.5-flash")  # You can also use "gemini-pro"
chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": [INITIAL_PROMPT]
    }
])

# 5. Function to interact with Gemini
def chat_with_gemini(user_input):
    response = chat.send_message(user_input)
    return response.text.strip()

# 6. CLI main loop
def main():
    print("Alita here (type 'exit' to quit)")

    while True:
        user_input = input("you : ")
        if user_input.lower() in {"exit", "quit"}:
            print("bye!")
            break
        reply = chat_with_gemini(user_input)
        print("Gemini:", reply)

if __name__ == "__main__":
    main()
