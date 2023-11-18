# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
class Solution(object):
    def countPairs(self, N, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(N)
        for edge in edges :
            u,v = edge[0], edge[1]
            uf.union(u,v)
        
        countDict = dict()
        for i in range(N):
            p = uf.find(i)
            if p in countDict:
                countDict[p]+=1
            else:
                countDict[p] = 1
        result = 0
        counts = countDict.values()
        cLen = len(counts)
        for i in range(cLen):
            for j in range(i+1, cLen):
                result += counts[i]*counts[j]  
    
        return result
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
    
    def printdata(self) :
        print(self.data)
    
