class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        layers = []

        for i in s:
            if i in brackets:
                if not layers:
                    return False
                if layers[-1] != brackets[i]: # Doesn't pop layer
                    return False
                else:  # Does pop layer
                    layers.pop() 
            else: 
                layers.append(i)
        if layers:
            return False
        else: 
            return True

   

                
