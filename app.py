import streamlit as st


st.title("👨‍💻 Welcome to My Portfolio")
st.write("Hello! I'm [Your Name], a software developer. Here are some of my projects:")

insta = st.Page("SeeWhoDoesntFollowYou/insta_main.py")
cards = st.Page("FlashcardAutomation/flashcard_main.py")
casino = st.Page("Casino/casino_main.py")

# Navigation links to main project pages
st.navigation(
        {
            "Insta": [insta],
            "Cards": [cards],
            "Casino": [casino],
        }
    ).run()

