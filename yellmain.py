import yellauth
import search
import json
import argparse
import sys
from urllib import *
import pprint
#from classearch import *

#input_location = "Boston, MA"
#input_term = input("Would you like to search for breakfast, lunch, or dinner?")
term = term
location = location
reach = user_search

def main():
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()
    """
    try:
        user_search(term, location)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )

#pprint.pprint(main)

if __name__ == '__main__':
    main()
