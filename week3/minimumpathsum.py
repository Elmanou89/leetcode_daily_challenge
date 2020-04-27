def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if  len(grid) == 0:
            return 0
        max_row = len(grid)
        max_col = len(grid[0])
        dp = {}
        for j in range(max_row):
            for i in range(max_col):
                max_top = 0
                max_left = 0
                if j > 0 and i > 0:
                    dp[(j,i)] = grid[j][i] + min(dp[(j-1,i)],dp[(j,i-1)])
                elif i == 0 and j == 0:
                    dp[(j,i)] = grid[j][i] 
                elif i==0:
                    dp[(j,i)] = grid[j][i] +  dp[(j-1,i)]
                else: #j==0
                    dp[(j,i)] = grid[j][i] +  dp[(j,i-1)]
                
        return dp[(max_row-1,max_col-1)]
