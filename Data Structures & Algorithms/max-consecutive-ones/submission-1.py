class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons = []
        m = 0
        for i in nums:
            if i == 1:
                m += 1
            else: 
                cons.append(m)
                m = 0
                
        cons.append(m)
        return max(cons)
