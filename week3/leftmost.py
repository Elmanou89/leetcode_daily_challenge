# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        n,m = binaryMatrix.dimensions()
        left_most_one = 200
        for i in range(n):
            left = 0
            right = m-1
            
            while left < right:
                mid = (left+right)//2
                if binaryMatrix.get(i,mid) == 0:
                    left = mid + 1
                else:
                    right = mid
            if left != m-1 or binaryMatrix.get(i,left) == 1:
                    left_most_one = min(left,left_most_one)
        if left_most_one != 200:
            return left_most_one
        else:
            return -1
                    
