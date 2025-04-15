import streamlit as st
from forms.contact import contact_form

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

st.title("About Me Section")

st.subheader("Experience and Qualification")
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/me_potrait.jpg", width=200)

with col2:
    st.title("Ogunsanya Ayobami Akanbi")
    st.write("Data Scientist | Machine Learning Engineer")
    if st.button("🧾 Contact me"):
        contact_form()  # Call the contact form directly

st.write(
    """
        - 2 years of experience in Data Science and Machine Learning
        - B.Sc. Marine Biology, University of Lagos
        - I got my knowledge in tech from the internet and self-study
        - Excellent tutor and problem-solver
    """
)

# Skills
st.write("## Skills")
st.write(
    """
       - Programming: Python, Javascript, Typescript, SQL
       - Data Visualization: Matplotlib, Seaborn, Plotly, Tableau, PowerBI
       - Modeling: Logistic Regression, Random Forest, XGBoost, Neural Networks
       - Database: MySQL, Sqlite, MongoDB
       - Web Development: HTML, CSS, Streamlit
       - LLM: GPT, BERT, Transformer
    """
)