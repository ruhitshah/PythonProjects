# 💬 Simple Keyword-Based Chatbot (Python)
This is a basic Python chatbot that uses a predefined dataset of intents, keywords, and responses to interact with users. It can respond to greetings, pricing inquiries, technical issues, services, and goodbyes — or prompt the user for clarification when it doesn’t understand.
## 📌 Features
- Predefined intents: greeting, pricing, technical issues, services, goodbyes, and unknown queries.
- Keyword matching to detect user intent.
- Randomized responses for a more natural conversation.
- Exit command to end the chat anytime.
## 📂 Project Structure
SimpleChatbot/
├── main.py # Main Python script
├── README.md # Project documentation
## 🛠 Requirements
- Python 3.6 or higher  
No additional external libraries are required (uses only Python’s standard library).
## 🚀 How to Run
1. Clone the repository
git clone https://github.com/yourusername/simple-chatbot.git
cd simple-chatbot
2. Run the chatbot
python chatbot.py
## Example interaction
Chatbot: Hello! Welcome to our software firm. How can I help you today?
You: hi
Chatbot: Hi there! Need help with something?
You: pricing
Chatbot: Our pricing depends on your requirements. Would you like to discuss details?
You: exit
Chatbot: Goodbye! Have a great day!
| Intent          | Keywords                           | Example User Input            |
| --------------- | ---------------------------------- | ----------------------------- |
| Greeting        | hello, hi, greetings, hey          | "hello"                       |
| Pricing         | price, cost, pricing, charge       | "What’s the price?"           |
| Technical Issue | issue, problem, bug, error         | "I found a bug"               |
| Services        | service, offer, solutions, product | "What services do you offer?" |
| Goodbye         | bye, goodbye, see you, exit        | "bye"                         |
| Unknown         | (anything else)                    | "Tell me a joke"              |
## How It Works
Intent Identification: Scans the user input for keywords and matches them to predefined intents in dataset.

Response Generation: Randomly picks a response from the intent’s list of possible replies.

Unknown Handling: If no keywords match, returns a generic clarification request.

## License
This project is open-source for educational purposes. You can modify and extend it freely.

## Author
Developed by Ruhit Shah as a learning project in Python chatbot development.
