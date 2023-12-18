#https://leetcode.com/problems/construct-quad-tree/description/
"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        N= len(grid)
        def hasSameValue(rowStart, rowEnd, colStart, colEnd):
            val = grid[rowStart][colStart]
            for i in range(rowStart,rowEnd+1):
                for j in range(colStart, colEnd+1):
                    if grid[i][j] != val:
                        return -1
            
            return val

        def buildNode(rowStart, rowEnd, colStart,colEnd):
            val = hasSameValue(rowStart, rowEnd, colStart,colEnd)
            if val == 0 or val == 1:
                return Node(True if val == 1 else False, True, None, None, None,None)

            midRow = rowStart+ (rowEnd-rowStart)/2
            midCol = colStart + (colEnd-colStart)/2
            return Node(
                False,
                False,
                buildNode(rowStart, midRow, colStart, midCol),
                buildNode(rowStart, midRow, midCol+1, colEnd),
                buildNode(midRow+1, rowEnd, colStart, midCol),
                buildNode(midRow+1,rowEnd, midCol+1, colEnd)
                )
        
        return buildNode(0, N-1, 0, N-1)


        