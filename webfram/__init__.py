from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/index')
@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")
