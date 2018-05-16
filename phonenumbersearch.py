import yellauth
import json
import argparse
from urllib2 import HTTPError
from urllib import quote
from urllib import urlencode
import pprint
import requests

API_KEY= ''

API_HOST = 'https://api.yelp.com'

phonepath = '/v3/businesses/search/phone/'

user_phone_input = raw_input("What phone number would you like to search for? ")

phonenumber = "+1{}".format(user_phone_input)

SEARCH_PHONE = "{0}{1}".format(phonepath + phonenumber)

def phone_number_query(host=API_HOST, path=SEARCH_PHONE, api_key=API_KEY, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return(response.json())

print(phone_number_query())
#reply = phone_number_query()
#print(reply)

"""
def phone_number_query():

    user_phone_input= raw_input("What phone number would you like to search for? ")

    phonenumber = "+1{}".format(user_phone_input)

    SEARCH_PHONE = phonepath + phonenumber

    SEARCH_PHONE = phonepath + phonenumber

    url_params = url_params or {}
    url = '{0}{1}'.format(API_HOST, quote(.encode('utf8')))
    headers = {
            'Authorization': 'Bearer %s' % api_key,
        }

ps = phone_number_query()
print(ps)
"""
"""
#SEARCH_PHONE = "+1{}".format(input_phone)
authenticate = yellauth.Auth()

auth = authenticate.automa(host=API_HOST, path=SEARCH_PHONE, api_key=API_KEY)
print(u'Querying {0}...'.format(url))
resp = requests.request('GET', url, headers=headers, params=url_params)
print(resp.json())
"""
