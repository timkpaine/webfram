import configparser
import os
import ujson
from flask import Flask
from flask import render_template


app = Flask(__name__, static_url_path='/static')


def main():
    sites = {}
    for site in os.listdir('sites'):
        c = configparser.ConfigParser()
        c.read('./sites/%s/%s.cfg' % (site, site))
        sites[site] = c

    @app.route('/<site>')
    def site(site='church'):
        c = sites[site]
        render = {}
        imports = ujson.loads(c.get('main', 'imports'))
        blocks = ujson.loads(c.get('main', 'blocks'))

        render['imports'] = imports
        render['blocks'] = blocks
        render['title'] = c.get('main', 'title')
        render['favicon'] = c.get('main', 'favicon')

        return render_template("index.html", **render)

    @app.route('/<site>/<state>')
    def site_states(site='church', state=None):
        c = sites[site]
        render = {}
        render['title'] = c.get('main', 'title')
        render['favicon'] = c.get('main', 'favicon')
        return render_template("state.html", **render)

    @app.route('/index')
    @app.route('/')
    @app.route('/home')
    def index():
        c = sites['church']
        render = {}
        imports = ujson.loads(c.get('main', 'imports'))
        blocks = ujson.loads(c.get('main', 'blocks'))
        render['imports'] = imports
        render['blocks'] = blocks
        render['title'] = c.get('main', 'title')
        render['favicon'] = c.get('main', 'favicon')
        return render_template("index.html", **render)

    @app.route('/<state>')
    def states(state=None):
        c = sites['church']
        render = {}
        render['title'] = c.get('main', 'title')
        render['favicon'] = c.get('main', 'favicon')
        return render_template("state.html", **render)

main()
