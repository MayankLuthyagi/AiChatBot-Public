import streamlit as st
import json
import google.generativeai as genai

# Load the API key from the config file
with open('config.json', 'r') as file:
    config = json.load(file)
api_key = config.get("API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Layout: Create two columns
col1, col2 = st.columns([1, 4])  # Two columns with different width ratios

# Card or label for image and description
with col1:
    # Displaying the image
    st.image("src/photo.jpg", width=200)  # Image on the left

with col2:
    # Creating a styled card/label with the description
    with st.container():
        st.markdown("""
        <div style="border: 1px solid #ddd; padding: 20px; border-radius: 10px; background-color: #f9f9f9; display: flex; flex-direction: column; align-items: flex-start;">
            <h3 style="margin: 0; color: #333; font-size: 18px;">Name: Mayank</h3>
            <p style="color: #666; font-size: 14px; margin: 5px 0;"><strong>Age:</strong> 22</p>
            <p style="color: #555; font-size: 14px; margin: 5px 0;"><strong>Description:</strong> He is your friend. Be open with him and chat about your day or talk to him as your friend.</p>
        </div>
        """, unsafe_allow_html=True)

# Initialize session state to hold chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Function to display the most recent message (left-aligned)
def display_recent_message():
    # Display only the last message (either user or AI)
    if len(st.session_state["messages"]) > 0:
        message = st.session_state["messages"][-1]
        st.markdown(f'<div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; background-color: {"#000000" if message["role"] == "ai" else "#f1f1f1"}; color: {"#ffffff" if message["role"] == "ai" else "#000000"}; margin-bottom: 5px; text-align: left;">{message["content"]}</div>', unsafe_allow_html=True)

# Use text input for user interaction
user_input = st.text_input("Your message:", key="user_input")

# Trigger the action when user presses Enter
if user_input:
    # Add user's message to the chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Prepare the conversation history for the API request
    conversation_history = ""
    for msg in st.session_state["messages"]:
        conversation_history += f"{msg['role']}: {msg['content']}\n"

    # Get AI's response using the full conversation history
    data = model.generate_content(f'''This is a conversation history. The previous messages are as follows:\n{conversation_history}\nNow, answer the following as if you are a 22-year-old Indian man named Mayank chatting with your friend who is struggling in his life you know:\n{user_input}''')
    ai_response = data._result.candidates[0].content.parts[0].text

    # Add AI's response to the chat history
    st.session_state["messages"].append({"role": "ai", "content": ai_response})

    # Display only the most recent message
    display_recent_message()
