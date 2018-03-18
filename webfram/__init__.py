import configparser
import sys
import os
import json
# import ujson
from flask import Flask, render_template, redirect
from .loader import read_state

app = Flask(__name__, static_url_path='/static')


def main():
    sites_allowed = sys.argv[1:] if sys.argv[1:] != ['webfram:app'] else sys.argv[2:]
    sites = {}
    states = {}
    for site in os.listdir('./sites'):
        if sites_allowed and site not in sites_allowed:
            continue
        else:
            c = configparser.ConfigParser()
            c.read('./sites/%s/%s.cfg' % (site, site))
            sites[site] = c
            states[site] = read_state('./sites/%s/states.csv' % site)

    @app.route('/<site>')
    @app.route('/<site>/')
    def site(site='test'):
        c = sites[site]
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

        return render_template("index.html", **render)

    @app.route('/<site>/<state>')
    @app.route('/<site>/<state>/')
    def site_states(site='test', state=None):
        c = sites[site]
        vals = states[site].get(state, [])
        render = {}
        render['site'] = site
        render['title'] = c.get('main', 'title')
        render['favicon'] = c.get('main', 'favicon')
        render['vals'] = vals
        return render_template("state.html", **render)

    @app.route('/index')
    @app.route('/')
    @app.route('/home')
    def index():
        return redirect("./test", code=302)

main()
