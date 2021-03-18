# Named-Entity-Recognition

Scraped data using wikipedia API and used spacy to perform NER(Named Entity Recognition) <br/>

Created a flask api that takes a wikipedia page name, scraps the data using wikipedia-api, perform NER using spacy and sends the annotated output to a streamlit app.<br/>

Streamlit app has two options(use the navigation menu at left side): <br/>
1. To use the flask-api from above and display that in app.

2. To directly perform NER in streamlit app itself using spacy_streamlit library. This option has more features including filter by entities and also better formatting. <br/>

In both options any wikipedia page can be passed in the search bar at the top of page. <br/>

Main streamlit app: https://streamlit-ner-app-as.herokuapp.com/  <br/>

Flask API: http://wikipedia-ner-app.herokuapp.com/get_wiki_ner?wiki_page=Sebastian_Thrun  <br/>
