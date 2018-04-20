import requests
import json
import os

#imports the file storing my api keys
#the os.pathabspath function broke the page online and took the most time to find a soulution
script_path = os.path.dirname(os.path.abspath( __file__ ))
api_file = os.path.join(script_path, "api_file.txt")
#assigns the json to a dict
api_keys = {}
#this loop parses the keys
with open(api_file, 'r') as file:
    api_keys = json.loads(file.read())

#assigns the keys to their own variables
tmdb_key = api_keys['tmdb_key']
nyt_key = api_keys['nyt_key']


class Search(object):
    def __init__(self, title=None):
        self.title = title

    #method for searching the movie database
    @classmethod
    def tmdb_info(self, title):
        parameters = {"api_key": tmdb_key, "language": 'en-us', "query": title}
        response = requests.get("https://api.themoviedb.org/3/search/movie?", params=parameters)
        data = response.json()
        data = data['results']
        return data

    #method for searching the nyt reviews database
    @classmethod
    def nytinfo(self, title):
        parameters = {"api-key": nyt_key, "query": title}
        response = requests.get("https://api.nytimes.com/svc/movies/v2/reviews/search.json", params=parameters)
        nytdata = response.json()
        nytdata = nytdata['results']
        return nytdata

    #this method searches tmdb for credit information I was never able to integrate this fully
    #the method works I just could never figure out how to move the movie id back and forth from the html template
    #or how to call a function from within the template
    #aparently this is possible I just couldn't figure out the proper structure for the code I think
    @classmethod
    def tmdb_credits(self, movie_id):
        parameters = {"api_key": tmdb_key}
        url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + str('/credits?')
        response = requests.get(url, params=parameters)
        credits = response.json()
        return credits

    #validates a search term
    def valid_search(self):
        title = self.title
        if title is not None:
            return title == title
        return False


