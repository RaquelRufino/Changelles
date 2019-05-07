class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):

        x = bin(A)
        x = str(x)[2:]
        x = x[::-1]
        x = x + (32 - len(x)) * '0'
        x = int(x, 2)
        return x
