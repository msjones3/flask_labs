from flask import *
app = Flask(__name__)
app.secret_key = 'thisisasecret'


@app.route('/')
def index():
    # flash a message that says "hello!"
    flash('hello!')
    return render_template('flash.html')


app.run(debug=True)