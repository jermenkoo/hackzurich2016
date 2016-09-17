import csv
import json
import os
import time

KEYS = ["Recorded_at", "Latitude", "Longitude", "Value"]

def knots_to_kmh(speed, rounding=True):
	if not isinstance(speed, (int, float)):
		speed = float(speed)
	return round((1.852 / 1000) * speed, [100, 2][rounding])

# iterate through all .json files in folder
def my_amazing_function():
	for dirpaths, dnames, fnames in os.walk(os.path.join(os.getcwd(), 'amagdata')):
		for filename in fnames:
			if 'csv' in filename:

				with open(os.path.join(dirpaths, filename)) as csvfile:
					print("[*] parsing {}".format(filename))
					reader = csv.DictReader(csvfile)
					
					rows = [row for row in reader if row['Field'] == 'GPS_SPEED']
					
					triples = [tuple(entry[key] for key in KEYS) for entry in rows]
					triples = [(dt, lat, lon, knots_to_kmh(spd)) for (dt, lat, lon, spd) in triples]

					yield analyse(triples)

def analyse(values):
	dang = []
	for idx in range(1, len(values), 1):
		if values[idx - 1][3] < 10.0:
			continue
		elif values[idx][3] > 3 * values[idx - 1][3]:
			dang += [values[idx]]
	return dang

def dangerous():
	for value in my_amazing_function():
		yield value
		time.sleep(5)