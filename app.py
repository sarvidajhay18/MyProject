from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local Css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
local_css("style/style.css")

# --- Load Assets ---
lottie_coding = load_lottieurl("https://lottie.host/6eeeaac3-110b-46f6-b949-b85a3977add6/GaWiYaYx0A.json")
img_contact_form = Image.open("images/webpageImage.png")
img_lottie_animation = Image.open("images/webpageImage2.png")

# --- Header Section ---
with st.container():
    st.title("This is my sample webpage")
    st.subheader("Hi :wave:, I am Jhay-r C. Sarvida")
    st.write("I am a Computer Engineering students from SNSU")
    st.write("[Github Link Here](https://github.com/YourEnemy1)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write("""
            I am a computer engineering student in Surigao del Norte State University.
            - This is a sample webpage only.
            - This is not a final project.
            - I'm going to finish this soon.
        """)
        st.write("For the meantime you can watch this youtube video to learn more about how to make a webpage!")
        st.write("[Youtube](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")

# --- Project ---

with st.container():
    st.write("---")
    st.header("My Project")
    st.write("##")
    image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
    with image_column:
        # insert image
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animation Inside Your Streamit App")
        st.write(
            """
            Learn how to use lottie files in streamlit!
            Animations make our web app more engaging and fun, and lottie files is the easiest way to do it.
            In this tutorial, I'll show you exactly how to do it.
            """
        )
        st.markdown("[Watch Here](https://youtu.be/TXSOitGoIne)")

with st.container():
    image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
    with image_column:
        st.image(img_contact_form) # insert image
    with text_column:
        st.subheader("How to add a contact form in your Streamit App")
        st.write(
            """
            Want to add a contact form to your streamlit website.
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service 'Form Submit'.
            """
        )
        st.markdown("[Watch Here](https://youtu.be/FOULV9Xij_8)")

# --- Contact Form ---
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/comekhazee2017@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()