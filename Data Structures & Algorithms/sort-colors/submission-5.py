class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            j = i-1

           
            while j>=0 and nums[j]>nums[j+1]:
                tmp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = tmp
                j -= 1

            

            
