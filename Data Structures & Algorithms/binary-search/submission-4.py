class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = len(nums)//2
        L,R = 0, len(nums)-1 

        while L<=R:
            if nums[m] > target:
                R = m-1
                m = (L+R)//2
            elif nums[m] < target:
                L = m+1
                m = (L+R)//2
            else:
                return m

        return -1


        