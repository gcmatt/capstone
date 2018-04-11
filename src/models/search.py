import requests
import json
import os

script_path = os.path.dirname(os.path.abspath( __file__ ))
api_file = os.path.join(script_path, "api_file.txt")
api_keys = {}
with open(api_file, 'r') as file:
    api_keys = json.loads(file.read())

tmdb_key = api_keys['tmdb_key']
nyt_key = api_keys['nyt_key']


class Search(object):
    def __init__(self, title=None):
        self.title = title


    @classmethod
    def tmdb_info(self, title):
        parameters = {"api_key": tmdb_key, "language": 'en-us', "query": title}
        response = requests.get("https://api.themoviedb.org/3/search/movie?", params=parameters)
        data = response.json()
        data = data['results']
        return data

    @classmethod
    def nytinfo(self, title):
        parameters = {"api-key": nyt_key, "query": title}
        response = requests.get("https://api.nytimes.com/svc/movies/v2/reviews/search.json", params=parameters)
        nytdata = response.json()
        nytdata = nytdata['results']
        return nytdata

    def valid_search(self):
        title = self.title
        if title is not None:
            return title == title
        return False


