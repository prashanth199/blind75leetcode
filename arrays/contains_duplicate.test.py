from unittest import TestCase,main
from contains_duplicate import Solution

class ContainsDuplicate(TestCase):

    def testOne(self):
        nums = [1,2,3,1]
        sol = Solution(nums)

        return self.assertTrue(sol.result)
    
    def testTwo(self):
        nums = [1,2,3,4]
        sol = Solution(nums)

        return self.assertFalse(sol.result)
    
    def testThree(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        sol = Solution(nums)

        return self.assertTrue(sol.result)


if __name__ == '__main__':
    main()