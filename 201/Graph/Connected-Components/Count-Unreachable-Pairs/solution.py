# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(cur):
            sz = 1 # size of cur
            visited.add(cur)
            nbrs = graph.get(cur,[])
            for nbr in nbrs:
                if nbr in visited:
                    continue
                sz+=dfs(nbr)
            return sz

        # convert edges to adj list graph
        def buildGraph():
            graph = {}
            for u, v in edges:
                graph.setdefault(u, []).append(v)
                graph.setdefault(v, []).append(u)
            return graph

        
        def computeResult(cc):
            ccsz = len(cc)
            result = 0
            for i in range(ccsz):
                for j in range(i+1, ccsz):
                    result += cc[i]*cc[j]
            return result

        graph = buildGraph()

        # for each node which is not been visited do a dfs and get the size of connected components
        visited = set()
        cc = []
        for i in range(n):
            if i in visited:
                continue
            cc.append(dfs(i))
        return computeResult(cc)
