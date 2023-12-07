# https://leetcode.com/problems/number-of-provinces/
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        N = len(isConnected)
        uf = UnionFind(N)
        count = N
        for i in range(N):
            for j in range(i+1,N):
                if isConnected[i][j] == False:
                    continue
                pi = uf.find(i)
                pj = uf.find(j)
                if pi != pj :
                    uf.union(i,j)
                    count -=1

        return count
        
class UnionFind:
    data = []
    def __init__(self, N):
        self.data = [ i for i in range(N)]
        #print(data)
    def find(self, n):
        #print(n)
        p = self.data[n]
        if(n==p):
            return n
        return self.find(p)
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2 :
            return False
        self.data[p1] = p2
        return True
    