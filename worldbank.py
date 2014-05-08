#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import json
import geonamescache
import wbfixes
import argparse

from collections import defaultdict

parser = argparse.ArgumentParser(description='Convert CSV to JSON for dataviz.')
parser.add_argument('csv', help='Source CSV file')
args = parser.parse_args()

# used for checks
gc = geonamescache.GeonamesCache()
countries_by_iso = gc.get_dataset_by_key(gc.get_countries(), 'iso3')
continents = gc.get_continents()

# recent years with most comprehensive datasets
# convert to strings to be able to get field position
years = [r for r in range(1990, 2013)]

# dict keyed by year containing country info
countries = {}

def get_float(val):
    if '' == val:
        return None
    return float(val)

with open(args.csv, 'rb') as f:
    r = csv.reader(f)
    headings = r.next()
    for row in r:
        iso = wbfixes.get_iso(row[1])
        if not iso: continue

        indicator = row[2]
        indicatorid = row[3]

        region = continents[countries_by_iso[iso]['continentcode']]['name']

        if iso not in countries:
            countries[iso] = {
                'name': row[0],
                'region': region,
            }
        # data per year starts with column index 4
        countries[iso][indicatorid] = zip(years, map(get_float, row[4:-1]))

with open('nations.json', 'w') as f:
    json.dump([v for i, v in countries.items()], f)
