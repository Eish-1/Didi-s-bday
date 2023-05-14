import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="HAPPYbdayNANDINIdi", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----

img_lottie_animation = Image.open("C:\\Users\\boogi\\Desktop\\Images\\art.jpeg")

# ---- HEADER SECTION ---- streamlit run C:\Users\boogi\Desktop\PYTHON_CWH\app2.py
with st.container():
    st.subheader("Hello! Nandini DI! 👋")
    st.title(" 🎊 HAPPY BIRTHDAY !! 🎊 ")
    st.image(img_lottie_animation)
    st.write("❤  YOU JUST TURNED 21 !! ❤")
    st.write("💙 I am very grateful for your presence , your guidance and ofcourse your smile 💙")
    st.write("🧡 I appreciate you guiding me! it's just my monkey brain still ends doing something else! Will control it from now on!!! 🧡")
    st.write("     ")
    st.write("( and about the pic, Miss.. that's the only one i could find hence i did some jugaad with it..)")