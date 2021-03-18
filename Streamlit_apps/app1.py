import streamlit as st
import requests
import wikipedia
import spacy

def app():
    user_input = st.text_input("Enter wikipedia page name", "Sebastian_Thrun")
    api_call=requests.get("http://wikipedia-ner-app.herokuapp.com/get_wiki_ner?wiki_page="+user_input).json()

    st.write(api_call['NER_data'], unsafe_allow_html=True)