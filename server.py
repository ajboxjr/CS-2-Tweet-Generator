from flask import Flask
app = Flask(__name__)
from sampling import *
from histogram import *
text = handle_input('text.txt')
histogram = Histogram(text)

@app.route('/<question_id>')
def hello_world(question_id):
    return str([stochastic_sample(histogram) for _ in range(int(question_id))])
