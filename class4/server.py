from flask import Flask, render_template
import sys  
from markov import *


marky = Markov()
app = Flask(__name__)

@app.route('/')
@app.route('/<int:number>')
def index(number=None):
    return render_template('home.html', sentence=number)

if __name__ == '__main__':
    app.run(debug=True)
