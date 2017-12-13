import configparser
import os
import ujson
from flask import Flask, render_template, redirect


app = Flask(__name__, static_url_path='/static')


def main():
    sites = {}
    for site in os.listdir('sites'):
        c = configparser.ConfigParser()
        c.read('./sites/%s/%s.cfg' % (site, site))
        sites[site] = c

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
        render = {}
        render['site'] = site
        render['title'] = c.get('main', 'title')
        render['favicon'] = c.get('main', 'favicon')
        return render_template("state.html", **render)

    @app.route('/index')
    @app.route('/')
    @app.route('/home')
    def index():
        return redirect("./church", code=302)

main()
