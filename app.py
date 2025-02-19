import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="👨‍💻", layout="wide")

st.title("👨‍💻 Welcome to My Portfolio")
st.write("Hello! I'm [Your Name], a software developer. Here are some of my projects:")

# Navigation links to main project pages
st.page_link("pages/SeeWhoDoesntFollowYou/main.py", label="📊 Instagram Analyzer")
st.page_link("pages/FlashcardAutomation/main.py", label="🤖 Flashcard Automation Tool")
st.page_link("pages/Casino/main.py", label="🎰 Casino Game")

