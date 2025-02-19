import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="👨‍💻", layout="wide")

st.title("👨‍💻 Welcome to My Portfolio")
st.write("Hello! I'm [Your Name], a software developer. Here are some of my projects:")

insta = st.Page(
    "SeeWhoDoesntFollowYou/insta_main.py", title="Insta")
cards = st.Page("FlashcardAutomation/flashcard_main.py", title="Cards")
casino = st.Page(
    "Casino/casino_main.py", title="Casino")

# Navigation links to main project pages
pg = st.navigation(
        {
            "Insta": [insta],
            "Cards": [cards],
            "Casino": [casino],
        }
    )

pg.run()
