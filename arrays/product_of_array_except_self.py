class Solution:

    def __init__(self,nums):
        self.result = self.getProductOfArrayExceptSelf(nums)
    """
    In This Approach We Maintain 2 arrays called prefix and suffix 
    The Size of Prefix and Suffix array will be size of array 'nums' 
    We set the first element of prefix and last element of suffix to 1
    i.e prefix[0] = 1  and suffix[n-1] = 1 where 'n' is the size of array 'nums'


    To fill the rest of elements in prefix array we loop through the array from 2nd index to last index and in each loop
    We Use the following formula 
    prefix[i] = prefix[i-1] * nums[i-1] 
    To fill up the prefix element at index i 

    To Fill the rest of the elements in suffix array we loop through the array from the 2 last index to the first index and in each loop
    We Use the following formula
    suffix[i] = suffix[i+1] * nums[i+1]
    To Fill up the suffix element at index i

    Now we have prefix and suffix array we use array called 'product' of size 'N' Which is the size of array 'nums'
    and Use the following formula to fill up products array
    
    products[i] = prefix[i] * suffix[i]

    The Time Complexity of This Algorithm is O(n)
    The Space Complexity of This Algorithm is O(n) + O(n) 

    """
    def getProductOfArrayExceptSelfUsingPrefixaAndSuffix(self,nums):
        
        
        n = len(nums)

        prefix = [-1] * n
        prefix[0] = 1

        suffix = [-1] * n 
        suffix[n-1] = 1

        product = [-1] * n

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for j in range(n-2,0-1,-1):
            suffix[j] = suffix[j+1] * nums[j+1]
        
        for i in range(n):
            product[i] = suffix[i] * prefix[i]
        
        return product
    
    """ 
    This is the Optimal Approach

    In This Approach We eleminate the need for suffix array 
    Here We maintain a prefix array like previous approach 
    And Instead of Suffix array we use a variable called suffix which is assaigned 1 as value
    i.e suffix = 1

    Like Previous Approach We Will Have Array called 'product' to store the product 
    previously we used product[i] = prefix[i] * suffix[i] to calculate the product 
    But In this approach since we have suffix as 1 so in order to fill up all the elements of product array 
    we will loop in reverse order and for each loop we will use
    product[i] = prefix[i] * suffix
    This will fill up the element of product but we have to update the suffix variable as well
    In the previous approach we used suffix[i] = suffix[i+1] * nums[i+1] to update suffix
    But in this approach we will use suffix = suffix * nums[i] To update the Suffix Variable

    The Time Complexity of This Algorithm is O(n)
    The Space Complexity of This Algorithm is O(n)  


    """
    
    def getProductOfArrayExceptSelf(self,nums):

        n = len(nums)

        prefix = [-1] * n 
        prefix[0] = 1

        suffix = 1

        products = [-1] * n

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for j in range(n-1,-1,-1):
            products[j] = prefix[j] * suffix
            suffix =  suffix * nums[i]
        
        return products


