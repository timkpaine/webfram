import csv
STATES = {
'AL':'alabama',
'AK': 'alaska',
'AZ': 'arizona',
'AR': 'arkansas',
'CA': 'california',
'CO': 'colorado',
'CT': 'connecticut',
'DE': 'delaware',
'DC': 'dc',
'FL': 'florida',
'GA': 'georgia',
'HI': 'hawaii',
'ID': 'idaho',
'IL': 'illinois',
'IN': 'indiana',
'IA': 'iowa',
'KS': 'kansas',
'KY': 'kentucky',
'LA': 'louisiana',
'ME': 'maine',
'MD': 'maryland',
'MA': 'massachusetts',
'MI': 'michigan',
'MN': 'minnesota',
'MS': 'mississippi',
'MO': 'missouri',
'MT': 'montana',
'NE': 'nebraska',
'NV': 'nevada',
'NH': 'new-hampshire',
'NJ': 'new-jersey',
'NM': 'new-mexico',
'NY': 'new-york',
'NC': 'north-carolina',
'ND': 'north-dakota',
'OH': 'ohio',
'OK': 'oklahoma',
'OR': 'oregon',
'PA': 'pennsylvania',
'PR': 'puerto-rico',
'RI': 'rhode-island',
'SC': 'south-carolina',
'SD': 'south-dakota',
'TN': 'tennessee',
'TX': 'texas',
'UT': 'utah',
'VM': 'vermont',
'VA': 'virginia',
'WA': 'washington',
'WV': 'west-virginia',
'WI': 'wisconsin',
'WY': 'wyoming'}

def read_state(f):
    ret = {k:[] for k in STATES.values()}
    with open(f, 'r') as fp:
        c = csv.DictReader(fp)
        for row in c:
            row['state'] = STATES[row['state']]
            ret[row['state']].append(row)
    return ret
