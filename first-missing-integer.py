class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        lista = [0] * 10 ** 7

        y = 1
        for i in A:
            
            if i > 0:
                
                
                lista[i] = 1
            
            y += 1
        
        n = 1
        for i in lista[1:y + 10]:
            
            if i == 0:
                
                return n
            
            n += 1
