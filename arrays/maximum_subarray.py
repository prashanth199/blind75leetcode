from sys import maxsize
class Solution:
    
    def __init__(self,nums) -> None:
        self.result = self.getMaximumSubarraySum(nums)

    def getMaximumSubarraySum(self,nums):
        maximum_so_far = -maxsize-1
        maximum_ending_here = 0

        for i,ele in enumerate(nums):
            maximum_ending_here+=ele

            if maximum_so_far < maximum_ending_here:
                maximum_so_far = maximum_ending_here
            
            if maximum_ending_here <= 0:
                maximum_ending_here = 0
        return maximum_so_far
    
    def printMaximumSubarrayList(self,nums):
        maximum_so_far = -maxsize-1
        maximum_ending_here = 0

        start = 0
        startIndex = 0
        endIndex = 0

        for i,ele in enumerate(nums):
            maximum_ending_here+=ele

            if maximum_so_far < maximum_ending_here:
                maximum_so_far = maximum_ending_here
                startIndex = start
                endIndex = i
            
            if maximum_ending_here <= 0:
                maximum_ending_here = 0
                start = i + 1
        return [nums[i] for i in range(startIndex,endIndex+1)]

    