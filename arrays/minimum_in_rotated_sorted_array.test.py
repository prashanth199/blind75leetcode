from unittest import TestCase,main

from minimum_in_rotated_sorted_array import Solution

class MinimumInRotatedSortedArrayTest(TestCase):

    def testOne(self):
        nums = [3,4,5,1,2]
        sol = Solution(nums)
        expected_result = 1
        actual_result = sol.result 
        return self.assertEqual(expected_result,actual_result)
        
    
    def testTwo(self):
        nums = [4,5,6,7,0,1,2]
        sol = Solution(nums)
        expected_result = 0
        actual_result = sol.result
        return self.assertEqual(expected_result,actual_result)
    
    def testThree(self):
        nums = [11,13,15,17]
        sol = Solution(nums)
        expected_result = 11
        actual_result = sol.result
        return self.assertEqual(expected_result,actual_result)
    


if __name__ == '__main__':
    main()