# File:                     : rest.py
# Description:              : recommends restaurant based on price and food type
# Author:                   : Joe Ryan <joe@clanryan.us
# Arguments:                : ?? possible command line ([$,$$,$$$,$$$$], food_type
#                               currently hard coded in for testing
"""
    Write a function that takes three parameters:
        - a restaurant file that is open for reading
        - the price range (one of $, $$, $$$, and $$$$)
        - a list of cuisine types
    return a list of restaurants (in the specified price range) and their
    ratings from highest to lowest

    restaurant file is text file of format:
        name
        rating
        price (one of $, $$, $$$, $$$$)
        list of cuisines served
        /n #blank line separates each restaurant

    * course uses list of lists, why not objects?
        - learn to program course hasn't covered object oriented programming yet


"""


def recommend(filename, price, cuisine):
    """ (file, str, list of str) -> list of str
    given the sample data:
        Restaurant name to rating:
        # dict of {str: int}
        {'Georgie Porgie': 87,
         'Queen St. Cafe': 82,
         'Dumplings R Us': 71,
         'Mexican Grill': 85,
         'Deep Fried Everything': 52}

        Price to list of restaurant names:
        # dict of {str, list of str}
        {'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
         '$$': ['Mexican Grill'],
         '$$$': ['Georgie Porgie'],
         '$$$$': []}

        Cuisine to list of restaurant names:
        # dict of {str, list of str}
        {'Canadian': ['Georgie Porgie'],
         'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
         'Malaysian': ['Queen St. Cafe'],
         'Thai': ['Queen St. Cafe'],
         'Chinese': ['Dumplings R Us'],
         'Mexican': ['Mexican Grill']}

    With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
    would produce this list:

        [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """
    
if __name__ == '__main__':
    # Hard coded FILENAME
    FILENAME = restaurant_small.txt
