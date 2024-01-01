from unittest import TestCase, main
from product_of_array_except_self import Solution

class ProductOfArrayExceptSelfTest(TestCase):

    def testOne(self):
        nums = [1,2,3,4]
        sol = Solution(nums)

        expected_result = [24,12,8,6]
        actual_result = sol.result

        return self.assertEqual(expected_result,actual_result)
    
    def testTwo(self):
        nums = [-1,1,0,-3,3]
        sol = Solution(nums)

        expected_result = [0,0,9,0,0]
        actual_result = sol.result

        return self.assertEqual(expected_result,actual_result)



if __name__ == '__main__':
    main()