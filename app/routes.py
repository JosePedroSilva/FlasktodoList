from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    notes = ['Note 1', 'Note 2', 'Note 4']
    return render_template('index.html', notes=notes)