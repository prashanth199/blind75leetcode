class Solution:
    
    def __init__(self,height) -> None:
        self.result = self.getContainerWithMostWater(height)

    def getContainerWithMostWater(self,height):

        left = 0
        right = len(height) - 1
        ans = 0

        while left < right:

            ans = max(ans,min(height[left],height[right])*(right-left))

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        
        return ans
