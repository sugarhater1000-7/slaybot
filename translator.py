import requests


def translate(text: str) -> str:

    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {"q": text,
               "target": "ru",
               "source": "en"}
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "KEY",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    translation = response.json()
    translation = translation['data']['translations'][0]['translatedText']

    return translation
