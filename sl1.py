import streamlit as st
#streamlit run sl1.py
st.title("About Us")
st.write("This app is created by the World Music Foundation to share music and uplift local businesses.")

# Learn More
st.markdown("---")
st.subheader("WMF")

with st.expander("Learn more about us and our goals"):
    st.markdown("**1. Hangry Cluck**")
    st.markdown("**1. Tea yard**")

about_page = st.Page(
    page="pages/1_about.py",
    title="About Us",
    icon=":material/density_medium:",

)
drinks_page = st.Page(
    page="pages/2_drinks.py",
    title="Drinks",
    icon=":material/coffee:",
)

# Navigation Setup
pg = st.navigation(pages=[about_page, drinks_page])

# Run Navigation
pg.run()
