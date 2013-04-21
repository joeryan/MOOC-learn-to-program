import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_empty_list(self):
        L = []
        a1.swap_k(L, 1)
        self.assertEqual([], L)

    def test_swap_1item_list(self):
        L = [1]
        expectL = [1]
        a1.swap_k(L, 1)
        self.assertEqual(expectL, L)

    def test_swap_2item_list(self):
        L = [1,2]
        expectL = [2,1]
        a1.swap_k(L, 1)
        self.assertEqual(expectL, L)

    def test_swap_3item_list(self):
        L = [1,2,3]
        expectL = [3,2,1]
        a1.swap_k(L, 1)
        self.assertEqual(expectL, L)

    def test_swap_multi_item_list(self):
        L = [1,2,3,4,5,6,7,8]
        expectL = [6,7,8,4,5,1,2,3]
        a1.swap_k(L, 3)
        self.assertEqual(expectL, L)
                            

if __name__ == '__main__':
    unittest.main(exit=False)
