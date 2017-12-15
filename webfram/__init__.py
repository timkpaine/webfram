import configparser
import os
import ujson
from flask import Flask, render_template, redirect
from .loader import read_state

app = Flask(__name__, static_url_path='/static')


def main():
    sites = {}
    states = {}
    for site in os.listdir('sites'):
        c = configparser.ConfigParser()
        c.read('./sites/%s/%s.cfg' % (site, site))
        sites[site] = c
        states[site] = read_state('./sites/%s/states.csv' % site)

    @app.route('/<site>')
    @app.route('/<site>/')
    def site(site='church'):
        c = sites[site]
        render = {}
        imports = ujson.loads(c.get('main', 'imports'))
        blocks = ujson.loads(c.get('main', 'blocks'))

        render['site'] = site
        render['imports'] = imports
        render['blocks'] = blocks
        render['title'] = c.get('main', 'title')
        render['favicon'] = c.get('main', 'favicon')

        return render_template("index.html", **render)

    @app.route('/<site>/<state>')
    @app.route('/<site>/<state>/')
    def site_states(site='church', state=None):
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
        return redirect("./church", code=302)

main()
