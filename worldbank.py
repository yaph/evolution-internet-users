# -*- coding: utf-8 -*-
import csv, json, geonamescache, wbfixes
from collections import defaultdict

# used for checks
gc = geonamescache.GeonamesCache()
countries_by_iso = gc.get_dataset_by_key(gc.get_countries(), 'iso3')
continents = gc.get_continents()

# recent years with most comprehensive datasets
# convert to strings to be able to get field position
years = [r for r in range(1990, 2012)]

# dict keyed by year containing country info
countries = {}

def get_float(val):
    if '' == val:
        return None
    return float(val)

with open('internet-users-gdp-population.csv', 'rb') as f:
    r = csv.reader(f)
    headings = r.next()
    for row in r:
        iso = wbfixes.get_iso(row[1])
        if iso is None: continue

        indicator = row[2]
        indicatorid = row[3]

        region = continents[countries_by_iso[iso]['continentcode']]['name']

        if iso not in countries:
            countries[iso] = {
                'name': row[0],
                'region': region,
            }
        countries[iso][indicatorid] = zip(years, map(get_float, row[4:-1]))

with open('nations.json', 'w') as f:
    json.dump([v for i, v in countries.items()], f)
