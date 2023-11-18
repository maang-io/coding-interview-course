# https://leetcode.com/problems/battleships-in-a-board/description/
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rowSz,colSz = len(board), len(board[0])
        dirns = [
            [-1,0],
            [1,0],
            [0,1],
            [0,-1]
        ]
        def dfs(cr, cc):
            # visit
            board[cr][cc] = '#'
            
            #explore neighbours
            for dirn in dirns:
                nr = cr + dirn[0]
                nc = cc + dirn[1]
                if nr < 0 or nr >= rowSz or nc < 0 or nc >= colSz:
                    continue
                if board[nr][nc] != 'X':
                    continue
                dfs(nr,nc)

        result = 0
        for r in range(rowSz):
            for c in range(colSz):
                if board[r][c] == 'X':
                    dfs(r,c)
                    result+=1
        return result
        