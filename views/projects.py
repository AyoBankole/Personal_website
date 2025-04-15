import streamlit as st

# custom CSS implementation
st.markdown(
    """
    <style>
    /* Overall page background */
    .stApp {
        background-color: #AFDDFF;
        color: #0A0E2A;
        font-family: 'Segoe UI', sans-serif;
        padding: 2rem;
    }

    /* Main title and subheaders */
    h1, h2, h3, h4 {
        color: #0A0E2A;
        font-weight: bold;
    }

    /* Text and markdown blocks */
    .stMarkdown {
        color: #0A0E2A;
        font-size: 1.05rem;
    }

    /* Image styling */
    img {
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(10, 14, 42, 0.3);
        margin-top: 10px;
    }

    /* Button styling */
    .stButton > button {
        background-color: #0A0E2A;
        color: #ffffff;
        font-weight: 600;
        border: none;
        border-radius: 10px;
        padding: 0.6em 1.2em;
        margin-top: 10px;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #233060;
        color: #ffffff;
        transform: scale(1.03);
    }

    /* Section spacing */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
    }

    /* Columns gap and alignment */
    .css-1kyxreq, .css-1v0mbdj {
        align-items: center !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Projects")
st.write("My Past Projects", icon="🚀")

# Define your image paths and captions
project_images = [
    ("./assets/job_tracker.png", "Project 1: Job Tracker"),
    ("./assets/visovox_ai.png", "Project 2: Visovox AI"),
    ("./assets/multi_chatbot.png", "Project 3: Multilingual Chatbot for CircleCare AI"),
    ("./assets/recommendation.png", "Project 4: Movie recommendation system"),
    ("./assets/telecomchurn.png", "Project 5: Telecommunications Churn Prediction"),
]

# Display in 3 rows and 2 columns
for i in range(0, len(project_images), 2):
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(project_images[i][0], caption=project_images[i][1], use_container_width=True)

    with col2:
        if i + 1 < len(project_images):
            st.image(project_images[i + 1][0], caption=project_images[i + 1][1], use_container_width=True)
        else:
            st.empty() 