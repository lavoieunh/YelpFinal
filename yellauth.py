import json
import pprint
import requests

#url = '{0}{1}'.format(host, quote(path.encode('utf8')))

#url_params = url_params or {}



class Auth(object):

    def automa(self, host, path, api_key, url_params=None):
        url_params = url_params or {}
        url = '{0}{1}'.format(host, quote(path.encode('utf8')))
        headers = {
            'Authorization': 'Bearer %s' % api_key,
        }
        return

