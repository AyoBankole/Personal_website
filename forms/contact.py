import streamlit as st
import re
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the webhook URL from environment variable
WEBHOOK_URL = os.getenv("WEBHOOK_URL")


def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def contact_form():
    if not WEBHOOK_URL:
        st.error("Webhook URL is not configured. Please contact the administrator.", icon="⚠️")
        return

    with st.form("Contact Form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not name:
                st.error("Please enter your name", icon="👤")
                return

            if not email:
                st.error("Please enter your email", icon="✉️")
                return

            if not message:
                st.error("Please enter your message", icon="💬")
                return

            if not is_valid_email(email):
                st.error("Please enter a valid email", icon="❗")
                return

            data = {
                "name": name,
                "email": email,
                "message": message
            }

            try:
                response = requests.post(WEBHOOK_URL, json=data)
                if response.status_code == 200:
                    st.success("Message sent successfully", icon="✅")
                else:
                    st.error("An error occurred while sending your message", icon="⚠️")
            except requests.exceptions.RequestException as e:
                st.error(f"Failed to send message: {e}", icon="⚠️")