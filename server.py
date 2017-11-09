from flask import Flask, render_template
app = Flask(__name__)
from sampling import *
from histogram import *
text = handle_input('text.txt')
histogram = Histogram(text)
weighted_arr = weighted_hist(histogram.tuple)
print(weighted_arr)

@app.route('/<int:population>')
def index():
    return render_template('hello.html', histogram=histogram)

if __name__ == '__main__':
    app.run(debug=True)
