import tweepy

CONSUMER_KEY = "5yldnPCK8iE4k0RXicumhkmat"
CONSUMER_SECRET_KEY = "vbiNEWWvpDWIDK0ibHAiGrXTrpObtyWcBzE5aMR2EptLwNTbXy"
ACCESS_TOKEN = "776850846202167296-L26aBmm3AnvpXSVPqtpHuB3bXR1YrB1"
ACCESS_TOKEN_SECRET = "vUvr9RZ5PIalgElMIyfl4iujcUPQvRqzunofPdsNtn2Q4"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

api.update_status("Hello World!")