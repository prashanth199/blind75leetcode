class Solution:
    def __init__(self,nums,target) -> None:
        self.result = self.getTwoSum(nums,target)

    """
    This Approach Uses Hashing Techique 
    The The idea is that we deduct 
    
    """    

    def getTwoSum(self,nums,target):

        nums_index_map = {}

        for i,num in enumerate(nums):
            remaining = target - num 
            if remaining in nums_index_map:
                return [nums_index_map[remaining], i]
            nums_index_map[num] = i 
        return [-1,-1]
    
    """
    This Approach Uses 2 Pointer Approach So The array has to be sorted
    This algorithm is suited when the data is sorted

    The Time Complexity is O(n) and The Space Complexity is O(1)
    
    """
    
    def getTwoSumUsingTwoPointer(self,nums,target):
        
        nums.sort()
        l = 0
        r = len(nums) - 1
        
        while l < r:

            sum = nums[l] + nums[r]

            if sum < target:
                l+=1
            elif sum > target:
                r-=1
            else:
                return [l,r] 
        return [-1,-1]
            

            


