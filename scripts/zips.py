import csv


def parseZips(filename):
    al = []
    with open(filename, 'r') as fp:
        r = csv.DictReader(fp)
        for item in r:
            al.append(item)

    zipmap = {}
    zipsbystate = {}
    allzips = []
    for d in al:
        zipmap[d['Zip Code']] = d
        state = d['State Abbreviation']
        if state not in zipsbystate:
            zipsbystate[state] = [d['Zip Code']]
        else:
            zipsbystate[state].append(d['Zip Code'])
        allzips.append(d['Zip Code'])

    assert(len(allzips) == len(set(allzips)))

    return zipmap, zipsbystate, allzips
