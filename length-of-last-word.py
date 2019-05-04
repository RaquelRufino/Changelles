class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        

        A = A.split()
        if len(A) == 0:
            return 0
 
        return len(A[-1])
