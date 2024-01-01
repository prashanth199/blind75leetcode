from unittest import TestCase, main
from maximum_subarray_using_divide_and_conquer import Solution

class MaximumSubArrayUsingDivideAndConquerTest(TestCase):
    
    def testOne(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        sol = Solution(nums)

        expected_result = 6
        actual_result = sol.result

        self.assertEqual(expected_result, actual_result)
    
    def testTwo(self):
        nums = [1]
        sol = Solution(nums)

        expected_result = 1
        actual_result = sol.result

        self.assertEqual(expected_result, actual_result)

    def testThree(self):
        nums = [5, 4, -1, 7, 8]
        sol = Solution(nums)

        expected_result = 23
        actual_result = sol.result

        self.assertEqual(expected_result, actual_result)

if __name__ =='__main__':
    main()
