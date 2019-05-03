class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        
        max_terminando_aqui = max_ate_agora = A[0]

        for x in A[1:]:
            max_terminando_aqui = max(x, max_terminando_aqui + x)
            max_ate_agora = max(max_ate_agora, max_terminando_aqui)
        return max_ate_agora

