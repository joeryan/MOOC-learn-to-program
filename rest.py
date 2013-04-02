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
    return a list of restaurants (in the specified price range) and 
    their ratings from highest to lowest

    restaurant file is text file of format:
        name
        rating
        price (one of '$', '$$', '$$$', '$$$$')
        list of cuisines served
        /n #blank line separates each restaurant

    * Learn To Program course series from University of Toronto MOOC
      puts examples in docstrings.  This clutters docstring for any
      complex function/class and is not uutilized here
    * course uses list of lists, why not objects?
        - learn to program course hasn't covered object oriented programming yet


"""


def recommend(filename, price, cuisine):
    """ (file, str, list of str) -> list of str

    When provided a file opened for reading (of correct format), 
      Price (one of '$'-'$$$$'), and a list of cuisines:
      recommend returns a sorted list of restaurants and the ratings 
    """

    # read file into dictionaries
    names2rating, price2names, cuisine2names = read_dictionaries(filename)

    # filter names by price
    names_by_price = filter_by_price(price2names, price)

    # select from names_by_price those with cuisine
    names_with_cuisine = select_by_cuisine(names_by_price, cuisine)

    # sort by the restaurants by rating
    result = sort_by_rating(names_with_cuisine, names2rating)
    return result

def read_dictionaries(filename):
    """ (file) -> {str: int}, {str, list of str}, {str: list of str}

    When given restaurant file in format listed in module docstring:
    read_dictionaries returns the dictionaries containing:
    {rest_name: rating}, {price: rest_names}, {rest_name: cuisines}
    """
    # initialize empty dictionaries
    name2rating ={}
    cuisine2name ={}
    price2name = {'$': [], '$$': [], '$$$': [], '$$$$': []}
        
    # create dictionaries based on [name, rating, price, [type]]
    count=0
    for line in filename:
        # strip off trailing newline
        line = line.strip('\n')
        # restaurant listing is 4 items long with a blank line
        # decide which item we are on and store into temp variable
        # when we reach 5th item (should be "") add to dicts
        if count%5 == 0:
            name=line
        elif count%5 == 1:
            # for rating strip ending %
            rating = line.strip('%')
        elif count%5 == 2:
            price = line
        elif count % 5 == 3:
            # for cuisine: split into an array of str
            cuisine =  line.split(',')
        else:
            name2rating[name]=rating
            price2name[price].append(name)
            for cuisine_name in cuisine:
                # create new key if it doesn't exist, append if it does
                if cuisine_name not in cuisine2name.keys():
                    cuisine2name[cuisine_name] = [name]
                else:
                    cuisine2name[cuisine_name].append(name)
        # increment how many lines we've read
        count += 1
        
    # return completely built dictionaries
    return (name2rating, price2name, cuisine2name)
        
    
        


if __name__ == '__main__':
    # run test code if called from command line
    # Hard coded FILENAME
    FILENAME = open('/home/joe/projects/python/MOOC-learn-to-program/restaurants_small.txt', 'r')

    name2rating, price2name, cusine2name = read_dictionaries(FILENAME)
    # results = recommend(FILENAME, '$', ['Chinese', 'Thai'])
    print (name2rating, price2name, cusine2name)