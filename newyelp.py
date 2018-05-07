import yellauth
import search
import json
import argparse
#import sys
#from urllib.error import HTTPError
import pprint
#from classearch import *

#API_KEY= 'gaoLv6PFU7nmgHAy2b2d7TVGrEzb5hSKbHZBpS-KIrZAgkkhtOtTJClZbYWKvNPaJXbd4l43Q-7h4SvAJJ-Zbs2BJ4IZ3AILc6-cwQS7hL4M_6LM4ikR1Qajs7j3WXYx'

#API_HOST = 'https://api.yelp.com'

#SEARCH_PATH = '/v3/businesses/search'

#auth = Auth()

input_location = "Boston, MA"
input_term = raw_input("Would you like to search for breakfast, lunch, or dinner?")
#location = location
reach = user_search

#alocation = "Boston, MA"
#aterm = input("Would you like to search for breakfast, lunch, or dinner?")

auth = Auth.automa(host=API_HOST, path=SEARCH_PATH, api_key=API_KEY)

def yelpquery(authentication, location, term):
    return(input)
