
from urllib import *
import json
import requests
from yellauth import *
import pprint

API_KEY= 'gaoLv6PFU7nmgHAy2b2d7TVGrEzb5hSKbHZBpS-KIrZAgkkhtOtTJClZbYWKvNPaJXbd4l43Q-7h4SvAJJ-Zbs2BJ4IZ3AILc6-cwQS7hL4M_6LM4ikR1Qajs7j3WXYx'

API_HOST = 'https://api.yelp.com'

SEARCH_PATH = '/v3/businesses/search'

#auth = Auth()

alocation = raw_input("What city and state would you like to search in?")
aterm = raw_input("Would you like to search for breakfast, lunch, or dinner?")

#auth = Auth.automa(host=API_HOST, path=SEARCH_PATH, api_key=API_KEY)

def business_search(api_key, term, location):

    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """
    url_params = {
    'term': term.replace(' ', '+'),
    'location': location.replace(' ', '+'),
    'limit': 2
    }

    #data = (auth)
    #otdata = json.loads(data)
    #str_data = json.dumps(otdata)
    #reply = auth.automa()
    #return auth(API_HOST, SEARCH_PATH, API_KEY, params=url_params)


"""
def selection(yellauth, user_search):
    if term == "breakfast":
        return (yellauth.automa(yellauth.API_HOST, yellauth.SEARCH_PATH, yellauth.API_KEY, url_params=url_params) )

    yellauth.automa(yellauth.API_HOST, yellauth.API_KEY, url_params=url_params)

"""

#doink = user_search(API_KEY, aterm, alocation )
