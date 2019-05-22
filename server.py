from flask import Flask
from random import randint
from flask import render_template
from flask import request
import model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll-dice')
def ada_page():
    return render_template('roll_dice.html', __diceroll__ = str(randint(1,6)))

@app.route('/form')
def form():
    return render_template('form_1.html')

@app.route('/process', methods=['POST'])
def process_form():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '
    if title != '':
        greeting += title + ' '
    if name != '':
        greeting += name

    return render_template('results.html', greeting=greeting)


@app.route('/spamalam')
def spam_detector():
    return render_template('spam_form.html')

@app.route('/MMMM_PROCESSING_SPAAM', methods=["POST"])
def process_spam():
    submission = request.form["mess"]
    prediction = model.predict(submission)
    prediction = 'yr message looks like ' + prediction

    return render_template('spam_output.html', prediction=prediction, submission=submission)
