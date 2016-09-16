import csv
import json
import os

avgs = []

# iterate through all .json files in folder
def my_amazing_function():
	for dirpaths, dnames, fnames in os.walk(os.path.join(os.getcwd(), 'amagdata')):
		for filename in fnames:
			if 'csv' in filename:
				
				with open(os.path.join(dirpaths, filename)) as csvfile:
					print("[*] parsing {}".format(filename))
					reader = csv.DictReader(csvfile)
					
					rows = [row for row in reader]
					rows = list(filter(lambda row: row['Field'] == 'GPS_SPEED', rows))
					speeds = [entry['Value'] for entry in rows]
					speeds = list(map(lambda spd: int(spd) * 1.852 / 1000.0, speeds))
					speeds = list(filter(None, speeds))
					speeds = list(map(lambda spd: round(spd, 2), speeds))
					
					avgs.append(max(speeds))

	return round(sum(avgs) / len(avgs), 2)
