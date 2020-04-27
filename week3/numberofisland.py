def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if(len(grid)) == 0:
            return 0
        max_row = len(grid)
        max_col = len(grid[0])
        def mark_adj_ones(j,i,grid):
            if j >= max_row or i >= max_col or i < 0 or j < 0:
                return
            if grid[j][i] == '0':
                return
            else:
                grid[j][i] = '0'
                mark_adj_ones(j+1,i,grid)
                mark_adj_ones(j,i+1,grid)
                mark_adj_ones(j-1,i,grid)
                mark_adj_ones(j,i-1,grid)
                
        count = 0
        for j in range(max_row):
            for i in range(max_col):
                if grid[j][i] == '1':
                    count += 1
                    mark_adj_ones(j,i,grid)
        return count
