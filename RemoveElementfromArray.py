class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):


        A [:]= [i for i in A if i!=B]
        return len(A)

