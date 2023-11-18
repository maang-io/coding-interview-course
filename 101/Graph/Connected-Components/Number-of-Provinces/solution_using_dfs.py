# https://leetcode.com/problems/number-of-provinces/
class Solution(object):
    # adj matrix representation
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        N = len(isConnected)
        count = 0
        visited = set()
        for i in range(0, N):
            if i in visited:
                continue
            self.dfs(isConnected, i, visited)
            count+=1
        return count
    
    def dfs(self,isConnected, cur, visited) :
        N = len(isConnected)
        visited.add(cur)
        for i in range(0, N):
            if i in visited or isConnected[i][cur] == False:
                continue
            self.dfs(isConnected,i,visited)
