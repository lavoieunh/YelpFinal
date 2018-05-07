
#This works - DO NOT CHANGE
print("Only the /categories/alias is supported at this point. Try entering hotdog as an example ")
alias = input('Please enter your input: ')
HOST_NAME = []

PATH = '/v3/categories/' 
NEW_P = alias
#HOSTNAME = HOSTNAME.append(NEW_PATH)
NEW_PATH = (PATH + NEW_P )


print(NEW_PATH)


"""
###Basis of the above - it allows us to search the path specified

https://api.yelp.com/v3/businesses/{id}

print("Only the /categories/alis is supported at this point. Try entering hotdog as an example ")
alias = input('Please enter your input: ')
HOST_NAME = []

PATH = '/v3/categories/alias' 
NEW_P = alias
#HOSTNAME = HOSTNAME.append(NEW_PATH)
NEW_PATH = (PATH + NEW_P )

https://api.yelp.com/v3/businesses/search?


print(NEW_PATH)
"""


def query_api(term, location):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(API_KEY, term, location)

    businesses = response.get('businesses')

    if alias: 
        print

    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return

    business_id = businesses[0]['id']

    print(u'{0} businesses found, querying business info ' \
        'for the top result "{1}" ...'.format(
            len(businesses), business_id))
    response = get_business(API_KEY, business_id)

    print(u'Result for business "{0}" found:'.format(business_id))
    pprint.pprint(response, indent=2)