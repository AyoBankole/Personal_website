import streamlit as st

# CSS implementation
st.markdown(
    """
    <style>
    /* Main page background */
    .stApp {
        background-color: #9ACBD0;
        color: #0A0E2A;
        font-family: 'Segoe UI', sans-serif;
        padding: 2rem;
    }

    /* Titles and subtitles */
    h1, h2, h3, h4 {
        color: #0A0E2A;
        font-weight: bold;
    }

    .stMarkdown {
        color: #0A0E2A;
        font-size: 1.05rem;
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
        transform: scale(1.03);
    }

    /* Image styling */
    img {
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(10, 14, 42, 0.3);
    }

    /* Grey sidebar */
    section[data-testid="stSidebar"] {
        background-color: #d3d3d3;
    }

    /* Sidebar text */
    .sidebar .markdown-text-container {
        color: #0A0E2A !important;
    }

    /* Sidebar links */
    .sidebar a {
        color: #0A0E2A !important;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# PAGE SETUP
about_page = st.Page(
    "./views/about_me.py",
    title="About Me",
    icon="🧠", 
    default=True
)

chatbot_page = st.Page(
    "./views/chatbot.py",
    title="Ask Lupin_AI",
    icon="💬"
)

projects_page = st.Page(
    "./views/projects.py",
    title="My Past Projects",
    icon="🚀"
)

# Create our navigation bar
page = st.navigation(
    {
        "Information": [about_page],
        "Projects": [projects_page],
        "Chatbot": [chatbot_page],
    }
)

# Add logos and links to the sidebar
st.logo("assets/my_logo.png")
st.sidebar.markdown("Made with love by [AyoBankole](https://github.com/AyoBankole)")

# Run the navigation bar
page.run()