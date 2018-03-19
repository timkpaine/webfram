import os.path
import requests
from bs4 import BeautifulSoup
from base64 import b64encode
import pandas as pd


bb = b"r\x8b\xa7\xb7*\x1f~'\x1e"
base = 'http://www.' + b64encode(bb).decode() + '.org'

w = BeautifulSoup(requests.get(base).text, 'html5lib')
x = w.findAll('div', {'class': 'browse-by-office'})[0].findAll('a')


res = {}

sublinks = {}
for a in x:
    sublinks[a['href'][1:-1]] = base + a['href']

print('stage1')
# sublinks = {'airport': sublinks['airport']}  # TODO

for cat in sublinks:
    res[cat] = {}
    s = BeautifulSoup(requests.get(sublinks[cat]).text, 'html5lib')
    states = s.findAll('div', {'class': 'list-group geo-major'})[0].findAll('a')
    sublinks[cat] = []
    for statelink in states:
        sublinks[cat].append(statelink['href'])
        res[cat][statelink['href'][1:-1]] = {}

print('stage2')

for cat in sublinks:
    l = sublinks[cat]
    sublinks[cat] = {}
    for statelink in l:
        res[cat][statelink[1:-1]] = {}
        c = BeautifulSoup(requests.get(base + statelink).text, 'html5lib')
        counties = c.findAll('div', {'class': 'list-group geo-major'})[0].findAll('a')
        sublinks[cat][statelink] = []
        for countylink in counties:
            sublinks[cat][statelink].append(countylink['href'])
            res[cat][statelink[1:-1]][countylink['href'][1:-1]] = {}

print('stage3')

span_properties = ['streetAddress', 'addressLocality', 'addressRegion', 'postalCode']
a_properties = ['telephone']
for cat in sublinks:
    for statelink in sublinks[cat]:
        for countylink in sublinks[cat][statelink]:
            res[cat][statelink[1:-1]][countylink[1:-1]] = []
            listings = BeautifulSoup(requests.get(base + countylink).text, 'html5lib').findAll('p', {'class': 'condensed-listing'})
            for listing in listings:
                res[cat][statelink[1:-1]][countylink[1:-1]].append({})
                res[cat][statelink[1:-1]][countylink[1:-1]][-1]['name'] = listing.findAll('a', {'class': 'name'})[0].text
                for item in span_properties:
                    found = listing.findAll('span', {'itemprop': item})
                    if found:
                        res[cat][statelink[1:-1]][countylink[1:-1]][-1][item] = found[0].text or found[0].get('content', '')
                for item in a_properties:
                    found = listing.findAll('a', {'itemprop': item})
                    if found:
                        res[cat][statelink[1:-1]][countylink[1:-1]][-1][item] = found[0].text


for item in res:
    dat = res[item]
    data = []

    for k1 in dat:
        for k2 in dat[k1]:
            for k3 in dat[k1][k2]:
                k3['state'] = k1.split('-')[0]
                k3['county'] = k2.split('-')[1]
                data.append(k3)

    df = pd.DataFrame(data)
    df.to_csv(os.path.join('data_out', item), index=False)

print('stage4')
