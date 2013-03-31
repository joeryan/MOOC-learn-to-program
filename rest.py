# File:                     : rest.py
# Description:              : recommends restaurant based on price and food type
# Author:                   : Joe Ryan <joe@clanryan.us
# Arguments:                : ?? possible command line ([$,$$,$$$,$$$$], food_type
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
