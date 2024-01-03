from unittest import TestCase,main
from search_in_rotated_sorted_array import Solution 

class SearchInRotatedSortedArrayTest(TestCase):

    def testOne(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        sol = Solution(nums,target)

        expected_result = 4
        actual_result = sol.result

        return self.assertEqual(expected_result,actual_result)
    
    def testTwo(self):
        nums=[4,5,6,7,0,1,2] 
        target = 3

        sol = Solution(nums,target)

        expected_result = -1 
        actual_result = sol.result

        return self.assertEqual(expected_result,actual_result)
    
    def testThree(self):
        nums=[1] 
        target = 0

        sol = Solution(nums,target)

        expected_result = -1 
        actual_result = sol.result

        return self.assertEqual(expected_result,actual_result)
    




if __name__ == '__main__':
    main()