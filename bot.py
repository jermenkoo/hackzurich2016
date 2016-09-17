import requests as r
import time
import tweepy

from reporter import *

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
		if not danger:
			continue
		else:
			for crap in danger:
				try:
					_, *rest = crap
					print("[*] trying to update status...")
					lat, lon, _ = map(float, rest)

					URL = "http://www.overpass-api.de/api/xapi?*[maxspeed=*][bbox={},{},{},{}]"
					URL = URL.format(lon, lat, lon + 0.01, lat + 0.01)

					resp = r.get(URL).text

					try:
						speed = int(resp.split('k="maxspeed" v=')[1].split("/>")[0][1:-1])
					except Exception:
						speed = 50

					# print(rest, "spd", int(speed))

					status = "Dangerous driving detected: {}!".format(rest)
					if rest[-1] > speed:
						status += " Speed exceeded by: {}".format(rest[-1] - speed)

					api.update_status(status)
					time.sleep(5)
				except Exception as e:
					print("[!] Exception has occured, trying again in 5 seconds!")
					print(e)
					time.sleep(5)
					continue
