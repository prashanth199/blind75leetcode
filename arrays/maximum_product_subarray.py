class Solution:

    def __init__(self,nums) -> None:
        self.result = self.getMaximumProductSubarray(nums)
    
    def getMaximumProductSubarray(self,nums):

        ans = float('-inf')
        prefix,suffix = 1,1
        n = len(nums)

        for i in range(n):

            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            prefix = prefix * nums[i]
            suffix = suffix * nums[n-i-1]

            ans = max(ans,max(prefix,suffix))
        return ans

