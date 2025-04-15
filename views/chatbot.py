import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# --- Custom Light Blue Theme CSS ---
st.markdown(
    """
    <style>
    body {
        background-color: #AFDDFF; /* Light blue background */
        color: #0A0E2A; /* Deep blue text */
        font-family: 'Segoe UI', sans-serif;
    }

    .stApp {
        background-color: #AFDDFF;
        padding: 2rem;
    }

    h1, h2, h3, h4 {
        color: #0A0E2A; /* Deep blue headings */
    }

    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #0A0E2A;
        border: 1px solid #0A0E2A;
        border-radius: 8px;
        padding: 0.4em;
    }

    .stButton > button {
        background-color: #0A0E2A;
        color: #AFDDFF;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 0.5em 1em;
        transition: background-color 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #1c244a;
        color: #AFDDFF;
    }

    .stMarkdown {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        color: #0A0E2A;
        border-left: 4px solid #0A0E2A;
    }

    .stSpinner {
        color: #0A0E2A !important;
    }

    label, .css-1cpxqw2 {
        color: #0A0E2A;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Streamlit UI ---
st.image("./assets/my toon.jpg", width=200)
st.title("Lupin - AI Assistant")
st.subheader("Ask anything about Technology or Artificial Intelligence.")

# --- Chat Input Form ---
with st.form("chat_form"):
    user_input = st.text_input("You:", placeholder="e.g. How does reinforcement learning work?")
    submitted = st.form_submit_button("Ask")

if submitted and user_input:
    with st.spinner("Thinking..."):

        chat_completion = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that answers questions related to technology and artificial intelligence in a concise and clear manner."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=0.5,
            max_completion_tokens=1024,
            top_p=1,
            stop=None,
            stream=False
        )

        response = chat_completion.choices[0].message.content
        st.markdown(f"**Lupin:** {response}")