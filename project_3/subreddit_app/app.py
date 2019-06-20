import flask
from model import LemmaTokenizer, classify_text
from joblib import load
import numpy as np

# ----- CONFIG -----#
app = flask.Flask(__name__)  # initialise Flask app var
app.config['DEBUG'] = True


# ----- ROUTES -----#
@app.route("/", methods= ["GET", "POST"])
def home():
    '''Gets prediction using the HTML form'''
    if flask.request.method == 'POST':
        reddit_text = flask.request.form.get('reddit_text')
        if reddit_text:
            score = classify_text(reddit_text, mdl)
            results = {'class 1': score[0, 1], 'class 0': score[0, 0]}
            return flask.jsonify(result=results)
        else:
            return flask.jsonify(result='Input needed')

    return flask.render_template('index.html')


# ----- MAIN SENTINEL -----#
if __name__ == '__main__':
    mdl = load('../model/tfidf_lr.joblib')
    app.run()
