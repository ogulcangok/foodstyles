from flask import Flask, request
import spacy
app = Flask(__name__)


@app.route('/api/v1/get-entities',methods =["POST"])
def hello_world():  # put application's code here
    recipes = request.get_json()
    nlp_ner = spacy.load("model/model-best")
    result = {}
    for i, text in recipes.items():
        doc = nlp_ner(text)
        result[i] = [(ent.text, ent.start, ent.end) for ent in doc.ents]

    return result


if __name__ == '__main__':
    app.run()
