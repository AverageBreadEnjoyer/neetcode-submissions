class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                val_1 = nums[i]
                val_2 = nums[j]
                if i != j and val_1 + val_2 == target:
                    return [min(i, j), max(i,j)]
