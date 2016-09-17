import json
import requests as r

BASE_URL = "https://www.googleapis.com/language/translate/v2?key={}&q={}&source={}&target={}"
GOOGLE_TRANSLATE_API_KEY = 'AIzaSyCfzt6Z5S_e0sTjaZNUOL9tT3BoeEHUSCQ'

def translate(text, src_lang='en', tgt_lang='en'):
	if tgt_lang != 'en':
		REQ_URL = BASE_URL.format(GOOGLE_TRANSLATE_API_KEY, text, src_lang, tgt_lang)
		
		translation = r.get(REQ_URL).text
		translation = json.loads(translation)

		return translation['data']['translations'][0]['translatedText']
	return text
