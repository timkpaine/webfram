import requests
from bs4 import BeautifulSoup
from base64 import b64encode


bb = b"r\x8b\xa7\xb7*\x1f~'\x1e"
base = 'http://www.' + b64encode(bb).decode() + '.org'

w = BeautifulSoup(requests.get(base).text, 'html5lib')
x = w.findAll('div', {'class': 'browse-by-office'})[0].findAll('a')


res = {}

sublinks = {}
for a in x:
    sublinks[a['href'][1:-1]] = base + a['href']


# sublinks = {'airport': sublinks['airport']}  # TODO

for cat in sublinks:
    res[cat] = {}
    s = BeautifulSoup(requests.get(sublinks[cat]).text, 'html5lib')
    states = s.findAll('div', {'class': 'list-group geo-major'})[0].findAll('a')
    sublinks[cat] = []
    for statelink in states:
        sublinks[cat].append(statelink['href'])
        res[cat][statelink['href'][1:-1]] = {}


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


span_properties = ['streetAddress', 'addressLocality', 'addressRegion', 'postalCode']
a_properties = ['telephone']
for cat in sublinks:
    for statelink in sublinks[cat]:
        for countylink in sublinks[cat][statelink]:
            res[cat][statelink[1:-1]][countylink[1:-1]] = []
            listings = BeautifulSoup(requests.get(base + countylink).text, 'html5lib').findAll('p', {'class': 'condensed-listing'})
            for listing in listings:
                res[cat][statelink[1:-1]][countylink[1:-1]].append({})
                for item in span_properties:
                    found = listing.findAll('span', {'itemprop': item})
                    if found:
                        res[cat][statelink[1:-1]][countylink[1:-1]][-1][item] = found[0].text or found[0].get('content', '')
                for item in a_properties:
                    found = listing.findAll('a', {'itemprop': item})
                    if found:
                        res[cat][statelink[1:-1]][countylink[1:-1]][-1][item] = found[0].text

print(res)
