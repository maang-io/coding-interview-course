#https://leetcode.com/problems/max-area-of-island/
class Solution(object):
    dirns = [
        [-1,0],
        [1,0],
        [0,1],
        [0,-1]
    ]
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid :
            return 0
        rowSz = len(grid)
        colSz = len(grid[0])
        result = 0
        for r in range(0,rowSz):
            for c in range(0, colSz):
                if grid[r][c] == 0:
                    continue
                sz = self.dfs(grid, r,c)
                print(sz)
                result = max(result,sz)
        
        return result

        
    def dfs(self, grid, r, c):
        # we laready make sure that it is a land
        # visit it and mark it visited so that we dont visit it again
        sz = 1
        grid[r][c] = 0
        # try visiting nbrs
        rowSz = len(grid)
        colSz = len(grid[0])
        for dirn in self.dirns:
            nr = r + dirn[0]
            nc = c + dirn[1]
            if nr < 0 or nr >= rowSz or nc < 0 or nc >= colSz or grid[nr][nc] == 0:
                continue
            # found land
            sz+= self.dfs(grid, nr,nc)
        return sz