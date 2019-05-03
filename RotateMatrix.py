class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        
        A = [(i)[::-1] for i in zip(*A)]
        
        return A
