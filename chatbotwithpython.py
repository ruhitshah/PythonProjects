
dataset = {
    "greeting": {
        "keywords": ["hello", "hi", "greetings", "hey"],
        "responses": ["Hello! How can I assist you today?", 
                      "Hi there! Need help with something?"]
    },
    "pricing": {
        "keywords": ["price", "cost", "pricing", "charge"],
        "responses": ["Our pricing depends on your requirements. Would you like to discuss details?",
                      "You can check our pricing plans on our website. Do you need a link?"]
    },
    "technical_issue": {
        "keywords": ["issue", "problem", "bug", "error"],
        "responses": ["I'm sorry to hear about the issue. Can you describe the problem?",
                      "Let me assist you with the issue. Please provide more details."]
    },
    "services": {
        "keywords": ["service", "offer", "solutions", "product"],
        "responses": ["We offer software development, system integration, and maintenance services.",
                      "Our services include web development, mobile apps, and cloud solutions. What are you looking for?"]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "exit"],
        "responses": ["Goodbye! Feel free to reach out anytime.", 
                      "Take care! We’re here if you need us."]
    },
    "unknown": {
        "responses": ["I'm sorry, I didn't understand that. Could you please rephrase?",
                      "Can you provide more details? I'm here to help."]
    }
}

# NLU function to identify user intent based on keywords
def identify_intent(user_input):
    for intent, data in dataset.items():
        if intent != "unknown":
            for keyword in data["keywords"]:
                if keyword.lower() in user_input.lower():
                    return intent
    return "unknown"

# Function to generate response
import random

def generate_response(intent):
    return random.choice(dataset[intent]["responses"])

# Chatbot function
def chatbot():
    print("Chatbot: Hello! Welcome to our software firm. How can I help you today?")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        # Identify intent
        intent = identify_intent(user_input)
        # Generate response
        response = generate_response(intent)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

