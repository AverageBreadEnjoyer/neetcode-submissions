# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower = 1
        higher = n

        m = (lower + higher) // 2

        res = guess(m)
        print(f"Lower: {lower}, Higher: {higher}")
        print(f"m: {m}")
        while lower <= higher:
            if res == 0:
                return m
            
            if res == 1:
                lower = m + 1
                m = (lower + higher) // 2
                res = guess(m)

                print(f"Lower: {lower}, Higher: {higher}")
                print(f"m: {m}")
                

            if res == -1:
                higher = m - 1 
                m = (lower + higher) // 2
                res = guess(m)
                
                print(f"Lower: {lower}, Higher: {higher}")
                print(f"m: {m}")

        
        print(f"Lower: {lower}, Higher: {higher}")
        print(f"m: {m}")
        return -1
        
        
