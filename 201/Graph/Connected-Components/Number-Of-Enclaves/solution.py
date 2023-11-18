# https://leetcode.com/problems/number-of-enclaves/description/
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rowSz,colSz = len(grid), len(grid[0])
        visited = [[False for _ in range(colSz)] for _ in range(rowSz)]
        dirns = [
            [-1,0],
            [1,0],
            [0,1],
            [0,-1]
        ]

        def dfs(r,c):
            # visite (r,c)
            visited[r][c] = True

            # explore neighbours
            for dirn in dirns:
                nr = r + dirn[0]
                nc = c + dirn[1]
                if nr < 0 or nr >= rowSz or nc < 0 or nc >= colSz:
                    continue
                if visited[nr][nc] or grid[nr][nc] == 0:
                    continue
                dfs(nr,nc)
                
        
        # first column and last col
        for r in range(rowSz):
            if grid[r][0] == 1:
                dfs(r,0)
            
            if grid[r][colSz-1] == 1:
                dfs(r,colSz-1)


        # first row and last row
        for c in range(colSz):
            if grid[0][c] == 1:
                dfs(0,c)

            if grid[rowSz-1][c] == 1:
                dfs(rowSz-1,c)

        count = 0
        for r in range(rowSz):
            for c in range(colSz):
                if grid[r][c] == 1 and visited[r][c]==False:
                    count+=1
        return count