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
                   'searchtext': 'Search by affiliation, state, city, or zipcode',
                   'class': 'darkbox',
                   'background': 'church.png'})
    blocks.append({'title': 'Browse', 'span1': 'Browse places of worship by state', 'statelist': True})
    blocks.append({'title': 'Section 3', 'span1': 'Span 3', 'subtitle': 'Subtitle3', 'span2': 'Span 3 - 2', 'class': 'lightbox'})
    blocks.append({'title': 'Section 4', 'span1': 'Span 4', 'subtitle': 'Subtitle4', 'span2': 'Span 4 - 2'})
    blocks.append({'title': 'Section 5', 'span1': 'Span 5', 'subtitle': 'Subtitle5', 'span2': 'Span 5 - 2', 'class': 'clearbox'})
    blocks.append({'title': 'Section 6', 'span1': 'Span 6', 'subtitle': 'Subtitle6', 'span2': 'Span 6 - 2', 'class': 'clearbox'})

    render['blocks'] = blocks
    render['title'] = 'Local Church'
    render['favicon'] = 'favicon.png'

    return render_template("index.html", **render)
