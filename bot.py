import requests as r
import time
import tweepy

from reporter import *
from translator import translate

CONSUMER_KEY = "5yldnPCK8iE4k0RXicumhkmat"
CONSUMER_SECRET_KEY = "vbiNEWWvpDWIDK0ibHAiGrXTrpObtyWcBzE5aMR2EptLwNTbXy"
ACCESS_TOKEN = "776850846202167296-L26aBmm3AnvpXSVPqtpHuB3bXR1YrB1"
ACCESS_TOKEN_SECRET = "vUvr9RZ5PIalgElMIyfl4iujcUPQvRqzunofPdsNtn2Q4"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

result = dangerous()

while True:
	for danger in result:
		if danger:
			for crap in danger:
				try:
					_, *rest = crap
					print("[*] parsing maximum speeds...")
					lat, lon, _ = map(float, rest)

					URL = "http://www.overpass-api.de/api/xapi?*[maxspeed=*][bbox={},{},{},{}]"
					URL = URL.format(lon, lat, lon + 0.005, lat + 0.005)

					try:
						resp = r.get(URL).text
					except:
						pass

					try:
						speed = int(resp.split('k="maxspeed" v=')[1].split("/>")[0][1:-1])
					except Exception:
						speed = 50

					rest = list(map(float, rest))

					status = "Dangerous driving detected: coord: {} {} spd: {} km/h!".format(*rest)
					if rest[-1] > speed:
						status += " Speed exceeded by: {} km/h!".format(round(rest[-1] - speed, 2))

					status = translate(status)

					print("[*] trying to update status...")
					api.update_status(status.replace(',', '.'))
					exit()
				except Exception:
					print("[!] Exception has occured! Sleeping for 5 seconds!")
				time.sleep(5)
