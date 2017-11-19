from flask import Flask
from flask import render_template


app = Flask(__name__, static_url_path='/static')


@app.route('/index')
@app.route('/')
@app.route('/home')
def index():
    render = {}
    blocks = []
    blocks.append({'title': 'Find Places of Worship in Your Area',
                   'span1': 'Local Church is your reference for places of worship in your local community.',
                   'searchtext':'Search by religious affiliation, state, county, city, or zipcode'})
    blocks.append({'title': 'Section 2', 'span1':'Span 2', 'subtitle': 'Subtitle2', 'span2': 'Span 2 - 2'})
    blocks.append({'title': 'Section 3', 'span1':'Span 3', 'subtitle': 'Subtitle3', 'span2': 'Span 3 - 2'})

    render['blocks'] = blocks
    render['title'] = 'Local Church'
    return render_template("index.html", **render)
