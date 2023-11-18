# https://leetcode.com/problems/number-of-islands/
class Solution(object):
    dirns = [
        [-1,0],
        [1,0],
        [0,1],
        [0,-1]
    ]
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid :
            return 0
        rowSz = len(grid)
        colSz = len(grid[0])
        count = 0
        for r in range(0,rowSz):
            for c in range(0, colSz):
                if grid[r][c] == '0':
                    continue
                self.bfs(grid, r,c)
                count+=1
        
        return count

    def numIslands_dfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid :
            return 0
        rowSz = len(grid)
        colSz = len(grid[0])
        count = 0
        for r in range(0,rowSz):
            for c in range(0, colSz):
                if grid[r][c] == '0':
                    continue
                self.dfs(grid, r,c)
                count+=1
        
        return count

    def dfs(self, grid, r, c):
        # we laready make sure that it is a land
        # visit it and mark it visited so that we dont visit it again
        grid[r][c] = '0'

        # try visiting nbrs
        rowSz = len(grid)
        colSz = len(grid[0])
        for dirn in self.dirns:
            nr = r + dirn[0]
            nc = c + dirn[1]
            if nr < 0 or nr >= rowSz or nc < 0 or nc >= colSz or grid[nr][nc] == '0':
                continue
            # found land
            self.dfs(grid, nr,nc)
                
    
    def bfs(self, grid, r, c):
        queue = deque([])
        queue.append((r,c))
        rowSz = len(grid)
        colSz = len(grid[0])
        while len(queue):
            qsz = len(queue)
            for _ in range(0,qsz):
                cr,cc = queue.popleft()
                for dirn in self.dirns:
                    nr = cr + dirn[0]
                    nc = cc+ dirn[1]
                    if nr < 0 or nr >= rowSz or nc < 0 or nc >= colSz or grid[nr][nc] == '0':
                        continue
                    grid[nr][nc] = '0'
                    queue.append((nr,nc))