import rest
import unittest


class TestRestaurantReccommend (Unittest.TestCase):
    
    def test_read_dictionaries(self):
        FILENAME = open("restaurant_small.txt", 'r')
        expected_price2name = { }
        expected_name2cuisine= {}
        expected_name2rating= {}
        name2rating, price2name, name2cuisine = rest.read_dictionaries(FILENAME)

        self.assertEqual(expected_name2rating, name2rating)
        self.assertEqual(expected_price2name, price2name)
        self.assertEqual(expected_name2cuisine, name2cuisine)

    def test_filter_by_price(self):
        expected_namesbyprice = {}
        price2name = {}
        price = '$'
        namesbyprice = rest.filter_by_price(price2name, price)

        self.assertEqual(expected_namesbyprice, namesbyprice)

    def test_filter_by_cuisine(self):
        expected_nameswithcuisine = {}
        names_by_price = {}
        cuisine = ['Thai', 'Chinese']

        names_with_cuisine = rest.filter_by_cuisine(names_by_price, cuisine)

        self.assertEqual(expected_nameswithcuisine, names_with_cuisine)

    def test_reccommend(self):
        FILENAME = open("restaurant_small.txt", 'r')
        expected_restaurant_list = {}
        price = '$'
        cuisine = ['Thai', 'Chinese']

        restaurants = rest.recommend(FILENAME, price, cuisine)

        self.assertEqual(expected_restaurant_list, restaurants)
        
        
        
