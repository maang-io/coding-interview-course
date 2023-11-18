# https://leetcode.com/problems/battleships-in-a-board/description/
class Solution(object):
    def countBattleships(self, board):
        if not board:
            return 0
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rowSz,colSz = len(board), len(board[0])
        result = 0
        for r in range(rowSz):
            for c in range(colSz):
                if board[r][c] == '.':
                    continue
                if r>0 and board[r-1][c] == 'X':
                    continue
                if c>0 and board[r][c-1] == 'X':
                    continue
                result+=1
        return result
        