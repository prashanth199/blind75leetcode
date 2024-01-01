from unittest import TestCase,main
from two_sum import Solution

class TwoSumTest(TestCase):

    def testOne(self):
        nums = [2,7,11,15] 
        target = 9
        sol = Solution(nums,target)
        expected_result = [0,1]
        actual_result = sol.result 
        return self.assertEqual(expected_result,actual_result)
    
    def testTwo(self):
        nums = [3,2,4]
        target = 6
        sol = Solution(nums,target)
        expected_result = [1,2]
        actual_result = sol.result
        return self.assertEqual(expected_result,actual_result)
    
    def testThree(self):
        nums = [3,3]
        target = 6
        sol = Solution(nums,target)
        expected_result = [0,1]
        actual_result = sol.result
        return self.assertEqual(expected_result,actual_result)



if __name__=='__main__':
    main()