import streamlit as st
#streamlit run sl1.py
st.set_page_config(page_title="About Us", layout="centered")
page_title="About Us"
layout="centered"
#st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("About Us")
st.write("This app is created by the World Music Foundation to share music and uplift local businesses.")


# Learn More
st.markdown("---")

with st.expander("Learn more about us and our goals"):
    st.write("https://theworldmusicfoundation.org/")

