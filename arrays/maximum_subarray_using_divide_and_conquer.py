from sys import maxsize

class Solution:

    def __init__(self,nums) -> None:
        self.result = self.getMaximumSubarraySum(nums,0,len(nums)-1)

    def getMaximumSubarraySum(self,nums,low,high):

        if low == high:
            return nums[low]
        

        mid = (low + high)//2

        left_sum = self.getMaximumSubarraySum(nums,low,mid)
        right_sum = self.getMaximumSubarraySum(nums,mid+1,high)
        crossing_sum = self.getMaximumCrossingSubarraySum(nums,low,mid,high)

        return max(left_sum,right_sum,crossing_sum)
    
    def getMaximumCrossingSubarraySum(self,nums,low,mid,high):

        maximum_so_far_in_left = -maxsize-1
        maximum_ending_here_in_left = 0

        for i in range(mid,low-1,-1):
            maximum_ending_here_in_left+=nums[i]

            if maximum_so_far_in_left<maximum_ending_here_in_left:
                maximum_so_far_in_left = maximum_ending_here_in_left
        
        
        maximum_so_far_in_right = -maxsize-1
        maximum_ending_here_in_right = 0

        for i in range(mid+1,high+1):
            maximum_ending_here_in_right+=nums[i]

            if maximum_so_far_in_right<maximum_ending_here_in_right:
                maximum_so_far_in_right = maximum_ending_here_in_right
        
        return (maximum_ending_here_in_left + maximum_ending_here_in_right)
        

