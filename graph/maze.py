class Solution_dfs(object):
    def hasPath(self, maze, start, dest):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        dirns = [[-1,0],[1,0],[0,-1],[0,1]]
        rowSz,colSz = len(maze), len(maze[0])
        visited = [[False for _ in range(colSz)] for _ in range(rowSz)]
        def dfs(cur):
            r,c = cur[0],cur[1]
            if r == dest[0] and c == dest[1] :
                return True
            visited[r][c] = True
            # explore all 4 different direction
            for dirn in dirns:
                nr,nc = r+dirn[0], c+dirn[1]
                while (nr >= 0 and nc >= 0 and nr < rowSz and nc < colSz and maze[nr][nc] == 0):
                    nr += dirn[0]
                    nc += dirn[1]
                nr = nr-dirn[0]
                nc = nc-dirn[1]
                if visited[nr][nc]:
                    continue
                canReach = dfs((nr,nc))
                if canReach:
                    return True
            
            return False # end of dfs                

        return dfs(start)


class Solution_bfs(object):
    def hasPath(self, maze, start, dest):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        dirns = [[-1,0],[1,0],[0,-1],[0,1]]
        rowSz,colSz = len(maze), len(maze[0])
        visited = [[False for _ in range(colSz)] for _ in range(rowSz)]
        def bfs():
            q = []
            q.append(start)
            visited[start[0]][start[1]] = True
            while q:
                r,c = q.pop()
                if r == dest[0] and c == dest[1] :
                    return True
                
                # explore all 4 different direction
                for dirn in dirns:
                    nr,nc = r+dirn[0], c+dirn[1]
                    while (nr >= 0 and nc >= 0 and nr < rowSz and nc < colSz and maze[nr][nc] == 0):
                        nr += dirn[0]
                        nc += dirn[1]
                    nr -= dirn[0]
                    nc -= dirn[1]
                    if visited[nr][nc]:
                        continue
                    visited[nr][nc] = True
                    q.append((nr,nc))
            
            return False # end of bfs                

        return bfs()


        