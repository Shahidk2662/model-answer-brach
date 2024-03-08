import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Calculate the expected prices
        expected_prices = [(121.2 + 120.48) / 2, (121.68 + 117.87) / 2]

        # Test the getDataPoint function
        for i, quote in enumerate(quotes):
            _, _, _, price = getDataPoint(quote)
            self.assertEqual(price, expected_prices[i])

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Calculate the expected prices
        expected_prices = [(119.2 + 120.48) / 2, (121.68 + 117.87) / 2]

        # Test the getDataPoint function
        for i, quote in enumerate(quotes):
            _, _, _, price = getDataPoint(quote)
            self.assertEqual(price, expected_prices[i])

if _name_ == '_main_':
    unittest.main()
