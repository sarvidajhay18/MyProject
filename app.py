from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from st_on_hover_tabs import on_hover_tabs

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
lottie_coding = load_lottieurl("https://lottie.host/a796d5ff-a73b-41c8-acd6-0628114760e7/jRTduUF2dv.json")
img_project1 = Image.open("images/Scouts.png")
img_lottie_animation = Image.open("images/Rank.png")

# --- Side Bar Section ---
with st.sidebar:
        tabs = on_hover_tabs(tabName=['Home', 'Project' ,'About', 'Contact'], 
                             iconName=['home', 'link', 'info', 'mail'],
                             styles = {'navtab': {'background-color':'#1e7aea',
                                                  'color': '#fcfcfc',
                                                  'font-size': '18px',
                                                  'transition': '1s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'
                                                  },
                                       'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                      'cursor': 'pointer'}
                                                          },
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'
                                                   },
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'
                                                    }
                                        },
                             key="1" ,default_choice=0)

# --- Home Section ---
if tabs =='Home':
    with st.container():
        column_left, column_right = st.columns((2,1))
        with column_left:
            st.write("---")
            st.title("Welcome To My Home Page")
            st.subheader("hi, I am Jhay-r C. Sarvida :wave:")
            st.write("I am a Computer Engineering students from SNSU")
            st.write("Visit my github link below to learn about my work.")
            st.write("[Github Link Here](https://github.com/sarvidajhay18/MyProject)")
        with column_right:
            st_lottie(lottie_coding, height=300, key="coding")

# --- Projects Section ---
elif tabs == 'Project':
    with st.container():
        st.write("---")
        st.header("My Project")
        st.write("##")
        image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
        with image_column:
            # insert image
            st.image(img_project1)
        with text_column:
            st.subheader("Snake Game App")
            st.write(
                """ 
                This is a Snake Game App made in Python. 
                """
                """ 
                This web app is not fully finish. 
                """
                """
                This is a sample for fun web app only. 
                """
            )
            st.markdown("[Github Link](https://github.com/sarvidajhay18/MyProject)")
    with st.container():
        image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
        with image_column:
            st.image(img_lottie_animation) # insert image
        with text_column:
            st.subheader("How to add a contact form in your Streamit App")
            st.write(
                """
                Want to add a contact form to your streamlit website.
                In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service 'Form Submit'.
                """
            )
            st.markdown("[Watch Here](https://youtu.be/FOULV9Xij_8)")

# --- About Section ---
elif tabs == 'About':
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((2,1))
        with left_column:
            st.header("About Me")
            st.write("##")
            st.write("I am a computer engineering student in Surigao del Norte State University.")
            st.write("I am currently studying Python, Java, Html and css.")

# --- feedback Section ---
elif tabs == 'Contact':
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((2,1))
        with left_column:
            st.header("Get in Touch With Me!")
            st.write("##")
  # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/jhaysarvida@gmail.com" method="POST">
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

