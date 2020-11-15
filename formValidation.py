import sqlite3
from flask import Flask, render_template, redirect, url_for, request, flash
app = Flask(__name__)
app.secret_key = 'thisisasecret'


@app.route('/')
def index():
    # just show the main page
    return render_template('validation.html')


@app.route('/form_submission', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
                flash('invalid credentials')
                redirect(url_for('index'))
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))

    return render_template('validation.html')

app.run(debug=True)