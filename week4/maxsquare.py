def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def is_square(j,i,length):
            for x in range(i,i+length+1):
                if matrix[j+length][x] == '0':
                    return False
            for y in range(j,j+length+1):
                if matrix[y][i+length] == '0':
                    return False
            return True
                    
        
        if len(matrix) == 0:
            return 0
        M = len(matrix)
        N = len(matrix[0])
        largest = 0
        for j in range(M):
            for i in range(N):
                if matrix[j][i] == '1':
                    #test largest square
                    sq_l = 1
                    while sq_l + i < N and sq_l + j < M:
                        if is_square(j,i,sq_l):
                            sq_l += 1
                        else:
                            break
                    largest = max(sq_l, largest)
        
        return largest**2
