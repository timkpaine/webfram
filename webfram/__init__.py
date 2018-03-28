import configparser
import sys
import json
# import ujson
from flask import Flask, render_template
from .loader import read_state

app = Flask(__name__, static_url_path='/static')


def main():
    site = sys.argv[-1]
    site = 'test' if site == 'run.py' or site == 'webfram:app' else site

    c = configparser.ConfigParser()
    c.read('./sites/%s/%s.cfg' % (site, site))

    site_data = c
    states = read_state('./sites/%s/states.csv' % site)

    @app.route('/index')
    @app.route('/')
    @app.route('/home')
    def site():
        c = site_data
        render = {}
        imports = json.loads(c.get('main', 'imports'))
        blocks = json.loads(c.get('main', 'blocks'))

        render['site'] = site
        render['imports'] = imports
        render['blocks'] = blocks
        render['title'] = c.get('main', 'title')
        render['name'] = c.get('main', 'name')
        render['keywords'] = c.get('main', 'keywords')
        render['favicon'] = c.get('main', 'favicon')
        render['adsense'] = c.get('main', 'adsense')
        render['analytics'] = c.get('main', 'analytics')

        return render_template("index.html", **render)

    @app.route('/<state>')
    @app.route('/<state>/')
    def site_states(state=None):
        c = site_data
        vals = states.get(state, [])
        render = {}
        render['site'] = site
        render['title'] = c.get('main', 'title')
        render['name'] = c.get('main', 'name')
        render['favicon'] = c.get('main', 'favicon')
        render['keywords'] = c.get('main', 'keywords')
        render['vals'] = vals
        render['adsense'] = c.get('main', 'adsense')
        render['analytics'] = c.get('main', 'analytics')
        return render_template("state.html", **render)


main()
