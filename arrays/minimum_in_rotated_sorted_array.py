class Solution:

    def __init__(self,nums) -> None:
        self.result = self.getMinimumInRotatedSortedArray(nums)
    
    def getMinimumInRotatedSortedArray(self,nums):

        low = 0
        high = len(nums) - 1
        

        ans = float('inf')

        """
        If The entire array is sorted
        """
        if nums[low] < nums[high]:
            ans = min(ans,nums[low])
        
        while low <= high:
            mid = (low+high)//2

            if(nums[low]<nums[high]):
                ans = min(ans,nums[low])
                break

            if nums[low] <= nums[mid]:
                ans = min(ans,nums[low])
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                high = high - 1
        return ans


