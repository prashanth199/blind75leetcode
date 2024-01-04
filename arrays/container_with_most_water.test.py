from unittest import TestCase, main
from container_with_most_water import Solution

class ContainerWithMostWater(TestCase):

    def testOne(self):

        height = [1,8,6,2,5,4,8,3,7]
        sol = Solution(height)

        expected_result = 49
        actual_result = sol.result 

        return self.assertEqual(expected_result,actual_result)
    
    def testTwo(self):
        height = [1,1]
        sol = Solution(height)

        expected_result = 1
        actual_result = sol.result

        return self.assertEqual(expected_result,actual_result)

if __name__ == '__main__':
    main()