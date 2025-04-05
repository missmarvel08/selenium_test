import requests

API_KEY = "YOUR_GOOGLE_TRANSLATE_API_KEY"
TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2"

def translate_text(text, target_lang="en"):
    params = {
        "q": text,
        "target": target_lang,
        "key": API_KEY
    }
    response = requests.post(TRANSLATE_URL, data=params)
    return response.json()["data"]["translations"][0]["translatedText"]