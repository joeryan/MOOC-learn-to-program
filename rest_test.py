import rest
import unittest


class TestRestaurantReccommend (unittest.TestCase):
    
    def test_read_dictionaries(self):

        FILENAME = open("restaurants_small.txt", 'r')

        expected_name2rating = {'Queen St. Cafe': '82',
                               'Deep Fried Everything': '52',
                               'Mexican Grill': '85',
                               'Georgie Porgie': '87',
                               'Dumplings R Us': '71'}
        
        expected_name2cuisine = {'Mexican': ['Mexican Grill'],
                                 'Chinese': ['Dumplings R Us'],
                                 'Canadian': ['Georgie Porgie'],
                                 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
                                 'Malaysian': ['Queen St. Cafe'],
                                 'Thai': ['Queen St. Cafe']}
        
        expected_price2name = {'$$': ['Mexican Grill'],
                               '$$$$': [],
                               '$': ['Queen St. Cafe',
                                     'Dumplings R Us',
                                     'Deep Fried Everything'],
                               '$$$': ['Georgie Porgie']}

        name2rating, price2name, name2cuisine = rest.read_dictionaries(FILENAME)

        self.assertEqual(expected_name2rating, name2rating)
        self.assertEqual(expected_price2name, price2name)
        self.assertEqual(expected_name2cuisine, name2cuisine)

    def test_filter_by_price(self):
        expected_namesbyprice = ['Queen St. Cafe',
                                     'Dumplings R Us',
                                     'Deep Fried Everything']

        price2name = {'$$': ['Mexican Grill'],
                               '$$$$': [],
                               '$': ['Queen St. Cafe',
                                     'Dumplings R Us',
                                     'Deep Fried Everything'],
                               '$$$': ['Georgie Porgie']}

        price = '$'
        namesbyprice = rest.filter_by_price(price2name, price)

        self.assertEqual(expected_namesbyprice, namesbyprice)

    def test_filter_by_cuisine(self):
        expected_names_with_cuisine = ['Queen St. Cafe',
                                     'Dumplings R Us']
        
        cuisine2names = {'Mexican': ['Mexican Grill'],
                                 'Chinese': ['Dumplings R Us'],
                                 'Canadian': ['Georgie Porgie'],
                                 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
                                 'Malaysian': ['Queen St. Cafe'],
                                 'Thai': ['Queen St. Cafe']}                            
        names_by_price = ['Queen St. Cafe',
                          'Dumplings R Us',
                          'Deep Fried Everything']
        cuisine = ['Thai', 'Chinese']

        names_with_cuisine = rest.filter_by_cuisine(names_by_price,
                                                    cuisine, cuisine2names)

        self.assertEqual(expected_names_with_cuisine, names_with_cuisine)

    def test_sort_by_rating(self):
        expected_sorted_names = [[82, 'Queen St. Cafe'],
                                    [71, 'Dumplings R Us']]
        names_with_cuisine = ['Queen St. Cafe',
                                     'Dumplings R Us']
        names_to_ratings = {'Queen St. Cafe': '82',
                               'Deep Fried Everything': '52',
                               'Mexican Grill': '85',
                               'Georgie Porgie': '87',
                               'Dumplings R Us': '71'}

        sorted_names = rest.sort_by_rating(names_with_cuisine, names_to_ratings)

        self.assertEqual(expected_sorted_names, sorted_names)
        
    def test_reccommend(self):
        FILENAME = open("restaurants_small.txt", 'r')
        expected_restaurant_list = [[82, 'Queen St. Cafe'],
                                    [71, 'Dumplings R Us']]
        price = '$'
        cuisine = ['Thai', 'Chinese']

        restaurants = rest.recommend(FILENAME, price, cuisine)

        self.assertEqual(expected_restaurant_list, restaurants)
        
        
if __name__ == '__main__':
    unittest.main()
