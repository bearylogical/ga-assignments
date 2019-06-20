import flask
from model import LemmaTokenizer, classify_text
from joblib import load
import numpy as np

# ----- CONFIG -----#
app = flask.Flask(__name__)  # initialise Flask app var
app.config['DEBUG'] = True

# ----- ROUTES -----#
@app.route("/")
def home():
    return flask.render_template('index.html')


@app.route('/input_page')
def send_form():
    return flask.render_template('input_page.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    '''Gets prediction using the HTML form'''
    if flask.request.method == 'POST':
        inputs = flask.request.form
        reddit_text = str(inputs['reddit_text'])

        score = classify_text(reddit_text, mdl)
        results = {'class 1': score[0, 1], 'class 0': score[0, 0]}
        del(score)
        return flask.jsonify(results)

# ----- MAIN SENTINEL -----#
if __name__ == '__main__':
    mdl = load('../model/tfidf_lr.joblib')
    app.run()
