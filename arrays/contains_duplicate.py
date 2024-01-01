class Solution:

    def __init__(self,nums) -> None:
        self.result = self.hasDuplicates(nums)
    
    
    """
    The Time complexity of this algorithm is O(NlogN) since we are sorting
    The Space Complexity of this algorithm is O(1) since we are not using any extra space
    """
    def hasDuplicates(self,nums):
        nums.sort()
        n = len(nums)

        for i in range(1,n):
            if nums[i] == nums[i-1]:
                return True
        return False
     
    """"
    This algorithm uses set to store unique elements 
    The Time Complexity of this algorithm is O(n) 
    The Space complexity of this algorithm is O(n) since we are using space to store uniqe elements
    """
    # def hasDuplicatesUsingSets(self,nums):
        
    #     unique_elements = set()
    #     n = len(nums)

    #     for i in range(n):
    #         unique_elements.add(nums[i])

    #     if len(unique_elements) < n :
    #         return True
        
    #     return False



    