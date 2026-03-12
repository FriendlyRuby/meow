import requests


def get_ongoing():

    url = "https://api.jikan.moe/v4/seasons/now"
    r = requests.get(url).json()

    result = []

    for anime in r["data"][:10]:

        title = anime["title"]
        score = anime["score"]
        url = anime["url"]

        result.append((title, score, url))

    return result