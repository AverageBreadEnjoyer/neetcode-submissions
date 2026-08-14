class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        """

        count = [0,0,0] #3 main catagories that it can be
        
        for i in nums: #Counts how many of each catagory is in nums
            count[i] += 1

        i = 0
        for j in range(len(count)): # what is the point of this?
            for k in range(count[j]): 
                nums[i] = j
                i += 1

        
            
        
            

        
