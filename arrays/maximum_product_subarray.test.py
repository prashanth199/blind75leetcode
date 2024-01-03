from unittest import TestCase,main
from maximum_product_subarray import Solution

class MaximumProductSubarrayTest(TestCase):

    def testOne(self):
        nums = [2,3,-2,4]
        sol = Solution(nums)
        expected_result = 6
        actual_result = sol.result 
        return self.assertEqual(expected_result,actual_result)
    
    def testTwo(self):
        nums = [-2,0,-1]
        sol = Solution(nums)
        expected_result = 0
        actual_result = sol.result
        return self.assertEqual(expected_result,actual_result)

if __name__ == '__main__':
    main()
