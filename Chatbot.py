"""
Name: Yeasir Arafat Shohan
Id: CA/CP/12437
Task 03: Basic Chatbot"""

"""This is a basic chatbot, which i was simply build with Python. We can also add machine learning model to get better p erformance"""

import random

class Chatbot:
    def __init__(self):
        self.responses = {
            "greetings": ["Hi there!", "Hello, how can I assist you?", "Hey, what's up?"],
            "farewell": ["Goodbye!", "See you later!", "Take care!"],
            "thanks": ["You're welcome!", "No problem at all!", "Glad I could help!"],
            "question": ["That's an intriguing question!", "I'm not entirely certain, but let's explore together!", "I'll do my best to find the answer."],
            "default": ["I'm not quite sure what you mean.", "Could you please rephrase that?", "I'm still learning, apologies!"]
        }

    def get_response(self, message):
        #Generate a response based on the message type.
        if "hello" in message or "hi" in message or "hey" in message:
            return random.choice(self.responses["greetings"])
        elif "bye" in message or "goodbye" in message:
            return random.choice(self.responses["farewell"])
        elif "thanks" in message or "thank you" in message:
            return random.choice(self.responses["thanks"])
        elif "?" in message:
            return random.choice(self.responses["question"])
        else:
            return random.choice(self.responses["default"])

def chat_with_user():
    #Until they decide to quit chat with user.
    chatbot = Chatbot()
    print("Welcome! Let's chat. (Type 'quit' to exit)")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Chat ended.")
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

# Start chatting
chat_with_user()
