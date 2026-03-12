import requests

def get_ongoing():

    url = "https://api.jikan.moe/v4/seasons/now"
    r = requests.get(url).json()

    anime_list = []

    for anime in r["data"][:10]:
        anime_list.append(anime["title"])

    return anime_list