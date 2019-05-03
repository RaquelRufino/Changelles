class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        
        lista = [0] * (10 ** 7)

        for i in A:
            
            lista[i] += 1
            
            if lista[i] > 1: return i
        
        return -1
