class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        
        A = A.split(" ")
        result = ""
        A = A[::-1]
        n = 0
        x = len(A) - 1
        
        for i in A:
            
            if x == n :
                result = result + i 
            else:
                result = result + i + " "
            
            n += 1
        
        return result
