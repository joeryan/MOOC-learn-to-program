import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_empty_price_chg(self):
        gainloss = a1.stock_price_summary([])
        self.assertAlmostEqual((0,0), gainloss)

    def test_all_gains_price_change(self):
        price_chg =[0.0, 0.10, 0.02, 0.13]
        expect_gainloss = (0.25,0)
        gainloss = a1.stock_price_summary(price_chg)
        self.assertAlmostEqual(expect_gainloss, gainloss)
        
    def test_all_losses_price_change(self):
        price_chg =[0.0, -0.10, -0.02, -0.13]
        expect_gainloss = (0,-0.25)
        gainloss = a1.stock_price_summary(price_chg)
        self.assertAlmostEqual(expect_gainloss, gainloss)

    def test_both_gainslosses_price_change(self):
        price_chg =[-0.20, 0.12, 0.03, -0.10, 0.0, 0.10, -0.02, -0.13, 0.20]
        expect_gainloss = (0.45,-0.45)
        gain,loss = a1.stock_price_summary(price_chg)
        self.assertAlmostEqual(expect_gainloss, (round(gain, 10),round(loss, 10)))

    def test_large_pricechange_list2(self):
        exp_result, price_chg = 0.0, []
        for i in range(100):
            price_chg.append(i/100.0)
            price_chg.append(-i/100.0)
            exp_result += i/100.0
        gain, loss = a1.stock_price_summary(price_chg)
        self.assertEqual((exp_result, -exp_result), (round(gain, 10),round(loss, 10)))
        
if __name__ == '__main__':
    unittest.main(exit=False)
