class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        
        n = len(A)
        result = 0
        i = 0
        for x in A[::-1]:
            
            result = result +  (ord(x) - ord("A") + 1) * (26 ** i)
            n -= 1
            i += 1
        
        
        return result
