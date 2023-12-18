#https://leetcode.com/problems/pascals-triangle/
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[] for _ in range(numRows)]
        result[0].append(1)
        for i in range (1, numRows):
            local = [1]
            prev = result[i-1]
            for j in range(1,len(prev)):
                local.append(prev[j-1]+ prev[j])
            local.append(1)
            result[i] = local
        return result
    


def generate(self, numRows: int) -> List[List[int]]:
    result = [[1]]
    for row in range(numRows-1):
        #for every row create row result
        rowResult = [1] # first col is always 1
        for col in range (1, row+1):
            rowResult.append(result[row][col-1]+result[row][col])
        rowResult.append(1) # last col is always 1
        result.append(rowResult)
    return result