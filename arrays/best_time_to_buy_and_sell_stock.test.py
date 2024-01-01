
from unittest import TestCase, main
from best_time_to_buy_and_sell import Solution


class BestTimeToBuyAndSellStockTest(TestCase):

    def testOne(self):
        prices = [7,1,5,3,6,4]
        sol = Solution(prices)
        expected_result = 5
        actual_result = sol.result

        return self.assertEqual(expected_result,actual_result)
    
    def testTwo(self):
        prices = [7,6,4,3,1]
        sol = Solution(prices)
        expected_result = 0
        actual_result = sol.result

        return self.assertEqual(expected_result,actual_result)

if __name__ == '__main__':
    main()