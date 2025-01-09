# AiChatBot

**AiChatBot** is an intelligent assistant designed to help you navigate and excel in programming languages. Whether you're a beginner learning the basics or tackling complex problems, AIChatBot provides instant solutions, explanations, and resources tailored to your needs.

[Try the live demo here!](https://learn-pro.streamlit.app/)

If the demo link does not work, it means I am upgrading the project.

## Features

- **Conversational AI**: The chatbot simulates human-like conversations.
- **Personalized Responses**: Tailored responses based on the context of your conversation.
- **Friend-like Interaction**: AiChatBot acts like a friendly companion who listens and talks about various topics.
- **Easy to Use**: Simply type in your message, and AiChatBot responds in real-time.

## Technologies Used

- **Google Gemini AI**: For generating human-like responses based on conversation history.
- **Streamlit**: For building the interactive web interface.
- **Python**: The programming language used for backend logic.

## Setup

To run this project locally, follow these steps:

### Prerequisites

- Python 3.6 or higher
- Streamlit
- Google Generative AI API key (configure with `config.json`)

### Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/MayankLuthyagi/AiChatBot-public.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Get your Google API key and add it to a `config.json` file with the following structure:

   ```json
   {
     "API_KEY": "your_api_key_here"
   }
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to the provided local URL to start chatting with the bot!

## How to Use

- Once the app is running, you will see the interface with an image and a description of the chatbot.
- Type your message in the input box, and AiChatBot will respond like a friend.
- You can continue the conversation, and the bot will remember the context of your chat.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any enhancements, bug fixes, or feature suggestions.

---

Built with ❤️ by Mayank
