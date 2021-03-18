import streamlit as st
import wikipedia
import spacy
from spacy_streamlit import visualize_ner
def app():
    user_input = st.text_input("Enter wikipedia page name", "Sebastian_Thrun")
    seb_t = wikipedia.page(user_input)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(seb_t.content)
    visualize_ner(doc, labels=nlp.get_pipe("ner").labels)