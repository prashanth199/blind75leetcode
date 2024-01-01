from unittest import TestCase, main
from three_sum import Solution
class ThreeSumTest(TestCase):

    def testOne(self):
        nums = [-1,0,1,2,-1,-4]
        expected = [[-1,-1,2],[-1,0,1]]

        sol = Solution(nums)
        self.assertEqual(expected,sol.result)

    def testTwo(self):
        nums = [0,1,1]
        expected = []

        sol = Solution(nums)
        self.assertEqual(expected,sol.result)

    def testThree(self):
        nums = [0,0,0]
        expected = [[0,0,0]]

        sol = Solution(nums)
        self.assertEqual(expected,sol.result)    

if __name__ == '__main__':
    main()