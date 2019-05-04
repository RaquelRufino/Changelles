class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):

        result = ""
        
        while A >= 1:
            
            r = (A) % 26
            
            
            if r == 0 :
                result =  "Z" + result
                A = (A) / 26 - 1
                
            else:
                
                result = chr(r + ord("A") -1) + result
                A = (A) / 26
        
        return result
