import csv


def parseCounties(filename):
    al = []
    with open(filename, 'r') as fp:
        r = csv.DictReader(fp)
        for item in r:
            al.append(item)

    return al
