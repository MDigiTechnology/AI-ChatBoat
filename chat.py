import os
import streamlit as st
# from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables from .env file
# load_dotenv()

# Set up the page configuration
st.set_page_config(
    page_title="Chat with me..",
    page_icon=":brain:",
    layout="wide",  # This will allow more space for a wide layout
)

# Get API Key
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the generative AI API
# gen_ai.configure(api_key=GOOGLE_API_KEY)
gen_ai.configure(api_key="AIzaSyCXe-yzo-d5vLkA2UOShlu77JoaNDUsE7I")

model = gen_ai.GenerativeModel("gemini-1.5-flash")

# Function to translate role for Streamlit messages
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat history if not present in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Add custom CSS for styling
st.markdown("""
    <style>
        /* Background color and overall layout */
        .stApp {
            background-color: #f4f7fc;
            font-family: 'Arial', sans-serif;
        }

        /* Centering the chat messages */
        .chat-message {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            margin-bottom: 15px;
        }

        /* User and assistant message styling */
        .user .stMarkdown {
            background-color: #DCF8C6;
            padding: 10px;
            border-radius: 10px;
            max-width: 70%;
            word-wrap: break-word;
            margin-bottom: 5px;
        }

        .assistant .stMarkdown {
            background-color: #E9E9E9;
            padding: 10px;
            border-radius: 10px;
            max-width: 70%;
            word-wrap: break-word;
            margin-bottom: 5px;
        }

        /* Title styling */
        .stTitle {
            font-size: 2.5em;
            font-weight: bold;
            color: #4B9CD3;
        }

        /* Input box styling */
        .stTextInput input {
            font-size: 1.2em;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #ccc;
            width: 100%;
        }

        /* Add spacing between messages and input */
        .stChatInput {
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Display title
st.title(":coffee: AI - ChatBot")

# Display previous chat history
for message in st.session_state.chat_history:
    with st.chat_message(translate_role_for_streamlit(message["role"])):
        st.markdown(message["text"])

# User input for new message
user_prompt = st.chat_input("Ask Your-Questions...")

# Send the user's prompt and get the model's response
if user_prompt:
    # Append user message to chat history
    st.session_state.chat_history.append({"role": "user", "text": user_prompt})

    # Display user message in the chat
    st.chat_message("user").markdown(user_prompt)

    # Generate the assistant's response
    gemini_response = model.generate_content(user_prompt)

    # Append assistant's response to chat history
    st.session_state.chat_history.append({"role": "model", "text": gemini_response.text})

    # Display assistant response in the chat
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
