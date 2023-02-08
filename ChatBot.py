# Define a list of responses
responses = ["Hello!", "Goodbye!", "What can I help you with today?", "I'm sorry, I don't understand."]

# Continuously ask the user for input until they type "quit"
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    # Print a random response from the list
    print("Chat Bot: " + responses[0])
