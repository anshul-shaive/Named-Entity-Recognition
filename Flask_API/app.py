from flask import Flask, request, jsonify
import wikipedia
import spacy
from spacy import displacy
import en_core_web_sm


app = Flask(__name__)
nlp = en_core_web_sm.load()

@app.route('/get_wiki_ner')
def get_wiki_ner():
    page = request.args.get('wiki_page', default = 'Sebastian_Thrun')
    wiki_page = wikipedia.page(page)
    doc = nlp(wiki_page.content)
    ner = displacy.render(doc, style="ent")
    return jsonify({'NER_data': ner})

@app.route('/')
def index():
    return jsonify({"Response": "API for Named Entity Recognition. Use get_wiki_ner route and pass wikipedia page name in wiki_page parameter"})


if __name__ == '__main__':
    app.run(threaded=True, port=5000)