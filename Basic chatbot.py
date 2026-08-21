from datetime import datetime

def chatbot():

    print("Welcome to the Basic Chatbot! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower().strip()
        if not user_input:
            continue

        if user_input in ["exit", "bye", "goodbye", "see you"]:
            print("Goodbye! Have a great day!")
            break
        elif user_input in ["hello", "welcome", "hi"]:
            print("Hello! How can I assist you today?")
        elif user_input in ["how are you", "how are you doing"]:
            print("I'm fine, thank you!")
        elif user_input in ["what is your name", "who are you", "name"]:
            print("Mein Name ist Chatbot.")
        elif user_input in ["what can you do", "what are your capabilities"]:
            print("I can answer your questions and provide information.")
        elif user_input in ["what is the weather", "how is the weather", "weather"]:
            print("I'm sorry, I cannot provide real-time weather information.")
        elif user_input in ["what is the time", "current time", "time"]:
            print(f"The current time is: {datetime.now().strftime('%H:%M:%S')}")
        elif user_input in ["what is the date", "current date", "date"]:
            print(f"The current date is: {datetime.now().strftime('%Y-%m-%d')}")
        elif user_input in ["what is the day", "current day", "day"]:
            print(f"Today is: {datetime.now().strftime('%A')}")
        else:
            print("I'm sorry, I didn't understand that.")

chatbot()