class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(arr: List[int])-> bool:

            L = 0
            R = len(arr)-1

            m = (L+R) // 2

            while L<=R:
                if target > arr[m]:
                    L = m+1 
                    m = (L+R) // 2

                elif target < arr[m]:
                    R = m-1
                    m = (L+R) // 2

                elif target == arr[m]:
                    return True
            
            return False

        for i in matrix:
            print(i)
            if binarySearch(i) == True:
                return True

        return False
            

                
                
                