#https://leetcode.com/problems/set-matrix-zeroes/description/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rowSz, colSz = len(matrix), len(matrix[0])
        rows = [False]*rowSz
        cols = [False]*colSz
        for r in range(rowSz):
            for c in range(colSz):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        
        for r in range(rowSz):
            for c in range(colSz):
                if rows[r]== True or cols[c] == True:
                    matrix[r][c] = 0

        

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rowSz, colSz = len(matrix), len(matrix[0])
        rows = [False]*rowSz
        cols = [False]*colSz
        fr = fc = False
        for r in range(rowSz):
            for c in range(colSz):
                if matrix[r][c] == 0:
                    if r == 0 :
                        fr = True
                    if c == 0:
                        fc = True
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, rowSz):
            for c in range(1, colSz):
                if matrix[r][0]== 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if fr == True:
            for c in range(colSz):
                matrix[0][c] = 0

        if fc == True:
            for r in range(rowSz):
                matrix[r][0] = 0                