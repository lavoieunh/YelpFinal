import oauth2 as oauth
from urllib import *
import requests

"""
APIKEY = ''

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
SEARCH_LIMIT = 3
"""

class Auth():

#alias = input('')
    PATH = '/v3/categories/alias'
    #NEW_PATH = PATH.append(alias)

# Defaults for our simple example.
#DEFAULT_TERM = 'dinner'
#DEFAULT_LOCATION = 'San Francisco, CA'
#SEARCH_LIMIT = 3

    def __init__(self, host, path, api_key, url_params=None):
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

        self.host = host
        self.path = path
        self.api_key = api_key
        self.url_params = url_params or {}
        url = '{0}{1}'.format(host, quote(path.encode('utf8')))
        headers = {
            'Authorization': 'Bearer %s' % api_key,
        }


        print(u'Querying {0} ...'.format(url))

        response = requests.request('GET', url, headers=headers, params=url_params)

        return(response.json())


    def search(self, api_key, term, location):
        """
        Query the Search API by a search term and location.
        Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
        Returns:
        dict: The JSON response from the request.
        """

        self.api_key = api_key
        self.term = term
        self.location = location

        url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
        }
        return requests(API_HOST, SEARCH_PATH, API_KEY, url_params=url_params)

authtest = Auth()
#authtest.request(API_HOST, SEARCH_PATH, APIKEY)
dog = authtest.search( "taco bell", "Boston, MA")
print(dog)
#authtest.search(API_HOST, APIKEY, SEARCH_PATH)
