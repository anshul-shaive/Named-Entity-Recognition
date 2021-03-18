import app1
import app2
import streamlit as st
PAGES = {
    "From_API": app1,
    "Direct": app2
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()