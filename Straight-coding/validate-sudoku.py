
# https://leetcode.com/problems/valid-sudoku/description/
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowSz,colSz = len(board), len(board[1])
        def isValid(rowStart, rowEnd, colStart, colEnd):
            numSet = set()
            for row in range(rowStart,rowEnd+1):
                for col in range(colStart, colEnd+1):
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in numSet:
                        return False
                    numSet.add(board[row][col])
            return True

        # validate each row
        for row in range(0,rowSz):
            if isValid(row, row, 0, colSz-1) == False:
                return False
        # validate each col
        for col in range(0,colSz):
            if isValid(0, rowSz-1, col, col) == False:
                return False

        # validate each square of size 09 the smaller grids
        for i in range(0, rowSz,3):
            for j in range(0, colSz,3):
                if isValid(i, i+2, j, j+2) == False:
                    return False
        
        return True