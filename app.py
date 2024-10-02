from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title= "My Webpage", page_icon="😎", layout= "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#Use local CSS
def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")

#Load Assets
lottie_coding = load_lottieurl("https://lottie.host/b66f6e28-c3ad-4271-bad9-f0779187fc88/f1rGaCVCfz.json")
image_contact_frm = Image.open("Image/Slide2.png")
#HEADER SECTION
with st.container():
    st.subheader("Hi, I am Rico :😎")
    st.title("A Social Media Manager From Philippines")
    st.write("I am an aspiring Social Media Manager Ready to Work with you")


#What I Do
with st.container ():
    st.write ("---")
    left_column, right_column = st.columns (2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """ 
                - Create and manage content tailored for startups on LinkedIn
                - Focus on professional branding and increasing engagement
                - Craft compelling posts and articles for visibility
                - Design eye-catching graphics to enhance posts
                - Optimize LinkedIn profiles for better visibility and networking
                - Ensure consistent, high-quality content to boost engagement and connections""")
with right_column:
    st_lottie(lottie_coding, height=450, key="coding")
    #-----Projects------#
with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns(2)
        with image_column:
            st.image(image_contact_frm)
        with text_column:
            st.subheader("Content Making and Graphic Desigining")
            st.write(
                """
                A sample of LinkedIn Post to promote an online remote education system.
           """ )
            
#Contact
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/ricomandao@gmail.com" method="POST"
            <input type="hidden" name="_captcha" value="false">
            <input type="type" name="name" placeholder="Your name" required>
            <input type="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column: 
        st.empty()