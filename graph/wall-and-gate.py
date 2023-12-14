
from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        rowSz,colSz =len(rooms), len(rooms[0])
        EMPTY = 2147483647
        for r in range(rowSz):
            for c in range(colSz):
                if rooms[r][c] == 0:
                    q.append((r,c))
        
        dirns = [[-1,0],[1,0],[0,1],[0,-1]]
        while q:
            cr,cc = q.popleft()
            for dirn in dirns:
                nr = cr + dirn[0]
                nc = cc + dirn[1]
                if nr < 0 or nc < 0 or nr >= rowSz or nc>= colSz:
                    continue
                if rooms[nr][nc] == EMPTY:
                    rooms[nr][nc] = rooms[cr][cc]+1
                    q.append((nr,nc))
                
                
                
