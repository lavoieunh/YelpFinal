import json
import argparse
import pprint
import requests
import flask
from urllib2 import HTTPError
from urllib import quote
from urllib import urlencode

app = flask.Flask(__name__)   # create our flask app


API_KEY= ''
API_HOST = 'https://api.yelp.com'

BIZ_PATH = '/v3/businesses/search/'

PHONE_PATH = '/v3/businesses/search/phone'

input_location = "Boston, MA"
foodinput = raw_input("What food you want there? ")

SEARCH_PATH="{0}{1}".format(BIZ_PATH, input_location)

USER_PHONE = raw_input("What phone number would you like to search for? ")

PHONE_NUMBER = "+1{}".format(USER_PHONE)

SEARCH_PHONE = "{0}{1}".format(PHONE_PATH, PHONE_NUMBER)

#autho = yellauth.Auth()
#aut = auth.automa(host=API_HOST, path=SEARCH_PATH, api_key=API_KEY)

def auth(host, path, api_key, url_params=None):
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

client = auth


@app.route('/business')

def business_query(api_key=API_KEY, path=foodinput, url_params=None):

        #input_location = "Boston, MA"
        #input_term = raw_input("Would you like to search for breakfast, lunch, or dinner?")
        #location = location
        url_params = {
            foodinput,
            input_location
        }

        #respone = auth(API_KEY, path, )
        return auth(host=API_HOST, path=SEARCH_PATH, api_key=API_KEY, url_params=url_params)



@app.route('/phonenumber')
def phone_number_query(host=API_HOST, path=PHONE_PATH, api_key=API_KEY, url_params=None):
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

    url_params = {
        PHONE_PATH
            }

    print(u'Querying {0} ...'.format(url))

    return auth(host=API_HOST, path=PHONE_PATH, api_key=API_KEY, url_params=url_params)

#query = business_query()
#phone = phone_number_query()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
