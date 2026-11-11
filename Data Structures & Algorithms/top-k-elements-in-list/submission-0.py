class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_counts = {}
        result = []

        for number in nums:
            # If not a key already
            if number not in element_counts:
                element_counts[number] = 1
            
            # If it is a key
            else:
                element_counts[number] += 1
        
        for i in range(k):
            max_count = max(element_counts.values())

            # Append max count number to result
            for key, value in element_counts.items():
                if value == max_count:
                    result.append(key)
                    # Set to zero
                    element_counts[key] = 0
                    break
            

            
        return result
        
                


