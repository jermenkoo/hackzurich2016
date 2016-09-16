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
					api.update_status("Dangerous driving detected: {}!".format(rest))
					time.sleep(5)
				except Exception as e:
					print("[!] Exception has occured, trying again in 5 seconds!")
					print(e)
					time.sleep(5)
					continue
